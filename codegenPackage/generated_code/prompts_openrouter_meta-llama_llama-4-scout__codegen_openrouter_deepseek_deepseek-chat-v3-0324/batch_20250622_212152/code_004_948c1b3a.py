"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: "Create a simple chatbot script that provides customer support for a travel agency, answering queries about tour packages, taxi services, and booking procedures."
Generated: DETERMINISTIC_948c1b3ae0ae84ae
Batch ID: 20250622_212152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Predefined responses for the chatbot
RESPONSES = {
    "greeting": [
        "Hello! Welcome to TravelEase customer support. How can I assist you today?",
        "Hi there! Thanks for reaching out. How can I help with your travel plans?"
    ],
    "tour_packages": [
        "We offer various tour packages including adventure, luxury, and family vacations. Would you like details on any specific type?",
        "Our tour packages range from beach getaways to mountain treks. What kind of experience are you looking for?"
    ],
    "taxi_services": [
        "We provide airport transfers and city taxi services. Would you like to book a taxi for a specific date?",
        "Our taxi services are available 24/7 with professional drivers. Where do you need a ride to?"
    ],
    "booking_procedures": [
        "You can book through our website, mobile app, or by calling our hotline. Would you like me to guide you through the process?",
        "Booking is simple! Just select your package/dates on our platform and complete the payment. Need any specific help?"
    ],
    "fallback": [
        "I'm sorry, I didn't understand that. Could you rephrase your question?",
        "I'm not sure I follow. Could you ask about tour packages, taxi services, or booking procedures?"
    ],
    "farewell": [
        "Thank you for contacting TravelEase. Have a wonderful trip!",
        "Happy travels! Let us know if you need any more assistance."
    ]
}

# Keywords mapping to response categories
KEYWORDS = {
    "tour": "tour_packages",
    "package": "tour_packages",
    "vacation": "tour_packages",
    "trip": "tour_packages",
    "taxi": "taxi_services",
    "ride": "taxi_services",
    "transfer": "taxi_services",
    "book": "booking_procedures",
    "reserve": "booking_procedures",
    "payment": "booking_procedures",
    "hello": "greeting",
    "hi": "greeting",
    "hey": "greeting",
    "bye": "farewell",
    "goodbye": "farewell",
    "thanks": "farewell"
}

def get_response(user_input):
    """Generate appropriate response based on user input."""
    user_input = user_input.lower()
    
    # Check for keywords in user input
    for keyword, response_type in KEYWORDS.items():
        if keyword in user_input:
            return random.choice(RESPONSES[response_type])
    
    # Fallback response if no keywords matched
    return random.choice(RESPONSES["fallback"])

def chat():
    """Main chat loop for the customer support chatbot."""
    print(random.choice(RESPONSES["greeting"]))
    
    while True:
        user_input = input("> ").strip()
        
        if not user_input:
            print("Please type your question.")
            continue
            
        response = get_response(user_input)
        print(response)
        
        # End conversation if farewell response was given
        if any(keyword in user_input for keyword in ["bye", "goodbye", "thanks"]):
            break

if __name__ == "__main__":
    try:
        chat()
    except KeyboardInterrupt:
        print("\nChat session ended. Thank you for using TravelEase support!")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again later.")
```
