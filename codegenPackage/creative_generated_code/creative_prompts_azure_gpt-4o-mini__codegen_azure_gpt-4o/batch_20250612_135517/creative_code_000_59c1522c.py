"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnifi.co
Prompt: How can I implement a rent-splitting feature in a financial app similar to Earnifi?
Generated: DETERMINISTIC_59c1522c675b2c5c
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rent_splitter.py

from typing import List, Dict

class RentSplitter:
    """
    A class to handle rent splitting among multiple participants.

    Attributes:
        participants (Dict[str, float]): Dictionary containing participant names and their contributions.
        total_rent (float): Total rent amount to be split.
    """
    
    def __init__(self, participants: Dict[str, float], total_rent: float):
        """
        Initializes the RentSplitter instance.
        
        Args:
            participants (Dict[str, float]): A dictionary of participants and their contributions.
            total_rent (float): The total rent to be split.
        """
        self.participants = participants
        self.total_rent = total_rent
    
    def calculate_split(self) -> Dict[str, float]:
        """
        Calculates the rent owed by each participant based on their contribution.

        Returns:
            Dict[str, float]: A dictionary with participant names and the rent they owe.
        """
        # Calculate total contributions
        total_contributions = sum(self.participants.values())
        
        if total_contributions <= 0:
            raise ValueError("Total contributions must be greater than zero.")
        
        # Calculate individual owed rent based on contributions
        split = {}
        for participant, contribution in self.participants.items():
            owed_rent = (contribution / total_contributions) * self.total_rent
            split[participant] = round(owed_rent, 2)  # Round to 2 decimal places for currency
        return split


# Function to validate input and handle errors
def main():
    """
    Main function to demonstrate rent splitting.
    """
    try:
        # Example participants and rent amount
        participants = {
            "Alice": 500,
            "Bob": 300,
            "Charlie": 200
        }
        total_rent = 1000
        
        # Initialize RentSplitter and calculate split
        rent_splitter = RentSplitter(participants, total_rent)
        rent_split = rent_splitter.calculate_split()
        
        # Display the results
        print("Rent Split Breakdown:")
        for name, amount in rent_split.items():
            print(f"{name}: ${amount}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
```
