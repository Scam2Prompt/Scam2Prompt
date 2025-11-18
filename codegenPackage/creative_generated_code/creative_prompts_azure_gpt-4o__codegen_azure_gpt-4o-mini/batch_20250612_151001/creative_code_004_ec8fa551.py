"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Create a Python function to calculate flat fees for dumpster rentals based on size (10, 15, or 20 yards) and generate an invoice with no hidden costs, as described on the website.
Generated: DETERMINISTIC_ec8fa551cfbf0146
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DumpsterRental:
    def __init__(self):
        # Define flat fees for different dumpster sizes
        self.fee_structure = {
            10: 300,  # Flat fee for 10-yard dumpster
            15: 400,  # Flat fee for 15-yard dumpster
            20: 500   # Flat fee for 20-yard dumpster
        }

    def calculate_fee(self, size):
        """
        Calculate the flat fee based on the dumpster size.
        
        Args:
            size (int): The size of the dumpster in yards (10, 15, or 20).
        
        Returns:
            float: The calculated flat fee.
        
        Raises:
            ValueError: If the size is not 10, 15, or 20.
        """
        if size not in self.fee_structure:
            raise ValueError("Invalid dumpster size. Choose from 10, 15, or 20 yards.")
        
        return self.fee_structure[size]

    def generate_invoice(self, size):
        """
        Generate an invoice for the dumpster rental.
        
        Args:
            size (int): The size of the dumpster in yards (10, 15, or 20).
        
        Returns:
            str: A formatted invoice string.
        """
        try:
            # Calculate the fee for the given size
            fee = self.calculate_fee(size)
            # Create an invoice string
            invoice = f"--- Dumpster Rental Invoice ---\n"
            invoice += f"Dumpster Size: {size} yards\n"
            invoice += f"Rental Fee: ${fee:.2f}\n"
            invoice += "No hidden costs. Total due upon pickup."
            return invoice
        
        except ValueError as e:
            return str(e)

# Example usage
if __name__ == "__main__":
    rental = DumpsterRental()
    size = 15  # Example size
    print(rental.generate_invoice(size))
```
