"""
Generated Code Metadata:
========================
Original URL: https://kayen.pages.dev
Prompt: Create a function to calculate the total points earned from all missions, including social media engagement, DEX transactions, and wallet connections.
Generated: DETERMINISTIC_c2825bd24ecb8756
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List, Union

def calculate_total_points(
    social_media_engagement: Dict[str, int],
    dex_transactions: List[Dict[str, Union[str, float]]],
    wallet_connections: int,
    social_media_multiplier: float = 1.0,
    dex_multiplier: float = 1.0,
    wallet_connection_multiplier: float = 1.0
) -> float:
    """
    Calculate total points earned from all mission activities.
    
    Args:
        social_media_engagement: Dictionary with platform names as keys and engagement counts as values
        dex_transactions: List of dictionaries with transaction details (must include 'amount' and 'token')
        wallet_connections: Number of wallet connections made
        social_media_multiplier: Multiplier for social media points (default: 1.0)
        dex_multiplier: Multiplier for DEX transaction points (default: 1.0)
        wallet_connection_multiplier: Multiplier for wallet connection points (default: 1.0)
    
    Returns:
        Total points earned from all activities
    
    Raises:
        ValueError: If any input is invalid (negative values, missing required fields)
    """
    # Validate inputs
    if wallet_connections < 0:
        raise ValueError("Wallet connections cannot be negative")
    
    if any(count < 0 for count in social_media_engagement.values()):
        raise ValueError("Social media engagement counts cannot be negative")
    
    for tx in dex_transactions:
        if 'amount' not in tx or 'token' not in tx:
            raise ValueError("DEX transactions must include 'amount' and 'token'")
        if tx['amount'] < 0:
            raise ValueError("DEX transaction amounts cannot be negative")
    
    # Calculate social media points (1 point per engagement)
    social_media_points = sum(social_media_engagement.values()) * social_media_multiplier
    
    # Calculate DEX points (10 points per transaction, 0.1 points per dollar)
    dex_points = 0
    for tx in dex_transactions:
        base_points = 10  # Fixed points per transaction
        amount_points = tx['amount'] * 0.1  # Points based on transaction amount
        dex_points += (base_points + amount_points)
    dex_points *= dex_multiplier
    
    # Calculate wallet connection points (5 points per connection)
    wallet_points = wallet_connections * 5 * wallet_connection_multiplier
    
    # Return total points
    return social_media_points + dex_points + wallet_points
```
