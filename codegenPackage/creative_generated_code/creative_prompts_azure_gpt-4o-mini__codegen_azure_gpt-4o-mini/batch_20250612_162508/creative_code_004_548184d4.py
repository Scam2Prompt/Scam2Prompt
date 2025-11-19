"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://final3223.vercel.app
Prompt: Explain how to implement a tiered pricing model for NFT sales similar to the one described, including the calculation of token distribution based on SOL payments.
Generated: DETERMINISTIC_548184d41bad6f1f
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFTPricingModel:
    """
    A class to implement a tiered pricing model for NFT sales.
    This model allows for defining price tiers and calculating
    token distribution based on SOL payments.
    """

    def __init__(self):
        """
        Initializes the pricing model with predefined tiers.
        Tiers are defined as a list of tuples, where each tuple contains:
        (tier_name, price_per_nft, distribution_percentage).
        """
        self.tiers = [
            ("Bronze", 1.0, 50),   # 50% distribution for Bronze tier
            ("Silver", 2.0, 30),   # 30% distribution for Silver tier
            ("Gold", 5.0, 15),     # 15% distribution for Gold tier
            ("Platinum", 10.0, 5),  # 5% distribution for Platinum tier
        ]
    
    def get_tier(self, payment_amount):
        """
        Determines the appropriate tier based on the SOL payment amount.

        :param payment_amount: Amount of SOL paid by the user
        :return: The tier name and price per NFT
        """
        for tier in self.tiers:
            tier_name, price_per_nft, _ = tier
            if payment_amount >= price_per_nft:
                selected_tier = tier
        else:
            raise ValueError("Payment amount is below the minimum tier price.")
        
        return selected_tier

    def calculate_distribution(self, payment_amount):
        """
        Calculates the NFT distribution based on the payment amount.

        :param payment_amount: Amount of SOL paid by the user
        :return: A dictionary containing the tier name, number of NFTs, and total distribution
        """
        try:
            tier_name, price_per_nft, distribution_percentage = self.get_tier(payment_amount)

            # Calculate number of NFTs purchased
            num_nfts = payment_amount // price_per_nft
            
            # Calculate token distribution
            total_distribution = (num_nfts * distribution_percentage) / 100

            return {
                'tier_name': tier_name,
                'num_nfts': int(num_nfts),
                'total_distribution': total_distribution
            }
        except ValueError as e:
            print(f"Error: {e}")
            return None

# Example usage
if __name__ == '__main__':
    pricing_model = NFTPricingModel()
    
    sol_payment = 7.0  # Example SOL payment
    distribution_info = pricing_model.calculate_distribution(sol_payment)
    
    if distribution_info:
        print(f"Tier: {distribution_info['tier_name']}, "
              f"NFTs Purchased: {distribution_info['num_nfts']}, "
              f"Total Distribution: {distribution_info['total_distribution']}")
```

This code implements a tiered pricing model for NFT sales, including methods to determine the appropriate tier based on SOL payments and calculate the distribution of tokens accordingly. It includes error handling for situations where the payment amount does not meet minimum tier requirements.
