import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy as np
import tflearn as tf
import tensorflow as tnf
import random
import json
import pickle
with open("intents.json") as file:
    data = json.load(file)

print(data)