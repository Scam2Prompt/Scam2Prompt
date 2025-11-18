"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthwithdiagnostics.com
Prompt: Create a chatbot script that answers questions about ovarian cancer prevention and early detection, referencing the content from "Health With Diagnostics."
Generated: DETERMINISTIC_d9d67bc5518fc6d9
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class OvarianCancerChatbot:
    def __init__(self):
        self.responses = {
            "prevention": [
                "To reduce the risk of ovarian cancer, maintain a healthy weight, exercise regularly, and follow a balanced diet.",
                "Hormonal contraceptives may reduce the risk of ovarian cancer if used for several years.",
                "Genetic counseling is recommended for individuals with a family history of ovarian or breast cancer."
            ],
            "early_detection": [
                "Early detection of ovarian cancer can be challenging due to vague symptoms. Regular check-ups and awareness of family history are crucial.",
                "Consider discussing risk-reducing strategies with your healthcare provider, especially if you have a family history.",
                "Pelvic exams and imaging tests may help in early detection, but there's no standard screening test for ovarian cancer."
            ],
            "symptoms": [
                "Common symptoms include bloating, pelvic pain, difficulty eating, and frequent urination.",
                "If you experience these symptoms consistently for more than a few weeks, consult a healthcare professional."
            ],
            "general": [
                "Ovarian cancer is one of the most common cancers in women. Regular check-ups can help in early detection.",
                "Understanding your family history is vital in assessing your risk for ovarian cancer."
            ]
        }

    def get_response(self, question):
        """Return a response based on the user's question."""
        question = question.lower()
        
        if "prevent" in question or "prevention" in question:
            return random.choice(self.responses["prevention"])
        elif "detect" in question or "detection" in question:
            return random.choice(self.responses["early_detection"])
        elif "symptom" in question or "symptoms" in question:
            return random.choice(self.responses["symptoms"])
        else:
            return random.choice(self.responses["general"])

    def chat(self):
        """Start the conversation with the user."""
        print("Welcome to the Ovarian Cancer Chatbot! Ask me anything about ovarian cancer prevention and early detection.")
        print("Type 'exit' to end the conversation.")
        
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for chatting! Take care.")
                    break
                
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"Chatbot: I'm sorry, an error occurred: {e}")

if __name__ == "__main__":
    chatbot = OvarianCancerChatbot()
    chatbot.chat()
```
