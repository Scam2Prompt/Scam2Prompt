"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://srhfoundation.ca
Prompt: Develop a chatbot using an NLP library that can answer questions about SRH Life Foundation articles, such as "What are the benefits of proper waste disposal?" or "How does dental trauma affect oral health?"
Generated: DETERMINISTIC_56402ed91db9ae3d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import nltk
from nltk.chat.util import Chat, reflections
import re

# Ensure the nltk packages are downloaded
nltk.download('punkt')

# Define a set of pairs for the chatbot's response
pairs = [
    [
        r'What are the benefits of proper waste disposal\?',
        ['Proper waste disposal helps protect the environment, conserves resources, and reduces pollution.']
    ],
    [
        r'How does dental trauma affect oral health\?',
        ['Dental trauma can lead to pain, infection, misalignment of teeth, and long-term dental issues if not treated promptly.']
    ],
    [
        r'What is the purpose of the SRH Life Foundation\?',
        ['The SRH Life Foundation aims to promote health literacy and improve community health outcomes through education and resources.']
    ],
    [
        r'Hi|Hello|Hey',
        ['Hello! How can I assist you today?']
    ],
    [
        r'Exit|Bye',
        ['Goodbye! Have a great day!']
    ],
    [
        r'(.*)',
        ['I am not sure about that. Can you please provide more details or ask another question?']
    ]
]

# Create a chatbot class
class Chatbot:
    def __init__(self, pairs):
        self.chatbot = Chat(pairs, reflections)

    def start_chat(self):
        print("Welcome to the SRH Life Foundation Chatbot! Type 'Exit' to end the chat.")
        try:
            self.chatbot.converse()
        except (KeyboardInterrupt, SystemExit):
            print("\nChat ended.")

if __name__ == "__main__":
    # Create and start the chatbot
    srh_chatbot = Chatbot(pairs)
    srh_chatbot.start_chat()
```

### Requirements:
- Ensure you have the `nltk` library installed. You can install it using:
  ```
  pip install nltk
  ```
- Run the code in a Python environment. Interact with the chatbot by asking questions related to the SRH Life Foundation articles.
