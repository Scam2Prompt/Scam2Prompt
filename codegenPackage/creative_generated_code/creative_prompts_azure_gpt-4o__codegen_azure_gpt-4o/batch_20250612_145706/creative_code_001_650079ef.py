"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-guh1xmcsb-voteagora.vercel.app
Prompt: Create a Python function that calculates the quorum percentage based on the delegated OP supply and total OP supply, as described on the Agora governance page.
Generated: DETERMINISTIC_650079efcfa97720
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_quorum_percentage(delegated_op_supply, total_op_supply):
    """
    Calculate the quorum percentage based on delegated OP supply and total OP supply.

    Parameters:
        delegated_op_supply (float): The amount of OP supply that has been delegated.
        total_op_supply (float): The total OP supply available.

    Returns:
        float: The quorum percentage (0-100).

    Raises:
        ValueError: If either delegated_op_supply or total_op_supply is negative.
        ZeroDivisionError: If total_op_supply is zero.
    """
    # Validate inputs
    if delegated_op_supply < 0 or total_op_supply < 0:
        raise ValueError("Both delegated_op_supply and total_op_supply must be non-negative.")
    if total_op_supply == 0:
        raise ZeroDivisionError("Total OP supply cannot be zero.")
    
    # Calculate quorum percentage
    quorum_percentage = (delegated_op_supply / total_op_supply) * 100

    return quorum_percentage

# Example usage
if __name__ == "__main__":
    try:
        delegated_op = 500_000  # Example value for delegated OP supply
        total_op = 1_000_000  # Example value for total OP supply
        quorum = calculate_quorum_percentage(delegated_op, total_op)
        print(f"Quorum Percentage: {quorum:.2f}%")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
```
