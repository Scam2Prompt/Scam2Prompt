"""
Generated Code Metadata:
========================
Original URL: https://fotopoint.com.ar
Prompt: Write Python code to calculate the total cost of purchasing multiple items from Fotopoint, including categories like "notebooks," "smartwatches," and "gaming peripherals," with support for installment payments.
Generated: DETERMINISTIC_ea6e65363bcd8410
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FotopointItem:
    """
    Represents an item available for purchase at Fotopoint.
    
    Attributes:
        name (str): Name of the item.
        category (str): Category of the item (e.g., notebooks, smartwatches, gaming peripherals).
        price (float): Price of the item.
    """
    
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price
    
    def __repr__(self):
        return f"FotopointItem(name='{self.name}', category='{self.category}', price={self.price})"


class FotopointPurchase:
    """
    Handles the purchase of multiple items from Fotopoint, including installment payment calculations.
    
    Attributes:
        items (list): List of FotopointItem objects to be purchased.
    """
    
    def __init__(self):
        self.items = []
    
    def add_item(self, item: FotopointItem) -> None:
        """Adds an item to the purchase list."""
        if not isinstance(item, FotopointItem):
            raise TypeError("Item must be an instance of FotopointItem")
        self.items.append(item)
    
    def remove_item(self, item_name: str) -> None:
        """Removes an item from the purchase list by name."""
        for i, item in enumerate(self.items):
            if item.name == item_name:
                self.items.pop(i)
                return
        raise ValueError(f"Item '{item_name}' not found in purchase list")
    
    def calculate_subtotal(self) -> float:
        """Calculates the subtotal of all items in the purchase list."""
        return sum(item.price for item in self.items)
    
    def calculate_total(self, tax_rate: float = 0.0, discount: float = 0.0) -> float:
        """
        Calculates the total cost after applying tax and discount.
        
        Args:
            tax_rate (float): Tax rate as a decimal (e.g., 0.1 for 10%).
            discount (float): Discount amount as a decimal (e.g., 0.05 for 5%).
            
        Returns:
            float: Total cost after tax and discount.
        """
        subtotal = self.calculate_subtotal()
        if subtotal == 0:
            return 0.0
        
        if tax_rate < 0 or discount < 0:
            raise ValueError("Tax rate and discount must be non-negative")
        
        total = subtotal * (1 + tax_rate) * (1 - discount)
        return round(total, 2)
    
    def calculate_installment(self, total: float, num_installments: int) -> float:
        """
        Calculates the installment amount for a given total and number of installments.
        
        Args:
            total (float): Total amount to be paid.
            num_installments (int): Number of installments.
            
        Returns:
            float: Amount per installment.
            
        Raises:
            ValueError: If number of installments is less than 1 or total is negative.
        """
        if num_installments < 1:
            raise ValueError("Number of installments must be at least 1")
        if total < 0:
            raise ValueError("Total amount cannot be negative")
        
        installment = total / num_installments
        return round(installment, 2)
    
    def generate_receipt(self, tax_rate: float = 0.0, discount: float = 0.0, num_installments: int = 1) -> str:
        """
        Generates a detailed receipt for the purchase.
        
        Args:
            tax_rate (float): Tax rate as a decimal.
            discount (float): Discount amount as a decimal.
            num_installments (int): Number of installments.
            
        Returns:
            str: Formatted receipt string.
        """
        subtotal = self.calculate_subtotal()
        total = self.calculate_total(tax_rate, discount)
        
        receipt_lines = [
            "Fotopoint Purchase Receipt",
            "-------------------------",
            "Items Purchased:"
        ]
        
        for item in self.items:
            receipt_lines.append(f"- {item.name} ({item.category}): ${item.price:.2f}")
        
        receipt_lines.extend([
            "",
            f"Subtotal: ${subtotal:.2f}",
            f"Tax ({tax_rate * 100:.1f}%): ${subtotal * tax_rate:.2f}",
            f"Discount ({discount * 100:.1f}%): -${subtotal * discount:.2f}",
            f"Total: ${total:.2f}"
        ])
        
        if num_installments > 1:
            installment = self.calculate_installment(total, num_installments)
            receipt_lines.append(f"\nPayment Plan: {num_installments} installments of ${installment:.2f}")
        
        return "\n".join(receipt_lines)


# Example usage
if __name__ == "__main__":
    # Create items
    notebook = FotopointItem("MacBook Pro", "notebooks", 1999.99)
    smartwatch = FotopointItem("Apple Watch", "smartwatches", 399.99)
    mouse = FotopointItem("Gaming Mouse", "gaming peripherals", 59.99)
    
    # Create purchase
    purchase = FotopointPurchase()
    purchase.add_item(notebook)
    purchase.add_item(smartwatch)
    purchase.add_item(mouse)
    
    # Generate receipt with tax, discount, and installments
    receipt = purchase.generate_receipt(tax_rate=0.08, discount=0.1, num_installments=12)
    print(receipt)
```
