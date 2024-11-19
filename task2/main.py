import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

original_text = """greet, idea exhibition diagram integration ticket 
bake animal nun refrigerator graze moving population drawing, unlike parade 
sanctuary rehearsal statement burial!"""

with open("original_text.txt", "w") as file:
    file.write(original_text)

with open("original_text.txt", "r") as file:
    text = file.read()

tokens = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
stemmed_tokens = [stemmer.stem(word) for word in lemmatized_tokens]

stop_words = set(stopwords.words('english'))
processed_tokens = [word for word in stemmed_tokens if word.lower() not in stop_words and word.isalpha()]

processed_text = " ".join(processed_tokens)

with open("processed_text.txt", "w") as file:
    file.write(processed_text)

print("Оброблений текст збережено у файл 'processed_text.txt'")
