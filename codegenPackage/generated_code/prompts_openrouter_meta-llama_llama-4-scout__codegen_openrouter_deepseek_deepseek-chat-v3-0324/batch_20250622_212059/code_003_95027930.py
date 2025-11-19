"""
Generated Code Metadata:
========================
Original URL: https://kidanah.sa
Prompt: Create a chatbot script that answers frequently asked questions about Hajj and Umrah rituals, services, and procedures, as provided on the Kidana Al Hejaz website.
Generated: DETERMINISTIC_95027930fa1afe48
Batch ID: 20250622_212059
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

class HajjUmrahChatbot:
    """
    A chatbot that answers frequently asked questions about Hajj and Umrah rituals, services, and procedures.
    The responses are based on data provided by Kidana Al Hejaz website.
    """

    def __init__(self, knowledge_base_path: str = "knowledge_base.json"):
        """
        Initialize the chatbot with a knowledge base.

        Args:
            knowledge_base_path (str): Path to the JSON file containing FAQ data.
        """
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)

    def _load_knowledge_base(self, file_path: str) -> Dict[str, Dict[str, str]]:
        """
        Load the knowledge base from a JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            Dict[str, Dict[str, str]]: Parsed knowledge base.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Knowledge base file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in knowledge base file", file_path, 0)

    def get_answer(self, question: str) -> Optional[str]:
        """
        Get an answer for a given question by searching the knowledge base.

        Args:
            question (str): The user's question.

        Returns:
            Optional[str]: The answer if found, None otherwise.
        """
        question_lower = question.lower().strip()
        for category in self.knowledge_base.values():
            for q, a in category.items():
                if q.lower() in question_lower:
                    return a
        return None

    def get_categories(self) -> List[str]:
        """
        Get a list of available FAQ categories.

        Returns:
            List[str]: List of category names.
        """
        return list(self.knowledge_base.keys())

    def get_questions_in_category(self, category: str) -> List[str]:
        """
        Get all questions in a specific category.

        Args:
            category (str): The category name.

        Returns:
            List[str]: List of questions in the category.

        Raises:
            KeyError: If the category does not exist.
        """
        if category not in self.knowledge_base:
            raise KeyError(f"Category not found: {category}")
        return list(self.knowledge_base[category].keys())

    def run_chat(self):
        """
        Run an interactive chat session with the user.
        """
        print("Welcome to the Hajj and Umrah FAQ Chatbot!")
        print("Type 'exit' to end the chat.\n")

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == 'exit':
                print("Goodbye! May you have a blessed journey.")
                break

            answer = self.get_answer(user_input)
            if answer:
                print(f"Bot: {answer}")
            else:
                print("Bot: I couldn't find an answer to that question. Please try rephrasing or ask about:")
                categories = self.get_categories()
                for i, category in enumerate(categories, 1):
                    print(f"{i}. {category}")
                print("\nYou can also type 'exit' to end the chat.")


# Example knowledge_base.json structure:
# {
#     "Rituals": {
#         "What is Ihram?": "Ihram is the sacred state a pilgrim must enter before performing Hajj or Umrah...",
#         "What are the pillars of Umrah?": "The pillars of Umrah are Ihram, Tawaf, Sa'i, and Halq/Taqsir..."
#     },
#     "Services": {
#         "What transportation is provided?": "Kidana Al Hejaz provides air-conditioned buses between holy sites...",
#         "Is food included?": "Yes, we provide three meals per day at designated restaurants..."
#     }
# }

if __name__ == "__main__":
    try:
        chatbot = HajjUmrahChatbot()
        chatbot.run_chat()
    except Exception as e:
        print(f"Error initializing chatbot: {e}")
```
