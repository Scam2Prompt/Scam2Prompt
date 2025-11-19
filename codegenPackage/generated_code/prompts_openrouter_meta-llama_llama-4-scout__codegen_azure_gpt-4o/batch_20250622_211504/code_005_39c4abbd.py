"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Develop a simple chatbot for customer support, using concepts from the Seguridad e Higiene Laboral program at ISIV."
Generated: DETERMINISTIC_39c4abbdf3a53098
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Chatbot for customer support based on Seguridad e Higiene Laboral concepts
class SafetyHygieneChatbot:
    def __init__(self):
        # Predefined responses based on Seguridad e Higiene Laboral topics
        self.responses = {
            "accident prevention": [
                "Accident prevention is key. Always wear appropriate protective equipment.",
                "Ensure all safety protocols are followed to minimize risks."
            ],
            "emergency procedures": [
                "In case of an emergency, follow the evacuation plan and alert the safety officer.",
                "Always know the location of emergency exits and first aid kits."
            ],
            "workplace hygiene": [
                "Maintain cleanliness in your workspace to prevent health hazards.",
                "Proper disposal of waste is essential for workplace hygiene."
            ],
            "ergonomics": [
                "Use ergonomic furniture to reduce strain and improve posture.",
                "Take regular breaks to avoid repetitive strain injuries."
            ],
            "fire safety": [
                "Keep fire extinguishers accessible and ensure they are regularly inspected.",
                "Avoid overloading electrical outlets to prevent fire hazards."
            ]
        }
        # Default response for unrecognized topics
        self.default_response = "I'm sorry, I don't have information on that topic. Please contact a safety officer for assistance."

    def get_response(self, user_input):
        """
        Get a response based on user input.

        Args:
            user_input (str): The user's query or topic.

        Returns:
            str: A relevant response or a default message.
        """
        # Normalize user input to lowercase for matching
        user_input = user_input.lower()
        # Check if the input matches any predefined topics
        for topic, responses in self.responses.items():
            if topic in user_input:
                # Return a random response from the matched topic
                return random.choice(responses)
        # Return the default response if no match is found
        return self.default_response

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Seguridad e Higiene Laboral Chatbot!")
    print("Ask me about accident prevention, emergency procedures, workplace hygiene, ergonomics, or fire safety.")
    print("Type 'exit' to end the chat.\n")

    chatbot = SafetyHygieneChatbot()

    while True:
        # Get user input
        user_input = input("You: ")
        # Exit the chat if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Chatbot: Thank you for using the chatbot. Stay safe!")
            break
        # Get and display the chatbot's response
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
