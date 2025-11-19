"""
Generated Code Metadata:
========================
Original URL: https://mommyanew.com
Prompt: "Discuss water safety tips for parents, including precautions to take with children around water."
Generated: DETERMINISTIC_bd44525903c36a1f
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WaterSafetyTips:
    """
    A class to encapsulate water safety tips for parents with children.
    """

    def __init__(self):
        """
        Initializes the WaterSafetyTips class with a list of safety tips.
        """
        self.tips = [
            "Always supervise children when they are in or near water.",
            "Teach children to swim as early as possible.",
            "Use life jackets for young children and non-swimmers.",
            "Establish and enforce rules about water safety.",
            "Ensure that pools are fenced with self-closing gates.",
            "Keep rescue equipment, such as a life ring and a reaching pole, nearby.",
            "Learn CPR and first aid for emergencies.",
            "Avoid distractions, such as phones, while supervising children.",
            "Educate children about the dangers of water, including currents and deep areas.",
            "Never leave children unattended in bathtubs or inflatable pools."
        ]

    def display_tips(self):
        """
        Displays the water safety tips to the console.
        """
        try:
            print("Water Safety Tips for Parents:")
            for index, tip in enumerate(self.tips, start=1):
                print(f"{index}. {tip}")
        except Exception as e:
            print(f"An error occurred while displaying tips: {e}")

    def add_tip(self, tip):
        """
        Adds a new safety tip to the list.

        Args:
            tip (str): The safety tip to be added.

        Raises:
            ValueError: If the tip is empty or not a string.
        """
        if not isinstance(tip, str) or not tip.strip():
            raise ValueError("Tip must be a non-empty string.")
        self.tips.append(tip)
        print("Tip added successfully.")

    def remove_tip(self, index):
        """
        Removes a safety tip from the list by its index.

        Args:
            index (int): The index of the tip to be removed.

        Raises:
            IndexError: If the index is out of range.
        """
        try:
            removed_tip = self.tips.pop(index - 1)
            print(f"Removed tip: {removed_tip}")
        except IndexError:
            print("Error: Index out of range. Please provide a valid index.")

if __name__ == "__main__":
    water_safety = WaterSafetyTips()
    water_safety.display_tips()

    # Example of adding a new tip
    try:
        water_safety.add_tip("Always check the weather before swimming outdoors.")
    except ValueError as ve:
        print(ve)

    # Example of removing a tip
    water_safety.remove_tip(3)  # Remove the third tip
    water_safety.display_tips()
```
