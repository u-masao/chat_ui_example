import json

import gradio as gr
import openai


def respond(chat_history, message):
    with open("config/secret.json", "r") as fo:
        api_key = json.load(fo)["api_key"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        api_key=api_key,
        messages=[{"role": "user", "content": message}],
    )
    response_message = response["choices"][0]["message"]["content"]
    return chat_history + [[message, response_message]]


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    msg.submit(respond, [chatbot, msg], chatbot)

demo.launch()
