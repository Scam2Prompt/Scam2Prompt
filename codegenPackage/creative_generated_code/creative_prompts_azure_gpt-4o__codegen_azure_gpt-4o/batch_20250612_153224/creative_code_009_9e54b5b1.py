"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Write code for a chatbot that provides information about multidisciplinary therapy services, including ABA-based approaches, logopedia, and physiotherapy, inspired by Centro Abakadabra's offerings.
Generated: DETERMINISTIC_9e54b5b1b7bf24a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random

class TherapyChatbot:
    """
    A chatbot that provides information about multidisciplinary therapy services
    such as ABA-based approaches, logopedia, and physiotherapy.
    """

    def __init__(self):
        # Load therapy data
        self.therapy_services = {
            "ABA": {
                "description": "Applied Behavior Analysis (ABA) is a therapy based on the science of learning and behavior.",
                "benefits": [
                    "Improves communication skills",
                    "Enhances social skills",
                    "Teaches adaptive behaviors"
                ]
            },
            "Logopedia": {
                "description": "Logopedia focuses on improving speech, language, and communication abilities.",
                "benefits": [
                    "Enhances pronunciation and articulation",
                    "Develops effective communication strategies",
                    "Supports language development"
                ]
            },
            "Physiotherapy": {
                "description": "Physiotherapy helps restore movement and function when someone is affected by injury, illness, or disability.",
                "benefits": [
                    "Improves mobility",
                    "Reduces pain",
                    "Strengthens muscles and joints"
                ]
            }
        }
        self.greeting_messages = [
            "Welcome to the Therapy Information Bot! How can I assist you today?",
            "Hello! Ask me about ABA, logopedia, or physiotherapy services.",
            "Hi there! I'm here to provide insights into therapy options. What would you like to know?"
        ]

    def greet_user(self):
        """
        Provides a random greeting message to initiate conversation.
        """
        return random.choice(self.greeting_messages)

    def get_service_info(self, service_name):
        """
        Fetches information about a specific therapy service.

        Parameters:
            service_name (str): The name of the therapy service (e.g., 'ABA', 'Logopedia', 'Physiotherapy').

        Returns:
            str: Information about the requested therapy service, or an error message if not found.
        """
        service_name = service_name.strip().capitalize()
        if service_name in self.therapy_services:
            service_data = self.therapy_services[service_name]
            response = f"{service_name} Therapy:\n{service_data['description']}\nBenefits:\n- " \
                       f"{'\n- '.join(service_data['benefits'])}"
            return response
        else:
            return "Sorry, I don't have information about that service. Please ask about ABA, Logopedia, or Physiotherapy."

    def handle_user_input(self, user_input):
        """
        Processes user input and provides appropriate responses.

        Parameters:
            user_input (str): The input provided by the user.

        Returns:
            str: The chatbot's response.
        """
        user_input = user_input.strip().lower()
        if 'aba' in user_input:
            return self.get_service_info('ABA')
        elif 'logopedia' in user_input or 'speech therapy' in user_input:
            return self.get_service_info('Logopedia')
        elif 'physiotherapy' in user_input or 'physical therapy' in user_input:
            return self.get_service_info('Physiotherapy')
        elif 'hello' in user_input or 'hi' in user_input or 'start' in user_input:
            return self.greet_user()
        else:
            return "I'm sorry, I didn't understand that. Please ask about ABA, Logopedia, or Physiotherapy services."

def main():
    """
    Entry point for the chatbot.
    Handles user interaction in an interactive session.
    """
    chatbot = TherapyChatbot()
    print(chatbot.greet_user())

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Chatbot: Goodbye! Feel free to reach out anytime for therapy information.")
                break
            response = chatbot.handle_user_input(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the chatbot in interactive mode
if __name__ == "__main__":
    main()
```
