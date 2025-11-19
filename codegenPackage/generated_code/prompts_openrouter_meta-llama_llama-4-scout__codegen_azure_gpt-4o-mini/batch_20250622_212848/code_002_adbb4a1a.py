"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Generate a code snippet to implement a simple chatbot that provides RV repair services information, including services offered, pricing, and contact details, for a company like On The Road Again RV Service & Repair.
Generated: DETERMINISTIC_adbb4a1ab50006e7
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class RVRepairChatbot:
    def __init__(self):
        # Initialize the chatbot with service information
        self.services = {
            "Oil Change": {"price": 99.99, "description": "Complete oil change service."},
            "Tire Rotation": {"price": 79.99, "description": "Rotate and balance tires."},
            "Brake Inspection": {"price": 49.99, "description": "Comprehensive brake system check."},
            "Electrical Repair": {"price": 120.00, "description": "Diagnosis and repair of electrical issues."},
            "Plumbing Repair": {"price": 150.00, "description": "Fixing leaks and plumbing issues."}
        }
        self.contact_details = {
            "phone": "1-800-555-0199",
            "email": "info@ontheroadagainrv.com",
            "address": "123 RV Lane, Camp City, CA 90210"
        }

    def get_services(self):
        """Return a list of services offered with pricing and descriptions."""
        return json.dumps(self.services, indent=4)

    def get_contact_details(self):
        """Return the contact details for the RV repair service."""
        return json.dumps(self.contact_details, indent=4)

    def handle_query(self, query):
        """Handle user queries and provide appropriate responses."""
        query = query.lower()
        if "services" in query:
            return self.get_services()
        elif "pricing" in query:
            return self.get_services()  # Pricing is included in services
        elif "contact" in query:
            return self.get_contact_details()
        else:
            return "I'm sorry, I didn't understand that. Please ask about our services, pricing, or contact details."

def main():
    """Main function to run the chatbot."""
    chatbot = RVRepairChatbot()
    print("Welcome to On The Road Again RV Service & Repair Chatbot!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Thank you for using our service. Goodbye!")
            break
        
        try:
            response = chatbot.handle_query(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Chatbot: An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
