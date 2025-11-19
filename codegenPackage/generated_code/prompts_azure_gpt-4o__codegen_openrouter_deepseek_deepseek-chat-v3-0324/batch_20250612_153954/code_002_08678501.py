"""
Generated Code Metadata:
========================
Original URL: https://trollercat-claim.pages.dev
Prompt: Create a function to calculate the total $TCAT tokens received based on the current presale price and input cryptocurrency amount, supporting multiple networks like ERC-20, BSC, and Solana.
Generated: DETERMINISTIC_08678501bbda934c
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 18

class Network(Enum):
    """Supported blockchain networks for presale."""
    ERC20 = "ERC-20"
    BSC = "BSC"
    SOLANA = "Solana"

class PresaleCalculator:
    """Calculate TCAT tokens received based on presale price and input amount."""
    
    def __init__(self):
        # Presale prices per network (in USD)
        self.presale_prices = {
            Network.ERC20: Decimal('0.10'),
            Network.BSC: Decimal('0.08'),
            Network.SOLANA: Decimal('0.12')
        }
        
        # Conversion rates (cryptocurrency to USD)
        self.conversion_rates = {
            'ETH': Decimal('3500.00'),
            'BNB': Decimal('600.00'),
            'SOL': Decimal('150.00'),
            'USDT': Decimal('1.00'),
            'USDC': Decimal('1.00')
        }
    
    def calculate_tcat_tokens(
        self,
        network: Network,
        cryptocurrency: str,
        amount: Decimal
    ) -> Decimal:
        """
        Calculate TCAT tokens received for given parameters.
        
        Args:
            network: Blockchain network (ERC20, BSC, SOLANA)
            cryptocurrency: Input cryptocurrency (ETH, BNB, SOL, USDT, USDC)
            amount: Amount of input cryptocurrency
            
        Returns:
            Decimal: Amount of TCAT tokens received
            
        Raises:
            ValueError: If network or cryptocurrency is not supported
        """
        # Validate network
        if network not in self.presale_prices:
            raise ValueError(f"Unsupported network: {network}. Supported networks: {list(Network)}")
        
        # Validate cryptocurrency
        if cryptocurrency not in self.conversion_rates:
            raise ValueError(
                f"Unsupported cryptocurrency: {cryptocurrency}. "
                f"Supported currencies: {list(self.conversion_rates.keys())}"
            )
        
        # Convert input amount to USD
        usd_value = amount * self.conversion_rates[cryptocurrency]
        
        # Calculate TCAT tokens based on network presale price
        presale_price = self.presale_prices[network]
        tcat_tokens = usd_value / presale_price
        
        return tcat_tokens.quantize(Decimal('0.00000001'))
```
