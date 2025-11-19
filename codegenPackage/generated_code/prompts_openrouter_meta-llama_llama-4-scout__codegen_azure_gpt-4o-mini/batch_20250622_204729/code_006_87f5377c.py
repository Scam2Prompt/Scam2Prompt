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
    def __init__(self):
        self.responses = {
            "admission": "Our admission process includes an application form, an interview, and submission of previous academic records. Please visit our website for detailed information.",
            "educational_levels": "We offer education from preschool through high school, including bilingual programs in English and Spanish.",
            "extracurricular_activities": "We provide a variety of extracurricular activities including sports, music, arts, and clubs to enhance our students' learning experience.",
            "default": "I'm sorry, I didn't understand that. Can you please rephrase your question?"
        }

    def get_response(self, user_input):
        """
        Get a response based on user input.

        Args:
            user_input (str): The user's question.

        Returns:
            str: The chatbot's response.
        """
        user_input = user_input.lower()
        
        if re.search(r'admission', user_input):
            return self.responses["admission"]
        elif re.search(r'educational levels|grades|curriculum', user_input):
            return self.responses["educational_levels"]
        elif re.search(r'extracurricular activities|clubs|sports', user_input):
            return self.responses["extracurricular_activities"]
        else:
            return self.responses["default"]

    def run(self):
        """
        Run the chatbot in a loop until the user decides to exit.
        """
        print("Welcome to the Unidad Educativa Bilingüe de la Inmaculada Chatbot!")
        print("You can ask me about admission processes, educational levels, and extracurricular activities.")
        print("Type 'exit' to end the chat.")

        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for chatting! Goodbye!")
                    break
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    chatbot = BilingualSchoolChatbot()
    chatbot.run()
```
