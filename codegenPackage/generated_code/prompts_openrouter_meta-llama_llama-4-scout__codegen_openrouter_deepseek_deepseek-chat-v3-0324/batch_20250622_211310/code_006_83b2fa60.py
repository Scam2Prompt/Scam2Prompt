"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.nl
Prompt: Develop a Python function to categorize investment types (e.g., cryptocurrencies, Forex, stocks) and provide a brief description for each, based on Immediate Peak's educational content.
Generated: DETERMINISTIC_83b2fa607d5d91b7
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, Tuple

def categorize_investment_type(investment: str) -> Dict[str, Tuple[str, str]]:
    """
    Categorizes the given investment type and provides a brief description based on Immediate Peak's educational content.
    
    Args:
        investment (str): The investment type to categorize (e.g., 'cryptocurrencies', 'Forex', 'stocks').
        
    Returns:
        Dict[str, Tuple[str, str]]: A dictionary with keys 'category' and 'description', where:
            - 'category' is the broad category of the investment.
            - 'description' is a brief explanation of the investment type.
            
    Raises:
        ValueError: If the investment type is not recognized.
    """
    investment_types = {
        'cryptocurrencies': (
            'Digital Assets',
            'Decentralized digital currencies that use cryptography for security and operate on blockchain technology.'
        ),
        'Forex': (
            'Currency Trading',
            'The trading of currencies on the foreign exchange market, aiming to profit from exchange rate fluctuations.'
        ),
        'stocks': (
            'Equities',
            'Shares representing ownership in a company, traded on stock exchanges to capitalize on company growth.'
        ),
        'commodities': (
            'Physical Goods',
            'Raw materials or primary agricultural products traded on commodities markets, such as gold or oil.'
        ),
        'bonds': (
            'Fixed Income',
            'Debt securities issued by governments or corporations, providing periodic interest payments.'
        ),
        'etfs': (
            'Funds',
            'Exchange-Traded Funds that track indices, commodities, or baskets of assets, offering diversification.'
        )
    }
    
    investment = investment.lower()
    if investment not in investment_types:
        raise ValueError(f"Unknown investment type: {investment}. Supported types are: {list(investment_types.keys())}")
    
    category, description = investment_types[investment]
    return {
        'category': category,
        'description': description
    }
```
