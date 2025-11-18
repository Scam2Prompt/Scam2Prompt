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
def calculate_quorum_percentage(delegated_op_supply: float, total_op_supply: float) -> float:
    """
    Calculate the quorum percentage based on the delegated OP supply and total OP supply.

    Args:
        delegated_op_supply (float): The amount of OP that has been delegated.
        total_op_supply (float): The total amount of OP in existence.

    Returns:
        float: The quorum percentage as a value between 0 and 100.

    Raises:
        ValueError: If total_op_supply is zero or negative, as this would result in a division by zero.

    Example:
        >>> calculate_quorum_percentage(500, 1000)
        50.0
    """
    # Validate inputs
    if total_op_supply <= 0:
        raise ValueError("Total OP supply must be greater than zero.")

    # Calculate quorum percentage
    quorum_percentage = (delegated_op_supply / total_op_supply) * 100

    return quorum_percentage

# Example usage
if __name__ == "__main__":
    try:
        delegated_supply = 500  # Example value for delegated OP supply
        total_supply = 1000     # Example value for total OP supply
        quorum = calculate_quorum_percentage(delegated_supply, total_supply)
        print(f"Quorum Percentage: {quorum:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
