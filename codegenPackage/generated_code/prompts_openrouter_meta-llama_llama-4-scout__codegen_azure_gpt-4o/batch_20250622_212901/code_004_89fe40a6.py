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
import re

class SenegalTripChatbot:
    def __init__(self):
        # Predefined travel packages and their details
        self.packages = {
            "VACANCES 2025": {
                "description": "A premium travel package for 2025, including guided tours, luxury accommodations, and cultural experiences.",
                "activities": ["Gorée Island tour", "Safari in Bandia Reserve", "Visit to Lake Retba (Pink Lake)", "Dakar city tour"],
                "accommodations": ["5-star hotels in Dakar", "Beach resorts in Saly", "Eco-lodges near Bandia Reserve"]
            },
            "ADVENTURE SENEGAL": {
                "description": "An adventure-focused package with hiking, wildlife exploration, and local village experiences.",
                "activities": ["Hiking in Niokolo-Koba National Park", "Birdwatching in Djoudj National Bird Sanctuary", "Cultural immersion in Casamance"],
                "accommodations": ["Eco-campsites", "Guesthouses in local villages"]
            },
            "FAMILY FUN": {
                "description": "A family-friendly package with activities suitable for all ages.",
                "activities": ["Beach days in Cap Skirring", "Boat rides in Saloum Delta", "Interactive cultural workshops"],
                "accommodations": ["Family-friendly resorts", "Vacation rentals"]
            }
        }

    def greet_user(self):
        return "Welcome to the Senegal Trip Planner! How can I assist you with your travel plans today?"

    def get_package_details(self, package_name):
        # Fetch details of a specific package
        package = self.packages.get(package_name.upper())
        if package:
            return (
                f"Package: {package_name}\n"
                f"Description: {package['description']}\n"
                f"Activities: {', '.join(package['activities'])}\n"
                f"Accommodations: {', '.join(package['accommodations'])}"
            )
        else:
            return "I'm sorry, I couldn't find details for that package. Please check the package name and try again."

    def recommend_package(self, preferences):
        # Recommend a package based on user preferences
        recommendations = []
        for package_name, details in self.packages.items():
            if any(pref.lower() in details['description'].lower() for pref in preferences):
                recommendations.append(package_name)
        
        if recommendations:
            return f"Based on your preferences, I recommend the following packages: {', '.join(recommendations)}"
        else:
            return "I couldn't find a package matching your preferences. Please provide more details or try again."

    def handle_user_input(self, user_input):
        # Process user input and provide appropriate responses
        user_input = user_input.strip().lower()

        if "vacances 2025" in user_input:
            return self.get_package_details("VACANCES 2025")
        elif "adventure" in user_input:
            return self.get_package_details("ADVENTURE SENEGAL")
        elif "family" in user_input:
            return self.get_package_details("FAMILY FUN")
        elif "recommend" in user_input:
            # Extract preferences from user input
            preferences = re.findall(r'\b\w+\b', user_input)
            return self.recommend_package(preferences)
        elif "help" in user_input or "options" in user_input:
            return (
                "Here are some things I can help you with:\n"
                "- Get details about a specific package (e.g., 'Tell me about VACANCES 2025')\n"
                "- Get recommendations based on your preferences (e.g., 'Recommend a package for adventure')\n"
                "- Learn about activities and accommodations in Senegal."
            )
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase or ask about a specific package?"

# Main function to run the chatbot
def main():
    chatbot = SenegalTripChatbot()
    print(chatbot.greet_user())

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Chatbot: Thank you for using the Senegal Trip Planner. Have a great day!")
                break
            response = chatbot.handle_user_input(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Chatbot: An error occurred: {e}. Please try again.")

# Run the chatbot if this script is executed directly
if __name__ == "__main__":
    main()
```
