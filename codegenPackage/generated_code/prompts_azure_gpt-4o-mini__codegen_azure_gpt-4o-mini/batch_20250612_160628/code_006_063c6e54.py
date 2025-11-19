"""
Generated Code Metadata:
========================
Original URL: https://presale-artyfact.pages.dev
Prompt: Develop a method to calculate the prize pool distribution for Artyfact's Play-and-Earn games based on NFT sales.
Generated: DETERMINISTIC_063c6e5461f45e37
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PrizePoolDistributor:
    """
    A class to calculate the prize pool distribution for Artyfact's Play-and-Earn games
    based on NFT sales.
    """

    def __init__(self, total_sales: float, distribution_percentages: dict):
        """
        Initializes the PrizePoolDistributor with total sales and distribution percentages.

        :param total_sales: Total amount of NFT sales (float).
        :param distribution_percentages: A dictionary with keys as prize categories and values as percentages (dict).
        """
        self.total_sales = total_sales
        self.distribution_percentages = distribution_percentages

    def validate_distribution(self):
        """
        Validates that the distribution percentages sum up to 100%.

        :raises ValueError: If the total percentage is not equal to 100.
        """
        total_percentage = sum(self.distribution_percentages.values())
        if total_percentage != 100:
            raise ValueError("Distribution percentages must sum up to 100%. Current total: {}".format(total_percentage))

    def calculate_distribution(self) -> dict:
        """
        Calculates the prize pool distribution based on the total sales and distribution percentages.

        :return: A dictionary with prize categories and their corresponding amounts (dict).
        :raises ValueError: If total sales is negative or distribution percentages are invalid.
        """
        if self.total_sales < 0:
            raise ValueError("Total sales cannot be negative.")

        self.validate_distribution()

        distribution = {}
        for category, percentage in self.distribution_percentages.items():
            distribution[category] = (percentage / 100) * self.total_sales

        return distribution


# Example usage
if __name__ == "__main__":
    try:
        total_nft_sales = 100000.0  # Example total sales amount
        distribution_percentages = {
            "First Prize": 50,
            "Second Prize": 30,
            "Third Prize": 20
        }

        distributor = PrizePoolDistributor(total_nft_sales, distribution_percentages)
        prize_distribution = distributor.calculate_distribution()
        print("Prize Pool Distribution:", prize_distribution)

    except ValueError as e:
        print("Error:", e)
```
