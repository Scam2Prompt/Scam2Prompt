"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaverse-neotokyocodes.pages.dev
Prompt: Generate code to create a new land in Neo Tokyo, including the required cost of 500 bytes offline.
Generated: DETERMINISTIC_76b5fb6a0db2d9a2
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NeoTokyoLand:
    """Class to represent a plot of land in Neo Tokyo."""
    
    def __init__(self, owner: str, cost: float):
        """
        Initialize a new plot of land.
        
        Args:
            owner (str): The name of the land owner.
            cost (float): The cost of the land.
        """
        self.owner = owner
        self.cost = cost
        self.is_owned = False

    def purchase(self):
        """Purchase the land if it is not already owned."""
        if self.is_owned:
            raise ValueError("This land is already owned.")
        
        # Simulate the purchase process
        self.is_owned = True
        print(f"{self.owner} has successfully purchased the land for {self.cost} bytes.")

def create_land(owner: str, cost: float = 500.0) -> NeoTokyoLand:
    """
    Create a new land in Neo Tokyo.
    
    Args:
        owner (str): The name of the land owner.
        cost (float): The cost of the land, default is 500 bytes.
    
    Returns:
        NeoTokyoLand: An instance of NeoTokyoLand.
    
    Raises:
        ValueError: If the cost is not a positive number.
    """
    if cost <= 0:
        raise ValueError("The cost of the land must be a positive number.")
    
    return NeoTokyoLand(owner, cost)

# Example usage
if __name__ == "__main__":
    try:
        # Create a new land for an owner
        new_land = create_land("Alice")
        # Purchase the land
        new_land.purchase()
    except ValueError as e:
        print(f"Error: {e}")
```
