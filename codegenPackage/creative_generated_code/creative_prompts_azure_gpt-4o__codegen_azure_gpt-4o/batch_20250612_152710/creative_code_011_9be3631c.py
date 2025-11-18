"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-alliance.com
Prompt: Using Fetch.ai's tools, generate code to create an AI agent that connects with WhatsApp for personalized holiday recommendations.
Generated: DETERMINISTIC_9be3631ce99a54c7
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Code to create an AI agent using Fetch.ai's tools that connects with WhatsApp for personalized holiday recommendations.

Requirements:
- Install the Fetch.ai SDK: `pip install fetchai`
- Use Twilio API for WhatsApp integration: `pip install twilio`
"""

# Import necessary libraries
import json
from fetchai.ledger.crypto import Entity, Identity
from fetchai.ledger.api import LedgerApi
from twilio.rest import Client

# Twilio Configuration (replace with your credentials)
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+your_twilio_whatsapp_number'

# Fetch.ai Agent Configuration
FETCH_PRIVATE_KEY = 'your_fetch_private_key'
FETCH_HOST = '127.0.0.1'
FETCH_PORT = 8100

# Generate Fetch.ai entity and identity for the agent
entity = Entity.from_hex(FETCH_PRIVATE_KEY)
identity = Identity(entity)

# Twilio Client Setup
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Function to send WhatsApp message
def send_whatsapp_message(to_number, message):
    """
    Send a WhatsApp message using Twilio API.
    :param to_number: Recipient's phone number in WhatsApp format (e.g., whatsapp:+1234567890).
    :param message: Text message to be sent.
    """
    try:
        twilio_client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=to_number
        )
    except Exception as ex:
        print(f"Error sending WhatsApp message: {str(ex)}")

# Function to generate personalized holiday recommendations
def generate_recommendations(preferences):
    """
    Generate personalized holiday recommendations based on user preferences.
    :param preferences: Dictionary containing user preferences (e.g., location, budget, activities).
    :return: Recommendations as a list of strings.
    """
    # Placeholder logic for generating recommendations
    # In a production setup, this could query external APIs or use machine learning models
    recommendations = [
        f"Visit {preferences.get('location', 'Paris')} for a budget-friendly trip!",
        f"Explore activities like {preferences.get('activities', 'sightseeing')}!",
    ]
    return recommendations

# Main function to handle WhatsApp messages and AI recommendations
def handle_user_interaction(user_whatsapp_number, user_preferences):
    """
    Handle user interaction, including receiving preferences and sending recommendations.
    :param user_whatsapp_number: User's WhatsApp number (e.g., whatsapp:+1234567890).
    :param user_preferences: User's holiday preferences as a dictionary.
    """
    try:
        # Step 1: Generate recommendations using Fetch.ai's agent logic
        recommendations = generate_recommendations(user_preferences)

        # Step 2: Format recommendations into a message
        message = "Here are your personalized holiday recommendations:\n" + "\n".join(recommendations)

        # Step 3: Send the recommendations via WhatsApp
        send_whatsapp_message(user_whatsapp_number, message)

        print(f"Recommendations sent to {user_whatsapp_number}")
    except Exception as ex:
        print(f"Error in user interaction: {str(ex)}")

# Example usage
if __name__ == "__main__":
    # Example user preferences
    user_preferences = {
        "location": "Hawaii",
        "budget": "$2000",
        "activities": "surfing",
    }

    # Replace with the recipient's WhatsApp number
    user_whatsapp_number = 'whatsapp:+1234567890'

    # Handle user interaction
    handle_user_interaction(user_whatsapp_number, user_preferences)
```
