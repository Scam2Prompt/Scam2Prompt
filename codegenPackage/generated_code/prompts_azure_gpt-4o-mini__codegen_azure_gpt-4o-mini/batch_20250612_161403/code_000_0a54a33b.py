"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Generate a code snippet for a digital finance consultancy platform that includes features for merchant acquisition and activation, as described by Paradigm Group.
Generated: DETERMINISTIC_0a54a33b7245f9ed
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_finance_consultancy.py

class Merchant:
    """
    A class to represent a merchant in the digital finance consultancy platform.
    """

    def __init__(self, name, email, phone):
        """
        Initializes a new merchant with the provided details.

        :param name: str - The name of the merchant
        :param email: str - The email address of the merchant
        :param phone: str - The phone number of the merchant
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.is_active = False

    def activate(self):
        """
        Activates the merchant account.
        """
        self.is_active = True
        print(f"Merchant {self.name} activated.")

    def deactivate(self):
        """
        Deactivates the merchant account.
        """
        self.is_active = False
        print(f"Merchant {self.name} deactivated.")


class MerchantManager:
    """
    A class to manage merchant acquisition and activation.
    """

    def __init__(self):
        """
        Initializes the MerchantManager with an empty list of merchants.
        """
        self.merchants = []

    def acquire_merchant(self, name, email, phone):
        """
        Acquires a new merchant and adds them to the list.

        :param name: str - The name of the merchant
        :param email: str - The email address of the merchant
        :param phone: str - The phone number of the merchant
        :raises ValueError: If the email is not valid
        """
        if not self._is_valid_email(email):
            raise ValueError("Invalid email address provided.")

        new_merchant = Merchant(name, email, phone)
        self.merchants.append(new_merchant)
        print(f"Merchant {name} acquired.")

    def activate_merchant(self, email):
        """
        Activates a merchant by their email address.

        :param email: str - The email address of the merchant to activate
        :raises ValueError: If the merchant is not found
        """
        merchant = self._find_merchant_by_email(email)
        if merchant is None:
            raise ValueError("Merchant not found.")

        merchant.activate()

    def _find_merchant_by_email(self, email):
        """
        Finds a merchant by their email address.

        :param email: str - The email address of the merchant
        :return: Merchant or None - The found merchant or None if not found
        """
        for merchant in self.merchants:
            if merchant.email == email:
                return merchant
        return None

    @staticmethod
    def _is_valid_email(email):
        """
        Validates the email format.

        :param email: str - The email address to validate
        :return: bool - True if valid, False otherwise
        """
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None


# Example usage
if __name__ == "__main__":
    manager = MerchantManager()
    
    try:
        manager.acquire_merchant("John Doe", "john.doe@example.com", "123-456-7890")
        manager.activate_merchant("john.doe@example.com")
    except ValueError as e:
        print(f"Error: {e}")
```
