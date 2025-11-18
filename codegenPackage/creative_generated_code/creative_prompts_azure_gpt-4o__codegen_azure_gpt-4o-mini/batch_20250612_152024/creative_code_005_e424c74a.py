"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Create a chatbot script to answer common questions about IELTS and PTE preparation, referencing the personalized training approach highlighted by RNW International.
Generated: DETERMINISTIC_e424c74afd492c48
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class IELTS_PTE_Chatbot:
    """
    A simple chatbot to answer common questions about IELTS and PTE preparation,
    referencing the personalized training approach of RNW International.
    """

    def __init__(self):
        self.responses = {
            "greeting": [
                "Hello! I’m here to help you with your IELTS and PTE preparation. How can I assist you today?",
                "Hi there! What questions do you have regarding IELTS or PTE preparation?",
            ],
            "ielts_overview": "The IELTS (International English Language Testing System) is designed to assess your English skills. It consists of four components: Listening, Reading, Writing, and Speaking.",
            "pte_overview": "The PTE (Pearson Test of English) is an English language test that measures your reading, writing, listening, and speaking skills, often used for study abroad and migration.",
            "personalized_training": "At RNW International, we offer personalized training programs tailored to your individual strengths and weaknesses to maximize your preparation efficiency.",
            "study_materials": "We provide a variety of study materials including practice tests, online resources, and personalized feedback to help you improve.",
            "test_format": "Both tests have different formats. IELTS has a paper-based or computer-based format, while PTE is entirely computer-based. It's essential to familiarize yourself with the structure of the test you choose.",
            "common_questions": "Some common questions include: What is the best way to prepare? How long should I study? What resources are recommended?",
            "help": "I'm here to provide information about IELTS and PTE preparation. You can ask about test formats, study tips, or our personalized training approach."
        }

    def get_response(self, user_input):
        """
        Returns a response based on user input.

        :param user_input: str: The user's question input.
        :return: str: The chatbot's response.
        """
        user_input = user_input.lower().strip()
        
        if "hi" in user_input or "hello" in user_input:
            return random.choice(self.responses["greeting"])
        elif "ielts" in user_input:
            return self.responses["ielts_overview"]
        elif "pte" in user_input:
            return self.responses["pte_overview"]
        elif "personalized training" in user_input or "tailored approach" in user_input:
            return self.responses["personalized_training"]
        elif "study materials" in user_input:
            return self.responses["study_materials"]
        elif "test format" in user_input:
            return self.responses["test_format"]
        elif "common questions" in user_input:
            return self.responses["common_questions"]
        else:
            return self.responses["help"]

def main():
    """
    Main function to run the IELTS and PTE chatbot.
    """
    chatbot = IELTS_PTE_Chatbot()
    
    print("Welcome to the IELTS & PTE Preparation Chatbot!")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Good luck with your preparation!")
                break
            
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}\n")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
