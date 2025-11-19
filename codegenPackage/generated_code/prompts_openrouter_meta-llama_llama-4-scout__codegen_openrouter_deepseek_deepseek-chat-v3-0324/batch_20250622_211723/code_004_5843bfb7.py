"""
Generated Code Metadata:
========================
Original URL: https://bazaar.lol
Prompt: Develop a chatbot that provides resources and support for individuals struggling with social media addiction, using the themes and concerns presented on the webpage.
Generated: DETERMINISTIC_5843bfb721fc2bdd
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
import random

class SocialMediaAddictionChatbot:
    """
    A chatbot that provides resources and support for individuals struggling with social media addiction.
    The chatbot offers educational resources, coping strategies, and support options.
    """

    def __init__(self):
        """
        Initializes the chatbot with predefined resources and responses.
        """
        self.resources = self._load_resources()
        self.greetings = [
            "Hello! I'm here to help you with social media addiction.",
            "Hi there! Let's talk about managing your social media use.",
            "Welcome! I can provide support for social media addiction."
        ]
        self.farewells = [
            "Take care! Remember, small steps lead to big changes.",
            "Goodbye! You're not alone in this journey.",
            "See you later! Stay strong and mindful."
        ]

    def _load_resources(self) -> Dict[str, List[str]]:
        """
        Loads predefined resources from a dictionary (simulated here for simplicity).
        In a production environment, this could load from a database or API.

        Returns:
            Dict[str, List[str]]: A dictionary of resource categories and their content.
        """
        return {
            "education": [
                "Social media addiction can lead to anxiety and reduced productivity.",
                "Excessive use can disrupt sleep patterns and real-life relationships.",
                "Studies show that limiting social media can improve mental health."
            ],
            "strategies": [
                "Set daily time limits for social media apps.",
                "Turn off notifications to reduce distractions.",
                "Engage in offline hobbies to replace screen time."
            ],
            "support": [
                "Consider talking to a mental health professional.",
                "Join support groups for digital detox.",
                "Use apps that track and limit your social media usage."
            ]
        }

    def get_response(self, user_input: str) -> str:
        """
        Generates a response based on the user's input.

        Args:
            user_input (str): The user's input message.

        Returns:
            str: The chatbot's response.
        """
        user_input = user_input.lower().strip()

        if any(word in user_input for word in ["hi", "hello", "hey"]):
            return random.choice(self.greetings)
        elif any(word in user_input for word in ["bye", "goodbye", "exit"]):
            return random.choice(self.farewells)
        elif "education" in user_input:
            return self._get_resource("education")
        elif "strategy" in user_input or "tip" in user_input:
            return self._get_resource("strategies")
        elif "support" in user_input or "help" in user_input:
            return self._get_resource("support")
        else:
            return "I'm not sure how to help with that. Try asking about 'education', 'strategies', or 'support'."

    def _get_resource(self, category: str) -> str:
        """
        Retrieves a random resource from the specified category.

        Args:
            category (str): The resource category ('education', 'strategies', 'support').

        Returns:
            str: A randomly selected resource from the category.
        """
        if category in self.resources:
            return random.choice(self.resources[category])
        else:
            return "Sorry, I couldn't find any resources on that topic."

    def run(self):
        """
        Runs the chatbot in an interactive loop.
        """
        print(random.choice(self.greetings))
        print("You can ask about 'education', 'strategies', or 'support'. Type 'exit' to quit.")

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "bye", "goodbye"]:
                print(random.choice(self.farewells))
                break
            response = self.get_response(user_input)
            print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot = SocialMediaAddictionChatbot()
    chatbot.run()
```
