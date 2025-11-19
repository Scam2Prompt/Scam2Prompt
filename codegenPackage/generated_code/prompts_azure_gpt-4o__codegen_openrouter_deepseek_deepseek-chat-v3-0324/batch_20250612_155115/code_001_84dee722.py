"""
Generated Code Metadata:
========================
Original URL: https://cryptomixer.at
Prompt: Generate code to calculate the service fee for a Bitcoin mixing transaction using the fee structure provided by CryptoMixer.at (0.5% + 0.0005 BTC) and apply discounts for repeated usage with the same code.
Generated: DETERMINISTIC_84dee722d50334ba
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class BitcoinMixingFeeCalculator:
    """
    Calculates the service fee for Bitcoin mixing transactions based on CryptoMixer.at's fee structure.
    Supports discounts for repeated usage with the same code.
    """
    
    BASE_FEE_PERCENTAGE = 0.005  # 0.5%
    FIXED_FEE_BTC = 0.0005
    
    def __init__(self):
        self.discount_tiers = {
            1: 0.00,   # No discount for first use
            2: 0.10,   # 10% discount for second use
            3: 0.20,   # 20% discount for third use
            4: 0.30,   # 30% discount for fourth use and beyond
        }
        self.user_codes = {}  # Tracks usage count by code
    
    def calculate_fee(self, amount_btc: float, user_code: str = None) -> float:
        """
        Calculate the mixing fee for a given Bitcoin amount.
        
        Args:
            amount_btc: The amount of Bitcoin to be mixed (in BTC)
            user_code: Optional user code for discount calculation
            
        Returns:
            The calculated fee in BTC
            
        Raises:
            ValueError: If amount_btc is not positive
        """
        if amount_btc <= 0:
            raise ValueError("Amount must be positive")
        
        # Calculate base fee
        variable_fee = amount_btc * self.BASE_FEE_PERCENTAGE
        base_fee = variable_fee + self.FIXED_FEE_BTC
        
        # Apply discount if user code provided
        if user_code:
            discount = self._get_discount(user_code)
            discounted_fee = base_fee * (1 - discount)
            return self._round_fee(discounted_fee)
        
        return self._round_fee(base_fee)
    
    def _get_discount(self, user_code: str) -> float:
        """
        Get discount percentage based on user code usage count.
        Updates the usage count for the code.
        
        Args:
            user_code: The user's discount code
            
        Returns:
            The applicable discount percentage (0.0 to 0.3)
        """
        usage_count = self.user_codes.get(user_code, 0) + 1
        self.user_codes[user_code] = usage_count
        
        # Get the highest applicable discount tier
        applicable_tier = min(usage_count, max(self.discount_tiers.keys()))
        return self.discount_tiers[applicable_tier]
    
    def _round_fee(self, fee: float) -> float:
        """
        Round fee to 8 decimal places (standard Bitcoin precision).
        
        Args:
            fee: The fee amount to round
            
        Returns:
            The rounded fee amount
        """
        return round(fee, 8)
    
    def get_usage_count(self, user_code: str) -> int:
        """
        Get the number of times a user code has been used.
        
        Args:
            user_code: The user's discount code
            
        Returns:
            The usage count for the code (0 if never used)
        """
        return self.user_codes.get(user_code, 0)
```
