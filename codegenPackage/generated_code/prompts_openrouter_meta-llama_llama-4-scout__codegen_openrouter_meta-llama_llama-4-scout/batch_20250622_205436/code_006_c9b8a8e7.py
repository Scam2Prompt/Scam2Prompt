"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Generate a digital rate card for a sports business, including a value matrix for digital inventory to support partner discussions around value and intellectual property.
Generated: DETERMINISTIC_c9b8a8e70b1aabcd
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_rate_card.py

class DigitalRateCard:
    def __init__(self):
        """
        Initialize the digital rate card with an empty inventory and rate matrix.
        """
        self.inventory = {}
        self.rate_matrix = {}

    def add_inventory(self, ad_unit, description, impressions, clicks, ctr):
        """
        Add a digital inventory item.

        Args:
            ad_unit (str): Ad unit name (e.g. "homepage_billboard")
            description (str): Brief description of the ad unit
            impressions (int): Expected monthly impressions
            clicks (int): Expected monthly clicks
            ctr (float): Expected click-through rate (CTR)
        """
        self.inventory[ad_unit] = {
            "description": description,
            "impressions": impressions,
            "clicks": clicks,
            "ctr": ctr
        }

    def add_rate(self, ad_unit, rate_type, rate_value):
        """
        Add a rate to the rate matrix.

        Args:
            ad_unit (str): Ad unit name (e.g. "homepage_billboard")
            rate_type (str): Rate type (e.g. "cpm", "cpc")
            rate_value (float): Rate value
        """
        if ad_unit not in self.rate_matrix:
            self.rate_matrix[ad_unit] = {}
        self.rate_matrix[ad_unit][rate_type] = rate_value

    def get_inventory(self, ad_unit=None):
        """
        Get digital inventory.

        Args:
            ad_unit (str, optional): Ad unit name (e.g. "homepage_billboard"). Defaults to None.

        Returns:
            dict: Digital inventory
        """
        if ad_unit:
            return self.inventory.get(ad_unit)
        return self.inventory

    def get_rate(self, ad_unit, rate_type):
        """
        Get rate from the rate matrix.

        Args:
            ad_unit (str): Ad unit name (e.g. "homepage_billboard")
            rate_type (str): Rate type (e.g. "cpm", "cpc")

        Returns:
            float: Rate value
        """
        if ad_unit in self.rate_matrix and rate_type in self.rate_matrix[ad_unit]:
            return self.rate_matrix[ad_unit][rate_type]
        return None

    def calculate_revenue(self, ad_unit, impressions, rate_type):
        """
        Calculate revenue based on impressions and rate.

        Args:
            ad_unit (str): Ad unit name (e.g. "homepage_billboard")
            impressions (int): Impressions
            rate_type (str): Rate type (e.g. "cpm")

        Returns:
            float: Revenue
        """
        rate = self.get_rate(ad_unit, rate_type)
        if rate:
            if rate_type == "cpm":
                return (impressions / 1000) * rate
            elif rate_type == "cpc":
                # Assume a CTR of 0.1% for CPC calculation
                ctr = self.inventory[ad_unit]["ctr"]
                clicks = impressions * ctr / 100
                return clicks * rate
        return 0


def main():
    rate_card = DigitalRateCard()

    # Add digital inventory
    rate_card.add_inventory(
        "homepage_billboard",
        "Billboard on the homepage",
        1000000,
        5000,
        0.5
    )
    rate_card.add_inventory(
        "sidebar_banner",
        "Banner in the sidebar",
        500000,
        2000,
        0.4
    )

    # Add rates to the rate matrix
    rate_card.add_rate("homepage_billboard", "cpm", 10.0)
    rate_card.add_rate("homepage_billboard", "cpc", 2.0)
    rate_card.add_rate("sidebar_banner", "cpm", 8.0)
    rate_card.add_rate("sidebar_banner", "cpc", 1.5)

    # Print digital inventory
    print("Digital Inventory:")
    for ad_unit, details in rate_card.get_inventory().items():
        print(f"Ad Unit: {ad_unit}")
        print(f"Description: {details['description']}")
        print(f"Impressions: {details['impressions']}")
        print(f"Clicks: {details['clicks']}")
        print(f"CTR: {details['ctr']}%")
        print()

    # Print rate matrix
    print("Rate Matrix:")
    for ad_unit, rates in rate_card.rate_matrix.items():
        print(f"Ad Unit: {ad_unit}")
        for rate_type, rate_value in rates.items():
            print(f"{rate_type.upper()}: ${rate_value:.2f}")
        print()

    # Calculate revenue
    impressions = 1000000
    ad_unit = "homepage_billboard"
    rate_type = "cpm"
    revenue = rate_card.calculate_revenue(ad_unit, impressions, rate_type)
    print(f"Revenue for {ad_unit} at ${rate_card.get_rate(ad_unit, rate_type):.2f} {rate_type}: ${revenue:.2f}")


if __name__ == "__main__":
    main()
```
