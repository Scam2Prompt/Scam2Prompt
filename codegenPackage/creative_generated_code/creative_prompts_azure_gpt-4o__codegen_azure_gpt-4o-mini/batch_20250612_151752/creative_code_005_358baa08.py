"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Develop a code snippet for handling customer inquiries and generating quotes for automotive parts, including "essuie glace" and "produits d'entretiens," as described on the Distribution Pièces Service website.
Generated: DETERMINISTIC_358baa08954cac34
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AutomotivePart:
    """Class to represent an automotive part with its properties."""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class CustomerInquiry:
    """Class to handle customer inquiries and generate quotes for automotive parts."""
    
    def __init__(self):
        self.parts = []  # A list to store requested automotive parts

    def add_part(self, part):
        """Add an automotive part to the inquiry."""
        if isinstance(part, AutomotivePart):
            self.parts.append(part)
        else:
            raise ValueError("Only AutomotivePart instances can be added.")

    def calculate_total(self):
        """Calculate the total price of all parts in the inquiry."""
        return sum(part.price for part in self.parts)

    def generate_quote(self):
        """Generate a quote including the list of parts and total price."""
        if not self.parts:
            raise ValueError("No parts added to the inquiry.")

        quote = "QUOTE\n"
        quote += f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}\n"
        quote += "Requested Parts:\n"
        for part in self.parts:
            quote += f" - {part}\n"
        total_price = self.calculate_total()
        quote += f"Total Price: ${total_price:.2f}\n"
        return quote


# Example usage
if __name__ == "__main__":
    try:
        # Create instance of CustomerInquiry
        inquiry = CustomerInquiry()

        # Adding automotive parts
        inquiry.add_part(AutomotivePart("essuie glace", 20.50))
        inquiry.add_part(AutomotivePart("produits d'entretiens", 15.75))

        # Generate and print the quote
        print(inquiry.generate_quote())

    except ValueError as e:
        print(f"Error: {e}")
```
