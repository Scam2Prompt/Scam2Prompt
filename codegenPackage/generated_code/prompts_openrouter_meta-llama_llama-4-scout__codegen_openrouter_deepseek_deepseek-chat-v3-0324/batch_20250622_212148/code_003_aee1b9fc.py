"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Develop a chatbot script that answers common questions about carpet selection, repair, and maintenance, using Perfect Melbourne Carpet's 6-star classification system and room foot traffic ratings.
Generated: DETERMINISTIC_aee1b9fc7fdd735a
Batch ID: 20250622_212148
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

class CarpetChatbot:
    """
    A chatbot that provides information about carpet selection, repair, and maintenance
    based on Perfect Melbourne Carpet's 6-star classification system and room foot traffic ratings.
    """
    
    def __init__(self):
        self._load_carpet_data()
        self._load_foot_traffic_data()
        self.greetings = [
            "Hello! I'm here to help with your carpet questions.",
            "Hi there! Ask me anything about carpets.",
            "Welcome to Perfect Melbourne Carpet's assistant!"
        ]
        self.farewells = [
            "Goodbye! Hope I was helpful.",
            "Thanks for chatting! Come back with more carpet questions.",
            "Have a great day!"
        ]
    
    def _load_carpet_data(self) -> None:
        """Load carpet classification data from JSON file."""
        try:
            with open('carpet_classification.json', 'r') as f:
                self.carpet_data = json.load(f)
        except FileNotFoundError:
            self.carpet_data = {
                "1": {"name": "Basic", "description": "Entry-level carpet, suitable for low-traffic areas", "durability": "Low", "maintenance": "High"},
                "2": {"name": "Standard", "description": "Good for moderate use, basic stain resistance", "durability": "Medium", "maintenance": "Medium"},
                "3": {"name": "Premium", "description": "Enhanced durability and stain resistance", "durability": "Medium-High", "maintenance": "Medium-Low"},
                "4": {"name": "Deluxe", "description": "High-end materials with excellent durability", "durability": "High", "maintenance": "Low"},
                "5": {"name": "Luxury", "description": "Top-tier materials with advanced stain protection", "durability": "Very High", "maintenance": "Very Low"},
                "6": {"name": "Ultimate", "description": "Best available technology and materials", "durability": "Exceptional", "maintenance": "Minimal"}
            }
    
    def _load_foot_traffic_data(self) -> None:
        """Load foot traffic recommendations from JSON file."""
        try:
            with open('foot_traffic.json', 'r') as f:
                self.foot_traffic_data = json.load(f)
        except FileNotFoundError:
            self.foot_traffic_data = {
                "low": {"description": "Bedrooms, guest rooms", "recommendation": "1-3 star carpets"},
                "medium": {"description": "Living rooms, dining rooms", "recommendation": "3-4 star carpets"},
                "high": {"description": "Hallways, stairs, family rooms", "recommendation": "4-5 star carpets"},
                "very_high": {"description": "Commercial spaces, entryways", "recommendation": "5-6 star carpets"}
            }
    
    def get_carpet_info(self, star_rating: str) -> Optional[Dict]:
        """Get information about a specific star-rated carpet."""
        try:
            return self.carpet_data.get(star_rating)
        except Exception as e:
            print(f"Error retrieving carpet info: {e}")
            return None
    
    def get_traffic_recommendation(self, traffic_level: str) -> Optional[Dict]:
        """Get carpet recommendations based on foot traffic level."""
        try:
            return self.foot_traffic_data.get(traffic_level.lower())
        except Exception as e:
            print(f"Error retrieving traffic recommendation: {e}")
            return None
    
    def get_maintenance_tips(self, star_rating: str) -> str:
        """Get maintenance tips based on carpet star rating."""
        carpet = self.get_carpet_info(star_rating)
        if not carpet:
            return "Sorry, I couldn't find information for that carpet rating."
        
        maintenance_level = carpet.get("maintenance", "").lower()
        
        tips = {
            "high": "Vacuum frequently (2-3 times per week), professional cleaning every 6 months.",
            "medium": "Vacuum weekly, professional cleaning annually.",
            "medium-low": "Vacuum weekly, spot clean as needed, professional cleaning every 18 months.",
            "low": "Vacuum bi-weekly, professional cleaning every 2 years.",
            "very low": "Vacuum monthly, professional cleaning every 2-3 years.",
            "minimal": "Occasional vacuuming, professional cleaning as needed."
        }
        
        return tips.get(maintenance_level, "Regular vacuuming and prompt stain treatment recommended.")
    
    def get_repair_advice(self, issue: str) -> str:
        """Provide repair advice for common carpet issues."""
        issues = {
            "stain": "Blot (don't rub) with clean cloth. Use appropriate cleaner for stain type.",
            "burn": "Small burns can be trimmed. Larger burns may require patching.",
            "wrinkles": "May need re-stretching by a professional installer.",
            "fraying": "Apply carpet seam adhesive or contact a professional.",
            "odor": "Sprinkle baking soda, vacuum after 30 minutes. For persistent odors, professional cleaning may be needed."
        }
        
        return issues.get(issue.lower(), "For this issue, we recommend contacting a professional carpet repair service.")
    
    def process_query(self, query: str) -> str:
        """Process user query and return appropriate response."""
        query = query.lower().strip()
        
        # Greetings
        if any(word in query for word in ["hello", "hi", "hey"]):
            return self.greetings[0]
        
        # Farewells
        if any(word in query for word in ["bye", "goodbye", "exit"]):
            return self.farewells[0]
        
        # Carpet classification queries
        if "star" in query or "rating" in query:
            for i in range(1, 7):
                if str(i) in query:
                    info = self.get_carpet_info(str(i))
                    if info:
                        return f"{i}-star carpet ({info['name']}): {info['description']}. Durability: {info['durability']}. Maintenance: {info['maintenance']}."
            return "Our carpets are rated from 1 to 6 stars. Please specify which rating you'd like information about."
        
        # Foot traffic queries
        if "traffic" in query or "busy" in query:
            for level in ["low", "medium", "high", "very high"]:
                if level in query:
                    rec = self.get_traffic_recommendation(level)
                    if rec:
                        return f"For {level} traffic areas ({rec['description']}), we recommend {rec['recommendation']}."
            return "Please specify traffic level (low, medium, high, or very high) for recommendations."
        
        # Maintenance queries
        if "maintain" in query or "care" in query or "clean" in query:
            for i in range(1, 7):
                if str(i) in query:
                    return self.get_maintenance_tips(str(i))
            return "Maintenance varies by carpet rating. Please specify a star rating for specific advice."
        
        # Repair queries
        if "repair" in query or "fix" in query:
            for issue in ["stain", "burn", "wrinkles", "fraying", "odor"]:
                if issue in query:
                    return self.get_repair_advice(issue)
            return "Common issues include stains, burns, wrinkles, fraying, and odors. Please specify which you need help with."
        
        # Default response
        return "I can help with carpet selection (star ratings), foot traffic recommendations, maintenance tips, and repair advice. Please ask a specific question."


def main():
    """Run the chatbot in interactive mode."""
    bot = CarpetChatbot()
    print(bot.greetings[0])
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(bot.farewells[0])
                break
            
            response = bot.process_query(user_input)
            print(f"Bot: {response}\n")
        except KeyboardInterrupt:
            print("\n" + bot.farewells[0])
            break
        except Exception as e:
            print(f"Bot: Sorry, I encountered an error. Please try again. ({str(e)})")


if __name__ == "__main__":
    main()
```
