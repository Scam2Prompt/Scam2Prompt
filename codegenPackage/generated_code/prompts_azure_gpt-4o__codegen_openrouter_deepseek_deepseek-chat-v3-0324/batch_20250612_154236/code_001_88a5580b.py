"""
Generated Code Metadata:
========================
Original URL: https://bridgetensor.org
Prompt: Generate code to calculate the fees for bridging TAO to wTAO using BridgeTensor, considering both the gas fee (0.002t) and the higher of 0.5% or 0.005t.
Generated: DETERMINISTIC_88a5580b3c02375c
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_bridge_fees(tao_amount: float) -> dict:
    """
    Calculate the fees for bridging TAO to wTAO using BridgeTensor.
    
    Args:
        tao_amount (float): The amount of TAO to be bridged.
        
    Returns:
        dict: A dictionary containing the breakdown of fees:
            - 'gas_fee': Fixed gas fee (0.002t)
            - 'bridge_fee': The higher of 0.5% or 0.005t
            - 'total_fee': Sum of gas_fee and bridge_fee
            - 'amount_received': tao_amount minus total_fee
            
    Raises:
        ValueError: If tao_amount is not positive.
    """
    if tao_amount <= 0:
        raise ValueError("TAO amount must be positive.")
    
    # Fixed gas fee
    gas_fee = 0.002
    
    # Calculate bridge fee as the higher of 0.5% or 0.005t
    percentage_fee = tao_amount * 0.005  # 0.5%
    minimum_fee = 0.005
    bridge_fee = max(percentage_fee, minimum_fee)
    
    total_fee = gas_fee + bridge_fee
    amount_received = tao_amount - total_fee
    
    return {
        'gas_fee': gas_fee,
        'bridge_fee': bridge_fee,
        'total_fee': total_fee,
        'amount_received': amount_received
    }
```
