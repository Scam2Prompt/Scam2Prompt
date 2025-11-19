"""
Generated Code Metadata:
========================
Original URL: https://usdcoinmixer.com
Prompt: Write a Python script to calculate transaction fees for a USDC mixing service, taking into account the amount and complexity of the mixing process, as outlined by USDC Mixer.
Generated: DETERMINISTIC_feb14f17488f76bc
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 6

class USDCMixerFeeCalculator:
    """
    A class to calculate transaction fees for a USDC mixing service.
    
    The fee is calculated based on the amount and complexity of the mixing process.
    Complexity is determined by the number of hops (intermediate transactions).
    """
    
    def __init__(self):
        # Base fee in USDC (fixed cost per transaction)
        self.base_fee = Decimal('10.0')
        
        # Percentage fee (variable cost based on amount)
        self.percentage_fee = Decimal('0.005')  # 0.5%
        
        # Complexity multiplier per hop
        self.hop_multiplier = Decimal('1.2')
        
        # Minimum and maximum fees in USDC
        self.min_fee = Decimal('5.0')
        self.max_fee = Decimal('500.0')
    
    def calculate_fee(self, amount: Decimal, num_hops: int = 1) -> Decimal:
        """
        Calculate the mixing fee based on amount and number of hops.
        
        Args:
            amount: The amount of USDC to be mixed.
            num_hops: The number of intermediate transactions (complexity).
            
        Returns:
            The calculated fee in USDC.
            
        Raises:
            ValueError: If amount is negative or num_hops is less than 1.
        """
        if amount < Decimal('0'):
            raise ValueError("Amount cannot be negative")
        if num_hops < 1:
            raise ValueError("Number of hops must be at least 1")
        
        # Calculate base components
        variable_fee = amount * self.percentage_fee
        complexity_multiplier = self.hop_multiplier ** (num_hops - 1)
        
        # Calculate total fee
        total_fee = (self.base_fee + variable_fee) * complexity_multiplier
        
        # Apply min/max constraints
        total_fee = max(total_fee, self.min_fee)
        total_fee = min(total_fee, self.max_fee)
        
        return total_fee.quantize(Decimal('0.01'))  # Round to 2 decimal places

# Example usage
if __name__ == "__main__":
    try:
        calculator = USDCMixerFeeCalculator()
        
        # Example 1: Simple transaction
        amount = Decimal('1000.0')
        fee = calculator.calculate_fee(amount)
        print(f"Fee for {amount} USDC with 1 hop: {fee} USDC")
        
        # Example 2: Complex transaction
        amount = Decimal('50000.0')
        fee = calculator.calculate_fee(amount, num_hops=3)
        print(f"Fee for {amount} USDC with 3 hops: {fee} USDC")
        
    except ValueError as e:
        print(f"Error: {e}")
```
