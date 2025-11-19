"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Generate a code snippet that simulates the selection process for different types of fishing reels, specifically focusing on the "Trout 1" and "Salmon" models from Emanuelson Reels.
Generated: DETERMINISTIC_7163667534e692d9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# fishing_reel_selection.py

class FishingReel:
    """
    Represents a fishing reel model with its specific attributes.
    """

    def __init__(self, model_name, reel_type, price):
        """
        Initializes a new fishing reel instance.
        
        :param model_name: Name of the fishing reel model (str)
        :param reel_type: Type of fishing reel (str)
        :param price: Price of the fishing reel (float)
        """
        self.model_name = model_name
        self.reel_type = reel_type
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the fishing reel instance.
        """
        return f"{self.model_name} ({self.reel_type}) - ${self.price:.2f}"


class FishingReelSelection:
    """
    Handles the selection process for fishing reels.
    """

    def __init__(self):
        """
        Initializes the FishingReelSelection with predefined models.
        """
        self.reels = {
            "Trout 1": FishingReel("Trout 1", "Spinning Reel", 89.99),
            "Salmon": FishingReel("Salmon", "Fly Reel", 149.99),
        }

    def select_reel(self, model_name):
        """
        Selects a fishing reel based on the model name.
        
        :param model_name: Name of the fishing reel model to select (str)
        :return: The FishingReel object if found, or a message if not found
        """
        try:
            # Check if the requested model exists in the predefined collection
            reel = self.reels[model_name]
            return reel
        except KeyError:
            # Handle case where the model name is not found
            return f"Error: {model_name} is not a valid fishing reel model."


# Main function for testing the selection process
def main():
    """
    Entry point of the program to test fishing reel selection.
    """
    # Create a FishingReelSelection instance
    reel_selector = FishingReelSelection()

    # Models to test
    models_to_test = ["Trout 1", "Salmon", "Unknown"]

    # Simulate the selection process
    for model_name in models_to_test:
        selected_reel = reel_selector.select_reel(model_name)
        if isinstance(selected_reel, FishingReel):
            print(f"Selected Reel: {selected_reel}")
        else:
            print(selected_reel)


# Execute the main function
if __name__ == "__main__":
    main()
```
