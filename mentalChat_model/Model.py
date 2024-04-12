from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
import time
time.clock = time.time

import collections.abc
collections.Hashable = collections.abc.Hashable

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

chatbot = ChatBot("mentalChat")
trainer = ChatterBotCorpusTrainer(chatbot)
list_trainer = ListTrainer(chatbot)
# trainer.export_for_training("./my_export.json")

# trainer.train("Training\intents.json")
# trainer.train("")
while(True):
    myInput = input("You: ")
    response = chatbot.get_response(myInput)
    print(response)
