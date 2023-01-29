from tensorflow.python.keras.optimizer_v1 import SGD
from tensorflow.python.keras.layers import Dense, Activation, Dropout
from tensorflow.python.keras.models import Sequential
import random
import json
import pickle
from tabnanny import verbose
import tensorflow as tf

import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
tf.compat.v1.disable_eager_execution()


lemmatizer = WordNetLemmatizer()
file = open('Backend/Learn/TliorDictionary.json')
dictionary = json.loads(file.read())

words = []
classes = []
itemHolder = []
ignore_characters = ['?', '.', '!', ',']

for wordBlock in dictionary['dictionary']:
    for pattern in wordBlock['patterns']:
        word_list = nltk.wordpunct_tokenize(pattern)
        words.extend(word_list)
        itemHolder.append((word_list, wordBlock['tag']))
        if wordBlock['tag'] not in classes:
            classes.append(wordBlock['tag'])

words = [lemmatizer.lemmatize(word)
         for word in words if word not in ignore_characters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words, open('Backend/Learn/words.pkl', 'wb'))
pickle.dump(classes, open('Backend/Learn/classes.pkl', 'wb'))

training = []
empty_output = [0] * len(classes)

for item in itemHolder:
    bag = []
    word_patterns = item[0]
    words_patterns = [lemmatizer.lemmatize(
        word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    row_output = list(empty_output)
    row_output[classes.index(item[1])] = 1
    training.append([bag, row_output])

random.shuffle(training)
training = np.array(training)

trainning_x = list(training[:, 0])
trainning_y = list(training[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(trainning_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(trainning_y[0]), activation="softmax"))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd, metrics=['accuracy'])

prev = model.fit(np.array(trainning_x), np.array(trainning_y),
                 epochs=200, batch_size=5, verbose=1)
model.save('Backend/Learn/ai_model1.h5', prev)
print("Done")
