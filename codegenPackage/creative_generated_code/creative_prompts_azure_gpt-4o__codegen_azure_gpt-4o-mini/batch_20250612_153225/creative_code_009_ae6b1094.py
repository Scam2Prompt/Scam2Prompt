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
import random

class FAQChatbot:
    def __init__(self):
        """
        Initializes the FAQChatbot with predefined answers.
        """
        self.faqs = {
            "What is DBT therapy?": "DBT (Dialectical Behavior Therapy) is a cognitive-behavioral treatment designed to help people manage emotions and improve interpersonal relationships.",
            "What is the duration of DBT therapy?": "DBT therapy typically lasts for about 6 months, but the duration can vary depending on individual needs and progress.",
            "How are groups formed in DBT therapy?": "Groups in DBT therapy are usually formed based on the common needs of participants, ensuring a supportive and understanding environment.",
            "What are the components of DBT therapy?": "DBT therapy consists of four main components: individual therapy, group skills training, phone coaching, and a consultation team for therapists."
        }

    def get_answer(self, question):
        """
        Retrieves the answer to a given FAQ question.

        Args:
            question (str): The question asked by the user.

        Returns:
            str: The answer to the question, or a message if the question is not found.
        """
        # Normalize the question for matching
        normalized_question = question.strip().capitalize()
        return self.faqs.get(normalized_question, "I'm sorry, I don't have an answer for that question.")

    def run_chat(self):
        """
        Starts the chatbot interaction loop.
        It continues to prompt the user for questions until they choose to exit.
        """
        print("Welcome to the DBT Therapy FAQ Chatbot!")
        print("You can ask me anything about DBT therapy. Type 'exit' to end the chat.\n")

        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for chatting! Have a great day!")
                    break
                
                # Fetch the response from the FAQ
                response = self.get_answer(user_input)
                print(f"Chatbot: {response}")
                
            except Exception as e:
                print(f"Chatbot: An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    # Run the chatbot if this script is executed directly
    chatbot = FAQChatbot()
    chatbot.run_chat()
```
