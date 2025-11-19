"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Develop a simple chatbot script that provides information about museum activities for visitors and families, inspired by the content on the Museo Vasca Votiva di Noceto site.
Generated: DETERMINISTIC_0b1c131b140bca2b
Batch ID: 20250622_212109
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

# Sample data structure for museum activities
MUSEUM_ACTIVITIES = {
    "exhibitions": {
        "current": [
            {
                "title": "Ancient Basque Artifacts",
                "description": "Explore a collection of ancient Basque artifacts dating back to 2000 BC.",
                "location": "Main Hall",
                "date": "Ongoing"
            },
            {
                "title": "Sacred Votive Offerings",
                "description": "A special exhibit showcasing votive offerings from the Bronze Age.",
                "location": "East Wing",
                "date": "Until December 2023"
            }
        ],
        "upcoming": [
            {
                "title": "Basque Mythology",
                "description": "An immersive experience into Basque mythology and folklore.",
                "location": "Main Hall",
                "date": "January 2024"
            }
        ]
    },
    "workshops": [
        {
            "title": "Pottery Making",
            "description": "Learn ancient pottery techniques with our expert artisans.",
            "age_group": "8+",
            "schedule": "Every Saturday, 10:00-12:00"
        },
        {
            "title": "Storytelling for Kids",
            "description": "Interactive storytelling sessions featuring Basque legends.",
            "age_group": "5-10",
            "schedule": "Every Sunday, 15:00-16:00"
        }
    ],
    "tours": [
        {
            "title": "Guided Historical Tour",
            "description": "A comprehensive tour of the museum's collections with our expert guides.",
            "duration": "1.5 hours",
            "languages": ["Italian", "English", "Spanish"]
        },
        {
            "title": "Family Discovery Tour",
            "description": "Interactive tour designed for families with children.",
            "duration": "1 hour",
            "languages": ["Italian", "English"]
        }
    ]
}

class MuseumChatbot:
    """A simple chatbot that provides information about museum activities."""
    
    def __init__(self):
        """Initialize the chatbot with museum activity data."""
        self.activities = MUSEUM_ACTIVITIES
        self.greetings = [
            "hello", "hi", "hey", "greetings", "good morning", "good afternoon"
        ]
        self.farewells = [
            "bye", "goodbye", "see you", "farewell", "quit", "exit"
        ]
    
    def get_response(self, user_input: str) -> str:
        """Generate a response based on user input.
        
        Args:
            user_input: The user's message/query
            
        Returns:
            str: The chatbot's response
        """
        user_input = user_input.lower().strip()
        
        # Check for greetings
        if any(greeting in user_input for greeting in self.greetings):
            return self._generate_greeting()
        
        # Check for farewells
        if any(farewell in user_input for farewell in self.farewells):
            return "Thank you for visiting Museo Vasca Votiva di Noceto! Have a wonderful day."
        
        # Handle specific queries
        if "exhibition" in user_input or "exhibit" in user_input:
            return self._get_exhibitions_info()
        elif "workshop" in user_input:
            return self._get_workshops_info()
        elif "tour" in user_input:
            return self._get_tours_info()
        elif "family" in user_input or "children" in user_input or "kids" in user_input:
            return self._get_family_activities()
        elif "help" in user_input:
            return self._get_help_message()
        else:
            return "I'm sorry, I didn't understand your query. You can ask about exhibitions, workshops, tours, or family activities. Type 'help' for more options."
    
    def _generate_greeting(self) -> str:
        """Generate a greeting message."""
        return (
            "Welcome to Museo Vasca Votiva di Noceto information chatbot!\n"
            "I can provide information about:\n"
            "- Current and upcoming exhibitions\n"
            "- Workshops and activities\n"
            "- Guided tours\n"
            "- Family-friendly programs\n\n"
            "How can I help you today?"
        )
    
    def _get_exhibitions_info(self) -> str:
        """Generate information about current and upcoming exhibitions."""
        current_exhibitions = "\n".join(
            f"- {exh['title']} ({exh['date']}): {exh['description']} Location: {exh['location']}"
            for exh in self.activities["exhibitions"]["current"]
        )
        
        upcoming_exhibitions = "\n".join(
            f"- {exh['title']} ({exh['date']}): {exh['description']} Location: {exh['location']}"
            for exh in self.activities["exhibitions"]["upcoming"]
        )
        
        return (
            "Current Exhibitions:\n"
            f"{current_exhibitions}\n\n"
            "Upcoming Exhibitions:\n"
            f"{upcoming_exhibitions}"
        )
    
    def _get_workshops_info(self) -> str:
        """Generate information about workshops."""
        workshops = "\n".join(
            f"- {ws['title']} (Age {ws['age_group']}): {ws['description']} Schedule: {ws['schedule']}"
            for ws in self.activities["workshops"]
        )
        
        return (
            "Workshops and Activities:\n"
            f"{workshops}"
        )
    
    def _get_tours_info(self) -> str:
        """Generate information about guided tours."""
        tours = "\n".join(
            f"- {tour['title']} ({tour['duration']}): {tour['description']} Languages: {', '.join(tour['languages'])}"
            for tour in self.activities["tours"]
        )
        
        return (
            "Guided Tours:\n"
            f"{tours}"
        )
    
    def _get_family_activities(self) -> str:
        """Generate information about family-friendly activities."""
        family_workshops = [
            ws for ws in self.activities["workshops"] 
            if "5" in ws["age_group"] or "8" in ws["age_group"] or "10" in ws["age_group"]
        ]
        family_tours = [
            tour for tour in self.activities["tours"] 
            if "Family" in tour["title"]
        ]
        
        workshop_info = "\n".join(
            f"- {ws['title']} (Age {ws['age_group']}): {ws['description']} Schedule: {ws['schedule']}"
            for ws in family_workshops
        )
        
        tour_info = "\n".join(
            f"- {tour['title']} ({tour['duration']}): {tour['description']}"
            for tour in family_tours
        )
        
        return (
            "Family-Friendly Activities:\n\n"
            "Workshops:\n"
            f"{workshop_info}\n\n"
            "Tours:\n"
            f"{tour_info}"
        )
    
    def _get_help_message(self) -> str:
        """Generate help message with available commands."""
        return (
            "You can ask me about:\n"
            "- 'Exhibitions' (current and upcoming)\n"
            "- 'Workshops' (activities and classes)\n"
            "- 'Tours' (guided visits)\n"
            "- 'Family activities' (programs for children)\n\n"
            "Or simply say 'hello' or 'goodbye'."
        )

def main():
    """Run the chatbot in interactive mode."""
    chatbot = MuseumChatbot()
    print(chatbot._generate_greeting())
    
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(chatbot.get_response(user_input))
                break
            response = chatbot.get_response(user_input)
            print(f"\nBot: {response}")
        except KeyboardInterrupt:
            print("\nBot: Thank you for visiting! Goodbye.")
            break
        except Exception as e:
            print(f"\nBot: Sorry, I encountered an error. Please try again. ({str(e)})")

if __name__ == "__main__":
    main()
```
