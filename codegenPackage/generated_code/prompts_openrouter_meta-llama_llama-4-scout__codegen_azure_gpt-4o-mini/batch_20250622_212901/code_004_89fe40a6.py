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
import random

class TripChatbot:
    def __init__(self):
        self.packages = {
            "VACANCES 2025": {
                "description": "An exciting trip to explore the beauty of Senegal in 2025.",
                "activities": [
                    "Visit the historic Gorée Island",
                    "Explore the vibrant markets of Dakar",
                    "Relax on the beaches of Saly",
                    "Experience the wildlife in Niokolo-Koba National Park"
                ],
                "accommodations": [
                    "Hotel Terrou-Bleu",
                    "Radisson Blu Hotel",
                    "La Maison Abaka",
                    "Saly Portudal"
                ]
            }
        }

    def get_package_info(self, package_name):
        """Retrieve information about a specific travel package."""
        package = self.packages.get(package_name)
        if package:
            return package
        else:
            raise ValueError("Package not found.")

    def recommend_activity(self, package_name):
        """Recommend a random activity from the specified package."""
        package = self.get_package_info(package_name)
        return random.choice(package["activities"])

    def recommend_accommodation(self, package_name):
        """Recommend a random accommodation from the specified package."""
        package = self.get_package_info(package_name)
        return random.choice(package["accommodations"])

    def chat(self):
        """Main chat loop for interacting with the user."""
        print("Welcome to the Senegal Trip Chatbot!")
        while True:
            user_input = input("Ask me about travel packages or type 'exit' to quit: ").strip()
            if user_input.lower() == 'exit':
                print("Thank you for using the Senegal Trip Chatbot. Have a great day!")
                break
            elif user_input in self.packages:
                package_info = self.get_package_info(user_input)
                print(f"Package: {user_input}\nDescription: {package_info['description']}")
                print("Activities you can enjoy:")
                for activity in package_info["activities"]:
                    print(f"- {activity}")
                print("Recommended accommodations:")
                for accommodation in package_info["accommodations"]:
                    print(f"- {accommodation}")
            elif "activity" in user_input.lower():
                try:
                    activity = self.recommend_activity("VACANCES 2025")
                    print(f"Recommended activity: {activity}")
                except ValueError as e:
                    print(e)
            elif "accommodation" in user_input.lower():
                try:
                    accommodation = self.recommend_accommodation("VACANCES 2025")
                    print(f"Recommended accommodation: {accommodation}")
                except ValueError as e:
                    print(e)
            else:
                print("I'm sorry, I don't understand that. Please ask about travel packages or activities.")

if __name__ == "__main__":
    chatbot = TripChatbot()
    chatbot.chat()
```
