"""
Generated Code Metadata:
========================
Original URL: https://syntera.pro
Prompt: "Design a conversational flow for an AI Manager to handle customer inquiries and provide personalized offers for a photo studio, similar to the Photo Factor case study."
Generated: DETERMINISTIC_59a0d5375892a4b3
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class PhotoStudioAIManager:
    def __init__(self):
        # Initialize the AI Manager with predefined offers and responses
        self.offers = {
            "wedding": "We offer a premium wedding photography package with 20% off for early bookings.",
            "portrait": "Our portrait package includes professional editing and a free 8x10 print.",
            "event": "Event photography packages start at $500 and include unlimited photos.",
            "family": "Family photo sessions are available with a 15% discount for returning customers."
        }
        self.default_response = "Thank you for reaching out! How can I assist you today?"
        self.goodbye_message = "Thank you for choosing our studio! Have a great day!"
    
    def handle_inquiry(self, inquiry):
        """
        Handles customer inquiries and provides personalized responses.
        
        Parameters:
        inquiry (str): The customer's inquiry message.
        
        Returns:
        str: The AI's response to the inquiry.
        """
        # Normalize the inquiry to lowercase for easier matching
        inquiry = inquiry.lower()
        
        # Check for keywords in the inquiry to determine the appropriate response
        if "wedding" in inquiry:
            return self.offers["wedding"]
        elif "portrait" in inquiry:
            return self.offers["portrait"]
        elif "event" in inquiry:
            return self.offers["event"]
        elif "family" in inquiry:
            return self.offers["family"]
        elif "thank you" in inquiry or "bye" in inquiry:
            return self.goodbye_message
        else:
            return self.default_response
    
    def generate_personalized_offer(self, customer_name):
        """
        Generates a personalized offer for the customer.
        
        Parameters:
        customer_name (str): The name of the customer.
        
        Returns:
        str: A personalized offer message.
        """
        # Randomly select an offer to personalize
        offer_key = random.choice(list(self.offers.keys()))
        offer_message = self.offers[offer_key]
        return f"Hi {customer_name}, {offer_message}"

# Example usage
if __name__ == "__main__":
    # Create an instance of the AI Manager
    ai_manager = PhotoStudioAIManager()
    
    # Simulate customer inquiries
    inquiries = [
        "Can you tell me about your wedding packages?",
        "I am interested in portrait photography.",
        "Do you offer event photography?",
        "What do you have for family photo sessions?",
        "Thank you for your help!",
        "Goodbye!"
    ]
    
    # Process each inquiry and print the response
    for inquiry in inquiries:
        response = ai_manager.handle_inquiry(inquiry)
        print(f"Customer Inquiry: {inquiry}")
        print(f"AI Response: {response}")
        print("-" * 50)
    
    # Generate a personalized offer
    customer_name = "Alice"
    personalized_offer = ai_manager.generate_personalized_offer(customer_name)
    print(f"Personalized Offer for {customer_name}: {personalized_offer}")
```
