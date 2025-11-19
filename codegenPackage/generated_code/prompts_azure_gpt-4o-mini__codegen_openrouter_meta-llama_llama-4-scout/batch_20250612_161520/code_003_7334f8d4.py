"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-de.web.app
Prompt: Create a function that calculates potential earnings from staking $MGLS tokens based on different annual return percentages.
Generated: DETERMINISTIC_7334f8d46492cf9c
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_staking_earnings(mgls_tokens: float, annual_return_percentages: list[float]) -> dict[float, float]:
    """
    Calculate potential earnings from staking $MGLS tokens based on different annual return percentages.

    Args:
    - mgls_tokens (float): The number of $MGLS tokens to stake.
    - annual_return_percentages (list[float]): A list of annual return percentages.

    Returns:
    - A dictionary where the keys are the annual return percentages and the values are the corresponding earnings.
    """

    # Initialize an empty dictionary to store the earnings for each annual return percentage
    earnings = {}

    # Check if the number of $MGLS tokens is valid (non-negative)
    if mgls_tokens < 0:
        raise ValueError("The number of $MGLS tokens must be non-negative.")

    # Check if the list of annual return percentages is valid (not empty)
    if not annual_return_percentages:
        raise ValueError("The list of annual return percentages must not be empty.")

    # Iterate over each annual return percentage
    for annual_return_percentage in annual_return_percentages:
        # Check if the annual return percentage is valid (between 0 and 100)
        if annual_return_percentage < 0 or annual_return_percentage > 100:
            raise ValueError("Annual return percentages must be between 0 and 100.")

        # Calculate the earnings for the current annual return percentage
        # Assuming the annual return percentage is a percentage value (e.g., 5 for 5%)
        earnings[annual_return_percentage] = mgls_tokens * (annual_return_percentage / 100)

    return earnings


def main():
    try:
        # Example usage
        mgls_tokens = 1000.0
        annual_return_percentages = [5.0, 10.0, 15.0]

        earnings = calculate_staking_earnings(mgls_tokens, annual_return_percentages)

        print("Potential Earnings:")
        for annual_return_percentage, earning in earnings.items():
            print(f"Annual Return: {annual_return_percentage}% -> ${earning:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
