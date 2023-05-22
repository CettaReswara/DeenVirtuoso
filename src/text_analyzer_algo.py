import weighting as wt
import islamic_lexicon as ilm
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import wordnet as wn
from nltk.sentiment import SentimentIntensityAnalyzer

def get_sentiment_score(word):
    synsets = wn.synsets(word, lang='ind')
    if synsets:
        # Ambil definisi pertama dari synset
        definition = synsets[0].definition()
        # Gunakan SentimentIntensityAnalyzer dari NLTK
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(definition)
        # Ambil skor komposit
        sentiment_score = sentiment_scores['compound']
        return sentiment_score
    else:
        return 0
    
def analyze_sentiment(text):
    sentiment_score = 0
    positive_words = 0
    negative_words = 0
    words = text.split()
    #print(words)
    for word in words:
        if get_sentiment_score(word) == 0:
            words.remove(word)
        elif get_sentiment_score(word) < 0:
            negative_words += get_sentiment_score(word)
        else:
            positive_words += get_sentiment_score(word)
    
    if negative_words > positive_words:
        sentiment_score = -negative_words
    else:
        sentiment_score = positive_words - negative_words

    for word in text.lower().split():
         if word == 'tidak' or '-' in word:
            sentiment_score *= -1
            
    print(sentiment_score)
    return sentiment_score

def full_analysis(text):
    constfull, constislam = 0.4, 0.6
    #constfull, constislam = wt.calculate_weight([ilm.sentiment_analysis(text, ilm.load_islamic_lexicon("./data/islamic_lexicon.csv"))], [analyze_sentiment(text)])
    sentimentnewestscore = constfull * ilm.sentiment_analysis(text, ilm.load_islamic_lexicon("./data/islamic_lexicon.csv")) + constislam * analyze_sentiment(text)
    return sentimentnewestscore



