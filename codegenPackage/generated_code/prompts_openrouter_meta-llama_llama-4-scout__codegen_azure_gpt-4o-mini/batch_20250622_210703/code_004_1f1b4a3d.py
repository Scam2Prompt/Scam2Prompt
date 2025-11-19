"""
Generated Code Metadata:
========================
Original URL: https://thegladiatorshoes.com
Prompt: "Design a safety shoe with a steel toe and composite midsole for manufacturing industry workers."
Generated: DETERMINISTIC_1f1b4a3dfead930e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SafetyShoe:
    """
    A class to represent a safety shoe designed for manufacturing industry workers.
    
    Attributes:
        brand (str): The brand of the safety shoe.
        size (float): The size of the safety shoe.
        steel_toe (bool): Indicates if the shoe has a steel toe.
        composite_midsole (bool): Indicates if the shoe has a composite midsole.
        color (str): The color of the safety shoe.
    """

    def __init__(self, brand: str, size: float, color: str):
        """
        Initializes a new instance of SafetyShoe.

        Args:
            brand (str): The brand of the safety shoe.
            size (float): The size of the safety shoe.
            color (str): The color of the safety shoe.

        Raises:
            ValueError: If size is not a positive number.
        """
        if size <= 0:
            raise ValueError("Size must be a positive number.")
        
        self.brand = brand
        self.size = size
        self.steel_toe = True  # Safety feature
        self.composite_midsole = True  # Safety feature
        self.color = color

    def describe(self) -> str:
        """
        Returns a description of the safety shoe.

        Returns:
            str: A string describing the safety shoe.
        """
        return (f"{self.brand} Safety Shoe\n"
                f"Size: {self.size}\n"
                f"Color: {self.color}\n"
                f"Steel Toe: {'Yes' if self.steel_toe else 'No'}\n"
                f"Composite Midsole: {'Yes' if self.composite_midsole else 'No'}")

    def is_suitable_for_work(self) -> bool:
        """
        Checks if the safety shoe is suitable for manufacturing work.

        Returns:
            bool: True if the shoe has steel toe and composite midsole, False otherwise.
        """
        return self.steel_toe and self.composite_midsole


# Example usage
if __name__ == "__main__":
    try:
        shoe = SafetyShoe(brand="SafetyFirst", size=10.5, color="Black")
        print(shoe.describe())
        print("Is suitable for work:", shoe.is_suitable_for_work())
    except ValueError as e:
        print(f"Error: {e}")
```
