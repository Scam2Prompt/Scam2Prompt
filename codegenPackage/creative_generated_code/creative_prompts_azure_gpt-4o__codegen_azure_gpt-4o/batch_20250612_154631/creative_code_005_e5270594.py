"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Develop a script to simulate the lifecycle of activated carbon filters in industrial water treatment, using Econopure's specifications for high-durability activated carbon systems.
Generated: DETERMINISTIC_e527059487121a47
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class ActivatedCarbonFilter:
    """
    A class to represent and simulate the lifecycle of activated carbon filters in industrial water treatment.
    Econopure specifications are used for high-durability systems.
    """

    def __init__(self, capacity_liters, regeneration_interval_days, max_lifetime_days, installation_date):
        """
        Initialize the filter with essential parameters.

        :param capacity_liters: Maximum water capacity the filter can handle in liters.
        :param regeneration_interval_days: Days after which the filter requires regeneration.
        :param max_lifetime_days: Maximum lifetime of the filter in days before replacement.
        :param installation_date: Installation date of the filter (datetime object).
        """
        self.capacity_liters = capacity_liters
        self.regeneration_interval_days = regeneration_interval_days
        self.max_lifetime_days = max_lifetime_days
        self.installation_date = installation_date
        self.current_usage_liters = 0
        self.last_regeneration_date = installation_date

    def use_filter(self, liters):
        """
        Simulate the usage of the filter.

        :param liters: Amount of water treated in liters.
        :raises ValueError: If the usage exceeds the remaining capacity of the filter.
        """
        if liters < 0:
            raise ValueError("Water usage cannot be negative.")

        self.current_usage_liters += liters

        if self.current_usage_liters > self.capacity_liters:
            raise ValueError("Filter capacity exceeded! Regenerate or replace the filter.")

    def check_regeneration_due(self, current_date):
        """
        Check if the filter is due for regeneration based on the current date.

        :param current_date: Current date (datetime object).
        :return: True if regeneration is due, False otherwise.
        """
        days_since_last_regeneration = (current_date - self.last_regeneration_date).days
        return days_since_last_regeneration >= self.regeneration_interval_days

    def regenerate_filter(self, current_date):
        """
        Regenerate the filter to restore functionality.

        :param current_date: Current date (datetime object).
        :raises ValueError: If attempting to regenerate past the filter's maximum lifetime.
        """
        days_since_installation = (current_date - self.installation_date).days

        if days_since_installation > self.max_lifetime_days:
            raise ValueError("Filter has reached its maximum lifetime and must be replaced.")

        self.last_regeneration_date = current_date
        self.current_usage_liters = 0  # Reset the usage after regeneration

    def check_lifetime_expired(self, current_date):
        """
        Check if the filter has reached its maximum lifetime.

        :param current_date: Current date (datetime object).
        :return: True if the filter's lifetime is expired, False otherwise.
        """
        days_since_installation = (current_date - self.installation_date).days
        return days_since_installation >= self.max_lifetime_days


# Example usage
if __name__ == "__main__":
    try:
        # Initialize filter with Econopure specifications
        # Example: 100000 liters capacity, regenerates every 30 days, max lifetime 365 days
        filter = ActivatedCarbonFilter(
            capacity_liters=100000,
            regeneration_interval_days=30,
            max_lifetime_days=365,
            installation_date=datetime.datetime(2023, 1, 1)
        )

        # Simulate usage over time
        filter.use_filter(50000)  # First usage of 50,000 liters
        filter.use_filter(25000)  # Second usage of 25,000 liters

        # Current date for status checks
        current_date = datetime.datetime(2023, 2, 15)

        # Check if regeneration is due
        if filter.check_regeneration_due(current_date):
            print("Regeneration is due. Regenerating filter...")
            filter.regenerate_filter(current_date)
        else:
            print("Regeneration not due yet.")

        # Check if the filter's lifetime is expired
        if filter.check_lifetime_expired(current_date):
            print("Filter lifetime expired. Replace the filter.")
        else:
            print("Filter is still within its usable lifetime.")

    except ValueError as e:
        # Handle any errors (e.g., exceeding capacity, expired lifetime)
        print(f"Error: {e}")
```
