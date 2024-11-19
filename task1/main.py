import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import string

nltk.download('gutenberg')
nltk.download('stopwords')

text = gutenberg.words('milton-paradise.txt')

print(f"Кількість слів у тексті: {len(text)}")

fdist = FreqDist(text)
most_common_words = fdist.most_common(10)

words, counts = zip(*most_common_words)
plt.figure(figsize=(10, 5))
plt.bar(words, counts)
plt.title("10 найбільш вживаних слів")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()

stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in text if word.isalpha() and word.lower() not in stop_words]

filtered_fdist = FreqDist(filtered_words)
filtered_most_common_words = filtered_fdist.most_common(10)

filtered_words, filtered_counts = zip(*filtered_most_common_words)
plt.figure(figsize=(10, 5))
plt.bar(filtered_words, filtered_counts)
plt.title("10 найбільш вживаних слів після фільтрації")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()
