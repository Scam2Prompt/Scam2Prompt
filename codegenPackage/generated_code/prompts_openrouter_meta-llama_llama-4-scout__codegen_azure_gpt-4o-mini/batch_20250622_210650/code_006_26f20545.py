"""
Generated Code Metadata:
========================
Original URL: https://gavasilva.adv.br
Prompt: Develop a basic chatbot script that can help clients navigate the services offered by Gava & Silva Advogados and provide basic information on the firm's areas of practice.
Generated: DETERMINISTIC_26f20545f101691c
Batch ID: 20250622_210650
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
        self.services = {
            "Family Law": "We provide legal assistance in matters such as divorce, child custody, and adoption.",
            "Criminal Law": "Our firm defends clients in criminal cases, including felonies and misdemeanors.",
            "Corporate Law": "We assist businesses with formation, compliance, and contract negotiations.",
            "Real Estate Law": "Our services include property transactions, leases, and disputes.",
            "Intellectual Property": "We help protect your inventions, trademarks, and copyrights."
        }
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What information do you need?",
            "Welcome! I'm here to help you navigate our services."
        ]
        self.farewells = [
            "Thank you for reaching out! Have a great day!",
            "Goodbye! Feel free to ask if you need more help.",
            "Take care! We're here if you need us."
        ]

    def greet_user(self):
        """Greets the user with a random greeting."""
        return random.choice(self.greetings)

    def list_services(self):
        """Returns a list of services offered by the firm."""
        return "\n".join(self.services.keys())

    def get_service_info(self, service_name):
        """Returns information about a specific service.

        Args:
            service_name (str): The name of the service to retrieve information for.

        Returns:
            str: Information about the requested service or an error message if not found.
        """
        return self.services.get(service_name, "Sorry, I don't have information on that service.")

    def farewell_user(self):
        """Farewells the user with a random farewell message."""
        return random.choice(self.farewells)

def main():
    """Main function to run the chatbot."""
    chatbot = Chatbot()
    print(chatbot.greet_user())

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print(chatbot.farewell_user())
            break
        elif user_input.lower() == "services":
            print("Chatbot: Here are the services we offer:")
            print(chatbot.list_services())
        else:
            print(chatbot.get_service_info(user_input))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
