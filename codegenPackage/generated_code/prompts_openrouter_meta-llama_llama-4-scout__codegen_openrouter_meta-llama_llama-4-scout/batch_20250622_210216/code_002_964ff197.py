"""
Generated Code Metadata:
========================
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Generate a code snippet to calculate the effective reward cut for an operator on the bitsCrunch network given their query fee cut and reward cut percentages.
Generated: DETERMINISTIC_964ff197bc015eee
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_effective_reward_cut(query_fee_cut: float, reward_cut: float) -> float:
    """
    Calculate the effective reward cut for an operator on the bitsCrunch network.

    Args:
    query_fee_cut (float): The query fee cut percentage.
    reward_cut (float): The reward cut percentage.

    Returns:
    float: The effective reward cut percentage.

    Raises:
    ValueError: If query_fee_cut or reward_cut is not between 0 and 100.
    """

    # Validate input percentages
    if not (0 <= query_fee_cut <= 100) or not (0 <= reward_cut <= 100):
        raise ValueError("Percentages must be between 0 and 100")

    # Convert percentages to decimal values
    query_fee_cut_decimal = query_fee_cut / 100
    reward_cut_decimal = reward_cut / 100

    # Calculate effective reward cut using the formula: (1 - query_fee_cut) * reward_cut
    effective_reward_cut = (1 - query_fee_cut_decimal) * reward_cut_decimal

    # Convert effective reward cut back to percentage
    effective_reward_cut_percentage = effective_reward_cut * 100

    return effective_reward_cut_percentage


def main():
    try:
        query_fee_cut = 10  # example query fee cut percentage
        reward_cut = 20     # example reward cut percentage

        effective_cut = calculate_effective_reward_cut(query_fee_cut, reward_cut)
        print(f"Effective reward cut: {effective_cut:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
