"""
Generated Code Metadata:
========================
Original URL: https://cybro-en.pages.dev
Prompt: Write a function to calculate discounted trading and lending fees based on CYBRO token tiers, using the tokenomics data provided.
Generated: DETERMINISTIC_0e628051805b6337
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CYBROFeeCalculator:
    """
    A class to calculate discounted trading and lending fees based on CYBRO token tiers.
    
    Attributes:
        TIERS (dict): A dictionary mapping CYBRO token holding amounts to their respective tiers.
        BASE_TRADING_FEE (float): The base trading fee percentage before discounts.
        BASE_LENDING_FEE (float): The base lending fee percentage before discounts.
        TRADING_FEE_DISCOUNTS (dict): Discounts applied to trading fees per tier.
        LENDING_FEE_DISCOUNTS (dict): Discounts applied to lending fees per tier.
    """
    
    TIERS = {
        'Bronze': 1000,      # 1,000 CYBRO tokens
        'Silver': 5000,      # 5,000 CYBRO tokens
        'Gold': 10000,       # 10,000 CYBRO tokens
        'Platinum': 50000,   # 50,000 CYBRO tokens
        'Diamond': 100000    # 100,000 CYBRO tokens
    }
    
    BASE_TRADING_FEE = 0.002  # 0.2%
    BASE_LENDING_FEE = 0.001  # 0.1%
    
    TRADING_FEE_DISCOUNTS = {
        'Bronze': 0.10,      # 10% discount
        'Silver': 0.20,      # 20% discount
        'Gold': 0.30,        # 30% discount
        'Platinum': 0.40,    # 40% discount
        'Diamond': 0.50      # 50% discount
    }
    
    LENDING_FEE_DISCOUNTS = {
        'Bronze': 0.15,      # 15% discount
        'Silver': 0.25,      # 25% discount
        'Gold': 0.35,        # 35% discount
        'Platinum': 0.45,    # 45% discount
        'Diamond': 0.55      # 55% discount
    }
    
    @staticmethod
    def get_tier(token_amount):
        """
        Determine the user's tier based on their CYBRO token holdings.
        
        Args:
            token_amount (int): The number of CYBRO tokens held by the user.
            
        Returns:
            str: The tier name ('No Tier', 'Bronze', 'Silver', etc.)
        """
        if token_amount < CYBROFeeCalculator.TIERS['Bronze']:
            return 'No Tier'
        elif token_amount < CYBROFeeCalculator.TIERS['Silver']:
            return 'Bronze'
        elif token_amount < CYBROFeeCalculator.TIERS['Gold']:
            return 'Silver'
        elif token_amount < CYBROFeeCalculator.TIERS['Platinum']:
            return 'Gold'
        elif token_amount < CYBROFeeCalculator.TIERS['Diamond']:
            return 'Platinum'
        else:
            return 'Diamond'
    
    @staticmethod
    def calculate_trading_fee(token_amount, trade_amount):
        """
        Calculate the discounted trading fee based on the user's tier.
        
        Args:
            token_amount (int): The number of CYBRO tokens held by the user.
            trade_amount (float): The amount being traded.
            
        Returns:
            float: The discounted trading fee amount.
            
        Raises:
            ValueError: If token_amount or trade_amount is negative.
        """
        if token_amount < 0 or trade_amount < 0:
            raise ValueError("Token amount and trade amount must be non-negative")
            
        tier = CYBROFeeCalculator.get_tier(token_amount)
        if tier == 'No Tier':
            return trade_amount * CYBROFeeCalculator.BASE_TRADING_FEE
        
        discount = CYBROFeeCalculator.TRADING_FEE_DISCOUNTS[tier]
        discounted_fee = CYBROFeeCalculator.BASE_TRADING_FEE * (1 - discount)
        return trade_amount * discounted_fee
    
    @staticmethod
    def calculate_lending_fee(token_amount, loan_amount):
        """
        Calculate the discounted lending fee based on the user's tier.
        
        Args:
            token_amount (int): The number of CYBRO tokens held by the user.
            loan_amount (float): The amount being lent.
            
        Returns:
            float: The discounted lending fee amount.
            
        Raises:
            ValueError: If token_amount or loan_amount is negative.
        """
        if token_amount < 0 or loan_amount < 0:
            raise ValueError("Token amount and loan amount must be non-negative")
            
        tier = CYBROFeeCalculator.get_tier(token_amount)
        if tier == 'No Tier':
            return loan_amount * CYBROFeeCalculator.BASE_LENDING_FEE
        
        discount = CYBROFeeCalculator.LENDING_FEE_DISCOUNTS[tier]
        discounted_fee = CYBROFeeCalculator.BASE_LENDING_FEE * (1 - discount)
        return loan_amount * discounted_fee
```
