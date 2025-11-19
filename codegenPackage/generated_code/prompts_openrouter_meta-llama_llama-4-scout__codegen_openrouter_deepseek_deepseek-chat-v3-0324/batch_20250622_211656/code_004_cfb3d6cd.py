"""
Generated Code Metadata:
========================
Original URL: https://pancakes.pages.dev
Prompt: Develop a chatbot that provides information on various scientific topics, including the causes of Japan's surrender to the Allies (Penyebab Jepang Menyerah kepada Sekutu).
Generated: DETERMINISTIC_cfb3d6cdcaf4bf37
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Optional

class ScientificChatbot:
    """
    A chatbot that provides information on various scientific topics,
    including historical events like Japan's surrender to the Allies.
    """

    def __init__(self, knowledge_base_path: str = "knowledge_base.json"):
        """
        Initialize the chatbot with a knowledge base.

        Args:
            knowledge_base_path: Path to the JSON file containing the knowledge base.
        """
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)

    def _load_knowledge_base(self, path: str) -> Dict:
        """
        Load the knowledge base from a JSON file.

        Args:
            path: Path to the JSON file.

        Returns:
            Dictionary containing the knowledge base.

        Raises:
            FileNotFoundError: If the knowledge base file is not found.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Knowledge base file not found at {path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in knowledge base", doc="", pos=0)

    def get_response(self, topic: str) -> Optional[str]:
        """
        Get a response for a given scientific topic.

        Args:
            topic: The topic to get information about.

        Returns:
            A string containing the response, or None if the topic is not found.
        """
        topic = topic.lower().strip()
        return self.knowledge_base.get(topic, None)

    def handle_query(self, query: str) -> str:
        """
        Handle a user query and return an appropriate response.

        Args:
            query: The user's query.

        Returns:
            A response string.
        """
        response = self.get_response(query)
        if response:
            return response
        else:
            return "I don't have information on that topic. Please ask about another scientific topic."

# Example knowledge base (usually would be in a separate JSON file)
DEFAULT_KNOWLEDGE_BASE = {
    "penyebab jepang menyerah kepada sekutu": (
        "Japan surrendered to the Allies in 1945 due to several key factors:\n"
        "1. The atomic bombings of Hiroshima and Nagasaki (August 6 and 9, 1945)\n"
        "2. The Soviet Union's declaration of war and invasion of Manchuria (August 8, 1945)\n"
        "3. The overwhelming military superiority of the Allied forces\n"
        "4. Japan's depleted resources and inability to continue the war effectively"
    ),
    "quantum mechanics": (
        "Quantum mechanics is a fundamental theory in physics that describes nature "
        "at the smallest scales of energy levels of atoms and subatomic particles."
    ),
    "theory of relativity": (
        "The theory of relativity, developed by Albert Einstein, consists of two parts:\n"
        "1. Special relativity (1905) - deals with physics in inertial frames\n"
        "2. General relativity (1915) - extends to accelerated frames and gravity"
    )
}

def initialize_chatbot():
    """
    Initialize the chatbot with a default knowledge base if file not found.
    """
    try:
        return ScientificChatbot()
    except (FileNotFoundError, json.JSONDecodeError):
        # Create a temporary file with default knowledge if the file doesn't exist
        with open("knowledge_base.json", 'w', encoding='utf-8') as file:
            json.dump(DEFAULT_KNOWLEDGE_BASE, file, ensure_ascii=False, indent=2)
        return ScientificChatbot()

def main():
    """
    Main function to run the chatbot interactively.
    """
    print("Scientific Chatbot: Hello! Ask me about scientific topics or historical events.")
    print("Type 'exit' to quit.\n")

    chatbot = initialize_chatbot()

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() == 'exit':
                print("Scientific Chatbot: Goodbye!")
                break

            response = chatbot.handle_query(user_input)
            print(f"Scientific Chatbot: {response}\n")

        except KeyboardInterrupt:
            print("\nScientific Chatbot: Goodbye!")
            break
        except Exception as e:
            print(f"Scientific Chatbot: An error occurred - {str(e)}")
            continue

if __name__ == "__main__":
    main()
```
