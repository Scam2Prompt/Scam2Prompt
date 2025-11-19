"""
Generated Code Metadata:
========================
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Generate Python code to calculate token distribution for a presale model where 0.1 BASE equals 99,500 tokens, and implement tiered pricing for purchases of 25, 50, 100, 150, and 200 BASE.
Generated: DETERMINISTIC_c875179a85393477
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenDistribution:
    def __init__(self):
        # Base token conversion rate
        self.base_to_tokens_rate = 995000 / 0.1  # 0.1 BASE equals 99,500 tokens
        # Tiered pricing structure
        self.tiered_pricing = {
            25: 0.1,
            50: 0.2,
            100: 0.4,
            150: 0.6,
            200: 0.8
        }

    def calculate_tokens(self, base_amount):
        """
        Calculate the number of tokens based on the amount of BASE provided.
        
        :param base_amount: The amount of BASE to convert to tokens.
        :return: The number of tokens corresponding to the BASE amount.
        :raises ValueError: If the base_amount is not a positive number.
        """
        if base_amount <= 0:
            raise ValueError("Base amount must be a positive number.")
        
        # Calculate tokens based on the conversion rate
        tokens = base_amount * self.base_to_tokens_rate
        return tokens

    def get_price_for_tier(self, base_amount):
        """
        Get the price in BASE for a given tier.
        
        :param base_amount: The amount of BASE to check against the tiered pricing.
        :return: The price in BASE for the specified tier.
        :raises ValueError: If the base_amount is not in the defined tiers.
        """
        if base_amount not in self.tiered_pricing:
            raise ValueError("Base amount must be one of the defined tiers: {}".format(list(self.tiered_pricing.keys())))
        
        return self.tiered_pricing[base_amount]

    def purchase_tokens(self, base_amount):
        """
        Process a purchase of tokens based on the amount of BASE provided.
        
        :param base_amount: The amount of BASE to purchase tokens with.
        :return: A dictionary containing the base amount, token amount, and price tier.
        :raises ValueError: If the base_amount is not a positive number or not in the defined tiers.
        """
        # Get the price for the specified tier
        price_per_base = self.get_price_for_tier(base_amount)
        
        # Calculate the total tokens for the given base amount
        tokens = self.calculate_tokens(price_per_base)
        
        return {
            "base_amount": price_per_base,
            "tokens": tokens,
            "tier": base_amount
        }


# Example usage
if __name__ == "__main__":
    token_distribution = TokenDistribution()
    
    try:
        # Example purchase of 100 BASE
        purchase_info = token_distribution.purchase_tokens(100)
        print("Purchase Info:", purchase_info)
    except ValueError as e:
        print("Error:", e)
```
