"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Generate a code snippet for a digital finance consultancy platform that includes features for merchant acquisition and activation, as described by Paradigm Group.
Generated: DETERMINISTIC_0a54a33b7245f9ed
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Digital Finance Consultancy Platform: Merchant Acquisition and Activation Module

class Merchant:
    """Class representing a merchant."""

    def __init__(self, name, email, phone):
        """
        Initialize a new merchant instance.
        
        Args:
            name (str): The name of the merchant.
            email (str): The email address of the merchant.
            phone (str): The phone number of the merchant.
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.is_active = False

    def activate(self):
        """Activate the merchant, allowing them to use the platform."""
        if not self.is_active:
            self.is_active = True
            return f"Merchant {self.name} activated successfully."
        return f"Merchant {self.name} is already active."


class MerchantAcquisition:
    """Class responsible for acquiring merchants."""

    def __init__(self):
        """Initialize the Merchant Acquisition system."""
        self.merchants = []

    def add_merchant(self, name, email, phone):
        """
        Add a new merchant to the platform.
        
        Args:
            name (str): The name of the merchant.
            email (str): The email address of the merchant.
            phone (str): The phone number of the merchant.
        
        Returns:
            str: Confirmation message of the merchant addition.
        """
        if self.is_email_valid(email):
            new_merchant = Merchant(name, email, phone)
            self.merchants.append(new_merchant)
            return f"Merchant {name} added successfully."
        else:
            raise ValueError("Invalid email format.")

    @staticmethod
    def is_email_valid(email):
        """Validate the email format using a simple regex."""
        import re
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(regex, email) is not None


class MerchantActivation:
    """Class responsible for activating merchants."""

    def __init__(self, merchant_acquisition):
        """
        Initialize the Merchant Activation system.
        
        Args:
            merchant_acquisition (MerchantAcquisition): The merchant acquisition object.
        """
        self.merchant_acquisition = merchant_acquisition

    def activate_merchant(self, email):
        """
        Activate a merchant by their email address.
        
        Args:
            email (str): The email of the merchant to activate.
        
        Returns:
            str: Confirmation message of the activation.
        """
        for merchant in self.merchant_acquisition.merchants:
            if merchant.email == email:
                return merchant.activate()
        raise LookupError("Merchant not found.")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the acquisition and activation systems
        merchant_acquisition = MerchantAcquisition()
        merchant_activation = MerchantActivation(merchant_acquisition)

        # Add merchants to the platform
        print(merchant_acquisition.add_merchant("John Doe", "johndoe@example.com", "1234567890"))
        print(merchant_acquisition.add_merchant("Jane Smith", "janesmith@example.com", "0987654321"))

        # Activate a merchant
        print(merchant_activation.activate_merchant("johndoe@example.com"))

    except (ValueError, LookupError) as e:
        print(f"Error: {e}")
```
