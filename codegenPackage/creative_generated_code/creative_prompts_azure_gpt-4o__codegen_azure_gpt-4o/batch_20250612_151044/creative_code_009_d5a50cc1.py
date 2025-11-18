"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiomartdigital.com
Prompt: Create a chatbot script that helps customers navigate Jiomart Digital's product categories, such as home appliances and personal care, and assists with financing options.
Generated: DETERMINISTIC_d5a50cc11c421454
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging


# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Chatbot:
    def __init__(self):
        """
        Initialize chatbot with predefined product categories and financing options.
        """
        self.product_categories = {
            "home_appliances": ["Refrigerators", "Washing Machines", "Microwave Ovens", "Air Conditioners"],
            "personal_care": ["Hair Dryers", "Trimmers", "Electric Toothbrushes", "Body Massagers"]
        }
        self.financing_options = [
            "0% EMI for 6 months",
            "Credit Card EMI",
            "Pay Later with BNPL (Buy Now Pay Later)",
            "Bank Loan Assistance"
        ]
    
    def greet(self):
        """
        Greet the customer and provide navigation options.
        """
        greeting_message = "Welcome to Jiomart Digital! How can I assist you today?\n"
        greeting_message += "1. Browse Product Categories\n"
        greeting_message += "2. Learn about Financing Options\n"
        greeting_message += "3. Exit\n"
        return greeting_message
    
    def show_categories(self):
        """
        Display available product categories and their subcategories.
        """
        message = "Here are the available product categories:\n"
        for category, items in self.product_categories.items():
            message += f"- {category.replace('_', ' ').title()}: {', '.join(items)}\n"
        return message
    
    def show_financing_options(self):
        """
        Display available financing options.
        """
        message = "Here are the financing options we offer:\n"
        for idx, option in enumerate(self.financing_options, start=1):
            message += f"{idx}. {option}\n"
        return message
    
    def handle_user_input(self, user_input):
        """
        Handle user input and guide the conversation.
        """
        try:
            if user_input == "1":
                return self.show_categories()
            elif user_input == "2":
                return self.show_financing_options()
            elif user_input == "3":
                return "Thank you for visiting Jiomart Digital. Have a great day!"
            else:
                return "Invalid input. Please enter 1, 2, or 3."
        except Exception as e:
            logging.error(f"Error processing user input: {e}")
            return "An error occurred. Please try again later."
    
    def start_chat(self):
        """
        Start the chatbot interaction loop.
        """
        print(self.greet())
        while True:
            user_input = input("Enter your choice (1, 2, or 3): ")
            response = self.handle_user_input(user_input)
            print(response)
            if user_input == "3":
                break


if __name__ == "__main__":
    try:
        # Initialize and start the chatbot
        chatbot = Chatbot()
        chatbot.start_chat()
    except KeyboardInterrupt:
        print("\nChatbot session ended.")
    except Exception as e:
        logging.error(f"Unhandled exception occurred: {e}")
        print("An error occurred with the chatbot. Please try again later.")
```
