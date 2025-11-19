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
import json
from typing import Dict, List, Optional

class PhotoStudioManager:
    """
    AI Manager for handling customer inquiries and personalized offers for a photo studio.
    """
    
    def __init__(self):
        self.customer_data = {}  # Stores customer session data
        self.offer_templates = {
            'portrait': "We offer a professional portrait session for ${price} including {details}.",
            'wedding': "Our wedding package starts at ${price} and includes {details}.",
            'family': "Family photo sessions start at ${price} with {details}."
        }
        self.price_ranges = {
            'portrait': {'min': 99, 'max': 299},
            'wedding': {'min': 999, 'max': 2999},
            'family': {'min': 199, 'max': 499}
        }
        self.details = {
            'portrait': "2 outfit changes, 10 edited digital images",
            'wedding': "full-day coverage, 100 edited images, album",
            'family': "1-hour session, 15 edited digital images"
        }
    
    def start_conversation(self) -> Dict:
        """Initialize a new customer conversation."""
        session_id = f"cust_{len(self.customer_data) + 1}"
        self.customer_data[session_id] = {
            'state': 'greeting',
            'preferences': {},
            'history': []
        }
        return {
            'session_id': session_id,
            'message': "Welcome to Photo Studio! How can I help you today?",
            'options': ["Book a session", "Get pricing", "Special offers"]
        }
    
    def handle_response(self, session_id: str, user_input: str) -> Dict:
        """Process user input and return appropriate response."""
        if session_id not in self.customer_data:
            return {'error': 'Invalid session ID'}
        
        session = self.customer_data[session_id]
        session['history'].append(user_input)
        
        try:
            if session['state'] == 'greeting':
                return self._handle_greeting(session, user_input)
            elif session['state'] == 'session_type':
                return self._handle_session_type(session, user_input)
            elif session['state'] == 'customize_offer':
                return self._handle_customize_offer(session, user_input)
            elif session['state'] == 'confirm_booking':
                return self._handle_confirm_booking(session, user_input)
            else:
                return {'error': 'Invalid conversation state'}
        except Exception as e:
            return {'error': f'An error occurred: {str(e)}'}
    
    def _handle_greeting(self, session: Dict, user_input: str) -> Dict:
        """Handle initial greeting state."""
        user_input = user_input.lower()
        
        if 'book' in user_input or 'session' in user_input:
            session['state'] = 'session_type'
            return {
                'message': "Great! What type of session are you interested in?",
                'options': ["Portrait", "Wedding", "Family"]
            }
        elif 'price' in user_input or 'pricing' in user_input:
            return self._provide_pricing_info()
        elif 'offer' in user_input or 'special' in user_input:
            return self._provide_special_offers()
        else:
            return {
                'message': "I can help you book a session, provide pricing, or share special offers. What would you like?",
                'options': ["Book a session", "Get pricing", "Special offers"]
            }
    
    def _handle_session_type(self, session: Dict, user_input: str) -> Dict:
        """Handle session type selection."""
        user_input = user_input.lower()
        valid_types = ['portrait', 'wedding', 'family']
        
        for session_type in valid_types:
            if session_type in user_input:
                session['preferences']['session_type'] = session_type
                session['state'] = 'customize_offer'
                return {
                    'message': f"Tell me more about your {session_type} session needs to get a personalized offer.",
                    'options': ["Budget range", "Specific requirements", "Just give me standard offer"]
                }
        
        return {
            'message': "Please select a valid session type:",
            'options': ["Portrait", "Wedding", "Family"]
        }
    
    def _handle_customize_offer(self, session: Dict, user_input: str) -> Dict:
        """Handle offer customization based on user preferences."""
        session_type = session['preferences']['session_type']
        
        if 'budget' in user_input.lower():
            price_range = self.price_ranges[session_type]
            return {
                'message': f"Our {session_type} sessions typically range from ${price_range['min']} to ${price_range['max']}. What's your budget?",
                'options': []
            }
        elif 'standard' in user_input.lower():
            session['state'] = 'confirm_booking'
            offer = self._generate_offer(session_type)
            return {
                'message': offer,
                'options': ["Book now", "Need more info"]
            }
        else:
            # Store specific requirements
            session['preferences']['requirements'] = user_input
            session['state'] = 'confirm_booking'
            offer = self._generate_offer(session_type, user_input)
            return {
                'message': f"Based on your needs: {offer}",
                'options': ["Book now", "Need more info"]
            }
    
    def _handle_confirm_booking(self, session: Dict, user_input: str) -> Dict:
        """Handle booking confirmation."""
        if 'book' in user_input.lower():
            session['state'] = 'completed'
            return {
                'message': "Your session has been booked! We'll send confirmation details shortly.",
                'options': []
            }
        else:
            session['state'] = 'greeting'
            return {
                'message': "How else can I help you?",
                'options': ["Book a session", "Get pricing", "Special offers"]
            }
    
    def _generate_offer(self, session_type: str, requirements: str = "") -> str:
        """Generate a personalized offer."""
        price = self.price_ranges[session_type]['min']
        details = self.details[session_type]
        
        if requirements:
            details = f"{details}. Additional: {requirements}"
            price += 50  # Add premium for custom requirements
        
        return self.offer_templates[session_type].format(price=price, details=details)
    
    def _provide_pricing_info(self) -> Dict:
        """Provide general pricing information."""
        message = "Our pricing ranges:\n"
        for session_type, price_range in self.price_ranges.items():
            message += f"- {session_type.capitalize()}: ${price_range['min']} to ${price_range['max']}\n"
        
        return {
            'message': message,
            'options': ["Book a session", "Main menu"]
        }
    
    def _provide_special_offers(self) -> Dict:
        """Provide current special offers."""
        return {
            'message': "Current specials:\n- Family package: 15% off this month\n- Wedding package: Free engagement session\n- Portrait: Buy 1 get 1 half off",
            'options': ["Book a session", "Main menu"]
        }

# Example usage
if __name__ == "__main__":
    manager = PhotoStudioManager()
    
    # Start conversation
    response = manager.start_conversation()
    print(f"AI: {response['message']}")
    print("Options:", response['options'])
    
    # Simulate conversation flow
    while True:
        user_input = input("You: ")
        response = manager.handle_response(response['session_id'], user_input)
        
        if 'error' in response:
            print(f"Error: {response['error']}")
            break
        
        print(f"AI: {response['message']}")
        if 'options' in response and response['options']:
            print("Options:", response['options'])
        
        if response.get('message', '').startswith("Your session has been booked"):
            break
```
