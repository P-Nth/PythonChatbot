from tensorflow.python.keras.models import load_model
import random
import json
import pickle
from re import T
from unittest import result

import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()
file = open('Backend/Learn/TliorDictionary.json')
dictionary = json.loads((file).read())

words = pickle.load(open('Backend/Learn/words.pkl', 'rb'))
classes = pickle.load(open('Backend/Learn/classes.pkl', 'rb'))
model = load_model('Backend/Learn/ai_model1.h5')


def convert_to_words(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def converted_words(sentence):
    sentence_words = convert_to_words(sentence)
    bag = [0] * len(words)
    for wordItem in sentence_words:
        for i, word in enumerate(words):
            if word == wordItem:
                bag[i] = 1
    return np.array(bag)


def predict_word(sentence):
    bunch = converted_words(sentence)
    res = model.predict(np.array([bunch]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append(
            {'wordBlock': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(user_input):
    try:
        tag = user_input[0]['wordBlock']
        list_of_wordBlocks = dictionary['dictionary']
        for i in list_of_wordBlocks:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
    except IndexError:
        result = "I don't understand!"
    return result


print("Lets Go! It's working")

if __name__ == "__main__":
    while True:
        text = input("User: ")
        user_message = predict_word(text)
        if text == 'bye':
            break

        res = get_response(user_message)
        print("AI:", res)
