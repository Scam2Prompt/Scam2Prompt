"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Develop a chatbot using Python that answers customer inquiries about cleaning services, such as "What is included in the spring cleaning package?" or "Do you offer services in Fredericksburg?"
Generated: DETERMINISTIC_c58c04ea0b19c820
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, List, Optional

class CleaningServiceChatbot:
    """
    A chatbot that answers customer inquiries about cleaning services.
    Handles questions about services, pricing, locations, and general info.
    """
    
    def __init__(self):
        # Knowledge base for the chatbot
        self.knowledge_base = {
            "services": {
                "spring cleaning": {
                    "description": "Our spring cleaning package includes deep cleaning of all rooms, window washing, carpet shampooing, and organization services.",
                    "price": "$199 for up to 2000 sq ft"
                },
                "regular cleaning": {
                    "description": "Regular cleaning includes dusting, vacuuming, mopping, bathroom sanitization, and kitchen cleaning.",
                    "price": "$99 per visit"
                },
                "deep cleaning": {
                    "description": "Deep cleaning covers everything in regular cleaning plus inside appliances, baseboards, and hard-to-reach areas.",
                    "price": "$149 per visit"
                }
            },
            "locations": {
                "fredericksburg": "Yes, we serve the Fredericksburg area with all our cleaning services.",
                "arlington": "Yes, we provide services in Arlington with an additional $20 travel fee.",
                "alexandria": "Yes, we cover Alexandria with standard pricing."
            },
            "general": {
                "availability": "We operate Monday through Saturday from 8 AM to 6 PM.",
                "contact": "You can reach us at (555) 123-4567 or email@cleaningservice.com",
                "booking": "Bookings can be made through our website or by calling our office."
            }
        }
        
        # Patterns for intent recognition
        self.patterns = {
            "service_question": re.compile(r'(what|tell me|describe).*(spring|regular|deep) cleaning', re.IGNORECASE),
            "price_question": re.compile(r'how much|price|cost.*(spring|regular|deep) cleaning', re.IGNORECASE),
            "location_question": re.compile(r'do you (serve|offer|provide).*(fredericksburg|arlington|alexandria)', re.IGNORECASE),
            "general_question": re.compile(r'(availability|contact|hours|booking)', re.IGNORECASE)
        }
        
        # Default responses
        self.default_responses = [
            "I'm sorry, I didn't understand your question. Could you please rephrase it?",
            "I'm not sure I follow. Could you ask about our services, pricing, or locations?",
            "Could you clarify your question about our cleaning services?"
        ]
    
    def _get_service_info(self, service_type: str) -> Optional[str]:
        """Get information about a specific cleaning service."""
        service = self.knowledge_base["services"].get(service_type.lower())
        if service:
            return service["description"]
        return None
    
    def _get_service_price(self, service_type: str) -> Optional[str]:
        """Get pricing information for a specific cleaning service."""
        service = self.knowledge_base["services"].get(service_type.lower())
        if service:
            return f"The price for {service_type} cleaning is {service['price']}."
        return None
    
    def _get_location_info(self, location: str) -> Optional[str]:
        """Get information about service availability in a location."""
        return self.knowledge_base["locations"].get(location.lower())
    
    def _get_general_info(self, topic: str) -> Optional[str]:
        """Get general information about the cleaning service."""
        return self.knowledge_base["general"].get(topic.lower())
    
    def _get_random_default_response(self) -> str:
        """Return a random default response when the query isn't understood."""
        import random
        return random.choice(self.default_responses)
    
    def process_query(self, query: str) -> str:
        """
        Process the user's query and return an appropriate response.
        
        Args:
            query: The user's question about cleaning services
            
        Returns:
            str: The chatbot's response
        """
        try:
            # Check for service description questions
            service_match = self.patterns["service_question"].search(query)
            if service_match:
                service_type = service_match.group(2)
                response = self._get_service_info(service_type)
                if response:
                    return response
            
            # Check for pricing questions
            price_match = self.patterns["price_question"].search(query)
            if price_match:
                service_type = price_match.group(1)
                response = self._get_service_price(service_type)
                if response:
                    return response
            
            # Check for location questions
            location_match = self.patterns["location_question"].search(query)
            if location_match:
                location = location_match.group(2)
                response = self._get_location_info(location)
                if response:
                    return response
            
            # Check for general questions
            general_match = self.patterns["general_question"].search(query)
            if general_match:
                topic = general_match.group(1)
                response = self._get_general_info(topic)
                if response:
                    return response
            
            # If no matches found
            return self._get_random_default_response()
        
        except Exception as e:
            # Log the error in a production environment
            # logger.error(f"Error processing query: {e}")
            return "I'm having trouble answering your question right now. Please try again later."


def run_chatbot():
    """Run the chatbot in interactive mode."""
    chatbot = CleaningServiceChatbot()
    print("Welcome to Cleaning Services Chatbot! How can I help you today?")
    print("Type 'quit' to exit.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Goodbye! Have a great day.")
                break
                
            if not user_input:
                print("Please enter your question about our cleaning services.")
                continue
                
            response = chatbot.process_query(user_input)
            print(f"Bot: {response}\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye! Have a great day.")
            break
        except Exception as e:
            print("Bot: I encountered an error. Please try again.")


if __name__ == "__main__":
    run_chatbot()
```
