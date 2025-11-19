"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Create a chatbot using Python that answers questions about Springs International Ministries’ programs, such as “Where was Jesus on Saturday?” or details about Mission 2030.
Generated: DETERMINISTIC_b7ca9ed3814b2009
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Chatbot:
    def __init__(self):
        # Initialize the chatbot with a set of predefined responses
        self.responses = {
            "where was jesus on saturday": [
                "On Saturday, Jesus was in the tomb, resting after His crucifixion.",
                "According to the Gospels, Jesus was in the tomb on Saturday."
            ],
            "what is mission 2030": [
                "Mission 2030 is an initiative aimed at expanding our outreach and impact by the year 2030.",
                "The goal of Mission 2030 is to reach more communities and share the message of hope."
            ],
            "what programs does springs international ministries offer": [
                "Springs International Ministries offers various programs including community outreach, educational workshops, and spiritual retreats.",
                "We have programs focused on youth engagement, family support, and global missions."
            ]
        }

    def get_response(self, user_input):
        """
        Get a response from the chatbot based on user input.
        
        Args:
            user_input (str): The question or statement from the user.
        
        Returns:
            str: A response from the chatbot or a default message if no match is found.
        """
        # Normalize the user input to lower case for easier matching
        normalized_input = user_input.lower().strip()
        
        # Check if the input matches any known questions
        if normalized_input in self.responses:
            return random.choice(self.responses[normalized_input])
        else:
            return "I'm sorry, I don't have information on that. Can you ask something else?"

    def run(self):
        """
        Run the chatbot in a loop, allowing user interaction until they choose to exit.
        """
        print("Welcome to the Springs International Ministries Chatbot!")
        print("You can ask me about our programs or specific questions like 'Where was Jesus on Saturday?'.")
        print("Type 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            
            # Get and print the chatbot's response
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Create an instance of the Chatbot and run it
    try:
        chatbot = Chatbot()
        chatbot.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
