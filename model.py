import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

def process_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    
    sentiment_scores = sia.polarity_scores(text)
    emotions = {
        "happy": ["joy", "positive"],
        "sad": ["sadness"],
        "angry": ["anger"],
        "fearful": ["fear"],
        "surprised": ["surprise"],
        "disgusted": ["disgust"]
    }

    dominant_emotion = "neutral"
    if sentiment_scores["compound"] >= 0.5:
        dominant_emotion = "happy"
    elif sentiment_scores["compound"] <= -0.5:
        dominant_emotion = "sad"
    elif sentiment_scores["neg"] > 0.5:
        dominant_emotion = "angry"

    return dominant_emotion
