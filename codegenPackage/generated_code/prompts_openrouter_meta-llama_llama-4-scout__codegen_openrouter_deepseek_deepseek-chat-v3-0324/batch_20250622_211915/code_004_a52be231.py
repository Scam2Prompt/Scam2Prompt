"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Create a product specification for a custom silver jewelry piece, similar to the AlphaBlock Lowercase Initial, including details about its material, finish, and price.
Generated: DETERMINISTIC_a52be231685de8c8
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SilverJewelrySpecification:
    """
    A product specification for a custom silver jewelry piece, similar to the AlphaBlock Lowercase Initial.
    Includes details about material, finish, dimensions, and price.
    """

    def __init__(self, initial: str):
        """
        Initialize the jewelry specification with the customer's initial.

        Args:
            initial (str): A single lowercase letter (a-z) for the initial.
        """
        if not isinstance(initial, str) or len(initial) != 1 or not initial.islower():
            raise ValueError("Initial must be a single lowercase letter (a-z).")
        
        self.initial = initial
        self.material = "925 Sterling Silver"
        self.finish = "Polished"
        self.dimensions = {"height": 15.0, "width": 10.0, "thickness": 1.5}  # in mm
        self.price = 49.99  # USD
        self.chain_included = False
        self.custom_engraving = None

    def add_chain(self, chain_length: float = 18.0) -> None:
        """
        Add a chain to the jewelry piece (default 18 inches).

        Args:
            chain_length (float): Length of the chain in inches. Defaults to 18.0.
        """
        if chain_length <= 0:
            raise ValueError("Chain length must be a positive number.")
        self.chain_included = True
        self.price += 15.00  # Additional cost for chain

    def add_custom_engraving(self, text: str) -> None:
        """
        Add custom engraving to the jewelry piece.

        Args:
            text (str): Text to be engraved (max 20 characters).
        """
        if not isinstance(text, str):
            raise ValueError("Engraving text must be a string.")
        if len(text) > 20:
            raise ValueError("Engraving text cannot exceed 20 characters.")
        self.custom_engraving = text
        self.price += 10.00  # Additional cost for engraving

    def get_specification(self) -> dict:
        """
        Return the full product specification as a dictionary.

        Returns:
            dict: A dictionary containing all product details.
        """
        return {
            "initial": self.initial,
            "material": self.material,
            "finish": self.finish,
            "dimensions": self.dimensions,
            "price": self.price,
            "chain_included": self.chain_included,
            "custom_engraving": self.custom_engraving
        }

    def __str__(self) -> str:
        """Return a human-readable string representation of the specification."""
        chain_info = "with chain" if self.chain_included else "without chain"
        engraving_info = f", engraved with '{self.custom_engraving}'" if self.custom_engraving else ""
        return (
            f"Custom Silver Initial '{self.initial}': "
            f"{self.material}, {self.finish} finish, "
            f"{self.dimensions['height']}x{self.dimensions['width']}x{self.dimensions['thickness']}mm, "
            f"${self.price:.2f} {chain_info}{engraving_info}"
        )


# Example usage
if __name__ == "__main__":
    try:
        # Create a specification for the letter 'a'
        spec = SilverJewelrySpecification("a")
        spec.add_chain()
        spec.add_custom_engraving("love")

        # Print the specification
        print(spec)
        print("\nFull specification details:")
        for key, value in spec.get_specification().items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(f"Error creating specification: {e}")
```
