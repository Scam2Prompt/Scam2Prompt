"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Develop a simple chatbot that answers frequently asked questions about heart health and cardiology, based on Dr. S Nagendra Boopathy's FAQs.
Generated: DETERMINISTIC_299242b773312b0c
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a dictionary with FAQs and answers
class HeartHealthChatbot:
    def __init__(self):
        self.faqs = {
            "what is heart disease": "Heart disease refers to a range of conditions that affect the heart and blood vessels.",
            "what are the symptoms of heart disease": "Symptoms may include chest pain, shortness of breath, fatigue, and swelling in the legs and feet.",
            "how can I prevent heart disease": "You can prevent heart disease by exercising regularly, eating a healthy diet, not smoking, and managing stress.",
            "what is a heart attack": "A heart attack occurs when the blood flow to the heart is blocked, causing damage to the heart muscle.",
            "what are the risk factors for heart disease": "Risk factors include high blood pressure, high cholesterol, diabetes, obesity, and a family history of heart disease.",
        }

    def get_answer(self, question):
        """Returns the answer to a given question"""
        question = question.lower()
        for key in self.faqs:
            if key in question:
                return self.faqs[key]
        return "Sorry, I didn't understand your question or it is not in my database."

    def chat(self):
        """Starts a conversation with the user"""
        print("Welcome to the Heart Health Chatbot!")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                print("Chatbot: Goodbye!")
                break
            answer = self.get_answer(user_input)
            print(f"Chatbot: {answer}")


def main():
    try:
        chatbot = HeartHealthChatbot()
        chatbot.chat()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
