import os
import re
from collections import Counter
import nltk
 
nltk.download('stopwords')
 
file_path = os.getcwd()+ "/random_paragraphs.txt"
 
def process_text(file_path): 
  with open(file_path, 'r') as file:
    text = file.read()
 
  text = text.lower()
 
  text = re.sub(r'[^\w\s]', '', text)
 
  stop_words = nltk.corpus.stopwords.words('english')
 
  words = text.split()
 
  filtered_words = [word for word in words if word not in stop_words]

  return filtered_words
 
processed_text = process_text(file_path)
 
word_counts = Counter(processed_text)
 
print("Word Frequency Count:")
for word, count in word_counts.items():
  print(f"{word}: {count}")
