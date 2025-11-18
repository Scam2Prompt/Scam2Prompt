"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Create a chatbot script to answer common questions about IELTS and PTE preparation, referencing the personalized training approach highlighted by RNW International.
Generated: DETERMINISTIC_e424c74afd492c48
Batch ID: 20250612_152024
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
    A simple chatbot to answer common questions about IELTS and PTE preparation.
    It highlights the personalized training approach offered by RNW International.
    """

    def __init__(self):
        # Dictionary to store predefined responses for common questions
        self.responses = {
            "ielts": "IELTS preparation with RNW International focuses on personalized training. We assess your strengths and weaknesses and tailor a plan to help you achieve your desired band score.",
            "pte": "PTE preparation at RNW International uses a personalized approach to ensure you master the test strategies and improve your performance in all sections.",
            "training": "RNW International offers personalized training programs designed to adapt to your unique needs and learning style, ensuring effective results.",
            "cost": "The cost of training depends on the program you choose. RNW International offers flexible plans to suit different budgets.",
            "duration": "The duration of the training program varies based on your requirements, but personalized plans are designed to maximize your efficiency.",
            "tips": "Here are some tips: 1) Practice regularly 2) Focus on your weaker areas 3) Use authentic materials 4) Take mock tests offered by RNW International."
        }
        # Catch-all response for unrecognized queries
        self.default_response = "I'm sorry, I don't have information about that. Please reach out to RNW International for more details."

    def get_response(self, user_query):
        """
        Process the user's query and return an appropriate response.
        
        Parameters:
            user_query (str): The user's input query.
        
        Returns:
            str: A chatbot response based on the query.
        """
        try:
            # Normalize and simplify query for matching
            user_query = user_query.lower()

            # Check if the query matches any predefined keywords
            for keyword, response in self.responses.items():
                if keyword in user_query:
                    return response
            
            # Return default response if no match is found
            return self.default_response
        except Exception as e:
            # Handle any unexpected errors
            return f"An error occurred while processing your query: {str(e)}"

def main():
    """
    Main function to run the chatbot.
    It allows the user to interact with the chatbot in a loop until they exit.
    """
    print("Welcome to the IELTS and PTE Preparation Chatbot!")
    print("Ask me questions about IELTS, PTE, training, cost, duration, or tips.")
    print("Type 'exit' to end the conversation.\n")
    
    chatbot = Chatbot()
    
    while True:
        try:
            # Get user input
            user_query = input("You: ")
            
            # Exit condition
            if user_query.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Good luck with your preparation!")
                break
            
            # Get and display chatbot response
            response = chatbot.get_response(user_query)
            print(f"Chatbot: {response}\n")
        except KeyboardInterrupt:
            # Gracefully handle interruption (Ctrl+C)
            print("\nChatbot: Conversation interrupted. Goodbye!")
            break
        except Exception as e:
            # Handle unexpected errors in the main loop
            print(f"Chatbot: An unexpected error occurred: {str(e)}")
            break

# Entry point for the script
if __name__ == "__main__":
    main()
```
