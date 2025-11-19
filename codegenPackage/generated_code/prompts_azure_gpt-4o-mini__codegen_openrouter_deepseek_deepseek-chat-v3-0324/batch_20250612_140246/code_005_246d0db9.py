"""
Generated Code Metadata:
========================
Original URL: https://arbius-en.pages.dev
Prompt: Create a function that calculates the task fee based on the economic rules of the Arbius token supply and reward structure.
Generated: DETERMINISTIC_246d0db938a8d1c3
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_task_fee(
    current_supply: float,
    initial_supply: float = 1_000_000.0,
    base_fee: float = 0.01,
    fee_exponent: float = 2.0,
    max_fee: float = 100.0
) -> float:
    """
    Calculate the task fee based on the Arbius token economic rules.
    
    The fee follows a power law based on the current supply relative to initial supply.
    
    Args:
        current_supply: Current circulating supply of Arbius tokens
        initial_supply: Initial supply of Arbius tokens (default: 1,000,000)
        base_fee: Base fee in Arbius tokens (default: 0.01)
        fee_exponent: Exponent for fee calculation (default: 2.0)
        max_fee: Maximum fee cap in Arbius tokens (default: 100.0)
    
    Returns:
        Calculated task fee in Arbius tokens
    
    Raises:
        ValueError: If any numeric parameter is negative
    """
    # Validate inputs
    if any(x < 0 for x in (current_supply, initial_supply, base_fee, fee_exponent, max_fee)):
        raise ValueError("All parameters must be non-negative")
    
    if initial_supply == 0:
        raise ValueError("Initial supply cannot be zero")
    
    # Calculate the supply ratio
    supply_ratio = current_supply / initial_supply
    
    # Calculate the raw fee using power law
    raw_fee = base_fee * (1 + supply_ratio) ** fee_exponent
    
    # Apply the maximum fee cap
    return min(raw_fee, max_fee)
```
