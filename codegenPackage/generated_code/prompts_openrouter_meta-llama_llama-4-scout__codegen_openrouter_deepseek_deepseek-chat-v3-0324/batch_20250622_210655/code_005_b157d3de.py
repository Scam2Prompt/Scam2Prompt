"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: "What are the guidelines for loading a dumpster rental from Purple Dumpster, and what items are prohibited from being disposed of?"
Generated: DETERMINISTIC_b157d3deeaa6870a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dumpster_rental_guidelines.py

class DumpsterRentalGuidelines:
    """
    A class to represent the guidelines for loading a dumpster rental from Purple Dumpster.
    Includes loading procedures and prohibited items list.
    """
    
    def __init__(self):
        self.loading_guidelines = [
            "Distribute weight evenly throughout the dumpster",
            "Do not overload - keep debris level with the top of the container",
            "Break down large items to maximize space",
            "Place heavier items at the bottom",
            "Do not place items outside the dumpster",
            "Ensure all debris is properly secured to prevent spills during transport"
        ]
        
        self.prohibited_items = [
            "Hazardous waste (chemicals, asbestos, etc.)",
            "Batteries",
            "Tires",
            "Medical waste",
            "Flammable materials",
            "Compressed gas cylinders",
            "Liquids (paint, oil, etc.)",
            "Electronics (e-waste)",
            "Food waste (in most cases)",
            "Radioactive materials",
            "Any items classified as hazardous by local regulations"
        ]
    
    def get_loading_guidelines(self) -> list:
        """
        Returns the list of loading guidelines for the dumpster rental.
        
        Returns:
            list: Loading guidelines
        """
        return self.loading_guidelines
    
    def get_prohibited_items(self) -> list:
        """
        Returns the list of prohibited items for the dumpster rental.
        
        Returns:
            list: Prohibited items
        """
        return self.prohibited_items
    
    def is_item_prohibited(self, item: str) -> bool:
        """
        Checks if an item is prohibited from being disposed of in the dumpster.
        
        Args:
            item (str): The item to check
            
        Returns:
            bool: True if prohibited, False otherwise
        """
        return item.lower() in [i.lower() for i in self.prohibited_items]


def main():
    """Main function to demonstrate the DumpsterRentalGuidelines class."""
    try:
        guidelines = DumpsterRentalGuidelines()
        
        print("Purple Dumpster Loading Guidelines:")
        for i, guideline in enumerate(guidelines.get_loading_guidelines(), 1):
            print(f"{i}. {guideline}")
            
        print("\nProhibited Items:")
        for i, item in enumerate(guidelines.get_prohibited_items(), 1):
            print(f"{i}. {item}")
            
        # Example check
        test_item = "Paint"
        print(f"\nIs '{test_item}' prohibited? {guidelines.is_item_prohibited(test_item)}")
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
