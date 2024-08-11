import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint  # Updated import
import os

# Get the Hugging Face API token
HF_TOKEN = os.getenv('HF_TOKEN') or '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'

# Define the repository ID for the model
repo_id = "openai-community/gpt2"

# Initialize the HuggingFaceEndpoint model
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.7,              # Explicit parameter
    model_kwargs={"max_length": 50}  # Pass max_length within model_kwargs
)

# Example invocation of the model
# response = llm("What is Generative AI?")
# print(response)

st.title("✍️ CHATBOT ✍️")
st.write("This Chatbot is Powered by using GPT2 from Hugging Face")

user_input = st.text_input("You","Enter your Prompt here ....")

if st.button("Send"):
    if user_input:
        try:
            response = llm(user_input)
            st.write(f"Bot:{response}")
        except Exception as e:
            st.write(f"Error :{str(e)}")
    else:
        st.write("Please Enter a message.")