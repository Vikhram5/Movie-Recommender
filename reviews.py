from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from imdb import IMDb
import nltk
nltk.download('vader_lexicon')
ia = IMDb()

analyzer = SentimentIntensityAnalyzer()

def get_movie_reviews(movie):
    reviews = []
    try:
        ia.update(movie, info=['reviews'])
        if 'reviews' in movie:
            reviews = movie['reviews']
    except Exception as e:
        print(f"Error fetching reviews for movie '{movie['title']}': {e}")
    return reviews

def analyze_sentiment(text):
    vader_scores = analyzer.polarity_scores(text)
    textblob_analysis = TextBlob(text)
    
    # Define rules to combine the results
    if vader_scores['compound'] >= 0.05 and textblob_analysis.sentiment.polarity > 0:
        return "Positive"
    elif vader_scores['compound'] <= -0.05 and textblob_analysis.sentiment.polarity < -0.05:
        return "Negative"
    else:
        return "Neutral"
