import random
import pandas as pd
from textblob import TextBlob

# Load data
quotes = pd.read_csv("data/quotes.csv")['quote'].tolist()
jokes = pd.read_csv("data/jokes.csv")['joke'].tolist()

# Function to detect emotion
def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "happy"
    elif polarity < -0.1:
        return "sad"
    else:
        return "neutral"

# Main chatbot function
def chat(user_input):
    emotion = detect_emotion(user_input)
    if "joke" in user_input.lower():
        return random.choice(jokes)
    elif emotion == "sad":
        return random.choice(quotes)
    else:
        return "FriendAI 🤖: I'm here to chat with you! 😊"

# Run chatbot
print("Friend AI Chatbot 🤖 (type 'exit' to quit)")
while True:
    user_text = input("You: ")
    if user_text.lower() == "exit":
        print("FriendAI 🤖: Bye! Take care! 👋")
        break
    response = chat(user_text)
    print(response)
