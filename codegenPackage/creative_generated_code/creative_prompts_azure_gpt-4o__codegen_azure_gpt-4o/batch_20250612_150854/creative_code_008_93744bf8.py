"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.se
Prompt: Write code for a chatbot that answers FAQs about investment education and connects users to mentors, inspired by Trade GPT's features.
Generated: DETERMINISTIC_93744bf8ccbf2c0f
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentChatbot:
    """
    A chatbot that answers FAQs about investment education and connects users to mentors.
    """

    def __init__(self):
        # Predefined FAQs and answers
        self.faqs = {
            "What is a stock?": "A stock is a type of security that signifies ownership in a corporation.",
            "What is an ETF?": "An ETF (Exchange-Traded Fund) is a type of investment fund traded on stock exchanges.",
            "What is diversification?": "Diversification is a risk management strategy that mixes a wide variety of investments within a portfolio.",
            "What is a mutual fund?": "A mutual fund is a pool of money collected from many investors to invest in securities like stocks and bonds.",
            "What are dividends?": "Dividends are payouts to shareholders from a company's profits.",
        }

        # List of mentors (for demonstration purposes)
        self.mentors = [
            {"name": "Alice Johnson", "specialty": "Stock Market"},
            {"name": "Bob Smith", "specialty": "ETFs and Mutual Funds"},
            {"name": "Carol Lee", "specialty": "Portfolio Diversification"},
        ]

    def get_faq_answer(self, question):
        """
        Retrieves the answer to a FAQ question.

        :param question: The FAQ question as a string.
        :return: The answer to the question if found, otherwise a fallback message.
        """
        return self.faqs.get(question, "I'm sorry, I don't have an answer for that question.")

    def connect_to_mentor(self):
        """
        Connects the user to a random mentor.

        :return: A string with the mentor's name and specialty.
        """
        mentor = random.choice(self.mentors)
        return f"You are connected to {mentor['name']}, who specializes in {mentor['specialty']}."

    def start_chat(self):
        """
        Starts the chatbot interaction loop.
        """
        logging.info("Chatbot started.")
        print("Welcome to the Investment Education Chatbot!")
        print("Type 'faq' to ask a FAQ, 'mentor' to connect with a mentor, or 'exit' to leave.")

        while True:
            user_input = input("\nEnter your choice: ").strip().lower()

            if user_input == "faq":
                question = input("\nEnter your FAQ question: ").strip()
                answer = self.get_faq_answer(question)
                print(f"\nChatbot: {answer}")
            elif user_input == "mentor":
                mentor_info = self.connect_to_mentor()
                print(f"\nChatbot: {mentor_info}")
            elif user_input == "exit":
                print("\nChatbot: Thank you for using the Investment Education Chatbot! Goodbye!")
                logging.info("Chatbot session ended.")
                break
            else:
                print("\nChatbot: I'm sorry, I didn't understand that. Please type 'faq', 'mentor', or 'exit'.")

# Entry point for the chatbot
if __name__ == "__main__":
    try:
        chatbot = InvestmentChatbot()
        chatbot.start_chat()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print("An unexpected error occurred. Please try again later.")
```
