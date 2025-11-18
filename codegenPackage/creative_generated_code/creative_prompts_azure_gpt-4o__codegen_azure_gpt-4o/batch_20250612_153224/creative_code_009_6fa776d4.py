"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Develop a recommendation system for Emanuelson Reels that suggests leather cases for purchased reels, such as "Salmon Wide," based on user preferences.
Generated: DETERMINISTIC_6fa776d4edf37c83
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Recommendation system for Emanuelson Reels
class RecommendationSystem:
    def __init__(self):
        # Load product data and user preferences (mocked for simplicity)
        self.reels = ["Salmon Wide", "Trout Compact", "Pike Heavy"]
        self.leather_cases = {
            "Salmon Wide": ["Classic Brown Case", "Luxury Black Case"],
            "Trout Compact": ["Compact Tan Case", "Waterproof Green Case"],
            "Pike Heavy": ["Heavy-Duty Case", "Reinforced Leather Case"]
        }
        self.user_preferences = {}  # Will store user preferences

    def load_user_preferences(self, user_preferences_file):
        """
        Load user preferences from a JSON file.
        :param user_preferences_file: Path to the user preferences JSON file.
        """
        try:
            with open(user_preferences_file, 'r') as file:
                self.user_preferences = json.load(file)
        except FileNotFoundError:
            print("User preferences file not found. Starting with empty preferences.")
            self.user_preferences = {}
        except json.JSONDecodeError:
            print("Error decoding JSON file. Please check the file format.")
            self.user_preferences = {}

    def recommend_cases(self, purchased_reel):
        """
        Recommend leather cases based on the purchased reel.
        :param purchased_reel: The name of the purchased reel.
        :return: List of recommended leather cases.
        """
        if purchased_reel not in self.reels:
            print(f"Error: '{purchased_reel}' is not a valid reel.")
            return []
        
        recommendations = self.leather_cases.get(purchased_reel, [])
        return recommendations

    def update_user_preferences(self, user_id, purchased_reel):
        """
        Update user preferences with the purchased reel choice.
        :param user_id: The ID of the user.
        :param purchased_reel: The name of the purchased reel.
        """
        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = []
        
        self.user_preferences[user_id].append(purchased_reel)

    def save_user_preferences(self, user_preferences_file):
        """
        Save user preferences to a JSON file.
        :param user_preferences_file: Path to the user preferences JSON file.
        """
        try:
            with open(user_preferences_file, 'w') as file:
                json.dump(self.user_preferences, file, indent=4)
        except IOError:
            print("Error saving user preferences. Please check file permissions.")

# Main function for demonstration purposes
if __name__ == "__main__":
    recommendation_system = RecommendationSystem()

    # Load user preferences from a file (mocked file path)
    recommendation_system.load_user_preferences("user_preferences.json")

    # Recommend cases for a purchased reel
    purchased_reel = "Salmon Wide"
    suggestions = recommendation_system.recommend_cases(purchased_reel)
    print(f"Recommendations for '{purchased_reel}': {suggestions}")

    # Update user preferences and save them back to a file
    user_id = "user123"
    recommendation_system.update_user_preferences(user_id, purchased_reel)
    recommendation_system.save_user_preferences("user_preferences.json")
```
