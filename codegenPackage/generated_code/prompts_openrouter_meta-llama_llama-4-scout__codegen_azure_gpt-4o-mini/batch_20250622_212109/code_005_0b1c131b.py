"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Develop a simple chatbot script that provides information about museum activities for visitors and families, inspired by the content on the Museo Vasca Votiva di Noceto site.
Generated: DETERMINISTIC_0b1c131b140bca2b
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class MuseumChatbot:
    def __init__(self):
        self.activities = {
            "family": [
                "Join our family workshops every Saturday from 10 AM to 12 PM.",
                "Don't miss our interactive storytelling sessions on Sundays at 2 PM.",
                "Explore our scavenger hunt designed for families every weekend!"
            ],
            "exhibitions": [
                "Visit our latest exhibition on ancient artifacts, open until the end of the month.",
                "Check out the special exhibition on local artists, running through next month.",
                "Our photography exhibition showcases the beauty of Noceto, open daily."
            ],
            "events": [
                "We host monthly lectures on art history, the next one is on the 15th.",
                "Join us for our annual museum gala, tickets available on our website.",
                "Participate in our community art day, happening on the first Saturday of each month."
            ]
        }
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What information are you looking for?",
            "Welcome! Feel free to ask about our museum activities."
        ]
        self.farewells = [
            "Thank you for visiting! Have a great day!",
            "Goodbye! We hope to see you at the museum soon!",
            "Take care! Enjoy your time at the museum!"
        ]

    def get_greeting(self):
        """Return a random greeting message."""
        return random.choice(self.greetings)

    def get_farewell(self):
        """Return a random farewell message."""
        return random.choice(self.farewells)

    def get_activities(self, category):
        """Return activities based on the specified category."""
        try:
            if category in self.activities:
                return random.choice(self.activities[category])
            else:
                raise ValueError("Invalid category. Please choose 'family', 'exhibitions', or 'events'.")
        except ValueError as e:
            return str(e)

    def run(self):
        """Run the chatbot interaction loop."""
        print(self.get_greeting())
        while True:
            user_input = input("Ask about museum activities (type 'exit' to quit): ").strip().lower()
            if user_input == 'exit':
                print(self.get_farewell())
                break
            elif user_input in self.activities:
                print(self.get_activities(user_input))
            else:
                print("Please specify a category: 'family', 'exhibitions', or 'events'.")

if __name__ == "__main__":
    chatbot = MuseumChatbot()
    chatbot.run()
```
