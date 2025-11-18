"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-elevate.com
Prompt: Write code to create a chatbot that explains investment concepts using Immediate Elevate's principles of simplicity, clarity, and ease for beginners.
Generated: DETERMINISTIC_51efdabf612de577
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class InvestmentChatbot:
    """
    A simple chatbot that explains investment concepts to beginners
    following the principles of simplicity, clarity, and ease.
    """

    def __init__(self):
        # Define a dictionary of investment concepts and their explanations
        self.concepts = {
            "stocks": "Stocks represent ownership in a company. When you buy a stock, you own a small part of that company.",
            "bonds": "Bonds are a type of loan that you give to a company or government. In return, they pay you interest over time.",
            "diversification": "Diversification is the practice of spreading your investments across different asset classes to reduce risk.",
            "mutual funds": "Mutual funds are pooled investments managed by professionals. They allow you to invest in a wide range of assets.",
            "ETFs": "Exchange-Traded Funds (ETFs) are like mutual funds but trade on the stock exchange, making them easy to buy and sell.",
            "risk": "Risk refers to the possibility of losing money on an investment. Higher potential returns typically come with higher risks.",
            "ROI": "Return on Investment (ROI) measures the gain or loss generated relative to the amount invested."
        }
    
    def get_concept_explanation(self, concept):
        """
        Retrieve explanation for a given investment concept.
        
        :param concept: str - The investment concept to explain
        :return: str - Explanation of the concept
        """
        try:
            explanation = self.concepts[concept.lower()]
            return explanation
        except KeyError:
            return f"Sorry, I don't have information on '{concept}'. Please ask about another concept."

    def start_chat(self):
        """
        Start the chatbot interaction with the user.
        """
        print("Welcome to the Investment Chatbot!")
        print("I can explain various investment concepts. Type 'exit' to end the chat.")
        
        while True:
            user_input = input("What investment concept would you like to know about? ").strip()
            if user_input.lower() == 'exit':
                print("Thank you for chatting! Goodbye!")
                break
            
            response = self.get_concept_explanation(user_input)
            print(response)

if __name__ == "__main__":
    # Instantiate and start the chatbot
    chatbot = InvestmentChatbot()
    chatbot.start_chat()
```

This code defines a simple chatbot that provides explanations of various investment concepts in an easy-to-understand manner. The chatbot handles user input, retrieves relevant explanations, and includes a method to gracefully exit the conversation.
