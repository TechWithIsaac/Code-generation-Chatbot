import openai
import gradio as gr
from coder import API_KEY
from llama_index import VectorStoreIndex, SimpleDirectoryReader
openai.api_key = API_KEY

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()


def chatbot(input):
    if input:
        #messages.append({"role": "assistant", "content": reply})
        
        response = query_engine.query(str(input))
        return response

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want to code",
             theme="compact", server_name="0.0.0.0").launch()