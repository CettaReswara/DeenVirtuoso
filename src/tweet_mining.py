import csv
import tweepy

# Mengatur Consumer Key dan Consumer Secret
consumer_key = "QLQf3dUAljDbEDnRl9Amnsnfe"
consumer_secret = "KXW4anAYqxE7FDtaPDPVu0PBqS5Bx9putyouTouei9tEwiRFm3"

# Mengatur Access Token dan Access Token Secret
access_token = "1292359577292271618-28LRmx2NeieEX3BPa5YGlJNgzMdkPE"
access_token_secret = "nbUssIhiSifvTS8xAtpJR4fbXcji68RwAWbAs4c6bdODl"

#  Membuat objek OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Mengatur Access Token dan Access Token Secret
auth.set_access_token(access_token, access_token_secret)

# Membuat objek API
api = tweepy.API(auth)

# Faktor-faktor pencarian
query_keywords = ["islam", "muslim", "dakwah", "quran", "hadith"]
query_hashtags = ["islamic", "muslims", "dawah", "islamicquotes"]

# Jumlah tweet yang akan diambil
tweet_count = 1000

# Mengumpulkan tweet yang sesuai dengan faktor-faktor pencarian
tweets = []

# Pencarian berdasarkan kata kunci
for keyword in query_keywords:
    query = f"{keyword} -filter:retweets"
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="id").items(tweet_count):
        tweets.append(tweet.text)

# Pencarian berdasarkan hashtag
for hashtag in query_hashtags:
    query = f"#{hashtag} -filter:retweets"
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="id").items(tweet_count):
        tweets.append(tweet.text)

# Menyimpan tweet ke dalam file CSV
filename = "./data/twitter_dataset.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Tweet"])
    for tweet in tweets:
        writer.writerow([tweet])

print(f"Dataset berhasil disimpan dalam file {filename}")