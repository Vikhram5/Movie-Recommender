from flask import Flask,render_template,request,redirect,url_for
from homepage import *
from app import *
from reviews import *
import pickle

TMDB_API_KEY = "87ba1c3c074e58285a37ca4f9c297ec1"

app=Flask(__name__)

@app.route("/")
@app.route('/movies')
def top_movies():
    movies = get_top_movies()
    latest_movies = get_latest_movies()
    animated_movies = get_animated_movies()
    romantic_movies = get_romantic_movies()
    horror_movies = get_horror_movies()
    thriller_movies = get_thriller_movies()
    sci_fi_movies = get_sci_fi_movies()
    return render_template('homepage.html', movies=movies, latest_movies=latest_movies,
                           animated_movies=animated_movies, romantic_movies=romantic_movies,
                           horror_movies=horror_movies,
                           thriller_movies=thriller_movies, sci_fi_movies=sci_fi_movies)

@app.route("/home")
def home():
    suggestions = get_suggestions()
    return render_template('home.html',suggestions=suggestions)



@app.route("/similarity",methods=["POST"])
def similarity():
    movie = request.form['name']
    rc = rcmd(movie)   #movie recommendation
    if type(rc)==type('string'):
        return rc
    else:
        m_str="---".join(rc)
        return m_str
    
    
@app.route('/details', methods=['GET', 'POST'])
def more():
    movie_id = request.args.get('movie_id')
    movie_cast = get_movie_cast(movie_id)
    movie_crew = get_movie_crew(movie_id)
    movie_details = get_movie_details(movie_id)
    return render_template('details.html', movie_id=movie_id, movie_cast=movie_cast, movie_crew=movie_crew,
                           movie_details=movie_details)



from textblob import TextBlob

# Initialize IMDb
ia = IMDb()

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        movie_title = request.form['movie_title']
        movie = ia.search_movie(movie_title)[0]
        reviews = get_movie_reviews(movie)
        
        analyzed_reviews = []
        for review_dict in reviews:
            review_text = review_dict['content']
            sentiment = analyze_sentiment(review_text)
            analyzed_reviews.append((review_text, sentiment))
            
        return render_template('reviews.html', movie=movie, reviews=analyzed_reviews)

    return render_template('reviews.html')

@app.route("/recommend",methods=["POST"])
def recommend():
    title = request.form['title']
    cast_ids = request.form['cast_ids']
    cast_names = request.form['cast_names']
    cast_chars = request.form['cast_chars']
    cast_bdays = request.form['cast_bdays']
    cast_bios = request.form['cast_bios']
    cast_places = request.form['cast_places']
    cast_profiles = request.form['cast_profiles']
    imdb_id = request.form['imdb_id']
    poster = request.form['poster']
    genres = request.form['genres']
    overview = request.form['overview']
    vote_average = request.form['rating']
    vote_count = request.form['vote_count']
    release_date = request.form['release_date']
    runtime = request.form['runtime']
    status = request.form['status']
    rec_movies = request.form['rec_movies']
    rec_posters = request.form['rec_posters']

    suggestions = get_suggestions()

    # call the convert_to_list function for every string that needs to be converted to list
    rec_movies = convert_to_list(rec_movies)
    rec_posters = convert_to_list(rec_posters)
    cast_names = convert_to_list(cast_names)
    cast_chars = convert_to_list(cast_chars)
    cast_profiles = convert_to_list(cast_profiles)
    cast_bdays = convert_to_list(cast_bdays)
    cast_bios = convert_to_list(cast_bios)
    cast_places = convert_to_list(cast_places)

    # convert string to list (eg. "[1,2,3]" to [1,2,3])
    cast_ids = cast_ids.split(',')
    cast_ids[0] = cast_ids[0].replace("[","")
    cast_ids[-1] = cast_ids[-1].replace("]","")
    
    # rendering the string to python string
    for i in range(len(cast_bios)):
        cast_bios[i] = cast_bios[i].replace(r'\n', '\n').replace(r'\"','\"')
    
    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))} 
    casts = {cast_names[i]:[cast_ids[i], cast_chars[i], cast_profiles[i]] for i in range(len(cast_profiles))}
    cast_details = {cast_names[i]:[cast_ids[i], cast_profiles[i], cast_bdays[i], cast_places[i], cast_bios[i]] for i in range(len(cast_places))}

    return render_template('recommend.html',title=title,poster=poster,overview=overview,vote_average=vote_average,
        vote_count=vote_count,release_date=release_date,runtime=runtime,status=status,genres=genres,
        movie_cards=movie_cards,casts=casts,cast_details=cast_details)


if __name__ == '__main__':
    app.run(debug=True)



