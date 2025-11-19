"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Write a code snippet to create a simple chatbot that answers frequently asked questions about sleep apnea, TMJ disorders, and the services provided by the San Diego Sleep and TMJ Center.
Generated: DETERMINISTIC_c14b80c806f5c009
Batch ID: 20250622_204623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Chatbot:
    def __init__(self):
        # Initialize the chatbot with a set of FAQs
        self.faqs = {
            "sleep apnea": [
                "Sleep apnea is a serious sleep disorder that occurs when a person's breathing is interrupted during sleep.",
                "Common symptoms of sleep apnea include loud snoring, gasping for air during sleep, and excessive daytime sleepiness.",
                "Treatment options for sleep apnea include lifestyle changes, CPAP machines, and oral appliances."
            ],
            "TMJ disorders": [
                "TMJ disorders refer to problems with the jaw joint and surrounding muscles.",
                "Symptoms of TMJ disorders can include jaw pain, headaches, and difficulty chewing.",
                "Treatment may involve physical therapy, dental splints, or in some cases, surgery."
            ],
            "San Diego Sleep and TMJ Center": [
                "The San Diego Sleep and TMJ Center specializes in diagnosing and treating sleep apnea and TMJ disorders.",
                "We offer comprehensive evaluations and personalized treatment plans.",
                "Our team is dedicated to improving your sleep quality and overall health."
            ]
        }

    def get_response(self, question):
        """
        Get a response based on the user's question.
        
        Args:
            question (str): The user's question about sleep apnea, TMJ disorders, or services.
        
        Returns:
            str: A response from the chatbot or a default message if the question is not recognized.
        """
        question = question.lower()
        for key in self.faqs:
            if key in question:
                return random.choice(self.faqs[key])
        return "I'm sorry, I can only answer questions about sleep apnea, TMJ disorders, and the San Diego Sleep and TMJ Center."

    def chat(self):
        """
        Start a chat session with the user.
        """
        print("Welcome to the Sleep and TMJ Center Chatbot!")
        print("You can ask me about sleep apnea, TMJ disorders, or our services.")
        print("Type 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Have a great day!")
                break
            try:
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"Chatbot: An error occurred: {e}")

if __name__ == "__main__":
    # Run the chatbot
    chatbot = Chatbot()
    chatbot.chat()
```
