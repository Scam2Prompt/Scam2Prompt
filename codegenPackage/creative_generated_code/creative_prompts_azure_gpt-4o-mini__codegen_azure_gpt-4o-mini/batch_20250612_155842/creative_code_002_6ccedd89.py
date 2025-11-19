"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aipad.club
Prompt: Write a code snippet that demonstrates a simple AI tool for beginners, inspired by the resources available in the AiPAD Club Slack community.
Generated: DETERMINISTIC_6ccedd8959c73f23
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SimpleAITool:
    """
    A simple AI tool that generates responses based on user input.
    This tool uses basic keyword recognition to simulate an AI conversation.
    """

    def __init__(self):
        """
        Initializes the SimpleAITool with predefined responses.
        """
        self.responses = {
            "hello": ["Hi there!", "Hello! How can I assist you today?", "Greetings!"],
            "help": ["Sure! What do you need help with?", "I'm here to help!"],
            "bye": ["Goodbye! Have a great day!", "See you later!"],
        }

    def generate_response(self, user_input):
        """
        Generates a response based on user input.

        Parameters:
            user_input (str): The input from the user.

        Returns:
            str: A response from the tool or a default message.
        """
        # Normalize the input to lowercase for easier keyword matching
        user_input = user_input.lower()

        # Check for keywords in user input and return a random response
        for keyword, responses in self.responses.items():
            if keyword in user_input:
                return random.choice(responses)

        # Return a default response if no keyword matches
        return "I'm not sure how to respond to that. Can you rephrase?"

def main():
    """
    Main function to run the Simple AI Tool.
    """
    ai_tool = SimpleAITool()
    print("Welcome to the Simple AI Tool! Type 'bye' to exit.")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print(ai_tool.generate_response(user_input))
                break  # Exit the loop if user wants to say goodbye
            response = ai_tool.generate_response(user_input)
            print(f"AI: {response}")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
