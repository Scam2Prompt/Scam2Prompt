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

class RentSplitter:
    """
    A class to manage and calculate rent splitting among housemates.

    Attributes:
        total_rent (float): The total amount of rent to be split.
        housemates (dict): A dictionary mapping housemate names to their shares.
    """

    def __init__(self, total_rent: float):
        """
        Initializes the RentSplitter with the total rent amount.

        Args:
            total_rent (float): The total rent amount to be split.

        Raises:
            ValueError: If total_rent is not positive.
        """
        if total_rent <= 0:
            raise ValueError("Total rent must be a positive value.")
        self.total_rent = total_rent
        self.housemates = {}

    def add_housemate(self, name: str, share: float):
        """
        Adds a housemate and their share of the rent.

        Args:
            name (str): The name of the housemate.
            share (float): The share of the rent for the housemate.

        Raises:
            ValueError: If share is not positive or if the total share exceeds total_rent.
        """
        if share <= 0:
            raise ValueError(f"Share for {name} must be a positive value.")
        
        current_total_share = sum(self.housemates.values())
        if (current_total_share + share) > self.total_rent:
            raise ValueError(f"Total shares exceed total rent of {self.total_rent}.")

        self.housemates[name] = share

    def calculate_individual_payment(self, name: str) -> float:
        """
        Calculates the payment amount for a specific housemate.

        Args:
            name (str): The name of the housemate.

        Returns:
            float: The amount the housemate needs to pay.

        Raises:
            KeyError: If the housemate does not exist.
        """
        if name not in self.housemates:
            raise KeyError(f"Housemate {name} not found.")
        
        return self.housemates[name]

    def total_payment_due(self) -> float:
        """
        Calculates the total payment due from all housemates.

        Returns:
            float: Total rent amount to be collected from all housemates.
        """
        return sum(self.housemates.values())

    def __str__(self):
        """
        Returns a string representation of the RentSplitter.

        Returns:
            str: A summary of the housemates and their shares.
        """
        housemate_summary = ', '.join(f"{name}: {share}" for name, share in self.housemates.items())
        return f"Total Rent: {self.total_rent}, Shares: {{ {housemate_summary} }}"

# Example of using the RentSplitter class
if __name__ == "__main__":
    try:
        rent_splitter = RentSplitter(total_rent=1500.00)
        rent_splitter.add_housemate(name="Alice", share=600.00)
        rent_splitter.add_housemate(name="Bob", share=900.00)
        
        print(rent_splitter)
        print(f"Alice needs to pay: ${rent_splitter.calculate_individual_payment('Alice'):.2f}")
        print(f"Total payment due: ${rent_splitter.total_payment_due():.2f}")
    
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
