"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1o2.ir
Prompt: Implement a chatbot that can ask users random questions related to their favorite sitcoms or ice cream flavors, drawing from the style of dex.chat.
Generated: DETERMINISTIC_ed1c864adf458b8b
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ChatBot:
    def __init__(self):
        """
        Initializes the ChatBot with predefined questions about sitcoms and ice cream flavors.
        """
        self.sitcom_questions = [
            "Who is your favorite character from Friends?",
            "What is the funniest moment you recall from The Office?",
            "Which sitcom do you think has the best theme song?",
            "Do you prefer Parks and Recreation over Brooklyn Nine-Nine?",
            "Which sitcom's humor resonates with you the most?"
        ]
        
        self.ice_cream_questions = [
            "What is your favorite ice cream flavor?",
            "Do you prefer cones or cups for your ice cream?",
            "What toppings do you love on ice cream?",
            "Have you ever tried mixing different ice cream flavors?",
            "What is the most unique ice cream flavor you've tasted?"
        ]

    def ask_random_question(self):
        """
        Asks a random question about sitcoms or ice cream flavors.
        """
        # Combine questions into one list for randomness
        all_questions = self.sitcom_questions + self.ice_cream_questions
        
        # Pick a random question
        question = random.choice(all_questions)
        
        return question

def main():
    """
    Main function to interact with the ChatBot.
    """
    try:
        print("Welcome to the ChatBot!")
        chatbot = ChatBot()
        
        while True:
            command = input("\nType 'ask' to get a random question or 'exit' to quit: ").strip().lower()
            
            if command == 'ask':
                question = chatbot.ask_random_question()
                print("\nChatBot asks: " + question)
            elif command == 'exit':
                print("Goodbye! Thanks for chatting!")
                break
            else:
                print("Invalid input. Please type 'ask' or 'exit'.")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
