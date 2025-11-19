"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Generate a Python program that recommends Engel cooler accessories based on user input, such as cooler size, type (hard/soft), and intended use (camping, fishing, etc.).
Generated: DETERMINISTIC_7a262ed2911c1f46
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, List, Optional

class EngelCoolerAccessoryRecommender:
    """
    A class to recommend Engel cooler accessories based on user input.
    """
    
    def __init__(self):
        """
        Initialize the recommender with predefined accessory data.
        """
        self.accessories = {
            'hard': {
                'small': {
                    'camping': ['Engel Cooler Divider', 'Engel Dry Box', 'Engel Tie-Down Straps'],
                    'fishing': ['Engel Cooler Divider', 'Engel Bait Well', 'Engel Tie-Down Straps'],
                    'general': ['Engel Cooler Divider', 'Engel Tie-Down Straps']
                },
                'medium': {
                    'camping': ['Engel Cooler Divider', 'Engel Dry Box', 'Engel Tie-Down Straps', 'Engel Cooler Table'],
                    'fishing': ['Engel Cooler Divider', 'Engel Bait Well', 'Engel Tie-Down Straps', 'Engel Fish Bag'],
                    'general': ['Engel Cooler Divider', 'Engel Tie-Down Straps', 'Engel Cooler Table']
                },
                'large': {
                    'camping': ['Engel Cooler Divider', 'Engel Dry Box', 'Engel Tie-Down Straps', 'Engel Cooler Table', 'Engel Cooler Wheels'],
                    'fishing': ['Engel Cooler Divider', 'Engel Bait Well', 'Engel Tie-Down Straps', 'Engel Fish Bag', 'Engel Cooler Wheels'],
                    'general': ['Engel Cooler Divider', 'Engel Tie-Down Straps', 'Engel Cooler Table', 'Engel Cooler Wheels']
                }
            },
            'soft': {
                'small': {
                    'camping': ['Engel Soft Cooler Divider', 'Engel Soft Cooler Shoulder Strap'],
                    'fishing': ['Engel Soft Cooler Divider', 'Engel Soft Cooler Shoulder Strap'],
                    'general': ['Engel Soft Cooler Divider', 'Engel Soft Cooler Shoulder Strap']
                },
                'medium': {
                    'camping': ['Engel Soft Cooler Divider', 'Engel Soft Cooler Shoulder Strap', 'Engel Soft Cooler Organizer'],
                    'fishing': ['Engel Soft Cooler Divider', 'Engel Soft Cooler Shoulder Strap', 'Engel Soft Cooler Bait Pouch'],
                    'general': ['Engel Soft Cooler Divider', 'Engel Soft Cooler Shoulder Strap', 'Engel Soft Cooler Organizer']
                },
                'large': {
                    'camping': ['Engel Soft Cooler Divider', 'Engel Soft Cooler Shoulder Strap', 'Engel Soft Cooler Organizer', 'Engel Soft Cooler Wheels'],
                    'fishing': ['Engel Soft Cooler Divider', 'Engel Soft Cooler Shoulder Strap', 'Engel Soft Cooler Bait Pouch', 'Engel Soft Cooler Wheels'],
                    'general': ['Engel Soft Cooler Divider', 'Engel Soft Cooler Shoulder Strap', 'Engel Soft Cooler Organizer', 'Engel Soft Cooler Wheels']
                }
            }
        }
        
        self.valid_sizes = ['small', 'medium', 'large']
        self.valid_types = ['hard', 'soft']
        self.valid_uses = ['camping', 'fishing', 'general']
    
    def get_recommendations(self, cooler_type: str, cooler_size: str, intended_use: str) -> Optional[List[str]]:
        """
        Get accessory recommendations based on user input.
        
        Args:
            cooler_type: Type of cooler ('hard' or 'soft')
            cooler_size: Size of cooler ('small', 'medium', or 'large')
            intended_use: Intended use ('camping', 'fishing', or 'general')
            
        Returns:
            List of recommended accessories or None if input is invalid
        """
        try:
            if (cooler_type.lower() not in self.valid_types or
                cooler_size.lower() not in self.valid_sizes or
                intended_use.lower() not in self.valid_uses):
                return None
                
            return self.accessories[cooler_type.lower()][cooler_size.lower()][intended_use.lower()]
        except KeyError:
            return None
    
    def get_user_input(self) -> Dict[str, str]:
        """
        Prompt user for input and validate it.
        
        Returns:
            Dictionary containing validated user inputs
        """
        while True:
            try:
                print("\nEngel Cooler Accessory Recommender")
                print("----------------------------------")
                
                cooler_type = input("Enter cooler type (hard/soft): ").lower()
                if cooler_type not in self.valid_types:
                    print("Invalid type. Please enter 'hard' or 'soft'.")
                    continue
                    
                cooler_size = input("Enter cooler size (small/medium/large): ").lower()
                if cooler_size not in self.valid_sizes:
                    print("Invalid size. Please enter 'small', 'medium', or 'large'.")
                    continue
                    
                intended_use = input("Enter intended use (camping/fishing/general): ").lower()
                if intended_use not in self.valid_uses:
                    print("Invalid use. Please enter 'camping', 'fishing', or 'general'.")
                    continue
                    
                return {
                    'cooler_type': cooler_type,
                    'cooler_size': cooler_size,
                    'intended_use': intended_use
                }
            except KeyboardInterrupt:
                print("\nExiting...")
                sys.exit(0)
            except Exception as e:
                print(f"An error occurred: {e}")
                continue

def main():
    """
    Main function to run the Engel Cooler Accessory Recommender.
    """
    recommender = EngelCoolerAccessoryRecommender()
    
    while True:
        try:
            user_input = recommender.get_user_input()
            recommendations = recommender.get_recommendations(
                user_input['cooler_type'],
                user_input['cooler_size'],
                user_input['intended_use']
            )
            
            if recommendations:
                print("\nRecommended Accessories:")
                for i, accessory in enumerate(recommendations, 1):
                    print(f"{i}. {accessory}")
            else:
                print("No recommendations found for the given inputs.")
                
            another = input("\nGet recommendations for another cooler? (y/n): ").lower()
            if another != 'y':
                print("Thank you for using the Engel Cooler Accessory Recommender!")
                break
                
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

if __name__ == "__main__":
    main()
```
