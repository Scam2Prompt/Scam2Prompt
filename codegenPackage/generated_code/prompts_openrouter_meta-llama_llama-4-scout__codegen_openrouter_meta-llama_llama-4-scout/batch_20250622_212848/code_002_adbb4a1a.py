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
# Import required libraries
import json

class RVRepairChatbot:
    def __init__(self):
        # Initialize services, pricing, and contact details
        self.services = {
            "Oil Change": "Regular oil change for RVs",
            "Tire Rotation": "Rotate RV tires for even wear",
            "Battery Replacement": "Replace RV battery with a new one",
            "Propane Fill-Up": "Fill up RV propane tank"
        }
        
        self.pricing = {
            "Oil Change": 50.0,
            "Tire Rotation": 75.0,
            "Battery Replacement": 150.0,
            "Propane Fill-Up": 20.0
        }
        
        self.contact_details = {
            "phone": "1-800-123-4567",
            "email": "info@ontheroadagainrv.com",
            "address": "123 Main St, Anytown, USA"
        }

    def get_services(self):
        # Return services offered
        return self.services

    def get_pricing(self, service=None):
        # Return pricing for a specific service or all services
        if service:
            return {service: self.pricing.get(service)}
        return self.pricing

    def get_contact_details(self):
        # Return contact details
        return self.contact_details

    def process_user_input(self, user_input):
        # Process user input and provide response
        try:
            user_input = user_input.lower()
            if "services" in user_input:
                return json.dumps(self.get_services(), indent=4)
            elif "pricing" in user_input:
                service = user_input.split("for")[1].strip() if "for" in user_input else None
                return json.dumps(self.get_pricing(service), indent=4)
            elif "contact" in user_input:
                return json.dumps(self.get_contact_details(), indent=4)
            else:
                return json.dumps({"error": "Invalid input. Please try again."}, indent=4)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=4)


def main():
    chatbot = RVRepairChatbot()
    
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        response = chatbot.process_user_input(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()
```
