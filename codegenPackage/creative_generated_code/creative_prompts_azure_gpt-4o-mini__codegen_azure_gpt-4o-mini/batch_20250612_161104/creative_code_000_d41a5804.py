"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krajkovac.rs
Prompt: Generate a code snippet for a travel app that highlights Krajkovac's unique features, including Krajkovačko Lake and its historical significance.
Generated: DETERMINISTIC_d41a5804552b20a8
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TravelApp:
    """
    A simple travel app to highlight unique features of Krajkovac, including Krajkovačko Lake.
    """

    def __init__(self):
        self.features = []

    def add_feature(self, name: str, description: str, historical_significance: str):
        """
        Adds a feature to the travel app.

        :param name: Name of the feature.
        :param description: Description of the feature.
        :param historical_significance: Historical significance of the feature.
        """
        self.features.append({
            "name": name,
            "description": description,
            "historical_significance": historical_significance
        })

    def display_features(self):
        """
        Displays the features of Krajkovac.
        """
        if not self.features:
            print("No features available.")
            return

        for feature in self.features:
            print(f"Feature: {feature['name']}")
            print(f"Description: {feature['description']}")
            print(f"Historical Significance: {feature['historical_significance']}")
            print("-" * 40)

    def run(self):
        """
        Main method to run the travel app.
        """
        try:
            # Adding unique features of Krajkovac
            self.add_feature(
                name="Krajkovačko Lake",
                description="A beautiful lake known for its serene environment and natural beauty.",
                historical_significance="The lake has been a vital source of water and recreation for centuries."
            )

            # Display the features
            self.display_features()
        
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = TravelApp()
    app.run()
```
