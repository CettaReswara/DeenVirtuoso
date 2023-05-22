import csv
from faker import Faker
from lorem_text import lorem

fake = Faker("id_ID")

# Jumlah tweet palsu yang akan dibuat
tweet_count = 1000

# Daftar dummy data tweet
dummy_tweets = []

# Menghasilkan dummy data tweet dengan Faker
for _ in range(tweet_count):
    tweet_id = fake.uuid4()
    username = fake.user_name()
    tweet_text = lorem.sentence()

    dummy_tweet = {
        "Waktu": fake.iso8601(),
        "ID": tweet_id,
        "Username": username,
        "Teks": tweet_text
    }

    dummy_tweets.append(dummy_tweet)

# Menyimpan dummy data tweet ke dalam file CSV
filename = "./data/dummy_tweets.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Waktu", "ID", "Username", "Teks"])
    writer.writeheader()

    for tweet in dummy_tweets:
        writer.writerow(tweet)

print(f"Dataset berhasil disimpan dalam file {filename}")
