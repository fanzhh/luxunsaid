# coding: utf-8

from numpy import array
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from kears.layers import Embedding
from kearas.layers import Embedding
from keras.layers import Embedding
def load_doc(filename):
    file = open(filename,'r')
    text = file.read()
    file.close()
    return text
in_filename = 'luxun_sequences.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')
lines[:5]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)
vocab_size = len(tokenizer.word_index) + 1
vocab_size
sequences = array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]
X = sequences[:,:-1]
sequences[:,:-1]
sequences
sequences.shape
lines
type(lines)
tokenizer=Tokenizer()
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)
sequences
type(sequences)
len(sequences)
vocab_size = len(tokenizer.word_index) + 1
vocab_size
sequences2 = array(sequences)
sequences2.shape
sequences2
sequences2[:]
sequences2[:,1]
sequences
sequences[0]
len(sequences[0])
sequences
import numpy as np
print(np.asarray(sequences))
sequences
print(array(sequences))
for item in sequences:
    print(len(item))
    
i = 0
for item in sequences:
    print('%d,%d'%(i,len(item)))
    
for item in sequences:
    print('%d,%d'%(i,len(item)))
    i += 1
    
