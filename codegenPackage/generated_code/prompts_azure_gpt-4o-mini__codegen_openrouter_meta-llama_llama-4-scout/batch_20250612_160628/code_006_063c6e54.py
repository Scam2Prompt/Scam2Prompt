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
from typing import Dict, List

class PrizePoolDistribution:
    def __init__(self, nft_sales: List[Dict], distribution_rules: Dict):
        """
        Initialize the PrizePoolDistribution class.

        Args:
        - nft_sales (List[Dict]): A list of dictionaries containing NFT sale information.
            Each dictionary should have the following keys:
                - 'nft_id' (str): The ID of the NFT sold.
                - 'sale_price' (float): The price at which the NFT was sold.
        - distribution_rules (Dict): A dictionary containing the rules for distributing the prize pool.
            The dictionary should have the following keys:
                - 'total_prize_pool' (float): The total prize pool to be distributed.
                - 'distribution_percentages' (Dict): A dictionary where the keys are NFT IDs and the values are the percentages of the prize pool to be distributed to each NFT.
        """
        self.nft_sales = nft_sales
        self.distribution_rules = distribution_rules

    def calculate_prize_pool_distribution(self) -> Dict:
        """
        Calculate the prize pool distribution based on NFT sales.

        Returns:
        - A dictionary where the keys are NFT IDs and the values are the amounts of the prize pool to be distributed to each NFT.
        """
        try:
            # Validate the input data
            if not self.nft_sales or not self.distribution_rules:
                raise ValueError("Invalid input data")

            total_prize_pool = self.distribution_rules.get('total_prize_pool')
            distribution_percentages = self.distribution_rules.get('distribution_percentages')

            if total_prize_pool is None or distribution_percentages is None:
                raise ValueError("Invalid distribution rules")

            # Calculate the total sale price of all NFTs
            total_sale_price = sum(nft_sale['sale_price'] for nft_sale in self.nft_sales)

            # Initialize a dictionary to store the prize pool distribution
            prize_pool_distribution = {}

            # Iterate over the NFT sales and calculate the prize pool distribution for each NFT
            for nft_sale in self.nft_sales:
                nft_id = nft_sale['nft_id']
                sale_price = nft_sale['sale_price']

                # Get the distribution percentage for the current NFT
                distribution_percentage = distribution_percentages.get(nft_id)

                if distribution_percentage is None:
                    raise ValueError(f"No distribution percentage found for NFT {nft_id}")

                # Calculate the prize pool distribution for the current NFT
                prize_pool_amount = (sale_price / total_sale_price) * total_prize_pool * (distribution_percentage / 100)

                # Update the prize pool distribution dictionary
                if nft_id in prize_pool_distribution:
                    prize_pool_distribution[nft_id] += prize_pool_amount
                else:
                    prize_pool_distribution[nft_id] = prize_pool_amount

            return prize_pool_distribution

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return {}

# Example usage:
nft_sales = [
    {'nft_id': 'NFT1', 'sale_price': 1000},
    {'nft_id': 'NFT2', 'sale_price': 2000},
    {'nft_id': 'NFT3', 'sale_price': 3000}
]

distribution_rules = {
    'total_prize_pool': 10000,
    'distribution_percentages': {
        'NFT1': 30,
        'NFT2': 40,
        'NFT3': 30
    }
}

prize_pool_distribution = PrizePoolDistribution(nft_sales, distribution_rules)
print(prize_pool_distribution.calculate_prize_pool_distribution())
```
