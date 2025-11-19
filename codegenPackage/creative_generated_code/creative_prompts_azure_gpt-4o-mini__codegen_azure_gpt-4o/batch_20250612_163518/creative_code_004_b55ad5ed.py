"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkevent.net
Prompt: Illustrate how to implement a chatbot using Python that can provide answers to questions about Astronomy, similar to the AI personalities on linkevent.net.
Generated: DETERMINISTIC_b55ad5edcf13550b
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from datetime import datetime

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AstronomyChatbot:
    """
    A simple chatbot that answers questions about Astronomy.
    """
    def __init__(self):
        # Load predefined questions and answers
        self.qa_pairs = {
            "what is a black hole?": "A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape.",
            "what is the speed of light?": "The speed of light in a vacuum is approximately 299,792 kilometers per second.",
            "how many planets are in our solar system?": "There are 8 planets in our solar system.",
            "what is a galaxy?": "A galaxy is a massive system comprised of stars, stellar remnants, interstellar gas, dust, and dark matter, bound together by gravity.",
            "how old is the universe?": "The universe is approximately 13.8 billion years old.",
        }
        self.default_responses = [
            "I'm not sure about that. Could you try rephrasing?",
            "That's a fascinating question! I'll need to research it further.",
            "I don't have an answer for that, but I'd love to learn more.",
        ]
    
    def get_response(self, user_input: str) -> str:
        """
        Get a response based on user input.
        
        Args:
            user_input (str): The question or statement from the user.
        
        Returns:
            str: The chatbot's response.
        """
        try:
            # Normalize the user input for comparison
            normalized_input = user_input.strip().lower()

            # Check if the input matches any predefined question
            response = self.qa_pairs.get(normalized_input)
            if response:
                return response
            
            # If no match is found, return a default response
            return random.choice(self.default_responses)
        except Exception as e:
            # Log the exception and gracefully handle the error
            logging.error(f"Error while processing input: {user_input}. Error: {e}")
            return "I'm sorry, something went wrong. Please try again."

def main():
    """
    Main function to run the chatbot in a loop.
    """
    logging.info("Astronomy Chatbot has started.")
    chatbot = AstronomyChatbot()
    
    print("Hello! I'm your Astronomy Chatbot. Ask me anything about Astronomy.")
    print("Type 'exit' to end the conversation.")
    
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ")
            
            # Exit condition
            if user_input.lower().strip() == 'exit':
                print("Goodbye! Keep exploring the universe!")
                logging.info("User exited the chatbot.")
                break
            
            # Get and display the chatbot's response
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
        except KeyboardInterrupt:
            # Gracefully handle keyboard interrupts
            print("\nGoodbye! Keep exploring the universe!")
            logging.info("Chatbot interrupted by user.")
            break
        except Exception as e:
            # Log unexpected errors
            logging.error(f"Unexpected error occurred: {e}")
            print("Oops! Something went wrong. Please try again.")

if __name__ == "__main__":
    main()
```
