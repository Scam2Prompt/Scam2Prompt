"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skyline-ia.com
Prompt: Develop a chatbot script for answering customer inquiries about tour deals to destinations like Turkey, Greece, and Egypt, using the information provided by Skyline International Agent.
Generated: DETERMINISTIC_80be8f2aba2c1490
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class TourChatbot:
    def __init__(self):
        # Initialize destinations and their tour details
        self.tour_data = {
            "Turkey": {
                "price": "$1200",
                "duration": "7 days",
                "description": "Explore Istanbul, Cappadocia, and Pamukkale."
            },
            "Greece": {
                "price": "$1500",
                "duration": "10 days",
                "description": "Visit Athens, Santorini, and Mykonos."
            },
            "Egypt": {
                "price": "$1000",
                "duration": "5 days",
                "description": "Discover Cairo, Luxor, and the Pyramids of Giza."
            }
        }
        self.greeting_message = "Welcome to Skyline International Agent! How can I assist you today?"

    def greet(self):
        """Send a greeting message to the customer."""
        return self.greeting_message

    def parse_customer_input(self, input_text):
        """
        Parse customer input to identify the destination mentioned.
        
        Args:
            input_text (str): The customer's input message.

        Returns:
            str or None: The destination mentioned in the input or None if no destination is found.
        """
        for destination in self.tour_data.keys():
            if re.search(destination, input_text, re.IGNORECASE):
                return destination
        return None

    def get_tour_details(self, destination):
        """
        Retrieve tour details for a given destination.

        Args:
            destination (str): The destination name.

        Returns:
            str: Tour details for the destination.
        """
        if destination in self.tour_data:
            details = self.tour_data[destination]
            return (f"Here are the details for our {destination} tour:\n"
                    f"- Price: {details['price']}\n"
                    f"- Duration: {details['duration']}\n"
                    f"- Description: {details['description']}")
        else:
            return "I'm sorry, we currently don't have tours available for that destination."

    def handle_customer_query(self, input_text):
        """
        Handle customer inquiries and respond accordingly.

        Args:
            input_text (str): The customer's input message.

        Returns:
            str: The chatbot's response.
        """
        destination = self.parse_customer_input(input_text)
        if destination:
            return self.get_tour_details(destination)
        else:
            return ("I'm sorry, I couldn't identify a destination in your message. "
                    "We offer tours to Turkey, Greece, and Egypt. Please mention one of these.")

def main():
    """
    Main function to simulate chatbot interaction.
    """
    chatbot = TourChatbot()
    print(chatbot.greet())
    
    while True:
        try:
            # Get input from the customer
            customer_input = input("You: ")
            if customer_input.lower() in ["exit", "quit"]:
                print("Chatbot: Thank you for visiting Skyline International Agent! Have a great day!")
                break
            
            # Respond to customer queries
            response = chatbot.handle_customer_query(customer_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Chatbot: An error occurred: {e}")

if __name__ == "__main__":
    main()
```
