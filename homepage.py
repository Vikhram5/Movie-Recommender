import requests


TMDB_API_KEY = "87ba1c3c074e58285a37ca4f9c297ec1"
TMDB_TOP_MOVIES_URL = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=en-US&page=1"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"


TMDB_API_KEY = "df8dfa719d49c0e37a133568baa1a53f"

TMDB_TOP_MOVIES_URL = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=en-US&page=1"
TMDB_LATEST_MOVIES_URL = f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=en-US&page=1"
TMDB_ANIMATED_MOVIES_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=16"
TMDB_ROMANTIC_MOVIES_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=10749"
TMDB_HORROR_MOVIES_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=27"
TMDB_THRILLER_MOVIES_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=53"
TMDB_SCI_FI_MOVIES_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=878"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

TMDB_MOVIE_CAST1 = "https://api.themoviedb.org/3/movie/"
TMDB_MOVIE_CAST2 = f"/credits?api_key={TMDB_API_KEY}&language=en-US&page=1"

TMDB_MOVIE1 = "https://api.themoviedb.org/3/movie/"
TMDB_MOVIE2 = f"?api_key=df8dfa719d49c0e37a133568baa1a53f"

def get_top_movies():
    response = requests.get(TMDB_TOP_MOVIES_URL)
    if response.status_code == 200:
        data = response.json()
        movies = data.get('results', [])
        for movie in movies:
            poster_path = movie.get('poster_path')
            movie['poster_path'] = TMDB_IMAGE_BASE_URL + poster_path if poster_path else ""
        return movies
    else:
        return []


def get_latest_movies():
    response = requests.get(TMDB_LATEST_MOVIES_URL)
    if response.status_code == 200:
        data = response.json()
        latest_movies = data.get('results', [])
        for movie in latest_movies:
            poster_path = movie.get('poster_path')
            movie['poster_path'] = TMDB_IMAGE_BASE_URL + poster_path if poster_path else ""
        return latest_movies
    else:
        return []


def get_romantic_movies():
    response = requests.get(TMDB_ROMANTIC_MOVIES_URL)
    if response.status_code == 200:
        data = response.json()
        romantic_movies = data.get('results', [])
        for movie in romantic_movies:
            poster_path = movie.get('poster_path')
            movie['poster_path'] = TMDB_IMAGE_BASE_URL + poster_path if poster_path else ""
        return romantic_movies
    else:
        return []


def get_animated_movies():
    response = requests.get(TMDB_ANIMATED_MOVIES_URL)
    if response.status_code == 200:
        data = response.json()
        animated_movies = data.get('results', [])
        for movie in animated_movies:
            poster_path = movie.get('poster_path')
            movie['poster_path'] = TMDB_IMAGE_BASE_URL + poster_path if poster_path else ""
        return animated_movies
    else:
        return []


def get_horror_movies():
    response = requests.get(TMDB_HORROR_MOVIES_URL)
    if response.status_code == 200:
        data = response.json()
        horror_movies = data.get('results', [])
        for movie in horror_movies:
            poster_path = movie.get('poster_path')
            movie['poster_path'] = TMDB_IMAGE_BASE_URL + poster_path if poster_path else ""
        return horror_movies
    else:
        return []


def get_thriller_movies():
    response = requests.get(TMDB_THRILLER_MOVIES_URL)
    if response.status_code == 200:
        data = response.json()
        thriller_movies = data.get('results', [])
        for movie in thriller_movies:
            poster_path = movie.get('poster_path')
            movie['poster_path'] = TMDB_IMAGE_BASE_URL + poster_path if poster_path else ""
        return thriller_movies
    else:
        return []


def get_sci_fi_movies():
    response = requests.get(TMDB_SCI_FI_MOVIES_URL)
    if response.status_code == 200:
        data = response.json()
        sci_fi_movies = data.get('results', [])
        for movie in sci_fi_movies:
            poster_path = movie.get('poster_path')
            movie['poster_path'] = TMDB_IMAGE_BASE_URL + poster_path if poster_path else ""
        return sci_fi_movies
    else:
        return []


def get_movie_cast(movie_id):
    path = TMDB_MOVIE_CAST1 + movie_id + TMDB_MOVIE_CAST2
    response = requests.get(path)
    if response.status_code == 200:
        data = response.json()
        movie_cast = data.get('cast', [])
        for movie in movie_cast:
            poster_path = movie.get('profile_path')
            movie['poster_path'] = TMDB_IMAGE_BASE_URL + poster_path if poster_path else ""
        return movie_cast[:10]
    else:
        return []


def get_movie_crew(movie_id):
    path = TMDB_MOVIE_CAST1 + movie_id + TMDB_MOVIE_CAST2
    response = requests.get(path)
    if response.status_code == 200:
        data = response.json()
        movie_crew = data.get('crew', [])
        for movie in movie_crew:
            poster_path = movie.get('profile_path')
            movie['poster_path'] = TMDB_IMAGE_BASE_URL + poster_path if poster_path else ""
        return movie_crew[:10]
    else:
        return []
    
def get_movie_details(movie_id):
    path = TMDB_MOVIE1 + movie_id + TMDB_MOVIE2
    response = requests.get(path)
    if response.status_code == 200:
        data = response.json()
        movie_details = {}
        movie_details['original_title'] = data.get('original_title')
        movie_details['overview'] = data.get('overview')
        poster_path = data.get('poster_path')
        movie_details['poster_path'] = TMDB_IMAGE_BASE_URL + poster_path if poster_path else ""
        return movie_details
    else:
        return []
    
    
def fetch_movie_id(movie_name):
    url = f"https://api.themoviedb.org/3/search/TMDB_API_KEY={TMDB_API_KEY}&query={movie_name}&language=en-US"
    response = requests.get(url)
    data = response.json()

    if "results" in data and data["results"]:
        return data["results"][0]["id"]
    else:
        return None
    
    
    
def get_suggestions():
    data = pd.read_csv('main_data.csv')
    return list(data['movie_title'].str.capitalize())

