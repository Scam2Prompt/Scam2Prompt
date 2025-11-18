"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afebi.org
Prompt: Develop a chatbot using a natural language processing library that can answer questions about AFEBI's activities, such as "What is the agenda for Kongres ke-12 AFEBI 2024?"
Generated: DETERMINISTIC_9aa3b29776b2294b
Batch ID: 20250612_153526
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

# Ensure the NLTK data is available for the chatbot to use
nltk.download('punkt')

# Define a list of pairs, which consist of patterns and responses
pairs = [
    [
        r"what is the agenda for kongres ke%-12 afebi 2024?",
        "The agenda for Kongres ke-12 AFEBI 2024 includes discussions on digital transformation, financial literacy, and the impact of fintech on the economy."
    ],
    [
        r"what are the goals of afebi?",
        "AFEBI aims to promote the development of the fintech industry in Indonesia and serves as a platform for collaboration among stakeholders."
    ],
    [
        r"how can I become a member of afebi?",
        "You can become a member of AFEBI by visiting our official website and filling out the membership application form."
    ],
    [
        r"what is afebi?",
        "AFEBI stands for Asosiasi Fintech Indonesia, which is the Indonesian Fintech Association that supports and develops the fintech ecosystem."
    ],
    [
        r"quit",
        "Thank you for chatting! If you have more questions, feel free to ask."
    ],
]

# Create a chatbot using the defined pairs and reflections
def create_chatbot():
    print("AFEBI Chatbot is now running! Type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)
    return chatbot

# Main function to run the chatbot
def main():
    try:
        chatbot = create_chatbot()
        # Start the conversation
        chatbot.converse()
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
