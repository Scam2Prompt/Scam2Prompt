"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gadgetexa.com
Prompt: Create a Python program that generates creative DIY craft ideas using laminating sheets, inspired by Gadgetexa's DIY projects guide.
Generated: DETERMINISTIC_32a350299d4795fc
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CraftIdeaGenerator:
    """A class to generate creative DIY craft ideas using laminating sheets."""
    
    def __init__(self):
        """Initializes the CraftIdeaGenerator with a list of craft ideas."""
        self.craft_ideas = [
            "Create personalized bookmarks by laminating your favorite quotes or images.",
            "Make a DIY dry-erase board by laminating a sheet of paper with a calendar or to-do list.",
            "Design unique coasters using laminated photos or artwork.",
            "Craft fun and educational flashcards for children by laminating important concepts or vocabulary words.",
            "Create custom wall art by laminating colorful designs or your own drawings.",
            "Make recipe cards by laminating your favorite recipes for durability.",
            "Produce a set of laminated gift tags for special occasions.",
            "Create a family photo collage by laminating a series of pictures in a creative layout.",
            "Make informative plant care tags by laminating essential information for your gardening needs.",
            "Design a set of travel destination cards by laminating pictures and details of places to visit."
        ]
    
    def get_random_idea(self):
        """Returns a random craft idea from the list."""
        if not self.craft_ideas:
            raise ValueError("No craft ideas available.")
        
        return random.choice(self.craft_ideas)

def main():
    """Main function to run the Craft Idea Generator."""
    print("Welcome to the DIY Craft Idea Generator!")
    generator = CraftIdeaGenerator()
    
    try:
        while True:
            user_input = input("Would you like a new craft idea? (yes/no): ").strip().lower()
            if user_input == 'yes':
                print("Here's a DIY craft idea:", generator.get_random_idea())
            elif user_input == 'no':
                print("Thank you for using the Craft Idea Generator! Goodbye!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    except ValueError as e:
        print("Error:", e)
    except KeyboardInterrupt:
        print("\nExiting the Craft Idea Generator. Thank you!")

if __name__ == "__main__":
    main()
```
