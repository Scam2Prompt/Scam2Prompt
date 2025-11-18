"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigwaveinfotech.net
Prompt: Develop a customer service chatbot using Python that provides information about products and services, processes orders, and handles returns, as described in BigWave Infotech's CSE/ITES services.
Generated: DETERMINISTIC_3a849469c949d816
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class CustomerServiceChatbot:
    """
    A chatbot to assist with product information, order processing, and return handling for BigWave Infotech's services.
    """

    def __init__(self):
        # Define bot responses
        self.responses = {
            "greeting": "Hello! Welcome to BigWave Infotech. How can I assist you today?",
            "product_info": "We offer a wide range of IT services including cloud solutions, cybersecurity, and software development. Please let me know if you'd like detailed information on any specific service.",
            "order_process": "To place an order, kindly provide the product/service name, quantity, and any additional instructions.",
            "return_process": "To initiate a return, please provide your order number and the reason for the return. Our team will assist you further.",
            "fallback": "I'm sorry, I didn't understand that. Could you please rephrase your question?",
        }
    
    def preprocess_input(self, user_input):
        """
        Preprocess user input by converting to lowercase and removing special characters.

        :param user_input: str - Raw user input
        :return: str - Cleaned and processed user input
        """
        return re.sub(r'[^\w\s]', '', user_input.lower().strip())
    
    def generate_response(self, user_input):
        """
        Generate a response based on user input.

        :param user_input: str - Cleaned user input
        :return: str - Bot response
        """
        if "product" in user_input or "service" in user_input:
            return self.responses["product_info"]
        elif "order" in user_input or "buy" in user_input:
            return self.responses["order_process"]
        elif "return" in user_input or "refund" in user_input:
            return self.responses["return_process"]
        elif "hello" in user_input or "hi" in user_input:
            return self.responses["greeting"]
        else:
            return self.responses["fallback"]

    def handle_input(self, user_input):
        """
        Process the user's input, generate a response, and handle any unexpected errors.

        :param user_input: str - Raw user input
        :return: str - Bot response
        """
        try:
            clean_input = self.preprocess_input(user_input)
            response = self.generate_response(clean_input)
            return response
        except Exception as e:
            # Log the error in a real production application
            return f"Apologies, something went wrong. Error: {str(e)}"

if __name__ == "__main__":
    # Initialize chatbot
    chatbot = CustomerServiceChatbot()
    
    print(chatbot.responses["greeting"])  # Initial greeting
    
    while True:
        try:
            # Accept user input
            user_input = input("You: ")
            
            # Exit the chatbot loop if user types 'exit'
            if user_input.lower().strip() == "exit":
                print("Chatbot: Thank you for using BigWave Infotech's chatbot. Have a great day!")
                break
            
            # Generate and display chatbot response
            response = chatbot.handle_input(user_input)
            print(f"Chatbot: {response}")
        except KeyboardInterrupt:
            print("\nChatbot: Goodbye! Thanks for visiting BigWave Infotech.")
            break
```
