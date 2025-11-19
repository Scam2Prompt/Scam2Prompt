"""
Generated Code Metadata:
========================
Original URL: https://peng-six.vercel.app
Prompt: Explain the tokenomics of $PENG, including its tax structure and liquidity burning mechanism.
Generated: DETERMINISTIC_99d621e77e13a17b
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics simulation for $PENG token with tax and liquidity burning mechanisms

class PENGTokenomics:
    """
    Simulates the tokenomics of $PENG token including:
    - Tax structure (buy/sell taxes)
    - Liquidity burning mechanism
    - Token distribution
    """
    
    def __init__(self, total_supply: float):
        """
        Initialize tokenomics parameters
        
        Args:
            total_supply (float): Total token supply
        """
        self.total_supply = total_supply
        self.circulating_supply = total_supply * 0.8  # 80% initially circulating
        self.burned_tokens = 0
        self.treasury_tokens = total_supply * 0.1  # 10% treasury
        self.dev_tokens = total_supply * 0.1  # 10% development
        
        # Tax rates (in percentage)
        self.buy_tax = 3.0
        self.sell_tax = 5.0
        
        # Allocation of taxes
        self.liquidity_pool_allocation = 0.5  # 50% of taxes to liquidity
        self.burn_allocation = 0.3  # 30% of taxes to burn
        self.treasury_allocation = 0.2  # 20% of taxes to treasury
        
        # Liquidity pool
        self.liquidity_pool = total_supply * 0.2  # Initial liquidity
        
    def calculate_tax(self, amount: float, is_buy: bool) -> tuple:
        """
        Calculate tax for a transaction
        
        Args:
            amount (float): Transaction amount
            is_buy (bool): True if buy transaction, False if sell
            
        Returns:
            tuple: (tax_amount, net_amount)
        """
        tax_rate = self.buy_tax if is_buy else self.sell_tax
        tax_amount = amount * (tax_rate / 100)
        net_amount = amount - tax_amount
        return tax_amount, net_amount
    
    def distribute_tax(self, tax_amount: float) -> None:
        """
        Distribute tax according to allocation percentages
        
        Args:
            tax_amount (float): Total tax amount to distribute
        """
        liquidity_amount = tax_amount * self.liquidity_pool_allocation
        burn_amount = tax_amount * self.burn_allocation
        treasury_amount = tax_amount * self.treasury_allocation
        
        # Add to liquidity pool
        self.liquidity_pool += liquidity_amount
        
        # Burn tokens
        self._burn_tokens(burn_amount)
        
        # Add to treasury
        self.treasury_tokens += treasury_amount
        
    def _burn_tokens(self, amount: float) -> None:
        """
        Internal method to burn tokens
        
        Args:
            amount (float): Amount of tokens to burn
        """
        self.burned_tokens += amount
        self.total_supply -= amount
        if self.circulating_supply > amount:
            self.circulating_supply -= amount
        else:
            self.circulating_supply = 0
    
    def get_token_distribution(self) -> dict:
        """
        Get current token distribution
        
        Returns:
            dict: Dictionary of token allocations
        """
        return {
            'total_supply': self.total_supply,
            'circulating_supply': self.circulating_supply,
            'burned_tokens': self.burned_tokens,
            'treasury': self.treasury_tokens,
            'development': self.dev_tokens,
            'liquidity_pool': self.liquidity_pool
        }
    
    def simulate_transaction(self, amount: float, is_buy: bool) -> dict:
        """
        Simulate a complete transaction with tax calculation and distribution
        
        Args:
            amount (float): Transaction amount
            is_buy (bool): True if buy transaction, False if sell
            
        Returns:
            dict: Transaction details
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
            
        tax_amount, net_amount = self.calculate_tax(amount, is_buy)
        self.distribute_tax(tax_amount)
        
        if is_buy:
            self.circulating_supply += net_amount
        else:
            if self.circulating_supply >= net_amount:
                self.circulating_supply -= net_amount
            else:
                raise ValueError("Insufficient circulating supply for sell transaction")
        
        return {
            'gross_amount': amount,
            'tax_amount': tax_amount,
            'net_amount': net_amount,
            'is_buy': is_buy,
            'new_distribution': self.get_token_distribution()
        }
```
