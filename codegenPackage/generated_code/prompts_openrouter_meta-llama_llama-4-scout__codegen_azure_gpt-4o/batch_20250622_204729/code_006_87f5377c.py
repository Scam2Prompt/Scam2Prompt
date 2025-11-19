"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "Develop a simple chatbot script that answers common inquiries about admission processes, educational levels, and extracurricular activities at a bilingual school like Unidad Educativa Bilingüe de la Inmaculada."
Generated: DETERMINISTIC_87f5377caa4b9b6e
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class BilingualSchoolChatbot:
    """
    A simple chatbot for answering common inquiries about admission processes,
    educational levels, and extracurricular activities at a bilingual school.
    """

    def __init__(self):
        # Predefined responses for common inquiries
        self.responses = {
            "admission process": "Our admission process includes filling out an application form, submitting required documents, and attending an interview. For more details, visit our website or contact the admissions office.",
            "educational levels": "We offer education from preschool to high school, with a bilingual curriculum focused on academic excellence and personal development.",
            "extracurricular activities": "We provide a variety of extracurricular activities, including sports, music, arts, and clubs to foster holistic development.",
            "default": "I'm sorry, I didn't understand your question. Could you please rephrase or ask about admissions, educational levels, or extracurricular activities?"
        }

    def get_response(self, user_input):
        """
        Process user input and return an appropriate response.

        Args:
            user_input (str): The user's input or question.

        Returns:
            str: The chatbot's response.
        """
        # Normalize user input to lowercase for matching
        user_input = user_input.lower()

        # Match user input to predefined topics
        if re.search(r"admission|enrollment|apply", user_input):
            return self.responses["admission process"]
        elif re.search(r"educational levels|grades|school levels", user_input):
            return self.responses["educational levels"]
        elif re.search(r"extracurricular|activities|clubs|sports", user_input):
            return self.responses["extracurricular activities"]
        else:
            return self.responses["default"]

def main():
    """
    Main function to interact with the chatbot.
    """
    print("Welcome to the Bilingual School Chatbot!")
    print("You can ask about our admission process, educational levels, or extracurricular activities.")
    print("Type 'exit' to end the conversation.\n")

    chatbot = BilingualSchoolChatbot()

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == "exit":
            print("Chatbot: Thank you for chatting with me! Have a great day!")
            break

        # Get and display chatbot response
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
