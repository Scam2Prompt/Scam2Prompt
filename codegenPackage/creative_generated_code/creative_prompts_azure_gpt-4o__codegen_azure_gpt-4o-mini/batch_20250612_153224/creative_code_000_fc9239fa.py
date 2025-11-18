"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Write Python code to simulate a chatbot that provides information about programs for victims of human trafficking, similar to the virtual assistant described on Fundación Munasim Kullakita's website.
Generated: DETERMINISTIC_fc9239faf368544f
Batch ID: 20250612_153224
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
    A simple chatbot that provides information about programs for victims of human trafficking.
    """

    def __init__(self):
        # Initialize the chatbot with predefined responses
        self.programs_info = {
            "shelter": "We provide safe shelters for victims of human trafficking, offering a secure environment and support services.",
            "counseling": "Counseling services are available to help victims process their experiences and regain control of their lives.",
            "legal_support": "We assist victims in navigating legal processes, including obtaining restraining orders and legal representation.",
            "healthcare": "Healthcare services, including mental health support, are provided to ensure the well-being of victims.",
            "employment": "We offer job training and placement services to help victims rebuild their lives and gain independence."
        }
        self.welcome_message = "Hello! I'm here to provide information about programs for victims of human trafficking. How can I assist you today?"

    def get_welcome_message(self):
        """Return the welcome message of the chatbot."""
        return self.welcome_message

    def get_program_info(self, program_name):
        """
        Retrieve information about a specific program.
        
        Args:
            program_name (str): The name of the program to get information about.

        Returns:
            str: Information about the requested program or an error message if the program is not found.
        """
        try:
            # Normalize the input to handle case sensitivity
            normalized_name = program_name.lower()
            if normalized_name in self.programs_info:
                return self.programs_info[normalized_name]
            else:
                return "Sorry, I don't have information about that program. Please try another."
        except Exception as e:
            return f"An error occurred while retrieving the information: {str(e)}"

    def chat(self):
        """Start the chatbot interaction."""
        print(self.get_welcome_message())
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Chatbot: Thank you for reaching out. Take care!")
                break
            response = self.get_program_info(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        chatbot = Chatbot()
        chatbot.chat()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
