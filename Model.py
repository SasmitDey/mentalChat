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

# trainer.train("chatterbot.corpus.english.greetings")
# trainer.export_for_training("./my_export.json")


list_trainer.train([
    "I dont feel happy anymore",
    "It's completely understandable to feel alone in your struggles, but please know that you're not alone. Many people have gone through similar experiences, and there are supportive communities and professionals ready to listen and help you through this.",
    "I'm scared to talk about my mental health. What if people judge me?",
    "It's natural to feel scared about opening up, especially when it comes to something as personal as mental health. Remember that it's okay to take small steps at your own pace. There are understanding and compassionate people who won't judge you and will offer support when you're ready to share.",
    "I'm tired of feeling this way. Will things ever get better?",
    "It's completely understandable to feel exhausted from struggling with your mental health. While it may seem overwhelming right now, please remember that healing is possible. With support, self-care, and professional guidance, there's hope for brighter days ahead.",
    "I'm finding it hard to focus lately. What can I do to improve my concentration?",
    "Difficulty focusing can be challenging, especially when dealing with mental health issues. Remember to be patient with yourself. Break tasks into smaller, manageable steps, practice mindfulness or meditation, and consider seeking professional guidance for personalized strategies to improve concentration.",
    "I'm feeling guilty about taking time for self-care. Is it selfish to prioritize my mental health?",
    "It's absolutely not selfish to prioritize your mental health. Just like we need to take care of our physical well-being, taking care of our mental health is essential for overall wellness. Remember that by prioritizing self-care, you're better equipped to support yourself and others in the long run.",
    ]
) 
# trainer.train("data/corpus/")

flag = 1
while(flag==1):
    myInput = input("You: ")
    response = chatbot.get_response(myInput)
    print(response)


# app = Flask(__name__)
# @app.route("/")
# def home():
#     return render_template("index.html")
# # @app.route("/get")
# # def get_bot_response():
# #     userText = request.args.get('msg')
# #     return str(chatbot.get_response(userText))

# if __name__ == "__main__":
#     with app.app_context():
#         app.run()