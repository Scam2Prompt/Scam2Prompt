"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Develop a chatbot using Python and NLP libraries that can answer questions about the "Vivir es Convivir" program and its focus on fostering civic values in children.
Generated: DETERMINISTIC_3d297bed885eec43
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import nltk
from nltk.chat.util import Chat, reflections

# Ensure that the necessary NLTK resources are downloaded
nltk.download('punkt')

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today regarding the 'Vivir es Convivir' program?"]
    ],
    [
        r"what is the 'vivir es convivir' program?",
        ["'Vivir es Convivir' is a program focused on fostering civic values in children through various educational activities."]
    ],
    [
        r"what are civic values?",
        ["Civic values include respect, responsibility, fairness, caring, and citizenship, which are essential for community living."]
    ],
    [
        r"how does the program help children?",
        ["The program helps children by engaging them in activities that promote teamwork, empathy, and social responsibility."]
    ],
    [
        r"tell me more about the activities",
        ["Activities include workshops, community service projects, and interactive games that teach civic values."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! If you have any more questions, feel free to ask."]
    ],
    [
        r"quit|exit",
        ["Thank you for chatting! Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't have an answer for that. Can you ask something else about the program?"]
    ]
]

# Create a chatbot class
class CivicValuesChatbot:
    def __init__(self):
        self.chatbot = Chat(pairs, reflections)

    def start_chat(self):
        print("Welcome to the 'Vivir es Convivir' Chatbot! Type 'quit' to exit.")
        try:
            self.chatbot.converse()
        except Exception as e:
            print(f"An error occurred: {e}")

# Main function to run the chatbot
if __name__ == "__main__":
    chatbot = CivicValuesChatbot()
    chatbot.start_chat()
```

Make sure to install the NLTK library if you haven't already:

```bash
pip install nltk
```
