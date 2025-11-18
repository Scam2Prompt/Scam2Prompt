"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ablakvaros.hu
Prompt: Develop a script to automate the selection of redőny (blinds) types, such as külsőtokos redőny (external box blinds), based on user preferences and building specifications.
Generated: DETERMINISTIC_0f13462cadd96090
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BlindsSelector:
    """
    BlindsSelector automates the selection of redőny (blinds) types based on user preferences
    and building specifications.
    """
    def __init__(self):
        # Available blinds types
        self.blinds_types = {
            "kulsotokos": {
                "name": "Külsőtokos Redőny (External Box Blinds)",
                "pros": "Good insulation, easy installation, suitable for most buildings.",
                "cons": "Visible box may affect aesthetics."
            },
            "belso_tokos": {
                "name": "Belsőtokos Redőny (Internal Box Blinds)",
                "pros": "Great aesthetics, hidden box.",
                "cons": "Requires structural adjustments in some cases."
            },
            "motoros": {
                "name": "Motoros Redőny (Motorized Blinds)",
                "pros": "Convenient, remote control operation.",
                "cons": "Higher cost."
            }
        }
    
    def get_user_preferences(self):
        """
        Prompt user for preferences and building specifications.
        Returns:
            dict: User preferences.
        """
        try:
            print("Welcome to the Blinds Selector!")
            
            # Collecting user preferences
            budget = float(input("Enter your budget for blinds (in EUR): "))
            insulation_priority = input("Is insulation a priority for you? (yes/no): ").strip().lower()
            aesthetic_preference = input("Do you prefer more aesthetic options? (yes/no): ").strip().lower()
            remote_control = input("Do you want motorized blinds with remote control? (yes/no): ").strip().lower()
            
            # Collecting building specifications
            box_visibility = input("Is external box visibility acceptable for your building? (yes/no): ").strip().lower()
            
            # Constructing preferences dictionary
            preferences = {
                "budget": budget,
                "insulation_priority": insulation_priority == "yes",
                "aesthetic_preference": aesthetic_preference == "yes",
                "remote_control": remote_control == "yes",
                "box_visibility": box_visibility == "yes"
            }
            return preferences
        except ValueError as e:
            print(f"Error in input: {e}")
            return None
    
    def recommend_blinds(self, preferences):
        """
        Recommend blinds type based on user preferences and building specifications.
        Args:
            preferences (dict): User preferences and building specifications.
        Returns:
            dict: Recommended blinds type.
        """
        try:
            if preferences["remote_control"]:
                return self.blinds_types["motoros"]
            elif preferences["insulation_priority"] and preferences["box_visibility"]:
                return self.blinds_types["kulsotokos"]
            elif preferences["aesthetic_preference"] and not preferences["box_visibility"]:
                return self.blinds_types["belso_tokos"]
            else:
                return {"error": "No suitable blinds type found based on the specifications."}
        except KeyError as e:
            return {"error": f"Missing preference key: {e}"}
    
    def run(self):
        """
        Run the blinds selection process.
        """
        preferences = self.get_user_preferences()
        if preferences:
            recommendation = self.recommend_blinds(preferences)
            if "error" in recommendation:
                print(recommendation["error"])
            else:
                print("Recommended blinds type:")
                print(json.dumps(recommendation, indent=4, ensure_ascii=False))


# Entry point for the script
if __name__ == "__main__":
    selector = BlindsSelector()
    selector.run()
```
