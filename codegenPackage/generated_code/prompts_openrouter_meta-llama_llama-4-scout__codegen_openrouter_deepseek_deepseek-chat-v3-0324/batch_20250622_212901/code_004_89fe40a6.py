"""
Generated Code Metadata:
========================
Original URL: https://fodyem.com
Prompt: Develop a chatbot script that can help users plan their trip to Senegal, answering questions about different travel packages, such as "VACANCES 2025", and providing recommendations for activities and accommodations.
Generated: DETERMINISTIC_89fe40a6e606f343
Batch ID: 20250622_212901
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

class SenegalTravelChatbot:
    """
    A chatbot to assist users in planning their trip to Senegal.
    Provides information about travel packages, activities, and accommodations.
    """

    def __init__(self):
        """
        Initialize the chatbot with travel package data.
        """
        self.packages = self._load_packages()
        self.greetings = [
            "Hello! How can I help you plan your trip to Senegal?",
            "Welcome to Senegal Travel Assistant! What would you like to know?",
            "Hi there! Ready to plan your Senegalese adventure?"
        ]
        self.farewells = [
            "Have a wonderful trip to Senegal!",
            "Bon voyage! Enjoy your time in Senegal!",
            "Safe travels! Hope you have an amazing time in Senegal!"
        ]

    def _load_packages(self) -> Dict[str, Dict]:
        """
        Load travel packages from a JSON file.
        
        Returns:
            Dict: Dictionary of travel packages
        """
        try:
            with open('packages.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Warning: packages.json not found. Using default packages.")
            return {
                "VACANCES 2025": {
                    "description": "Premium all-inclusive package for 2025",
                    "duration": "10 days",
                    "price": "$2500",
                    "activities": ["Gorée Island tour", "Pink Lake visit", "Safari in Niokolo-Koba"],
                    "accommodations": ["5-star hotel in Dakar", "Beach resort in Saly"]
                },
                "SENEGAL ADVENTURE": {
                    "description": "Adventure package for thrill-seekers",
                    "duration": "7 days",
                    "price": "$1800",
                    "activities": ["Surfing in Ngor", "Hiking in Fathala Forest", "Quad biking in Lompoul desert"],
                    "accommodations": ["Eco-lodge", "Desert camp"]
                }
            }
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in packages.json")
            return {}

    def get_package_info(self, package_name: str) -> Optional[str]:
        """
        Get information about a specific travel package.
        
        Args:
            package_name: Name of the travel package
            
        Returns:
            str: Formatted information about the package or None if not found
        """
        package = self.packages.get(package_name.upper())
        if not package:
            return None
            
        info = [
            f"Package: {package_name.upper()}",
            f"Description: {package['description']}",
            f"Duration: {package['duration']}",
            f"Price: {package['price']}",
            "Activities: " + ", ".join(package['activities']),
            "Accommodations: " + ", ".join(package['accommodations'])
        ]
        return "\n".join(info)

    def recommend_activities(self, interest: str) -> str:
        """
        Recommend activities based on user interest.
        
        Args:
            interest: User's interest (beach, culture, adventure, etc.)
            
        Returns:
            str: Recommended activities
        """
        interest = interest.lower()
        recommendations = {
            "beach": ["Saly Beach relaxation", "Cap Skirring surfing", "Ile de Madeleine snorkeling"],
            "culture": ["Gorée Island history tour", "Saint-Louis jazz festival", "Touba religious sites"],
            "adventure": ["Lompoul desert safari", "Niokolo-Koba wildlife spotting", "Sine-Saloum kayaking"],
            "food": ["Thieboudienne cooking class", "Local market food tour", "Traditional Senegalese dinner"]
        }
        return recommendations.get(interest, ["Gorée Island tour", "Pink Lake visit", "Dakar city tour"])

    def recommend_accommodations(self, budget: str) -> str:
        """
        Recommend accommodations based on budget.
        
        Args:
            budget: User's budget (low, medium, high)
            
        Returns:
            str: Recommended accommodations
        """
        budget = budget.lower()
        recommendations = {
            "low": ["Hostels in Dakar", "Guesthouses in Saint-Louis", "Budget hotels in Saly"],
            "medium": ["3-star hotels", "Beach resorts", "Eco-lodges"],
            "high": ["5-star hotels in Dakar", "Luxury beach villas", "Premium safari camps"]
        }
        return recommendations.get(budget, ["3-star hotels", "Beach resorts"])

    def process_query(self, query: str) -> str:
        """
        Process user query and generate appropriate response.
        
        Args:
            query: User's input question/request
            
        Returns:
            str: Bot's response
        """
        query = query.lower().strip()
        
        if any(word in query for word in ["hi", "hello", "hey", "greetings"]):
            return self.greetings[0]
            
        if any(word in query for word in ["bye", "goodbye", "exit", "quit"]):
            return self.farewells[0]
            
        if "package" in query or "vacances" in query:
            for package_name in self.packages:
                if package_name.lower() in query:
                    info = self.get_package_info(package_name)
                    return info if info else f"Sorry, I couldn't find information about {package_name}."
            return "We offer these travel packages: " + ", ".join(self.packages.keys())
            
        if "activity" in query or "activities" in query or "do" in query:
            interest = next((word for word in ["beach", "culture", "adventure", "food"] if word in query), "general")
            return "Recommended activities: " + ", ".join(self.recommend_activities(interest))
            
        if "hotel" in query or "stay" in query or "accommodation" in query:
            budget = next((word for word in ["low", "medium", "high"] if word in query), "medium")
            return "Recommended accommodations: " + ", ".join(self.recommend_accommodations(budget))
            
        return "I can help with travel packages, activities, and accommodations. Could you be more specific?"

def main():
    """
    Main function to run the chatbot interactively.
    """
    bot = SenegalTravelChatbot()
    print(bot.greetings[0])
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit", "bye"]:
                print(f"\nBot: {bot.farewells[0]}")
                break
                
            response = bot.process_query(user_input)
            print(f"\nBot: {response}")
            
        except KeyboardInterrupt:
            print(f"\nBot: {bot.farewells[0]}")
            break
        except Exception as e:
            print(f"\nBot: Sorry, I encountered an error. Please try again.")
            print(f"[Error: {str(e)}]")

if __name__ == "__main__":
    main()
```
