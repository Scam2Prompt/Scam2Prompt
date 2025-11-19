"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Develop a chatbot script in Python that can answer common questions about handyman services in Wellington, such as availability and pricing.
Generated: DETERMINISTIC_6a4ea76233399546
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class HandymanChatbot:
    def __init__(self):
        # Predefined responses for common questions
        self.availability_responses = [
            "We are available Monday to Saturday from 8 AM to 6 PM.",
            "Our team is available for bookings on weekdays and Saturdays.",
            "You can book our services anytime between 8 AM and 6 PM, Monday to Saturday."
        ]
        
        self.pricing_responses = [
            "Our pricing starts at $50 per hour, depending on the service required.",
            "We offer competitive rates, starting from $50 per hour.",
            "Pricing varies based on the service; please contact us for a detailed quote."
        ]
        
        self.fallback_response = "I'm sorry, I didn't understand that. Can you please rephrase your question?"

    def get_response(self, user_input):
        """
        Get a response based on user input.
        
        Args:
            user_input (str): The question asked by the user.
        
        Returns:
            str: The chatbot's response.
        """
        user_input = user_input.lower()
        
        if "availability" in user_input:
            return random.choice(self.availability_responses)
        elif "pricing" in user_input:
            return random.choice(self.pricing_responses)
        else:
            return self.fallback_response

def main():
    """
    Main function to run the chatbot.
    """
    chatbot = HandymanChatbot()
    
    print("Welcome to the Handyman Services Chatbot! How can I assist you today?")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Chatbot: Thank you for chatting! Have a great day!")
                break
            
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
