"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Implement a chatbot that can ask users random questions related to their favorite sitcoms or ice cream flavors, drawing from the style of dex.chat.
Generated: DETERMINISTIC_ed1c864adf458b8b
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional

class ChatBot:
    """
    A chatbot that asks users random questions about their favorite sitcoms or ice cream flavors.
    Designed with a style similar to dex.chat.
    """

    def __init__(self):
        """Initialize the chatbot with predefined questions and responses."""
        self.sitcom_questions: List[str] = [
            "What's your favorite sitcom of all time?",
            "Which sitcom character do you relate to the most?",
            "If you could live in any sitcom universe, which would it be?",
            "What's the funniest sitcom episode you've ever watched?",
            "Who is your favorite sitcom duo or group?"
        ]

        self.ice_cream_questions: List[str] = [
            "What's your all-time favorite ice cream flavor?",
            "If you could invent a new ice cream flavor, what would it be?",
            "Do you prefer cones or cups for your ice cream?",
            "What's the weirdest ice cream flavor you've ever tried?",
            "Do you like toppings on your ice cream? If so, which ones?"
        ]

        self.responses: Dict[str, List[str]] = {
            "sitcom": [
                "That's a great choice!",
                "Interesting pick!",
                "I love that one too!",
                "Classic!",
                "You have good taste!"
            ],
            "ice_cream": [
                "Yummy!",
                "That sounds delicious!",
                "I'd love to try that!",
                "Great choice!",
                "One of my favorites too!"
            ]
        }

    def _get_random_question(self, category: str) -> str:
        """
        Get a random question from the specified category.

        Args:
            category: Either 'sitcom' or 'ice_cream'.

        Returns:
            A random question from the category.

        Raises:
            ValueError: If the category is invalid.
        """
        if category == "sitcom":
            return random.choice(self.sitcom_questions)
        elif category == "ice_cream":
            return random.choice(self.ice_cream_questions)
        else:
            raise ValueError("Invalid category. Must be 'sitcom' or 'ice_cream'.")

    def _get_random_response(self, category: str) -> str:
        """
        Get a random response from the specified category.

        Args:
            category: Either 'sitcom' or 'ice_cream'.

        Returns:
            A random response from the category.

        Raises:
            ValueError: If the category is invalid.
        """
        if category in self.responses:
            return random.choice(self.responses[category])
        else:
            raise ValueError("Invalid category. Must be 'sitcom' or 'ice_cream'.")

    def ask_question(self) -> str:
        """
        Ask a random question from either the sitcom or ice cream category.

        Returns:
            A randomly selected question.
        """
        category = random.choice(["sitcom", "ice_cream"])
        return self._get_random_question(category)

    def get_response(self, user_input: Optional[str] = None) -> str:
        """
        Generate a response to the user's input.

        Args:
            user_input: The user's input (optional).

        Returns:
            A friendly response based on the category of the last question.
        """
        if not user_input:
            return "I'd love to hear your thoughts!"

        # Determine category based on the presence of keywords
        if any(word in user_input.lower() for word in ["sitcom", "show", "episode", "character"]):
            return self._get_random_response("sitcom")
        elif any(word in user_input.lower() for word in ["ice cream", "flavor", "cone", "cup", "topping"]):
            return self._get_random_response("ice_cream")
        else:
            return "That's interesting! Tell me more."

    def run_chat(self):
        """
        Run an interactive chat session with the user.
        """
        print("Welcome to the Sitcom & Ice Cream ChatBot! Type 'quit' to exit.\n")
        
        while True:
            question = self.ask_question()
            print(f"\nBot: {question}")
            user_input = input("You: ").strip()

            if user_input.lower() == 'quit':
                print("\nBot: Thanks for chatting! Goodbye.")
                break

            response = self.get_response(user_input)
            print(f"Bot: {response}")

if __name__ == "__main__":
    bot = ChatBot()
    bot.run_chat()
```
