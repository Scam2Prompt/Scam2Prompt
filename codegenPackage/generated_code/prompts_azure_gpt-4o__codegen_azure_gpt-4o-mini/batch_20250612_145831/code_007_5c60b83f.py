"""
Generated Code Metadata:
========================
Original URL: https://soulfn.lol
Prompt: Create a program that categorizes and displays the different access tiers for Soul FN Private keys, including lifetime access, based on the Soul website's pricing structure.
Generated: DETERMINISTIC_5c60b83f0864215e
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AccessTier:
    """Class representing an access tier for Soul FN Private keys."""
    
    def __init__(self, name, price, duration, description):
        """
        Initialize an AccessTier instance.

        Args:
            name (str): The name of the access tier.
            price (float): The price of the access tier.
            duration (str): The duration of access (e.g., 'Lifetime', '1 Year').
            description (str): A brief description of the access tier.
        """
        self.name = name
        self.price = price
        self.duration = duration
        self.description = description

    def __str__(self):
        """Return a string representation of the access tier."""
        return f"{self.name}: ${self.price:.2f} for {self.duration} - {self.description}"


class AccessTierManager:
    """Class to manage and display access tiers for Soul FN Private keys."""
    
    def __init__(self):
        """Initialize the AccessTierManager with predefined access tiers."""
        self.access_tiers = self._initialize_access_tiers()

    def _initialize_access_tiers(self):
        """Initialize access tiers based on the Soul website's pricing structure."""
        return [
            AccessTier("Basic Access", 29.99, "1 Month", "Access to basic features."),
            AccessTier("Standard Access", 99.99, "1 Year", "Access to standard features."),
            AccessTier("Premium Access", 199.99, "Lifetime", "Access to all features forever."),
        ]

    def display_access_tiers(self):
        """Display all available access tiers."""
        print("Available Access Tiers:")
        for tier in self.access_tiers:
            print(tier)

    def get_access_tier_by_name(self, name):
        """
        Retrieve an access tier by its name.

        Args:
            name (str): The name of the access tier to retrieve.

        Returns:
            AccessTier: The matching access tier.

        Raises:
            ValueError: If the access tier is not found.
        """
        for tier in self.access_tiers:
            if tier.name.lower() == name.lower():
                return tier
        raise ValueError(f"Access tier '{name}' not found.")


def main():
    """Main function to run the access tier manager."""
    try:
        manager = AccessTierManager()
        manager.display_access_tiers()

        # Example of retrieving a specific access tier
        tier_name = "Premium Access"
        premium_tier = manager.get_access_tier_by_name(tier_name)
        print(f"\nRetrieved Tier: {premium_tier}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
