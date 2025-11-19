"""
Generated Code Metadata:
========================
Original URL: https://kadma-wine.co.il
Prompt: "Develop a chatbot script to handle customer inquiries about wine tours, tastings, and events at a winery like Kadma Wine, using a natural language processing library like NLTK or spaCy."
Generated: DETERMINISTIC_ca813c373edab3ee
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy
from spacy.matcher import PhraseMatcher
from typing import Dict, List, Optional

# Load the English language model
nlp = spacy.load("en_core_web_sm")

class WineTourChatbot:
    """
    A chatbot to handle inquiries about wine tours, tastings, and events.
    """
    
    def __init__(self):
        self.greetings = ["hi", "hello", "hey", "greetings"]
        self.farewells = ["bye", "goodbye", "see you", "farewell"]
        
        # Define patterns for different types of inquiries
        self.tour_keywords = ["tour", "visit", "winery", "vineyard"]
        self.tasting_keywords = ["tasting", "sample", "try", "flavor"]
        self.event_keywords = ["event", "party", "celebration", "dinner"]
        self.price_keywords = ["price", "cost", "fee", "charge"]
        self.schedule_keywords = ["time", "when", "schedule", "available"]
        
        # Prepare phrase matcher
        self.matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
        patterns = {
            "TOUR": self.tour_keywords,
            "TASTING": self.tasting_keywords,
            "EVENT": self.event_keywords,
            "PRICE": self.price_keywords,
            "SCHEDULE": self.schedule_keywords
        }
        
        for label, phrases in patterns.items():
            self.matcher.add(label, [nlp(text) for text in phrases])
    
    def process_input(self, user_input: str) -> Optional[str]:
        """
        Process user input and generate appropriate response.
        
        Args:
            user_input: The text input from the user
            
        Returns:
            str: The chatbot's response or None if no match found
        """
        doc = nlp(user_input.lower())
        
        # Check for greetings
        if any(token.text in self.greetings for token in doc):
            return "Hello! Welcome to Kadma Wine. How can I help you today?"
        
        # Check for farewells
        if any(token.text in self.farewells for token in doc):
            return "Thank you for visiting Kadma Wine. Have a wonderful day!"
        
        # Match patterns using phrase matcher
        matches = self.matcher(doc)
        categories = set()
        
        for match_id, start, end in matches:
            span = doc[start:end]
            categories.add(nlp.vocab.strings[match_id])
        
        # Generate responses based on matched categories
        responses = []
        
        if "TOUR" in categories:
            responses.append(
                "We offer guided tours of our winery daily from 10 AM to 4 PM. "
                "Tours last approximately 45 minutes and include a visit to our "
                "vineyards and production facilities."
            )
        
        if "TASTING" in categories:
            responses.append(
                "Our wine tastings are available from 11 AM to 5 PM. We offer "
                "three tasting packages: Standard (5 wines), Premium (8 wines), "
                "and Reserve (10 wines with cheese pairing)."
            )
        
        if "EVENT" in categories:
            responses.append(
                "We host various events throughout the year including wine pairing "
                "dinners, harvest festivals, and special holiday celebrations. "
                "Check our website for upcoming events."
            )
        
        if "PRICE" in categories:
            responses.append(
                "Tour prices start at $25 per person. Tasting packages range from "
                "$30 to $75. Event prices vary depending on the occasion. "
                "Group discounts are available for parties of 6 or more."
            )
        
        if "SCHEDULE" in categories:
            responses.append(
                "We're open Tuesday through Sunday from 10 AM to 6 PM. "
                "Closed on Mondays except for private events. "
                "Last tour departs at 4 PM, last tasting at 5 PM."
            )
        
        if responses:
            return " ".join(responses)
        
        return None
    
    def run_chat(self):
        """
        Run the chatbot in interactive mode.
        """
        print("Welcome to Kadma Wine Chatbot! Type 'quit' to exit.")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == "quit":
                print("Chatbot: Thank you for visiting Kadma Wine. Goodbye!")
                break
                
            response = self.process_input(user_input)
            
            if response:
                print(f"Chatbot: {response}")
            else:
                print("Chatbot: I'm sorry, I didn't understand that. Could you rephrase or ask about our tours, tastings, or events?")


if __name__ == "__main__":
    chatbot = WineTourChatbot()
    chatbot.run_chat()
```
