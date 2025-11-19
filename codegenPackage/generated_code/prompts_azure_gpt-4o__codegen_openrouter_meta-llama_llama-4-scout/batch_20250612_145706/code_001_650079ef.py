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
def calculate_quorum_percentage(delegated_supply: float, total_supply: float) -> float:
    """
    Calculate the quorum percentage based on the delegated OP supply and total OP supply.

    Args:
        delegated_supply (float): The delegated OP supply.
        total_supply (float): The total OP supply.

    Returns:
        float: The quorum percentage.

    Raises:
        ValueError: If the total supply is zero or negative.
        TypeError: If the inputs are not numbers.
    """

    # Check if inputs are numbers
    if not isinstance(delegated_supply, (int, float)) or not isinstance(total_supply, (int, float)):
        raise TypeError("Both delegated supply and total supply must be numbers.")

    # Check for division by zero
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")

    # Calculate the quorum percentage
    # Assuming the quorum percentage is the delegated supply divided by the total supply
    quorum_percentage = (delegated_supply / total_supply) * 100

    # Ensure the quorum percentage is between 0 and 100
    quorum_percentage = max(0, min(quorum_percentage, 100))

    return quorum_percentage


def main():
    try:
        delegated_supply = 1000000.0  # example delegated supply
        total_supply = 10000000.0  # example total supply

        quorum_percentage = calculate_quorum_percentage(delegated_supply, total_supply)
        print(f"Quorum percentage: {quorum_percentage}%")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
