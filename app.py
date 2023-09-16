import openai
import gradio as gr
from coder import API_KEY

openai.api_key = API_KEY

messages = [
    {"role": "system", "content": "convert the description in to java code"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": str(input)})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        #messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want to code",
             theme="compact", server_name="0.0.0.0").launch()

'''
system
convert the description in to python code
user
when user enters username and password
then authenticate the user
'''