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
# att_guarantee.py

class AT&T_Guarantee:
    """
    This class explains how the AT&T Guarantee SM works for new and existing customers.
    """

    def __init__(self):
        pass

    def new_customer_guarantee(self):
        """
        For new customers, the AT&T Guarantee SM provides a 30-day money-back guarantee.
        If the customer is not satisfied with their service, they can cancel and get a full refund.
        """
        print("For new customers, the AT&T Guarantee SM provides a 30-day money-back guarantee.")

    def existing_customer_guarantee(self):
        """
        For existing customers, the AT&T Guarantee SM provides a 30-day satisfaction guarantee.
        If the customer is not satisfied with their service, they can cancel and get a pro-rated refund.
        """
        print("For existing customers, the AT&T Guarantee SM provides a 30-day satisfaction guarantee.")

    def get_guarantee_details(self, customer_type):
        """
        Get the guarantee details based on the customer type.

        Args:
            customer_type (str): The type of customer (new or existing).

        Returns:
            str: The guarantee details.

        Raises:
            ValueError: If the customer type is not 'new' or 'existing'.
        """
        try:
            if customer_type.lower() == 'new':
                return "30-day money-back guarantee."
            elif customer_type.lower() == 'existing':
                return "30-day satisfaction guarantee with pro-rated refund."
            else:
                raise ValueError("Invalid customer type. Please enter 'new' or 'existing'.")
        except ValueError as e:
            print(f"Error: {e}")
            return None


def main():
    guarantee = AT&T_Guarantee()

    print("AT&T Guarantee SM Details:")
    print("---------------------------")

    print("New Customer Guarantee:")
    guarantee.new_customer_guarantee()

    print("\nExisting Customer Guarantee:")
    guarantee.existing_customer_guarantee()

    print("\nGet Guarantee Details:")
    print(guarantee.get_guarantee_details('new'))
    print(guarantee.get_guarantee_details('existing'))
    print(guarantee.get_guarantee_details('invalid'))

if __name__ == "__main__":
    main()
```
