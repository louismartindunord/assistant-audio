import tensorflow 
from os.path import join, dirname
import pathlib
from pathlib import Path
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import random 
import json
import tensorflow
import numpy





import os
#cache les warning liées à tensorflow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


words = []
labels = []
docs = []


def chatbot():
    path_to_text = pathlib.Path('../datas/intents.json')     
    with open(path_to_text) as file:
        data = json.load(file)
        
        
    #Transformation des textes grâce à LancasterStemmer
    for intent in data['intents']:
        for pattern in intent['patterns']:
            
    
        
    
chatbot()
    