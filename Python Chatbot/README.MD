PYTHON CHATBOT

Version 0.0.1

# Required Interprator

Use Python 3.10.4 64-bit or any other recommended interprator for this project

# Chatbot Client with Flask and JavaScript.

This chatbot can be deployed within a Flask app with jinja template.

It can also be configured so that the frontend is separated with the backend.

This will require you to use cors to enable the Cross Origin Resource Sharing

# Project Setup

This repo contains all the starter files.

No need for a vitual environment.

Go ahead and clone the repo now.

`$ git clone https://github.com/P-Nth/Python-Chatbot.git`

`$ cd "Python Chatbot"`

# Install dependencies

`$ pip install Flask torch torchvision nltk tensorflow keras `

`$ pip install flask-cors` #Only necesary if you want to create a separate frontend and communicate with the backend via api.

# Install nltk package

`$ python`

`> > > import nltk`

`> > > nltk.download('punkt')`

Modify TliorDictionary.json with different intents and responses for your Chatbot

# Run

Path to use `~/My-Python-Projects/Python Chatbot`

`$ python tliorai.py`

This will dump data.pth file. And then run the following command to test it in the console.

# Then Deploy The File Server:

First you need to configure and implement the index.html and open it on the browser.

And then configure scripts.js to post user input & fetch response from the backend.

Then run the main file to start the localhost api using the command below.

`$ python main.py`

# Credits:

Credits go to NeuralNine for helping out with the training of the neural network.

And more credits got to Python Engeneer for helping out with intergrating the ChatBot with the Frontend.
