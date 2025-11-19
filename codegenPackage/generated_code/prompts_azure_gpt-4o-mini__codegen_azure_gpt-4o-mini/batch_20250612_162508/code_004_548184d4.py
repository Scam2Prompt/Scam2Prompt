"""
Generated Code Metadata:
========================
Original URL: https://final3223.vercel.app
Prompt: Explain how to implement a tiered pricing model for NFT sales similar to the one described, including the calculation of token distribution based on SOL payments.
Generated: DETERMINISTIC_548184d41bad6f1f
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NFTMarketplace:
    def __init__(self):
        # Initialize the tiered pricing model with predefined tiers
        self.tiers = {
            "Bronze": {"price": 1.0, "supply": 100},
            "Silver": {"price": 2.0, "supply": 50},
            "Gold": {"price": 5.0, "supply": 20},
            "Platinum": {"price": 10.0, "supply": 10},
        }
        self.sold_nfts = {tier: 0 for tier in self.tiers}

    def calculate_distribution(self, payment_amount):
        """
        Calculate the distribution of NFTs based on the payment amount in SOL.
        
        Args:
            payment_amount (float): The amount paid in SOL.
        
        Returns:
            dict: A dictionary with the number of NFTs purchased from each tier.
        """
        distribution = {tier: 0 for tier in self.tiers}
        remaining_payment = payment_amount

        # Iterate through each tier to allocate NFTs based on the payment
        for tier, details in self.tiers.items():
            price = details["price"]
            available_supply = details["supply"] - self.sold_nfts[tier]

            # Calculate how many NFTs can be bought from the current tier
            if remaining_payment >= price and available_supply > 0:
                nfts_to_buy = min(available_supply, int(remaining_payment // price))
                distribution[tier] = nfts_to_buy
                remaining_payment -= nfts_to_buy * price

        return distribution

    def purchase_nfts(self, payment_amount):
        """
        Process the purchase of NFTs based on the payment amount.
        
        Args:
            payment_amount (float): The amount paid in SOL.
        
        Returns:
            dict: A dictionary with the number of NFTs purchased from each tier.
        
        Raises:
            ValueError: If the payment amount is less than or equal to zero.
        """
        if payment_amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")

        distribution = self.calculate_distribution(payment_amount)

        # Update the sold NFTs count based on the distribution
        for tier, count in distribution.items():
            self.sold_nfts[tier] += count

        return distribution

# Example usage
if __name__ == "__main__":
    marketplace = NFTMarketplace()
    
    try:
        payment = 15.0  # Example payment in SOL
        purchased_nfts = marketplace.purchase_nfts(payment)
        print("NFTs purchased distribution:", purchased_nfts)
    except ValueError as e:
        print(f"Error: {e}")
```
