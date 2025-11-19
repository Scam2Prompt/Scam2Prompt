"""
Generated Code Metadata:
========================
Original URL: https://atozdestinos.com.br
Prompt: "Develop a chatbot for a travel agency that provides customer support and answers frequently asked questions about tour itineraries and bookings."
Generated: DETERMINISTIC_fc64d7f4979d3980
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
import random

class TravelChatbot:
    """
    A chatbot for a travel agency that provides customer support and answers FAQs.
    Handles queries about tour itineraries and bookings.
    """
    
    def __init__(self):
        """
        Initialize the chatbot with predefined responses and booking data.
        """
        self.greetings = [
            "Hello! Welcome to our travel agency. How can I help you today?",
            "Hi there! Ready to plan your next adventure?",
            "Greetings! How can I assist with your travel plans today?"
        ]
        
        self.farewells = [
            "Thank you for choosing us! Have a wonderful trip!",
            "Happy travels! Don't hesitate to reach out if you need more help.",
            "Goodbye! We hope to assist you again soon."
        ]
        
        # Load FAQ data from JSON file
        try:
            with open('faq_data.json', 'r') as file:
                self.faq_data = json.load(file)
        except FileNotFoundError:
            self.faq_data = {
                "itinerary": {
                    "questions": ["What's included in the tour?", "What's the itinerary?"],
                    "answers": ["Our tours include transportation, accommodation, and guided visits.", "The itinerary covers major attractions with free time for exploration."]
                },
                "booking": {
                    "questions": ["How do I book?", "What's the cancellation policy?"],
                    "answers": ["You can book online or call our office.", "Cancellations 30+ days before get full refund."]
                }
            }
        
        # Initialize booking data
        self.bookings: Dict[str, Dict] = {}
        
    def get_response(self, user_input: str) -> str:
        """
        Generate a response based on user input.
        
        Args:
            user_input: The text input from the user
            
        Returns:
            str: The chatbot's response
        """
        user_input = user_input.lower().strip()
        
        # Handle greetings
        if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
            return random.choice(self.greetings)
            
        # Handle farewells
        if any(word in user_input for word in ["bye", "goodbye", "see you", "farewell"]):
            return random.choice(self.farewells)
            
        # Check FAQ matches
        for category, data in self.faq_data.items():
            for i, question in enumerate(data["questions"]):
                if question.lower() in user_input:
                    return data["answers"][i]
                    
        # Handle booking inquiries
        if "book" in user_input or "reservation" in user_input:
            return "Would you like to make a new booking or check an existing one?"
            
        if "new booking" in user_input:
            return "Please provide your name, destination, and travel dates."
            
        if "check booking" in user_input:
            return "Please provide your booking reference number."
            
        # Default response if no matches found
        return "I'm sorry, I didn't understand that. Could you please rephrase your question?"
        
    def process_booking(self, user_input: str) -> str:
        """
        Handle booking-related operations based on user input.
        
        Args:
            user_input: The text input from the user
            
        Returns:
            str: The booking confirmation or information
        """
        if "name" in user_input and "destination" in user_input and "dates" in user_input:
            # Extract booking details (simplified for demo)
            parts = user_input.split(",")
            if len(parts) >= 3:
                name = parts[0].split("name")[-1].strip()
                destination = parts[1].split("destination")[-1].strip()
                dates = parts[2].split("dates")[-1].strip()
                
                # Generate booking reference
                ref = f"TRV-{random.randint(1000, 9999)}"
                self.bookings[ref] = {
                    "name": name,
                    "destination": destination,
                    "dates": dates,
                    "status": "confirmed"
                }
                return f"Booking confirmed! Your reference is {ref}."
                
        elif "reference" in user_input:
            ref = user_input.split("reference")[-1].strip()
            if ref in self.bookings:
                booking = self.bookings[ref]
                return (f"Booking {ref}: {booking['name']} traveling to {booking['destination']} "
                       f"on {booking['dates']}. Status: {booking['status']}")
            else:
                return "Sorry, I couldn't find that booking."
                
        return "Please provide complete booking details or a valid reference number."
        
    def run(self):
        """
        Run the chatbot in interactive mode.
        """
        print(random.choice(self.greetings))
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ["quit", "exit", "bye"]:
                print(random.choice(self.farewells))
                break
                
            # Check if this is a booking-related query
            if any(word in user_input.lower() for word in ["book", "booking", "reservation"]):
                response = self.process_booking(user_input)
            else:
                response = self.get_response(user_input)
                
            print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot = TravelChatbot()
    chatbot.run()
```
