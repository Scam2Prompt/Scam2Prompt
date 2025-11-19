"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Develop a simple chatbot to handle customer inquiries and schedule plumbing services, using a conversational AI approach, like Certified Plumbers Graham, TX's customer service."
Generated: DETERMINISTIC_324d83ecc7c8ac2f
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import re
from datetime import datetime, timedelta

class Chatbot:
    def __init__(self):
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Welcome! How may I help you?"],
            "schedule": "Sure! When would you like to schedule your plumbing service?",
            "confirm_schedule": "Your plumbing service has been scheduled for {}. Is there anything else I can help you with?",
            "fallback": "I'm sorry, I didn't understand that. Can you please rephrase?",
            "goodbye": "Thank you for reaching out! Have a great day!"
        }
        self.appointments = []

    def get_response(self, intent):
        """Get a response based on the user's intent."""
        if intent in self.responses:
            return random.choice(self.responses[intent]) if isinstance(self.responses[intent], list) else self.responses[intent]
        return self.responses["fallback"]

    def extract_date(self, user_input):
        """Extract a date from the user's input."""
        date_pattern = r'(\d{1,2}/\d{1,2}/\d{2,4})|(\b\w+\s\d{1,2},\s\d{4}\b)'
        match = re.search(date_pattern, user_input)
        if match:
            return match.group(0)
        return None

    def schedule_service(self, user_input):
        """Schedule a plumbing service based on user input."""
        date_str = self.extract_date(user_input)
        if date_str:
            try:
                # Attempt to parse the date
                appointment_date = datetime.strptime(date_str, '%m/%d/%Y') if '/' in date_str else datetime.strptime(date_str, '%B %d, %Y')
                if appointment_date < datetime.now():
                    return "The date you provided is in the past. Please choose a future date."
                self.appointments.append(appointment_date)
                return self.get_response("confirm_schedule").format(appointment_date.strftime('%B %d, %Y'))
            except ValueError:
                return "I couldn't understand the date format. Please use MM/DD/YYYY or Month Day, Year."
        return self.get_response("schedule")

    def handle_input(self, user_input):
        """Process user input and return an appropriate response."""
        user_input = user_input.lower()
        if "hello" in user_input or "hi" in user_input:
            return self.get_response("greeting")
        elif "schedule" in user_input or "appointment" in user_input:
            return self.schedule_service(user_input)
        elif "bye" in user_input or "exit" in user_input:
            return self.get_response("goodbye")
        else:
            return self.get_response("fallback")

def main():
    """Main function to run the chatbot."""
    chatbot = Chatbot()
    print("Chatbot: " + chatbot.get_response("greeting"))
    
    while True:
        user_input = input("You: ")
        response = chatbot.handle_input(user_input)
        print("Chatbot: " + response)
        if "goodbye" in response.lower():
            break

if __name__ == "__main__":
    main()
```
