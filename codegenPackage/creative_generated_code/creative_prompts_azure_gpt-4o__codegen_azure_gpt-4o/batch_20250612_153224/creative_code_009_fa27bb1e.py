"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Create a chatbot for the "Comunidade MR" that can answer FAQs about the program, payment options, and provide emotional support resources.
Generated: DETERMINISTIC_fa27bb1e5cea8f5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ChatBotComunidadeMR:
    def __init__(self):
        # Initialize FAQs for the bot
        self.faqs = {
            "program": [
                "The Comunidade MR program is designed to support individuals in personal and professional growth.",
                "We offer workshops, mentorship programs, and a community space for engagement."
            ],
            "payment_options": [
                "You can pay via credit card, PayPal, or bank transfer.",
                "For assistance with payments, contact support at pagamentos@comunidademr.com."
            ],
            "emotional_support": [
                "We recommend speaking to trained professionals if you're in need of emotional support.",
                "Explore free resources like emotional support hotlines or meditation apps."
            ]
        }
        
        # Responses for emotional support queries
        self.emotional_support_resources = [
            "Here are some emotional support resources: 1-800-123-4567 (hotline), free apps like 'Calm' and 'Headspace'.",
            "Remember to take things one step at a time. Reach out to close friends or family if you need someone to talk to.",
            "Our community is here to support you. Check our forum for shared experiences and advice."
        ]

    def get_response(self, user_input):
        """
        Processes user input and provides a response based on the FAQ categories.
        Args:
            user_input (str): The user's input question or query.

        Returns:
            str: A chatbot response.
        """
        # Standardize input for matching purposes
        user_input = user_input.lower()

        # Check for program-related queries
        if "program" in user_input:
            return random.choice(self.faqs["program"])
        
        # Check for payment inquiries
        elif "payment" in user_input or "pay" in user_input:
            return random.choice(self.faqs["payment_options"])
        
        # Check for emotional support needs
        elif "emotional" in user_input or "support" in user_input:
            return random.choice(self.emotional_support_resources)
        
        # Default response for unrecognized queries
        else:
            return ("I'm sorry, I couldn't understand your question. "
                    "Can you please provide more details or contact support at ajuda@comunidademr.com?")
    

# Main application loop
def main():
    """
    Main function to run the chatbot. Handles user interaction.
    """
    chatbot = ChatBotComunidadeMR()
    print("Welcome to the Comunidade MR Chatbot! Type 'exit' to end the chat.")
    
    while True:
        try:
            # Get user input
            user_input = input("You: ")
            
            # Exit condition
            if user_input.lower() == "exit":
                print("Chatbot: Thank you for chatting with me! Have a great day!")
                break
            
            # Get and display the chatbot's response
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
        
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: Oops! Something went wrong. Error: {e}")
            print("Chatbot: Please try again later or contact support at ajuda@comunidademr.com.")

if __name__ == "__main__":
    main()
```
