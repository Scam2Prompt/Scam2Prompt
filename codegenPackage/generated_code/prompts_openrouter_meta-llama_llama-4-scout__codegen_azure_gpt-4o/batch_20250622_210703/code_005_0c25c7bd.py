"""
Generated Code Metadata:
========================
Original URL: https://g28haber.com
Prompt: Develop a simple chatbot that provides information about the Giresun University team’s success in artistic gymnastics.
Generated: DETERMINISTIC_0c25c7bd43eb2eca
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class GymnasticsChatbot:
    """
    A simple chatbot that provides information about the Giresun University team's success
    in artistic gymnastics.
    """

    def __init__(self):
        # Predefined responses about the team's success
        self.responses = [
            "The Giresun University artistic gymnastics team has won multiple regional championships.",
            "In 2022, the team secured first place in the national artistic gymnastics competition.",
            "The team is known for its exceptional performance in floor exercises and vault events.",
            "Giresun University's gymnastics team consistently ranks among the top 5 teams in Turkey.",
            "The team has produced several athletes who have gone on to compete internationally."
        ]

    def get_response(self, user_input):
        """
        Generate a response based on user input.

        Parameters:
            user_input (str): The user's input or question.

        Returns:
            str: A response about the team's success.
        """
        # Normalize user input to handle case-insensitivity
        user_input = user_input.lower()

        # Check if the user input contains keywords related to gymnastics success
        if "success" in user_input or "gymnastics" in user_input or "team" in user_input:
            # Randomly select a response from the predefined list
            return random.choice(self.responses)
        else:
            # Default response for unrecognized input
            return "I'm here to provide information about the Giresun University gymnastics team's success. Please ask me about their achievements!"

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Giresun University Gymnastics Chatbot!")
    print("Ask me about the team's success in artistic gymnastics. Type 'exit' to quit.")

    chatbot = GymnasticsChatbot()

    while True:
        try:
            # Get user input
            user_input = input("\nYou: ")

            # Exit condition
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye! Have a great day!")
                break

            # Generate and display the chatbot's response
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: Oops! Something went wrong. Error: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
