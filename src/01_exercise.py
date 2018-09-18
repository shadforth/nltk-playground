#!/usr/bin/env python3
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

def exercise_01():
  """
  Explore introductory NLP concepts in Python with NLTK.
  http://pythonforengineers.com/introduction-to-nltk-natural-language-processing-with-python/
  """

  # Define our sentence to be manipulated
  sentence = 'The quick brown fox, jumps over the lazy dog'

  # Splitting the sentence like this does not extract the punctuation marks
  sentence_split = sentence.split(' ')

  # Splitting the sentence with the word tokenizer provided by the NLTK library 
  # correctly identifies punctuation
  sentence_tokenised = word_tokenize(sentence)

  # NLTK's pos_tag() identifies features of the sentence, i.e. singular nouns (NN), 
  # adjectives (JJ), determiners (DT), etc.
  print(nltk.pos_tag(sentence_tokenised))

  # Print what all the tags mean with: `nltk.help.upenn_tagset()`

  # Find the definition of any word using lexical database, WordNet
  syns = wordnet.synsets('dog')
  print(syns)
  print(syns[0].name())
  print(syns[0].definition())
  print(syns[1].name())
  print(syns[2].definition())

if __name__ == '__main__':
  exercise_01()