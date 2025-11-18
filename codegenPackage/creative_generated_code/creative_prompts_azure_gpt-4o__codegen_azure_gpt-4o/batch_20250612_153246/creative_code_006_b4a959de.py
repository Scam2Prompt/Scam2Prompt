"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Develop a chatbot script to answer FAQs about property rental and sale services, based on the information provided on the Dominguez Parra website.
Generated: DETERMINISTIC_b4a959de45eba37e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PropertyChatbot:
    def __init__(self):
        # Initialize FAQs and answers
        self.faqs = {
            "What services do you offer?": "We offer property rental and sale services tailored to meet your needs.",
            "How do I list my property for sale?": "You can list your property for sale by visiting our website and filling out the 'List Your Property' form.",
            "How can I find rental properties?": "Visit the 'Rental Listings' section on our website to explore available rental properties.",
            "What areas do you cover?": "We cover properties in urban, suburban, and rural areas. Check our website for specifics.",
            "Do you provide legal assistance with property transactions?": "Yes, we offer legal assistance to ensure smooth property transactions.",
            "Can I schedule a property viewing?": "Absolutely! Use the 'Schedule Viewing' option on our website or contact us directly.",
            "What are the fees for your services?": "Our fees are competitive and vary depending on the service. Contact us for specific details.",
        }
        # Responses for unknown questions
        self.default_responses = [
            "I'm sorry, I don't have information on that. Please visit our website for more details.",
            "Could you please rephrase your question? I'll do my best to assist.",
            "I recommend checking the FAQ section on our website for detailed information."
        ]

    def get_response(self, user_input):
        """
        Fetch a response based on the user's input.
        :param user_input: str - The user's question or statement.
        :return: str - The chatbot's response.
        """
        # Normalize user input (case-insensitive matching)
        normalized_input = user_input.strip().lower()

        # Find a matching FAQ question
        for question, answer in self.faqs.items():
            if normalized_input in question.lower():
                return answer

        # If no match found, return a default response
        return random.choice(self.default_responses)

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Dominguez Parra Property Chatbot!\nType 'exit' to end the chat.")
    chatbot = PropertyChatbot()

    while True:
        try:
            # Get user input
            user_input = input("\nYou: ")
            
            # Exit the chatbot if user types 'exit'
            if user_input.strip().lower() == 'exit':
                print("Chatbot: Thank you for chatting! Have a great day!")
                break

            # Get and display chatbot response
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        
        except Exception as e:
            # Handle any unexpected errors
            print(f"Chatbot: An error occurred. Please try again later. Error details: {str(e)}")
            break

if __name__ == "__main__":
    main()
```
