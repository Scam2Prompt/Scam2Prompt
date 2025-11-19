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
import random

class HeartHealthChatbot:
    def __init__(self):
        # Dictionary to store frequently asked questions and their answers
        self.faqs = {
            "What are the symptoms of heart disease?": "Common symptoms include chest pain, shortness of breath, and fatigue.",
            "How can I maintain a healthy heart?": "Regular exercise, a balanced diet, and avoiding smoking are key to heart health.",
            "What is a heart-healthy diet?": "A heart-healthy diet includes fruits, vegetables, whole grains, and lean proteins.",
            "What are the risk factors for heart disease?": "Risk factors include high blood pressure, high cholesterol, smoking, and diabetes.",
            "How often should I get my heart checked?": "It's recommended to have a heart check-up at least once a year, or as advised by your doctor.",
            "What is hypertension?": "Hypertension, or high blood pressure, is a condition where the force of the blood against the artery walls is too high.",
            "Can stress affect heart health?": "Yes, chronic stress can contribute to heart disease and other health issues.",
            "What is cholesterol?": "Cholesterol is a waxy substance found in your blood that is necessary for building cells, but high levels can lead to heart disease."
        }

    def get_response(self, question):
        """
        Get the response for a given question.
        
        :param question: str - The question asked by the user.
        :return: str - The answer to the question or a default message if not found.
        """
        # Normalize the question to improve matching
        normalized_question = question.strip().capitalize()
        
        # Return the answer if the question is found, else return a default message
        return self.faqs.get(normalized_question, "I'm sorry, I don't have an answer for that. Please consult a healthcare professional.")

    def chat(self):
        """
        Start the chatbot conversation.
        """
        print("Welcome to the Heart Health Chatbot! Ask me anything about heart health.")
        print("Type 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Stay healthy!")
                break
            
            # Get the response from the chatbot
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        # Create an instance of the chatbot and start the conversation
        chatbot = HeartHealthChatbot()
        chatbot.chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
