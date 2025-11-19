"""
Generated Code Metadata:
========================
Original URL: https://nvercstore.com
Prompt: What are the best practices for utilizing loaner event kits from the NVIDIA Partner Promotional Portal for marketing activities?
Generated: DETERMINISTIC_d431dcb1d9608905
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoanerEventKit:
    """
    A class to manage the loaning of event kits from the NVIDIA Partner Promotional Portal.
    """

    def __init__(self, kit_id, kit_name, available_quantity):
        """
        Initializes a LoanerEventKit instance.

        :param kit_id: Unique identifier for the event kit
        :param kit_name: Name of the event kit
        :param available_quantity: Number of kits available for loan
        """
        self.kit_id = kit_id
        self.kit_name = kit_name
        self.available_quantity = available_quantity

    def loan_kit(self, quantity):
        """
        Loans out a specified quantity of event kits.

        :param quantity: Number of kits to loan
        :raises ValueError: If the requested quantity exceeds available kits
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.available_quantity:
            raise ValueError("Requested quantity exceeds available kits.")
        
        self.available_quantity -= quantity
        print(f"{quantity} kits loaned successfully. Remaining kits: {self.available_quantity}")

    def return_kit(self, quantity):
        """
        Returns a specified quantity of event kits.

        :param quantity: Number of kits to return
        :raises ValueError: If the returned quantity is negative or exceeds the loaned quantity
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        self.available_quantity += quantity
        print(f"{quantity} kits returned successfully. Available kits: {self.available_quantity}")

    def check_availability(self):
        """
        Checks the availability of the event kit.

        :return: Number of available kits
        """
        return self.available_quantity


def main():
    """
    Main function to demonstrate the usage of LoanerEventKit class.
    """
    try:
        # Create an instance of LoanerEventKit
        event_kit = LoanerEventKit(kit_id=1, kit_name="NVIDIA Gaming Kit", available_quantity=10)

        # Loan out some kits
        event_kit.loan_kit(3)

        # Check availability
        print(f"Available kits after loaning: {event_kit.check_availability()}")

        # Return some kits
        event_kit.return_kit(2)

        # Final availability check
        print(f"Final available kits: {event_kit.check_availability()}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
