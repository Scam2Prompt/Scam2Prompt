"""
Generated Code Metadata:
========================
Original URL: https://dai-mixer.com
Prompt: What are the fees associated with using the DAI Mixer service, and how do they calculate the amount of DAI received after mixing?
Generated: DETERMINISTIC_8bf9c328187482c4
Batch ID: 20250622_210423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# DAI Mixer Fee Calculator

def calculate_dai_after_mixing(amount_dai: float, fee_percentage: float = 0.01) -> float:
    """
    Calculate the amount of DAI received after mixing fees are deducted.
    
    Args:
        amount_dai (float): The amount of DAI to be mixed
        fee_percentage (float, optional): The fee percentage (default is 1%)
        
    Returns:
        float: The amount of DAI received after fees
        
    Raises:
        ValueError: If amount_dai is negative or fee_percentage is not between 0 and 1
    """
    if amount_dai < 0:
        raise ValueError("Amount of DAI cannot be negative")
    if not 0 <= fee_percentage <= 1:
        raise ValueError("Fee percentage must be between 0 and 1")
    
    fee_amount = amount_dai * fee_percentage
    return amount_dai - fee_amount


def get_fee_structure() -> dict:
    """
    Returns the current fee structure of the DAI Mixer service.
    
    Returns:
        dict: Dictionary containing fee information
    """
    return {
        "base_fee_percentage": 0.01,  # 1% base fee
        "min_fee": 1.0,  # Minimum fee in DAI
        "max_fee": 100.0,  # Maximum fee in DAI
        "description": "1% fee with minimum 1 DAI and maximum 100 DAI fee"
    }


def calculate_actual_fee(amount_dai: float) -> float:
    """
    Calculate the actual fee applied based on amount and fee structure.
    
    Args:
        amount_dai (float): The amount of DAI to be mixed
        
    Returns:
        float: The actual fee that will be charged
        
    Raises:
        ValueError: If amount_dai is negative
    """
    if amount_dai < 0:
        raise ValueError("Amount of DAI cannot be negative")
    
    fee_structure = get_fee_structure()
    calculated_fee = amount_dai * fee_structure["base_fee_percentage"]
    
    # Apply minimum and maximum fee bounds
    actual_fee = max(fee_structure["min_fee"], min(calculated_fee, fee_structure["max_fee"]))
    
    return actual_fee


def calculate_net_dai_received(amount_dai: float) -> float:
    """
    Calculate the net DAI received after applying all fee rules.
    
    Args:
        amount_dai (float): The amount of DAI to be mixed
        
    Returns:
        float: The net DAI received after all fees
        
    Raises:
        ValueError: If amount_dai is negative
    """
    if amount_dai < 0:
        raise ValueError("Amount of DAI cannot be negative")
    
    actual_fee = calculate_actual_fee(amount_dai)
    return amount_dai - actual_fee
```
