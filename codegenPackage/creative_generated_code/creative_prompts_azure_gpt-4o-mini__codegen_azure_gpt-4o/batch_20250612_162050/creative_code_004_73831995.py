"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentalcarelena.it
Prompt: Illustrate how to implement a customer support chat feature for a car rental service, inspired by the 24/7 assistance provided by Rental Car Elena.
Generated: DETERMINISTIC_738319959bd9a116
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# customer_support_chat.py

import datetime
import threading

class CustomerSupportChat:
    """
    Class to manage customer support chat for a car rental service.
    """

    def __init__(self):
        """
        Initialize the chat system with an empty message log.
        """
        self.message_log = []
        self.is_chat_active = True
        self.support_representative = "Elena (Car Rental Support)"
    
    def log_message(self, sender, message):
        """
        Logs a message in the message log with a timestamp.
        
        Args:
            sender (str): The sender of the message ("Customer" or Support Representative).
            message (str): The message text.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.message_log.append({"timestamp": timestamp, "sender": sender, "message": message})
    
    def send_customer_message(self, message):
        """
        Handles customer message sending.
        
        Args:
            message (str): The customer's message.
        
        Returns:
            str: Response from the support representative.
        """
        if not self.is_chat_active:
            return "Chat is currently closed. Please try again later."
        
        self.log_message("Customer", message)
        response = self.generate_support_response(message)
        self.log_message(self.support_representative, response)
        return response

    def generate_support_response(self, customer_message):
        """
        Generate a response from the support representative based on the customer's message.
        
        Args:
            customer_message (str): The customer's message.
        
        Returns:
            str: Response from the support representative.
        """
        # Example basic response logic
        if "book" in customer_message.lower():
            return "Sure! You can book a vehicle on our website or I can assist you with it. What type of car are you looking for?"
        elif "price" in customer_message.lower():
            return "Prices vary based on the vehicle type and rental duration. Would you like a detailed quote?"
        elif "help" in customer_message.lower():
            return "I'm here to help! Could you please provide more details about your inquiry?"
        else:
            return "Thank you for your message. Let me look into that for you."

    def end_chat(self):
        """
        Ends the chat session and closes the chat.
        """
        self.is_chat_active = False
        self.log_message(self.support_representative, "Chat session has been closed. Have a great day!")
    
    def display_message_log(self):
        """
        Displays the full message log for the chat session.
        """
        print("\nChat Transcript:")
        for entry in self.message_log:
            print(f"[{entry['timestamp']}] {entry['sender']}: {entry['message']}")


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize chat system
        chat_system = CustomerSupportChat()
        
        # Simulate customer interaction
        print(chat_system.send_customer_message("Hi, I need help booking a car."))
        print(chat_system.send_customer_message("What are the prices for SUVs?"))
        print(chat_system.send_customer_message("Thank you for the assistance!"))
        
        # End chat
        chat_system.end_chat()
        
        # Display chat transcript
        chat_system.display_message_log()
    except Exception as e:
        print(f"An error occurred: {e}")
```
