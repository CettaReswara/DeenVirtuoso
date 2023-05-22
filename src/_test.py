import islamic_lexicon as ilm
import text_analyzer_algo as taa
# Contoh penggunaan
filename = "./data/islamic_lexicon.csv"
islamic_lexicon = ilm.load_islamic_lexicon(filename)

text1 = "Pahala ibadah dan taqwa umat muslim akan mendapatkan rahmat dan berkah Allah, Subhanallah."

sentiment_label1 = ilm.sentiment_analysis(text1, islamic_lexicon)
print("Sentiment Label:", sentiment_label1)
wordnet_sentiment_label1 = taa.analyze_sentiment(text1)
print("Wordnet Sentiment Label:", wordnet_sentiment_label1)
print(taa.full_analysis(text1))
print()

text2 = "Kalian semua berdosa dan akan masuk neraka karena melakukan bid'ah besar! Astaghriullah..."

sentiment_label2 = ilm.sentiment_analysis(text2, islamic_lexicon)
print("Sentiment Label:", sentiment_label2)
wordnet_sentiment_label2 = taa.analyze_sentiment(text2)
print("Wordnet Sentiment Label:", wordnet_sentiment_label2)
print(taa.full_analysis(text2))
print()

text3 = "INNALILLAHI!!!!"
sentiment_label3 = ilm.sentiment_analysis(text3, islamic_lexicon)
print("Sentiment Label:", sentiment_label3)
sentiment_label3_after = ilm.sentiment_analysis(ilm.preprocess_text(text3), islamic_lexicon)
print("Sentiment Label After:", sentiment_label3_after)
wordnet_sentiment_label3 = taa.analyze_sentiment(text3)
print("Wordnet Sentiment Label:", wordnet_sentiment_label3)
print(taa.full_analysis(text3))
print()

textpos = "Pahala ibadah, tidak berkah, umat muslim akan mendapatkan rahmat dan berkah Allah!"

preprocessed_textpos = ilm.preprocess_text(textpos)
sentiment_labelpos = ilm.sentiment_analysis(preprocessed_textpos, islamic_lexicon)
wordnet_sentiment_labelpos = taa.analyze_sentiment(preprocessed_textpos)

print("Preprocessed Text:", preprocessed_textpos)
print("Sentiment Label:", sentiment_labelpos)
print("Wordnet Sentiment Label:", wordnet_sentiment_labelpos)
print(taa.full_analysis(preprocessed_textpos))
print()

textneg = "Pahala ibadah, berkah, umat muslim akan mendapatkan rahmat dan berkah Allah!"

preprocessed_textneg = ilm.preprocess_text(textneg)
sentiment_labelneg = ilm.sentiment_analysis(preprocessed_textneg, islamic_lexicon)
wordnet_sentiment_labelneg = taa.analyze_sentiment(preprocessed_textneg)

print("Preprocessed Text:", preprocessed_textneg)
print("Sentiment Label:", sentiment_labelneg)
print("Wordnet Sentiment Label:", wordnet_sentiment_labelneg)
print(taa.full_analysis(preprocessed_textneg))
print()

texttry = "Buat yg pacaran trus niat puasa full 30 hari, yakin mau lanjut? Hayooo, itu haram loh dan puasa kamu sdh pasti tidak diterima. Tidak ada pahalanya, tidak ada amalannya. hanya sekedar nahan lapar dan haus doang, bahasa kasarnya Allah ga butuh sama puasa kamu. gimana? Masih yakin mau lanjut?"
print(ilm.sentiment_analysis(ilm.preprocess_text(texttry), islamic_lexicon))
print(taa.full_analysis(ilm.preprocess_text(texttry)))