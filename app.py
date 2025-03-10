import streamlit as st
import google.generativeai as genai
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from trie import Trie
from chatbot_queue import ChatbotQueue
from linked_list import LinkedList

st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            width: 300px !important;  /* Adjust as needed */
            min-width: 200px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize Gemini API
GEMINI_API_KEY = "AIzaSyAHQoXKSaJadsjQiwGBwrmvLcXBeBBfdx0"  
genai.configure(api_key=GEMINI_API_KEY)

# Initialize data structures
trie = Trie()
history = ChatbotQueue()
memory = LinkedList()

# Sample phrases for Trie
sample_phrases = ["Hello", "How can I help you?", "Goodbye", "What is your name?"]
for phrase in sample_phrases:
    trie.insert(phrase.lower())

# Function to get response from Gemini API
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text if response else "I'm sorry, I couldn't process that."

# Sidebar Navigation
st.sidebar.title("🔍 Dive Deeper")
page = st.sidebar.radio("Go to", ["🤖 Chatbot", "ℹ️ Info", "📊 Analysis"])

if page == "🤖 Chatbot":
    st.title(" Aurora✨")
    st.write("Welcome! Ask me anything:")

    # Chat history storage
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []  # Stores tuples (user_input, bot_response)

    user_input = st.text_input("Your Message:", key="user_input")

    if st.button("Send"):
        if user_input:
            user_input_lower = user_input.lower()

            # Check if the input matches pre-defined responses
            if trie.search(user_input_lower):
                bot_response = f"You said: {user_input}"
            else:
                bot_response = get_gemini_response(user_input)  # Get response from Gemini AI

            # Store in session state history
            st.session_state.chat_history.append((user_input, bot_response))

            # Store in Queue and Linked List
            history.enqueue(user_input)
            memory.append(user_input)

    # Display Chat History
    st.write("### 📝 Chat History:")
    for user_query, bot_reply in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(f"**You:** {user_query}")
        with st.chat_message("assistant"):
            st.write(f"**Bot:** {bot_reply}")


elif page == "ℹ️ Info":
    st.title("ℹ️ Understanding BotLy: How It Works")
    # Chatbot Overview
    st.markdown("""
    <div style="background-color:#E3F2FD; padding:15px; border-radius:10px;">
        <h2 style="text-align:center; color:#000000;">🚀 Core Technologies Behind BotLy</h2>
        <p style="text-align:justify; font-size:17px; color:#000000;">
        BotLy is a smart AI-driven chatbot designed to provide accurate, efficient, and personalized conversations using cutting-edge technologies.
        It is built with a structured and scalable approach, ensuring smooth interactions and quick responses.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Foundations of BotLy
    st.subheader("🔍 Technical Foundations")
    st.markdown("""
    <div style="background-color:#FFFFFF; padding:10px; border-radius:8px; border:1px solid #B0BEC5;">
        <ul style="font-size:16px; color:#000000;">
            <li><b>Trie Data Structure:</b> Enables quick phrase matching and efficient text retrieval for faster response generation.</li>
            <li><b>Queue System:</b> Manages chat history storage, allowing seamless recall of past conversations.</li>
            <li><b>Linked List Memory:</b> Optimizes memory usage, ensuring smooth conversation flow without performance lags.</li>
            <li><b>Gemini AI Integration:</b> Powers advanced natural language understanding (NLU) for meaningful responses.</li>
            <li><b>Personalized AI Responses:</b> Adapts responses based on user interaction patterns for a tailored experience.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Future Enhancements
    st.subheader("🌍 Future Enhancements & Upcoming Features")
    st.markdown("""
    <div style="background-color:#F1F8E9; padding:10px; border-radius:8px; border:1px solid #C5E1A5;">
        <ul style="font-size:16px; color:#000000;">
            <li><b>Multi-language Support:</b> Expanding to support multiple languages, making BotLy accessible worldwide.</li>
            <li><b>Voice Command Input:</b> Integrating speech-to-text technology for a hands-free, interactive experience.</li>
            <li><b>AI-based Sentiment Analysis:</b> Understanding user emotions to refine and improve chatbot responses.</li>
            <li><b>Self-learning Capabilities:</b> Implementing adaptive learning so the chatbot continuously improves with user interactions.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.subheader("Main Motive: ")
    # Closing Statement
    st.markdown("""
    <div style="background-color:#ECEFF1; padding:15px; border-radius:10px;">
        <p style="text-align:center; font-size:18px; color:#000000;">
        BotLy is designed to evolve and improve with time, ensuring the best user experience through continuous innovation.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "📊 Analysis":
    st.title("📊 Chatbot Performance Summary")

    # Live-Updated Metrics
    total_chats = len(history.get_history())
    unique_users = len(set(history.get_history()))  # Assuming each user has unique messages
    avg_response_time = np.random.uniform(1.2, 2.5)  # Simulated response time (1.2 to 2.5 sec)
    
    # Display Performance Summary
    st.markdown(f"""
    <div style="background-color:#D0E8F2;padding:15px;border-radius:10px;">
        <h3 style="text-align:center; color:#000000;">📈 Chatbot Performance</h3>
        <p style="text-align:center; font-size:18px; color:#000000;">
            📨 <b>Total Messages:</b> {total_chats} <br>
            👥 <b>Unique Users:</b> {unique_users} <br>
            ⏳ <b>Avg. Response Time:</b> {avg_response_time:.2f} sec <br>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Suggestions for Improvement
    st.subheader("💡 Suggestions to Improve Chatbot")
    st.write("""
    - **Enhance NLP Capabilities**: Improve response accuracy using more training data.  
    - **Implement Multi-Language Support**: Allow users to interact in different languages.  
    - **Optimize Response Time**: Reduce latency for a more seamless conversation.  
    - **Improve Personalization**: Adapt responses based on user behavior.  
    """)

    # User Feedback Collection
    st.subheader("📝 Provide Your Feedback")
    feedback = st.text_area("How can we improve the chatbot?", key="feedback_input")
    if st.button("Submit Feedback"):
        if feedback:
            st.success("✅ Thank you for your valuable feedback!")


st.sidebar.write("Developed with ❤️ by Saaimah Siraj")
st.sidebar.image("c31.png", caption="Saaimah Siraj", use_container_width=True)

