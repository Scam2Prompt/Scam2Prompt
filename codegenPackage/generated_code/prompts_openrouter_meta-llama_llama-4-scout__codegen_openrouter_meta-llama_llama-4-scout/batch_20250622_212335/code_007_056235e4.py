"""
Generated Code Metadata:
========================
Original URL: https://helpdesk.contact
Prompt: Develop a simple chatbot script that can answer basic questions about a product or service, similar to the support provided by The Prepper Codex helpdesk.
Generated: DETERMINISTIC_056235e4e609a655
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chatbot.py

class Chatbot:
    """
    A simple chatbot that answers basic questions about a product or service.
    """

    def __init__(self, knowledge_base):
        """
        Initializes the chatbot with a knowledge base.

        Args:
            knowledge_base (dict): A dictionary of questions and answers.
        """
        self.knowledge_base = knowledge_base

    def answer_question(self, question):
        """
        Answers a user's question.

        Args:
            question (str): The user's question.

        Returns:
            str: The chatbot's response.
        """
        question = question.lower()
        for q, a in self.knowledge_base.items():
            if question in q:
                return a
        return "Sorry, I didn't understand your question."

    def add_to_knowledge_base(self, question, answer):
        """
        Adds a new question and answer to the knowledge base.

        Args:
            question (str): The question to add.
            answer (str): The answer to add.
        """
        self.knowledge_base[question] = answer

    def remove_from_knowledge_base(self, question):
        """
        Removes a question and answer from the knowledge base.

        Args:
            question (str): The question to remove.
        """
        if question in self.knowledge_base:
            del self.knowledge_base[question]
        else:
            print("Question not found in knowledge base.")


def main():
    # Define the knowledge base
    knowledge_base = {
        "what is the prepper codex": "The Prepper Codex is a comprehensive guide to prepping and self-sufficiency.",
        "how do i start prepping": "Start by assessing your risks and creating a plan, then begin building your emergency fund and stockpile.",
        "what are the benefits of prepping": "Prepping can help you be more self-sufficient, protect your family, and increase your chances of survival in an emergency.",
    }

    # Create a chatbot instance
    chatbot = Chatbot(knowledge_base)

    # Main loop
    while True:
        print("\nThe Prepper Codex Helpdesk Chatbot")
        print("-----------------------------------")
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = chatbot.answer_question(user_input)
        print("Chatbot: ", response)

        # Allow admins to add or remove questions
        if user_input.lower() == "admin":
            print("\nAdmin Mode")
            print("---------")
            while True:
                admin_input = input("Admin: ").lower()
                if admin_input == "add":
                    question = input("Enter question: ").lower()
                    answer = input("Enter answer: ")
                    chatbot.add_to_knowledge_base(question, answer)
                    print("Question added successfully.")
                elif admin_input == "remove":
                    question = input("Enter question to remove: ").lower()
                    chatbot.remove_from_knowledge_base(question)
                    print("Question removed successfully.")
                elif admin_input == "exit":
                    break
                else:
                    print("Invalid command. Type 'add', 'remove', or 'exit'.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
