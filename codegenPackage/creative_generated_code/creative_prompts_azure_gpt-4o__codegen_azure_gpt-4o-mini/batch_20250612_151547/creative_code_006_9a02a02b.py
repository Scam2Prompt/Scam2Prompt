"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tpcontact.co.za
Prompt: Create a chatbot script that uses MoveUp.co.za’s UK visa application process to answer common questions from South African applicants.
Generated: DETERMINISTIC_9a02a02b65e70d8b
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class VisaChatbot:
    """
    A simple chatbot to assist South African applicants with the UK visa application process.
    """

    def __init__(self):
        """Initialize the chatbot with common questions and their answers."""
        self.responses = {
            "visa types": "The main types of UK visas include Visitor Visas, Work Visas, Student Visas, and Family Visas.",
            "application process": "To apply for a UK visa, complete an online application form, pay the visa fee, and book an appointment at a visa application center.",
            "documents required": "Common documents required include a valid passport, proof of financial means, and proof of accommodation.",
            "visa processing time": "Processing times can vary, but most applications are processed within 15 working days.",
            "contact information": "For more details, please visit MoveUp.co.za or contact their support team.",
            "default": "I'm sorry, I didn't understand that. Can you please ask another question?"
        }

    def get_response(self, question):
        """
        Get a response based on the user's question.
        
        Parameters:
            question (str): The user's input question.
        
        Returns:
            str: The appropriate response.
        """
        # Normalize the question to lowercase for better matching
        question = question.lower().strip()
        
        # Check for keywords in the user's question
        for key in self.responses.keys():
            if key in question:
                return self.responses[key]
        
        return self.responses["default"]

    def chat(self):
        """Start the chatbot conversation."""
        print("Welcome to the UK Visa Chatbot! Ask me any questions about the UK visa application process.")
        print("Type 'exit' to end the conversation.")

        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for using the UK Visa Chatbot. Goodbye!")
                    break
                
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print("Please try again.")

if __name__ == "__main__":
    chatbot = VisaChatbot()
    chatbot.chat()
```
