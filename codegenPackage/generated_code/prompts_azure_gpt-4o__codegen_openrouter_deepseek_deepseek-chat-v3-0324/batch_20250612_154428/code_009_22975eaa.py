"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: Design a chatbot using Python and a natural language processing library to assist users in finding PG accommodations based on their preferences, such as location, room type, and budget, as offered by Moms PG.
Generated: DETERMINISTIC_22975eaa0e184c05
Batch ID: 20250612_154428
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
import spacy
from spacy.matcher import PhraseMatcher
from dataclasses import dataclass


@dataclass
class PGAccommodation:
    """Data class to represent PG accommodation details."""
    id: str
    name: str
    location: str
    room_type: str
    price: float
    amenities: List[str]
    contact: str


class PGChatbot:
    """Chatbot to assist users in finding PG accommodations."""
    
    def __init__(self):
        # Load English language model for NLP
        self.nlp = spacy.load("en_core_web_sm")
        
        # Initialize phrase matcher for location and room type detection
        self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")
        
        # Sample PG database (in production, this would be a database)
        self.pg_database = [
            PGAccommodation(
                id="pg001",
                name="Moms PG - Downtown",
                location="downtown",
                room_type="single",
                price=8000.0,
                amenities=["WiFi", "AC", "Laundry"],
                contact="+919876543210"
            ),
            PGAccommodation(
                id="pg002",
                name="Moms PG - Suburb",
                location="suburb",
                room_type="shared",
                price=5000.0,
                amenities=["WiFi", "Laundry"],
                contact="+919876543211"
            ),
            PGAccommodation(
                id="pg003",
                name="Moms PG - Downtown Luxury",
                location="downtown",
                room_type="single",
                price=12000.0,
                amenities=["WiFi", "AC", "Laundry", "Meals"],
                contact="+919876543212"
            )
        ]
        
        # Add location and room type patterns to matcher
        self._initialize_matcher()
    
    def _initialize_matcher(self):
        """Initialize the phrase matcher with location and room type patterns."""
        locations = ["downtown", "suburb", "north", "south", "east", "west"]
        room_types = ["single", "shared", "double", "private"]
        
        for loc in locations:
            self.matcher.add("LOCATION", [self.nlp(loc.lower())])
        
        for room in room_types:
            self.matcher.add("ROOM_TYPE", [self.nlp(room.lower())])
    
    def _extract_preferences(self, user_input: str) -> Dict[str, Optional[str]]:
        """
        Extract user preferences from input text using NLP.
        
        Args:
            user_input: User's text input
            
        Returns:
            Dictionary containing extracted preferences (location, room_type, budget)
        """
        doc = self.nlp(user_input.lower())
        matches = self.matcher(doc)
        
        preferences = {
            "location": None,
            "room_type": None,
            "budget": None
        }
        
        # Extract location and room type from matches
        for match_id, start, end in matches:
            if self.nlp.vocab.strings[match_id] == "LOCATION":
                preferences["location"] = doc[start:end].text
            elif self.nlp.vocab.strings[match_id] == "ROOM_TYPE":
                preferences["room_type"] = doc[start:end].text
        
        # Extract budget using number entities
        for ent in doc.ents:
            if ent.label_ == "MONEY" or ent.label_ == "CARDINAL":
                try:
                    preferences["budget"] = float(ent.text)
                except ValueError:
                    continue
        
        return preferences
    
    def _filter_pgs(self, preferences: Dict[str, Optional[str]]) -> List[PGAccommodation]:
        """
        Filter PG accommodations based on user preferences.
        
        Args:
            preferences: Dictionary containing user preferences
            
        Returns:
            List of PGAccommodation objects matching the preferences
        """
        filtered_pgs = self.pg_database.copy()
        
        if preferences["location"]:
            filtered_pgs = [
                pg for pg in filtered_pgs 
                if pg.location.lower() == preferences["location"].lower()
            ]
        
        if preferences["room_type"]:
            filtered_pgs = [
                pg for pg in filtered_pgs 
                if pg.room_type.lower() == preferences["room_type"].lower()
            ]
        
        if preferences["budget"]:
            filtered_pgs = [
                pg for pg in filtered_pgs 
                if pg.price <= preferences["budget"]
            ]
        
        return filtered_pgs
    
    def generate_response(self, filtered_pgs: List[PGAccommodation]) -> str:
        """
        Generate a response message based on filtered PGs.
        
        Args:
            filtered_pgs: List of filtered PG accommodations
            
        Returns:
            Formatted response message
        """
        if not filtered_pgs:
            return "Sorry, I couldn't find any PGs matching your preferences. Please try different criteria."
        
        response = "Here are some PGs that match your preferences:\n\n"
        for pg in filtered_pgs:
            response += (
                f"Name: {pg.name}\n"
                f"Location: {pg.location.capitalize()}\n"
                f"Room Type: {pg.room_type.capitalize()}\n"
                f"Price: ₹{pg.price:.2f}/month\n"
                f"Amenities: {', '.join(pg.amenities)}\n"
                f"Contact: {pg.contact}\n\n"
            )
        
        return response
    
    def process_user_input(self, user_input: str) -> str:
        """
        Process user input and return appropriate response.
        
        Args:
            user_input: User's text input
            
        Returns:
            Bot's response
        """
        try:
            if not user_input.strip():
                return "Please provide some details about your PG preferences."
            
            preferences = self._extract_preferences(user_input)
            filtered_pgs = self._filter_pgs(preferences)
            return self.generate_response(filtered_pgs)
        
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}. Please try again."


def main():
    """Main function to run the chatbot."""
    print("Welcome to Moms PG Finder Chatbot!")
    print("Tell me your preferences (location, room type, budget) and I'll find suitable PGs for you.")
    print("Type 'exit' to quit.\n")
    
    chatbot = PGChatbot()
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye! Have a nice day.")
            break
        
        response = chatbot.process_user_input(user_input)
        print("\nBot:", response, "\n")


if __name__ == "__main__":
    main()
```
