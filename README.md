# ✨ Simple ChatBot Using GPT-2 ✨

This Python script simulates a simple chatbot using Streamlit for the user interface and GPT-2 from Hugging Face for generating responses. The chatbot allows users to interact by sending messages and receiving AI-generated replies.

## Features

1. **GPT-2 Integration**
   - **AI-Powered Responses**: The chatbot uses the GPT-2 model hosted on Hugging Face to generate relevant and context-aware responses.

2. **Streamlit Interface**
   - **User-Friendly UI**: The application features a clean, modern interface designed with Streamlit, providing a seamless experience for users.
   - **Chat History**: Users can view the conversation history, with each user message and AI response displayed in a visually appealing format.

3. **Real-Time Interaction**
   - **Instant Responses**: Users can input prompts and receive immediate AI responses in real-time.

4. **Error Handling**
   - **Input Validation**: The system ensures that inputs are provided before attempting to generate a response, preventing errors and improving user experience.

## Implementation Details

1. **Generative Model**
   - **Model Used**: The script uses the GPT-2 model from Hugging Face.

2. **Chat Interface**
   - **Styled Messages**: User messages and bot responses are displayed in styled message bubbles, enhancing readability and the overall user experience.

3. **Input Handling**
   - **Text Input**: The script uses Streamlit's form and text input to capture user messages.
   - **Form Submission**: Upon submission, the chatbot generates a response, which is then added to the chat history.

## How to Use

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/simple-chatbot.git
   cd simple-chatbot
2. **Set Up API Token**
    Replace the placeholder HF_TOKEN in the script with your actual Hugging Face API token
    HF_TOKEN = "your_actual_api_token"

3. **Run the Script**
    streamlit run chatbot.py
