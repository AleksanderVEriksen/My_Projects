# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:08:55 2023

@author: eriks
"""
import os
import openai
import gradio

openai.api_key = os.getenv("OPENAI_API_KEY")

#= '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'
messages = []


# Creating personalized chatbot
system_msg = input('What chatbot personality would you like it to have?')
messages.append({"role" : "system", "content" : system_msg})

# Asking the bot question until quit() is typed
def ChatBot(user_input):
    messages.append({"role":"user", "content": user_input})
    response = openai.ChatCompletion(
        model = 'gpt-3.5-turbo', 
        message = messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant", "content":reply})
    return reply

demo = gradio.Interface(fn = ChatBot(), inputs = 'text', output = 'text', title = 'Simple Chatbot')

demo.launch()
