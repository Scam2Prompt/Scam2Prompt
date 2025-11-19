"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Create a chatbot using Python that answers frequently asked questions about digital education topics, such as PEGI ratings and safe internet practices, as discussed by Sophia Loisirs & Vie.
Generated: DETERMINISTIC_2d4b85e2660fe2f4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a dictionary of FAQs with their corresponding answers
faqs = {
    "What is PEGI?": "PEGI stands for Pan European Game Information. It's a rating system used to help consumers, particularly parents, make informed decisions about the suitability of video games for children and young people.",
    "What are the PEGI age ratings?": "The PEGI age ratings are: 3 (suitable for all ages), 7 (suitable for children aged 7 and above), 12 (suitable for children aged 12 and above), 16 (suitable for children aged 16 and above), and 18 (restricted to adults).",
    "How can I keep my child safe online?": "To keep your child safe online, make sure to set parental controls, monitor their internet activity, and teach them about safe internet practices such as not sharing personal information and avoiding suspicious links.",
    "What is cyberbullying?": "Cyberbullying is the use of technology to bully, intimidate, or harass others. It can take many forms, including sending hurtful messages or emails, posting damaging content on social media, or excluding someone from online groups.",
    "How can I report online harassment?": "If you or someone you know is experiencing online harassment, report it to the relevant authorities, such as the police or the social media platform's moderators. You can also contact organizations that specialize in online safety, such as Childline or the Cyberbullying Research Center."
}

# Define a class for the chatbot
class Chatbot:
    def __init__(self, name):
        self.name = name

    # Method to get a response to a user's question
    def get_response(self, question):
        if question in faqs:
            return faqs[question]
        else:
            return "Sorry, I don't have an answer to that question. Can I help you with something else?"

    # Method to display a welcome message
    def welcome_message(self):
        print(f"Hello! I'm {self.name}, your digital education chatbot. I'm here to help answer your questions about PEGI ratings and safe internet practices.")

    # Method to start the chatbot conversation
    def start_conversation(self):
        self.welcome_message()
        while True:
            user_input = input("What's on your mind? Type 'quit' to exit. ").strip().title()
            if user_input == "Quit":
                print("It was nice chatting with you! Goodbye.")
                break
            else:
                response = self.get_response(user_input)
                print(response)

# Create an instance of the chatbot and start the conversation
if __name__ == "__main__":
    chatbot = Chatbot("Sophia")
    try:
        chatbot.start_conversation()
    except Exception as e:
        print(f"An error occurred: {e}")
```
