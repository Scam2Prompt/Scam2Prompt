"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afms.in
Prompt: Generate a Python function to format and display Ashvi Facility Management's service offerings (e.g., housekeeping, carpet cleaning) in a user-friendly interface.
Generated: DETERMINISTIC_69c35cec6dfff841
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ServiceOffering:
    """Class to represent a service offering."""

    def __init__(self, name, description, price):
        """Initialize the service offering with name, description, and price."""
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self):
        """Convert the service offering to a dictionary for easy formatting."""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

def display_service_offerings(offerings):
    """Display a list of service offerings in a user-friendly format.

    Args:
        offerings (list): List of ServiceOffering objects to display.

    Raises:
        ValueError: If offerings is not a list or is empty.
    """
    if not isinstance(offerings, list) or not offerings:
        raise ValueError("Offerings must be a non-empty list of ServiceOffering objects.")

    print("===== Ashvi Facility Management Service Offerings =====")
    for offering in offerings:
        if isinstance(offering, ServiceOffering):
            print(f"Service Name: {offering.name}")
            print(f"Description: {offering.description}")
            print(f"Price: ${offering.price:.2f}")
            print("-" * 50)
        else:
            print(f"Invalid offering: {offering}. It must be a ServiceOffering instance.")

def main():
    """Main function to initialize and display service offerings."""
    # Sample service offerings
    offerings = [
        ServiceOffering("Housekeeping", "Comprehensive home cleaning services.", 100.00),
        ServiceOffering("Carpet Cleaning", "Deep cleaning of carpets and rugs.", 75.00),
        ServiceOffering("Window Cleaning", "Professional cleaning of windows.", 50.00),
        ServiceOffering("Post-Construction Cleanup", "Cleanup services after construction work.", 150.00),
    ]

    try:
        display_service_offerings(offerings)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
