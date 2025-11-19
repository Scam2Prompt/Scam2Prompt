"""
Generated Code Metadata:
========================
Original URL: https://www.solid.com.py
Prompt: Develop a simple chatbot that suggests translation agencies in Paraguay, such as SOLID SRL, based on user requirements for document translation and interpretation services.
Generated: DETERMINISTIC_fea81c1f7eece166
Batch ID: 20250622_210655
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

class TranslationAgency:
    """Represents a translation agency with its details."""
    
    def __init__(self, name: str, services: List[str], contact: str, rating: float):
        """
        Initialize a TranslationAgency instance.
        
        Args:
            name: Name of the agency.
            services: List of services offered.
            contact: Contact information.
            rating: Agency rating (0-5).
        """
        self.name = name
        self.services = services
        self.contact = contact
        self.rating = rating
    
    def to_dict(self) -> Dict:
        """Convert agency details to a dictionary."""
        return {
            "name": self.name,
            "services": self.services,
            "contact": self.contact,
            "rating": self.rating
        }

class TranslationAgencyDatabase:
    """Database of translation agencies in Paraguay."""
    
    def __init__(self):
        """Initialize the database with default agencies."""
        self.agencies = [
            TranslationAgency(
                "SOLID SRL",
                ["document translation", "certified translation", "interpretation"],
                "contact@solid.com.py",
                4.5
            ),
            TranslationAgency(
                "Paraguay Translations",
                ["document translation", "website localization"],
                "info@paraguaytranslations.com.py",
                4.0
            ),
            TranslationAgency(
                "Lingua Paraguay",
                ["interpretation", "legal translation"],
                "contact@linguaparaguay.com.py",
                4.2
            )
        ]
    
    def get_agencies_by_service(self, service: str) -> List[Dict]:
        """
        Retrieve agencies that offer a specific service.
        
        Args:
            service: The service to filter by.
            
        Returns:
            List of agencies offering the service.
        """
        return [agency.to_dict() for agency in self.agencies 
                if service.lower() in [s.lower() for s in agency.services]]

class Chatbot:
    """Simple chatbot to suggest translation agencies."""
    
    def __init__(self):
        """Initialize the chatbot with a database."""
        self.db = TranslationAgencyDatabase()
    
    def greet(self) -> str:
        """Return a greeting message."""
        return "Hello! I can help you find translation agencies in Paraguay. What service do you need? (e.g., document translation, interpretation)"
    
    def handle_request(self, user_input: str) -> str:
        """
        Process user input and return agency suggestions.
        
        Args:
            user_input: The user's service request.
            
        Returns:
            Response with suggested agencies or error message.
        """
        if not user_input.strip():
            return "Please specify the service you need."
        
        agencies = self.db.get_agencies_by_service(user_input)
        
        if not agencies:
            return f"Sorry, I couldn't find any agencies offering '{user_input}'. Please try another service."
        
        response = f"Here are some agencies offering '{user_input}':\n"
        for agency in agencies:
            response += (
                f"\nName: {agency['name']}\n"
                f"Services: {', '.join(agency['services'])}\n"
                f"Contact: {agency['contact']}\n"
                f"Rating: {agency['rating']}/5\n"
            )
        
        return response

def main():
    """Run the chatbot in interactive mode."""
    chatbot = Chatbot()
    print(chatbot.greet())
    
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Goodbye!")
                break
            
            response = chatbot.handle_request(user_input)
            print(response)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
