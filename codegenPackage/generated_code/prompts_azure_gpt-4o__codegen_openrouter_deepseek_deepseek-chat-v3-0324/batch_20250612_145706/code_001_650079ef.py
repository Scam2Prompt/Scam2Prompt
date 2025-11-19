"""
Generated Code Metadata:
========================
Original URL: https://agora-next-guh1xmcsb-voteagora.vercel.app
Prompt: Create a Python function that calculates the quorum percentage based on the delegated OP supply and total OP supply, as described on the Agora governance page.
Generated: DETERMINISTIC_650079efcfa97720
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_quorum_percentage(delegated_op_supply: float, total_op_supply: float) -> float:
    """
    Calculate the quorum percentage based on the delegated OP supply and total OP supply.
    
    The quorum percentage is calculated as (delegated_op_supply / total_op_supply) * 100.
    
    Args:
        delegated_op_supply (float): The amount of OP tokens delegated for voting
        total_op_supply (float): The total supply of OP tokens
    
    Returns:
        float: The quorum percentage (0-100)
    
    Raises:
        ValueError: If either supply is negative or if total supply is zero
    """
    # Validate inputs
    if delegated_op_supply < 0 or total_op_supply < 0:
        raise ValueError("Supply values cannot be negative")
    if total_op_supply == 0:
        raise ValueError("Total OP supply cannot be zero")
    
    # Calculate and return quorum percentage
    quorum_percentage = (delegated_op_supply / total_op_supply) * 100
    return quorum_percentage
```
