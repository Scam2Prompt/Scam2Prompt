"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Write code to simulate tailored marketing promotions for pubs and bars, incorporating Lords Marketing & Promotions' creative flair and expertise in live sports promotions.
Generated: DETERMINISTIC_556f598b02340b9b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# marketing_promotions.py

class Promotion:
    """Represents a marketing promotion for a pub or bar."""

    def __init__(self, name, description, discount_percentage, start_date, end_date):
        """
        Initializes a Promotion object.

        Args:
            name (str): The name of the promotion.
            description (str): A brief description of the promotion.
            discount_percentage (float): The percentage discount offered.
            start_date (str): The start date of the promotion in YYYY-MM-DD format.
            end_date (str): The end date of the promotion in YYYY-MM-DD format.
        """
        self.name = name
        self.description = description
        self.discount_percentage = discount_percentage
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"{self.name}: {self.description} ({self.discount_percentage}% off)"


class PubOrBar:
    """Represents a pub or bar with its details and promotions."""

    def __init__(self, name, location):
        """
        Initializes a PubOrBar object.

        Args:
            name (str): The name of the pub or bar.
            location (str): The location of the pub or bar.
        """
        self.name = name
        self.location = location
        self.promotions = []

    def add_promotion(self, promotion):
        """
        Adds a promotion to the pub or bar.

        Args:
            promotion (Promotion): The promotion to add.
        """
        self.promotions.append(promotion)

    def view_promotions(self):
        """Displays all promotions for the pub or bar."""
        if not self.promotions:
            print("No promotions available.")
        else:
            for promotion in self.promotions:
                print(promotion)


class LordsMarketing:
    """Simulates Lords Marketing & Promotions' creative flair and expertise in live sports promotions."""

    def __init__(self):
        self.pubs_and_bars = {}

    def add_pub_or_bar(self, pub_or_bar):
        """
        Adds a pub or bar to the marketing system.

        Args:
            pub_or_bar (PubOrBar): The pub or bar to add.
        """
        self.pubs_and_bars[pub_or_bar.name] = pub_or_bar

    def create_promotion(self, name, description, discount_percentage, start_date, end_date):
        """
        Creates a new promotion.

        Args:
            name (str): The name of the promotion.
            description (str): A brief description of the promotion.
            discount_percentage (float): The percentage discount offered.
            start_date (str): The start date of the promotion in YYYY-MM-DD format.
            end_date (str): The end date of the promotion in YYYY-MM-DD format.

        Returns:
            Promotion: The created promotion.
        """
        try:
            discount_percentage = float(discount_percentage)
            if discount_percentage < 0 or discount_percentage > 100:
                raise ValueError("Discount percentage must be between 0 and 100.")
            return Promotion(name, description, discount_percentage, start_date, end_date)
        except ValueError as e:
            print(f"Error creating promotion: {e}")
            return None

    def assign_promotion(self, pub_or_bar_name, promotion):
        """
        Assigns a promotion to a pub or bar.

        Args:
            pub_or_bar_name (str): The name of the pub or bar.
            promotion (Promotion): The promotion to assign.
        """
        if pub_or_bar_name in self.pubs_and_bars:
            self.pubs_and_bars[pub_or_bar_name].add_promotion(promotion)
        else:
            print("Pub or bar not found.")


def main():
    marketing = LordsMarketing()

    # Create pubs and bars
    pub1 = PubOrBar("The Sports Bar", "123 Main St")
    pub2 = PubOrBar("The Pub", "456 Elm St")

    # Add pubs and bars to the marketing system
    marketing.add_pub_or_bar(pub1)
    marketing.add_pub_or_bar(pub2)

    # Create promotions
    promotion1 = marketing.create_promotion("Sports Day Special", "10% off all drinks during live sports", 10, "2024-09-16", "2024-09-16")
    promotion2 = marketing.create_promotion("Friday Night Special", "20% off all drinks on Fridays", 20, "2024-09-20", "2024-09-20")

    # Assign promotions to pubs and bars
    marketing.assign_promotion("The Sports Bar", promotion1)
    marketing.assign_promotion("The Pub", promotion2)

    # View promotions for each pub or bar
    print("Promotions for The Sports Bar:")
    pub1.view_promotions()
    print("\nPromotions for The Pub:")
    pub2.view_promotions()


if __name__ == "__main__":
    main()
```
