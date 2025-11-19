"""
Generated Code Metadata:
========================
Original URL: https://token-graph.net
Prompt: How does the AT&T Guarantee SM work for new and existing customers?
Generated: DETERMINISTIC_1d9660dd80ad6a69
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ATTGuarantee:
    """
    A class to represent the AT&T Guarantee for new and existing customers.
    """

    def __init__(self, customer_type: str):
        """
        Initializes the ATTGuarantee class.

        Parameters:
        customer_type (str): The type of customer ('new' or 'existing').
        """
        self.customer_type = customer_type.lower()
        self.guarantee_details = {
            'new': "New customers can enjoy a 30-day satisfaction guarantee.",
            'existing': "Existing customers can benefit from a 30-day satisfaction guarantee on new services."
        }

    def get_guarantee_info(self) -> str:
        """
        Retrieves the guarantee information based on customer type.

        Returns:
        str: A message detailing the guarantee for the customer type.

        Raises:
        ValueError: If the customer type is not recognized.
        """
        if self.customer_type not in self.guarantee_details:
            raise ValueError("Invalid customer type. Please use 'new' or 'existing'.")

        return self.guarantee_details[self.customer_type]

def main():
    """
    Main function to demonstrate the AT&T Guarantee functionality.
    """
    try:
        # Example for new customer
        new_customer = ATTGuarantee('new')
        print(new_customer.get_guarantee_info())

        # Example for existing customer
        existing_customer = ATTGuarantee('existing')
        print(existing_customer.get_guarantee_info())

        # Example for invalid customer type
        invalid_customer = ATTGuarantee('invalid')
        print(invalid_customer.get_guarantee_info())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
