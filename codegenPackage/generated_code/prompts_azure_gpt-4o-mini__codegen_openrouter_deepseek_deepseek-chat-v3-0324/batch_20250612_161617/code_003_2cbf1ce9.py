"""
Generated Code Metadata:
========================
Original URL: https://newmoly.pages.dev
Prompt: Generate code to calculate the fees associated with buying and selling $Molly tokens based on the provided fee structure.
Generated: DETERMINISTIC_2cbf1ce9362452be
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MollyTokenFeeCalculator:
    """
    A class to calculate the fees associated with buying and selling $Molly tokens.
    """
    
    def __init__(self):
        """
        Initialize the fee structure for $Molly tokens.
        """
        self.buy_fee_percentage = 0.01  # 1% fee for buying
        self.sell_fee_percentage = 0.02  # 2% fee for selling
        self.min_fee = 0.01  # Minimum fee in $Molly tokens
        self.max_fee = 100.0  # Maximum fee in $Molly tokens
    
    def calculate_buy_fee(self, amount: float) -> float:
        """
        Calculate the fee for buying $Molly tokens.
        
        Args:
            amount (float): The amount of $Molly tokens to buy.
            
        Returns:
            float: The calculated fee.
            
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        
        fee = amount * self.buy_fee_percentage
        return self._apply_fee_limits(fee)
    
    def calculate_sell_fee(self, amount: float) -> float:
        """
        Calculate the fee for selling $Molly tokens.
        
        Args:
            amount (float): The amount of $Molly tokens to sell.
            
        Returns:
            float: The calculated fee.
            
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        
        fee = amount * self.sell_fee_percentage
        return self._apply_fee_limits(fee)
    
    def _apply_fee_limits(self, fee: float) -> float:
        """
        Apply minimum and maximum fee limits.
        
        Args:
            fee (float): The calculated fee before limits.
            
        Returns:
            float: The fee after applying limits.
        """
        if fee < self.min_fee:
            return self.min_fee
        elif fee > self.max_fee:
            return self.max_fee
        else:
            return fee


# Example usage
if __name__ == "__main__":
    calculator = MollyTokenFeeCalculator()
    
    try:
        buy_amount = 500.0
        buy_fee = calculator.calculate_buy_fee(buy_amount)
        print(f"Buy fee for {buy_amount} $Molly: {buy_fee}")
        
        sell_amount = 300.0
        sell_fee = calculator.calculate_sell_fee(sell_amount)
        print(f"Sell fee for {sell_amount} $Molly: {sell_fee}")
        
        # Test with negative amount
        # calculator.calculate_buy_fee(-100.0)
    except ValueError as e:
        print(f"Error: {e}")
```
