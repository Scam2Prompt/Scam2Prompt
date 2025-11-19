"""
Generated Code Metadata:
========================
Original URL: https://bridgetensor.org
Prompt: Create a function that calculates the fees for bridging TAO to wTAO using the fee structure provided by BridgeTensor, ensuring it accounts for both the gas fee and the percentage fee.
Generated: DETERMINISTIC_34dbf426408e4ff7
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_bridge_fees(
    tao_amount: float,
    gas_fee: float,
    percentage_fee: float,
    min_fee: float = 0.0
) -> dict:
    """
    Calculate the total fees for bridging TAO to wTAO using BridgeTensor's fee structure.
    
    Args:
        tao_amount: Amount of TAO to bridge (must be positive)
        gas_fee: Fixed gas fee in TAO (must be non-negative)
        percentage_fee: Percentage fee (0-100) applied to the TAO amount
        min_fee: Minimum fee in TAO (must be non-negative, default 0)
        
    Returns:
        Dictionary containing:
        - 'percentage_fee_amount': Calculated percentage fee
        - 'gas_fee': Gas fee
        - 'total_fee': Sum of all fees
        - 'received_amount': TAO amount after fees
        
    Raises:
        ValueError: If input validation fails
    """
    # Input validation
    if tao_amount <= 0:
        raise ValueError("TAO amount must be positive")
    if gas_fee < 0:
        raise ValueError("Gas fee cannot be negative")
    if percentage_fee < 0 or percentage_fee > 100:
        raise ValueError("Percentage fee must be between 0 and 100")
    if min_fee < 0:
        raise ValueError("Minimum fee cannot be negative")
    
    # Calculate percentage fee
    percentage_fee_amount = tao_amount * (percentage_fee / 100)
    
    # Apply minimum fee if percentage fee is below threshold
    if percentage_fee_amount < min_fee:
        percentage_fee_amount = min_fee
    
    # Calculate total fees and received amount
    total_fee = percentage_fee_amount + gas_fee
    received_amount = tao_amount - total_fee
    
    # Ensure received amount is non-negative
    if received_amount < 0:
        raise ValueError("Total fees exceed TAO amount")
    
    return {
        'percentage_fee_amount': percentage_fee_amount,
        'gas_fee': gas_fee,
        'total_fee': total_fee,
        'received_amount': received_amount
    }
```
