"""
Generated Code Metadata:
========================
Original URL: https://immediatepeak.org
Prompt: Create a chatbot that answers FAQs about Immediate Peak, its benefits, and the investment education firms it connects users with, using a knowledge base from the webpage content.
Generated: DETERMINISTIC_dde1b141fe76918a
Batch ID: 20250622_211310
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
import re

class FAQChatbot:
    """
    A chatbot that answers FAQs about Immediate Peak, its benefits, and investment education firms.
    Uses a knowledge base extracted from webpage content.
    """

    def __init__(self, knowledge_base_path: str):
        """
        Initialize the chatbot with a knowledge base.

        Args:
            knowledge_base_path (str): Path to the JSON file containing the knowledge base.
        """
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)
        self.greetings = ["hi", "hello", "hey", "greetings"]
        self.exit_commands = ["exit", "quit", "bye", "goodbye"]

    def _load_knowledge_base(self, path: str) -> Dict:
        """
        Load the knowledge base from a JSON file.

        Args:
            path (str): Path to the JSON file.

        Returns:
            Dict: The loaded knowledge base.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Knowledge base file not found at {path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in knowledge base file", path, 0)

    def _preprocess_input(self, user_input: str) -> str:
        """
        Preprocess user input by removing extra spaces and converting to lowercase.

        Args:
            user_input (str): Raw user input.

        Returns:
            str: Processed user input.
        """
        return re.sub(r'\s+', ' ', user_input).strip().lower()

    def _get_response(self, query: str) -> Optional[str]:
        """
        Get a response from the knowledge base based on the user's query.

        Args:
            query (str): Processed user query.

        Returns:
            Optional[str]: Response from the knowledge base or None if no match found.
        """
        for category in self.knowledge_base:
            for qa_pair in category["qa_pairs"]:
                if query in qa_pair["question"].lower():
                    return qa_pair["answer"]
        return None

    def _handle_greeting(self) -> str:
        """
        Handle greeting messages.

        Returns:
            str: Greeting response.
        """
        return "Hello! How can I help you with Immediate Peak today?"

    def _handle_exit(self) -> str:
        """
        Handle exit commands.

        Returns:
            str: Exit response.
        """
        return "Goodbye! Feel free to reach out if you have more questions."

    def start_chat(self):
        """
        Start the chatbot interaction loop.
        """
        print("Welcome to the Immediate Peak FAQ Chatbot!")
        print("Type 'exit' at any time to end the conversation.\n")

        while True:
            user_input = input("You: ")
            processed_input = self._preprocess_input(user_input)

            if not processed_input:
                print("Please enter a valid question.")
                continue

            if processed_input in self.greetings:
                print(f"Bot: {self._handle_greeting()}")
                continue

            if processed_input in self.exit_commands:
                print(f"Bot: {self._handle_exit()}")
                break

            response = self._get_response(processed_input)
            if response:
                print(f"Bot: {response}")
            else:
                print("Bot: I'm sorry, I don't have an answer to that question. "
                      "Please try rephrasing or ask about Immediate Peak, its benefits, "
                      "or the investment education firms it connects users with.")


# Example usage
if __name__ == "__main__":
    try:
        chatbot = FAQChatbot("knowledge_base.json")
        chatbot.start_chat()
    except Exception as e:
        print(f"Error initializing chatbot: {e}")
```

**Sample knowledge_base.json:**
```json
[
    {
        "category": "Immediate Peak Overview",
        "qa_pairs": [
            {
                "question": "What is Immediate Peak?",
                "answer": "Immediate Peak is a platform that connects users with investment education firms to help them learn about trading and investment strategies."
            }
        ]
    },
    {
        "category": "Benefits",
        "qa_pairs": [
            {
                "question": "What are the benefits of Immediate Peak?",
                "answer": "Immediate Peak provides access to educational resources, connects you with expert firms, and helps you make informed investment decisions."
            }
        ]
    },
    {
        "category": "Investment Education Firms",
        "qa_pairs": [
            {
                "question": "Which firms does Immediate Peak connect users with?",
                "answer": "Immediate Peak partners with reputable investment education firms that specialize in various trading strategies and market analysis."
            }
        ]
    }
]
```
