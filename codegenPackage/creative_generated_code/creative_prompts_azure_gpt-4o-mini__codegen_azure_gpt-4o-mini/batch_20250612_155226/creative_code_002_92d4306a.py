"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lyvely-claim.pages.dev
Prompt: Explain how to set up a membership model on Lyvely for my content creation business.
Generated: DETERMINISTIC_92d4306a42319652
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MembershipModel:
    """
    A class to represent a membership model for a content creation business.
    
    Attributes:
        membership_types (dict): A dictionary to hold different membership types and their benefits.
    """

    def __init__(self):
        """Initializes the membership model with basic membership types."""
        self.membership_types = {
            "basic": {
                "price": 5.99,
                "benefits": ["Access to basic content", "Monthly newsletter"]
            },
            "premium": {
                "price": 15.99,
                "benefits": ["Access to all content", "Exclusive webinars", "1-on-1 Q&A sessions"]
            },
            "vip": {
                "price": 29.99,
                "benefits": ["All premium benefits", "Personalized content", "Behind-the-scenes access"]
            }
        }

    def add_membership(self, name, price, benefits):
        """
        Adds a new membership type to the model.

        Args:
            name (str): The name of the membership type.
            price (float): The price of the membership.
            benefits (list): A list of benefits for the membership.

        Raises:
            ValueError: If the membership name already exists or if the price is negative.
        """
        if name in self.membership_types:
            raise ValueError(f"Membership type '{name}' already exists.")
        if price < 0:
            raise ValueError("Price must be a non-negative value.")

        self.membership_types[name] = {
            "price": price,
            "benefits": benefits
        }

    def remove_membership(self, name):
        """
        Removes a membership type from the model.

        Args:
            name (str): The name of the membership type.

        Raises:
            KeyError: If the membership type does not exist.
        """
        if name not in self.membership_types:
            raise KeyError(f"Membership type '{name}' does not exist.")

        del self.membership_types[name]

    def get_membership_info(self, name):
        """
        Retrieves the information for a specific membership type.

        Args:
            name (str): The name of the membership type.

        Returns:
            dict: A dictionary containing the membership price and benefits.

        Raises:
            KeyError: If the membership type does not exist.
        """
        if name not in self.membership_types:
            raise KeyError(f"Membership type '{name}' does not exist.")
        
        return self.membership_types[name]

    def list_memberships(self):
        """Returns a list of all available membership types."""
        return self.membership_types


# Example Usage
if __name__ == "__main__":
    try:
        membership_model = MembershipModel()
        print("Available Memberships:")
        print(membership_model.list_memberships())

        # Add a new membership type
        membership_model.add_membership("family", 9.99, ["Family content", "Shared access"])
        print("\nUpdated Memberships:")
        print(membership_model.list_memberships())

        # Get information about a specific membership
        print("\nFamily Membership Info:")
        print(membership_model.get_membership_info("family"))

        # Remove a membership type
        membership_model.remove_membership("basic")
        print("\nMemberships after removal:")
        print(membership_model.list_memberships())

    except Exception as e:
        print(f"An error occurred: {e}")
```
