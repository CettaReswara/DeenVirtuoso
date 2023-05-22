import csv
import re
import text_analyzer_algo as taa

def preprocess_text(text):
    # Menghapus karakter non-alfanumerik dan tanda baca
    text = re.sub(r'[^\w\s-]', '', text)
    
    # Menghapus angka
    text = re.sub(r'\d', '', text)
    
    # Mengubah teks menjadi huruf kecil
    text = text.lower()
    
    # Menghapus karakter berulang (contoh: "haaaappppyyyyy" menjadi "happpy")
    text = re.sub(r'(.)\1+', r'\1\1', text)
    
    # Menghapus spasi berlebihan
    text = re.sub(r'\s+', ' ', text)
    
    # Menghapus kata-kata pendek (kurang dari 3 karakter)
    text = re.sub(r'\b\w{1,2}\b', '', text)
    
    # Menghapus stopwords (kata umum yang tidak berkontribusi pada sentimen)
    stopwords = ['dan', 'atau', 'juga', 'dari', 'adalah']  # contoh stopwords, sesuaikan dengan kebutuhan
    text = ' '.join(word for word in text.split() if word not in stopwords)
    
    return text

def add_islamic_lexicon(filename):
    islamic_lexicon_current = load_islamic_lexicon("./data/islamic_lexicon.csv")
    islamic_lexicon_new = {}

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            waktu, ID, username, teks = row
            words = teks.split()
            for word in words :
                if word not in islamic_lexicon_current:
                    islamic_lexicon_new[word.lower()] = 'positive'

def load_islamic_lexicon(filename):
    islamic_lexicon = {}

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            word, sentiment = row
            islamic_lexicon[word.lower()] = sentiment.lower()

    return islamic_lexicon

def sentiment_analysis(text, islamic_lexicon):
    sentiment_score = 0
    pos_word = 0
    neg_word = 0
    
    # Menghitung skor sentimen berdasarkan kamus leksikon agama Islam
    for word in text.lower().split():
        if word in islamic_lexicon:
            if islamic_lexicon[word] == 'positive':
                pos_word+=1
            else:
                neg_word+=1
       
    
    if neg_word > pos_word:
        sentiment_score = -neg_word
    else :
        sentiment_score = pos_word - neg_word

    for word in text.lower().split():
         if word == 'tidak' or '-' in word:
            sentiment_score *= -1

    # Menentukan label sentimen berdasarkan skor sentimen
    return sentiment_score
