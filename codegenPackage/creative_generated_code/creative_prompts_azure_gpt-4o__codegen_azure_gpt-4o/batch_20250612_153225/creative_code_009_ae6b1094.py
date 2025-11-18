"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Create a chatbot script that answers FAQs about DBT therapy, including duration, group formation, and therapy components, using the information provided on the Mente Sana Psicología website.
Generated: DETERMINISTIC_ae6b10943ab2bdae
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class DBTChatbot:
    """
    A chatbot for answering FAQs about DBT therapy.
    """

    def __init__(self):
        """
        Initializes the chatbot with predefined FAQ data.
        """
        self.faq_data = self.load_faq_data()

    def load_faq_data(self):
        """
        Loads FAQ data for DBT therapy. This can be replaced with a database or API integration
        if needed in the future.

        Returns:
            dict: A dictionary containing DBT therapy FAQ questions and answers.
        """
        faq_data = {
            "What is the duration of DBT therapy?": "DBT therapy typically lasts 6 months to 1 year, depending on individual needs.",
            "How are DBT therapy groups formed?": "Groups are formed based on age, needs, and common therapeutic goals. Each group has 6-10 participants.",
            "What are the components of DBT therapy?": (
                "DBT therapy includes individual therapy sessions, skills training groups, "
                "phone coaching, and consultation teams for therapists."
            ),
        }
        return faq_data

    def get_response(self, user_question):
        """
        Retrieves a response to the user's question from the FAQ data.

        Args:
            user_question (str): The question asked by the user.

        Returns:
            str: The answer to the user's question or a fallback message.
        """
        # Normalize the user question for better matching
        normalized_question = user_question.lower()
        
        # Attempt to find a matching question in the FAQ data
        for question, answer in self.faq_data.items():
            if normalized_question in question.lower():
                return answer
        
        # Fallback response for unrecognized questions
        return (
            "I'm sorry, I couldn't find information about that. Please try rephrasing your question "
            "or visit the Mente Sana Psicología website for more details."
        )

def main():
    """
    Main function to interact with the DBT chatbot.
    """
    print("Welcome to the DBT Therapy Chatbot!")
    print("You can ask me questions about the duration, group formation, or components of DBT therapy.")
    print("Type 'exit' to end the conversation.\n")

    # Instantiate the chatbot
    chatbot = DBTChatbot()

    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Exit the loop if the user types 'exit'
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye! Have a great day!")
                break
            
            # Get and print the chatbot's response
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            # Handle any unexpected errors gracefully
            print(f"Chatbot: Oops, something went wrong! Error: {e}")

if __name__ == "__main__":
    main()
```
