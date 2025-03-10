import streamlit as st
from trie import Trie
from chatbot_queue import ChatbotQueue
from linked_list import LinkedList
import google.generativeai as genai

# Initialize Gemini API
genai.configure(api_key="AIzaSyAHQoXKSaJadsjQiwGBwrmvLcXBeBBfdx0")

# Function to get Gemini response
def get_gemini_response(query):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(query)
    return response.text if response else "I'm sorry, I couldn't process that."

# Initialize Data Structures
trie = Trie()
history = ChatbotQueue()
memory = LinkedList()

# Sample phrases for Trie
sample_phrases = ["Hello", "How can I help you?", "Goodbye", "What is your name?"]
for phrase in sample_phrases:
    trie.insert(phrase.lower())

# Chatbot UI function
def chatbot_ui():
    st.title("💬 AI Chatbot")
    
    # Add an animation
    st.markdown("<h3 style='text-align: center;'>Ask me anything!</h3>", unsafe_allow_html=True)

    user_input = st.text_input("Your Message:", key="user_input")

    if st.button("Send"):
        if user_input:
            user_input_lower = user_input.lower()
            
            # Check for predefined responses
            if trie.search(user_input_lower):
                response = f"You said: {user_input}"
            else:
                response = get_gemini_response(user_input)

            # Store history
            history.enqueue(user_input)
            memory.append(user_input)

            # Display response
            st.markdown(f"<div style='background:#f4f4f4;padding:10px;border-radius:10px;'>🤖 <b>Bot:</b> {response}</div>", unsafe_allow_html=True)

            # Display chat history
            st.write("### Chat History:")
            temp_history = []
            for _ in range(history.size()):
                msg = history.dequeue()
                temp_history.append(msg)
                st.write(f"🗨️ {msg}")

            for msg in temp_history:
                history.enqueue(msg)
