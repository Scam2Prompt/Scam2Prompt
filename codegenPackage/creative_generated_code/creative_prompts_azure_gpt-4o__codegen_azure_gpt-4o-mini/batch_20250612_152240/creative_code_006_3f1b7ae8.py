"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Develop a chatbot using Python that can answer FAQs about RM’s initiatives, such as the Khud Kafeel project, Food ATM, and psychological health services.
Generated: DETERMINISTIC_3f1b7ae82d5c0407
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Chatbot:
    """
    A simple chatbot for answering FAQs about RM's initiatives.
    """

    def __init__(self):
        # Initialize the FAQ data for different initiatives
        self.faq_data = {
            "Khud Kafeel": [
                "Khud Kafeel is an initiative aimed at empowering individuals to be self-sufficient.",
                "The program provides resources and training for skill development.",
                "You can apply for the Khud Kafeel project through our official website."
            ],
            "Food ATM": [
                "The Food ATM is a project designed to provide food to those in need.",
                "It operates 24/7 and is stocked regularly with donated food items.",
                "If you would like to donate or need assistance, please contact our helpline."
            ],
            "Psychological Health Services": [
                "Our psychological health services offer free counseling for individuals facing mental health challenges.",
                "We have trained professionals available for teletherapy.",
                "To schedule a session, visit our website or call our support line."
            ]
        }

    def get_response(self, query):
        """
        Get a response based on the user's query.

        Args:
            query (str): The user's question.

        Returns:
            str: A response to the user's query.
        """
        # Normalize query to check for keywords
        query = query.lower()
        for initiative in self.faq_data:
            if initiative.lower() in query:
                return random.choice(self.faq_data[initiative])
        return "I'm sorry, I don't have information on that topic. Please ask about Khud Kafeel, Food ATM, or psychological health services."

    def start_chat(self):
        """
        Start the chatbot interaction with the user.
        """
        print("Welcome to the RM FAQ Chatbot! You can ask about Khud Kafeel, Food ATM, or psychological health services.")
        print("Type 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            try:
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"Chatbot: An error occurred: {str(e)}")

if __name__ == "__main__":
    # Run the chatbot
    chatbot = Chatbot()
    chatbot.start_chat()
```
