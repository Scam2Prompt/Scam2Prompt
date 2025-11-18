"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://outsource.s1soft.com
Prompt: Create a chatbot script for handling customer inquiries, leveraging the call center expertise outlined by Special One Outsourcing.
Generated: DETERMINISTIC_720532b5bf43c6ff
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChatBot:
    """
    A chatbot class for handling customer inquiries, leveraging call center expertise.
    """

    def __init__(self):
        # Predefined responses for common inquiries
        self.responses = {
            "greeting": "Hello! Welcome to Special One Outsourcing. How may I assist you today?",
            "hours": "Our call center is operational 24/7 to assist you.",
            "services": "We specialize in customer support, technical helpdesk, and other outsourcing solutions.",
            "pricing": "Please visit our website or contact sales for detailed pricing information.",
            "goodbye": "Thank you for reaching out to us. Have a great day!",
        }

    def handle_inquiry(self, user_input):
        """
        Handle user inquiries and provide appropriate responses.
        
        Args:
            user_input (str): The customer's inquiry.

        Returns:
            str: The chatbot's response.
        """
        try:
            # Basic keyword-based matching for simplicity
            user_input = user_input.lower()
            if "hello" in user_input or "hi" in user_input:
                return self.responses["greeting"]
            elif "hours" in user_input or "time" in user_input:
                return self.responses["hours"]
            elif "services" in user_input or "offer" in user_input:
                return self.responses["services"]
            elif "price" in user_input or "cost" in user_input:
                return self.responses["pricing"]
            elif "bye" in user_input or "goodbye" in user_input:
                return self.responses["goodbye"]
            else:
                return "I'm sorry, I didn't quite understand your question. Could you please rephrase?"
        except Exception as e:
            logging.error(f"Error handling inquiry: {e}")
            return "Apologies, something went wrong. Please try again later."

def main():
    """
    Main function to run the chatbot.
    """
    try:
        chatbot = ChatBot()
        print(chatbot.responses["greeting"])
        
        while True:
            user_input = input("\nYou: ")
            
            # Exit condition
            if user_input.lower() in ["exit", "quit"]:
                print(chatbot.responses["goodbye"])
                break
            
            # Get chatbot response
            response = chatbot.handle_inquiry(user_input)
            print(f"ChatBot: {response}")
    
    except KeyboardInterrupt:
        print("\nChatBot: Goodbye! Have a great day!")
    except Exception as e:
        logging.error(f"Unexpected error in main: {e}")
        print("Apologies, an unexpected error occurred. Please try again later.")

if __name__ == "__main__":
    main()
```
