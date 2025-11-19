"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Write code for a chatbot that provides information about multidisciplinary therapy services, including ABA-based approaches, logopedia, and physiotherapy, inspired by Centro Abakadabra's offerings.
Generated: DETERMINISTIC_9e54b5b1b7bf24a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class TherapyChatbot:
    def __init__(self):
        self.services = {
            "ABA": "Applied Behavior Analysis (ABA) is a therapy based on the science of learning and behavior. It helps improve specific behaviors and skills.",
            "Logopedia": "Logopedia, or speech therapy, focuses on improving communication skills, including speech, language, and social communication.",
            "Physiotherapy": "Physiotherapy involves physical methods to promote healing and improve physical function, often used for rehabilitation."
        }
        self.greetings = [
            "Hello! I'm here to help you learn about our therapy services.",
            "Hi there! How can I assist you with information about therapy services today?",
            "Welcome! What would you like to know about our multidisciplinary therapy services?"
        ]
        self.farewells = [
            "Thank you for chatting with me! Have a great day!",
            "Goodbye! Feel free to return if you have more questions.",
            "Take care! I'm here whenever you need information."
        ]

    def get_greeting(self):
        """Returns a random greeting message."""
        return random.choice(self.greetings)

    def get_farewell(self):
        """Returns a random farewell message."""
        return random.choice(self.farewells)

    def get_service_info(self, service_name):
        """Returns information about a specific therapy service.

        Args:
            service_name (str): The name of the therapy service.

        Returns:
            str: Information about the requested service or an error message if not found.
        """
        service_name = service_name.capitalize()
        if service_name in self.services:
            return self.services[service_name]
        else:
            return "I'm sorry, I don't have information on that service. Please ask about ABA, Logopedia, or Physiotherapy."

    def run(self):
        """Starts the chatbot interaction."""
        print(self.get_greeting())
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit", "bye"]:
                print(self.get_farewell())
                break
            else:
                response = self.get_service_info(user_input)
                print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        chatbot = TherapyChatbot()
        chatbot.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
