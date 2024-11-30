import re
from collections import Counter

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

from sadle import Sadle


with open("dictionary.txt", 'r',  encoding='utf-8') as dct:
  english_words = dct.read().split()

names= []

nltk.download('vader_lexicon')

text_file = input("\nWelcome to Tanalyze. Tanalyze accepts text files and provides a total word count, ranked word count, list of characters and the main character from the text. \nEnter the file path of the text you want to analyse: ")
analysis_file_path = input("\nEnter the file path you want your analysis to be saved to: ")

def write_to_file(text):
  with open(analysis_file_path, 'a') as file:
    file.write(text)

def word_count(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        counter = Counter(words)
        ranked_words = counter.most_common()
        for word, count in ranked_words:
          # print(f"{word}: {count}")
          write_to_file(f"\n{word}: {count}")

def total_word_count(file_path):
  with open(file_path, 'r') as file:
    words = file.read().split()
    counter = Counter(words)
    total_count = counter.total()
    # print(f"\nTotal word count: {total_count}\n")
    write_to_file(f"\nTotal word count: {total_count}\n")

def identify_people(file_path):
  with open(file_path, 'r') as file:
      text = file.read()
      _names = []
      double_names = re.findall(r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b", text)
      # print("The characters in the text are:")
      write_to_file(f"\nThe characters in the text are:\n")
      for person in double_names:
        names.append(person)
        if person not in _names:
          _names.append(person)
          # print(person)
          write_to_file(f"{person}\n")

  # Identify single-named characters
  single_names = re.findall(r"\b[A-Z][a-z]+\b", text)
  for person in single_names:
    result = any(person in name for name in names)

    if person not in english_words and result is not True:
      names.append(person)
      if person not in _names:
        _names.append(person)
        # print(person)  
        write_to_file(f"{person}\n")

def identify_main_char():
    name_count = Counter(names)
    main_char = name_count.most_common(1)[0][0]
    # print(f"\nThe main character is {main_char}.")
    write_to_file(f"\nThe main character is {main_char}.\n")  

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    
    sentiment_scores = sid.polarity_scores(text)
    
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return sentiment

def launch_game():
  Sadle(text_file).start_game()

word_count(text_file)
total_word_count(text_file)
identify_people(text_file)
identify_main_char()
write_to_file(f"\nSentiment:{analyze_sentiment(text_file)}")
launch_game()





