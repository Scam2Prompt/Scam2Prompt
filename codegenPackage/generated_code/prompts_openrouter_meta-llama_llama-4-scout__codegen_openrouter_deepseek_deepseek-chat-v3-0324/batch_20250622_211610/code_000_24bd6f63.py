"""
Generated Code Metadata:
========================
Original URL: https://fullteco.cl
Prompt: Write a Python script to generate a quote for a lighting project in Puerto Montt, Chile, considering energy efficiency and modern design.
Generated: DETERMINISTIC_24bd6f634d5b53c4
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class LightingProjectQuote:
    """
    A class to generate quotes for lighting projects considering energy efficiency and modern design.
    """

    def __init__(self, project_name: str, location: str = "Puerto Montt, Chile"):
        """
        Initialize the LightingProjectQuote with project details.

        Args:
            project_name (str): Name of the project.
            location (str, optional): Location of the project. Defaults to "Puerto Montt, Chile".
        """
        self.project_name = project_name
        self.location = location
        self.items: List[Dict[str, float]] = []
        self.discount_rate: float = 0.0
        self.tax_rate: float = 0.19  # Chile's standard VAT rate

    def add_item(self, description: str, quantity: int, unit_price: float) -> None:
        """
        Add an item to the quote.

        Args:
            description (str): Description of the item.
            quantity (int): Quantity of the item.
            unit_price (float): Unit price of the item.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if unit_price <= 0:
            raise ValueError("Unit price must be greater than zero.")

        self.items.append({
            "description": description,
            "quantity": quantity,
            "unit_price": unit_price
        })

    def set_discount(self, discount_rate: float) -> None:
        """
        Set a discount rate for the quote.

        Args:
            discount_rate (float): Discount rate as a decimal (e.g., 0.1 for 10%).
        """
        if discount_rate < 0 or discount_rate > 1:
            raise ValueError("Discount rate must be between 0 and 1.")
        self.discount_rate = discount_rate

    def calculate_subtotal(self) -> float:
        """
        Calculate the subtotal of all items.

        Returns:
            float: Subtotal amount.
        """
        return sum(item["quantity"] * item["unit_price"] for item in self.items)

    def calculate_discount(self) -> float:
        """
        Calculate the discount amount.

        Returns:
            float: Discount amount.
        """
        subtotal = self.calculate_subtotal()
        return subtotal * self.discount_rate

    def calculate_tax(self) -> float:
        """
        Calculate the tax amount.

        Returns:
            float: Tax amount.
        """
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        return (subtotal - discount) * self.tax_rate

    def calculate_total(self) -> float:
        """
        Calculate the total amount including tax and discount.

        Returns:
            float: Total amount.
        """
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        return subtotal - discount + tax

    def generate_quote(self) -> str:
        """
        Generate a formatted quote with all details.

        Returns:
            str: Formatted quote as a string.
        """
        quote_lines = [
            f"QUOTE FOR LIGHTING PROJECT",
            f"Project: {self.project_name}",
            f"Location: {self.location}",
            f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}",
            "\nITEMS:",
            "Description\t\tQuantity\tUnit Price\tTotal"
        ]

        for item in self.items:
            total = item["quantity"] * item["unit_price"]
            quote_lines.append(
                f"{item['description']}\t\t{item['quantity']}\t\t${item['unit_price']:.2f}\t\t${total:.2f}"
            )

        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        total = self.calculate_total()

        quote_lines.extend([
            "\nSUMMARY:",
            f"Subtotal: ${subtotal:.2f}",
            f"Discount ({self.discount_rate * 100:.0f}%): -${discount:.2f}",
            f"Tax ({self.tax_rate * 100:.0f}%): +${tax:.2f}",
            f"TOTAL: ${total:.2f}",
            "\nNOTES:",
            "This quote includes energy-efficient and modern design lighting solutions.",
            "Valid for 30 days from the date of issue."
        ])

        return "\n".join(quote_lines)

    def save_quote_to_file(self, filename: Optional[str] = None) -> None:
        """
        Save the generated quote to a text file.

        Args:
            filename (Optional[str], optional): Name of the file. Defaults to 'quote_[project_name]_[date].txt'.
        """
        if filename is None:
            filename = f"quote_{self.project_name}_{datetime.datetime.now().strftime('%Y%m%d')}.txt"
        
        quote_text = self.generate_quote()
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(quote_text)
        except IOError as e:
            raise IOError(f"Failed to save quote to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a new quote
        quote = LightingProjectQuote("Office Building Lighting", "Puerto Montt, Chile")
        
        # Add items to the quote
        quote.add_item("LED Panel Lights", 20, 150.00)
        quote.add_item("Smart LED Bulbs", 50, 25.00)
        quote.add_item("Motion Sensors", 10, 45.00)
        
        # Apply a discount
        quote.set_discount(0.1)  # 10% discount
        
        # Generate and print the quote
        print(quote.generate_quote())
        
        # Save the quote to a file
        quote.save_quote_to_file()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
