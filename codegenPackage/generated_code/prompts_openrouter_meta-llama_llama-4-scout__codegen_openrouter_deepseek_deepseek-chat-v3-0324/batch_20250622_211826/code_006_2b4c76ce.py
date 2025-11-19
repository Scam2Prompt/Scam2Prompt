"""
Generated Code Metadata:
========================
Original URL: https://conferencesglobal.org
Prompt: Create a chatbot that can answer frequently asked questions (FAQs) about Conferences Global, such as abstract submission, registration, and invitation letter requests.
Generated: DETERMINISTIC_2b4c76ce2688c03c
Batch ID: 20250622_211826
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

class ConferenceFAQChatbot:
    """
    A chatbot designed to answer frequently asked questions about Conferences Global.
    Handles queries related to abstract submission, registration, and invitation letters.
    """

    def __init__(self, faq_file: str = "faq_data.json"):
        """
        Initialize the chatbot with FAQ data loaded from a JSON file.

        Args:
            faq_file (str): Path to the JSON file containing FAQ data. Defaults to "faq_data.json".
        """
        self.faq_data = self._load_faq_data(faq_file)

    def _load_faq_data(self, file_path: str) -> Dict[str, Dict[str, str]]:
        """
        Load FAQ data from a JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            Dict[str, Dict[str, str]]: Parsed FAQ data.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"FAQ data file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in FAQ data file", file_path, 0)

    def get_answer(self, category: str, question: str) -> Optional[str]:
        """
        Retrieve an answer for a given question in a specific category.

        Args:
            category (str): The category of the question (e.g., "abstract", "registration").
            question (str): The specific question to be answered.

        Returns:
            Optional[str]: The answer if found, None otherwise.
        """
        category_data = self.faq_data.get(category.lower())
        if not category_data:
            return None

        return category_data.get(question.lower())

    def handle_query(self, user_input: str) -> str:
        """
        Process user input and return an appropriate response.

        Args:
            user_input (str): The user's query.

        Returns:
            str: The chatbot's response.
        """
        user_input = user_input.lower().strip()
        
        # Check for common greetings
        if user_input in ["hi", "hello", "hey"]:
            return "Hello! How can I assist you with your conference-related questions today?"
        
        # Check for help command
        if user_input == "help":
            return "I can help with questions about abstract submission, registration, and invitation letters. Please ask your question."

        # Check for categories and questions
        for category, questions in self.faq_data.items():
            if user_input in questions:
                return questions[user_input]
            if any(q in user_input for q in questions):
                for q, answer in questions.items():
                    if q in user_input:
                        return answer

        return "I'm sorry, I couldn't find an answer to your question. Please try rephrasing or ask about abstract submission, registration, or invitation letters."

# Example usage
if __name__ == "__main__":
    # Sample FAQ data structure (usually loaded from a file)
    sample_faq_data = {
        "abstract": {
            "how to submit an abstract": "You can submit your abstract via our online submission system on the conference website.",
            "abstract submission deadline": "The deadline for abstract submission is October 31, 2023.",
            "abstract format requirements": "Abstracts should be no more than 300 words in MS Word format."
        },
        "registration": {
            "how to register": "Registration can be completed online through our conference website.",
            "registration fees": "Early bird registration is $300, regular registration is $400.",
            "registration deadline": "The registration deadline is November 15, 2023."
        },
        "invitation": {
            "how to get an invitation letter": "Invitation letters are available upon request after registration.",
            "invitation letter for visa": "Yes, we provide visa support letters for registered attendees."
        }
    }

    # Save sample data to a file
    with open("faq_data.json", 'w') as file:
        json.dump(sample_faq_data, file)

    # Initialize and run the chatbot
    chatbot = ConferenceFAQChatbot()
    
    print("Conference FAQ Chatbot initialized. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chatbot.handle_query(user_input)
        print(f"Bot: {response}")
```
