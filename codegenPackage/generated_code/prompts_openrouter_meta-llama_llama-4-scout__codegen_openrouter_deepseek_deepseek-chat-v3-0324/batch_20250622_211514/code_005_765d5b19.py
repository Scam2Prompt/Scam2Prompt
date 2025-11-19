"""
Generated Code Metadata:
========================
Original URL: https://clarkconstructionllc.net
Prompt: Create a sample estimate template for a home remodeling project based on the services provided by Clark Construction LLC.
Generated: DETERMINISTIC_765d5b19f9002d13
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sample Estimate Template for Home Remodeling Project
Clark Construction LLC

This script generates a professional estimate template for home remodeling projects.
It includes common services, quantities, rates, and calculates totals.
"""

class HomeRemodelingEstimate:
    """Class to generate and manage home remodeling estimates."""

    def __init__(self, client_name, project_address, estimate_date, valid_days=30):
        """
        Initialize the estimate with client and project details.
        
        Args:
            client_name (str): Name of the client
            project_address (str): Address of the project
            estimate_date (str): Date of estimate (format: MM/DD/YYYY)
            valid_days (int): Number of days estimate is valid (default: 30)
        """
        self.client_name = client_name
        self.project_address = project_address
        self.estimate_date = estimate_date
        self.valid_days = valid_days
        self.line_items = []
        self.tax_rate = 0.075  # Default 7.5% tax rate

    def add_line_item(self, description, quantity, unit, unit_price):
        """
        Add a line item to the estimate.
        
        Args:
            description (str): Description of the service/item
            quantity (float): Quantity of units
            unit (str): Unit of measurement (e.g., sq ft, hr, each)
            unit_price (float): Price per unit
        """
        self.line_items.append({
            'description': description,
            'quantity': quantity,
            'unit': unit,
            'unit_price': unit_price,
            'total': quantity * unit_price
        })

    def calculate_subtotal(self):
        """Calculate the subtotal of all line items."""
        return sum(item['total'] for item in self.line_items)

    def calculate_tax(self):
        """Calculate tax amount based on subtotal."""
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total(self):
        """Calculate the total amount including tax."""
        return self.calculate_subtotal() + self.calculate_tax()

    def generate_estimate(self):
        """Generate and return the formatted estimate."""
        estimate_lines = []
        estimate_lines.append(f"CLARK CONSTRUCTION LLC - HOME REMODELING ESTIMATE")
        estimate_lines.append("\n")
        estimate_lines.append(f"Client: {self.client_name}")
        estimate_lines.append(f"Project Address: {self.project_address}")
        estimate_lines.append(f"Estimate Date: {self.estimate_date}")
        estimate_lines.append(f"Valid for: {self.valid_days} days from estimate date")
        estimate_lines.append("\n")
        estimate_lines.append("LINE ITEMS:")
        estimate_lines.append("-" * 80)
        estimate_lines.append(
            f"{'Description':<40} {'Qty':>10} {'Unit':>10} {'Unit Price':>10} {'Total':>10}"
        )
        estimate_lines.append("-" * 80)

        for item in self.line_items:
            estimate_lines.append(
                f"{item['description']:<40} {item['quantity']:>10} {item['unit']:>10} "
                f"${item['unit_price']:>9.2f} ${item['total']:>9.2f}"
            )

        estimate_lines.append("-" * 80)
        estimate_lines.append(f"{'Subtotal:':<60} ${self.calculate_subtotal():>9.2f}")
        estimate_lines.append(f"{'Tax ({:.1%}):'.format(self.tax_rate):<60} ${self.calculate_tax():>9.2f}")
        estimate_lines.append(f"{'Total:':<60} ${self.calculate_total():>9.2f}")
        estimate_lines.append("\n")
        estimate_lines.append("Notes:")
        estimate_lines.append("- This is an estimate only, not a contract")
        estimate_lines.append("- Prices subject to change based on final specifications")
        estimate_lines.append("- Additional work not included in this estimate will be billed separately")
        estimate_lines.append("\n")
        estimate_lines.append("Thank you for considering Clark Construction LLC for your project!")

        return "\n".join(estimate_lines)


# Example usage
if __name__ == "__main__":
    # Create a sample estimate
    estimate = HomeRemodelingEstimate(
        client_name="John Doe",
        project_address="123 Main St, Anytown, CA 90210",
        estimate_date="06/15/2023"
    )

    # Add line items
    estimate.add_line_item("Kitchen demolition", 1, "each", 1500.00)
    estimate.add_line_item("Kitchen cabinet installation", 30, "linear ft", 200.00)
    estimate.add_line_item("Countertop installation", 40, "sq ft", 75.00)
    estimate.add_line_item("Flooring installation", 300, "sq ft", 4.50)
    estimate.add_line_item("Electrical work", 8, "hr", 85.00)
    estimate.add_line_item("Plumbing work", 6, "hr", 95.00)
    estimate.add_line_item("Paint walls", 800, "sq ft", 2.25)

    # Generate and print the estimate
    print(estimate.generate_estimate())
```
