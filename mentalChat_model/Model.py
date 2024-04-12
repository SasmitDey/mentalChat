from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer

"""Fixing time problem in first run"""
import time
time.clock = time.time

"""Fixing collections hashable problem"""
import collections.abc
collections.Hashable = collections.abc.Hashable

"""Removing unwanted logs from terminal"""
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

"""convokit to get corpuses"""
from convokit import Corpus, download
# corpus = Corpus(filename=download("subreddit-depression"))

"""Importing flask"""
from flask import Flask, render_template, request




chatbot = ChatBot("mentalChat")
trainer = ChatterBotCorpusTrainer(chatbot)
list_trainer = ListTrainer(chatbot)
# trainer.export_for_training("./my_export.json")

# trainer.train("Training\mentalhealth.json")
# trainer.train("")
flag = 1
# while(flag==1):
#     myInput = input("You: ")
#     response = chatbot.get_response(myInput)
#     print(response)


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))
if __name__ == "__main__":
    app.run()    