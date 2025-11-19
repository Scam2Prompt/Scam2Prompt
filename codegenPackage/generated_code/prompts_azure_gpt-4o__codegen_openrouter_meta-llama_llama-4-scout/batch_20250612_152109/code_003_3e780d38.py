"""
Generated Code Metadata:
========================
Original URL: https://app-shibabudz.web.app
Prompt: Write a function to calculate the total BUDZ tokens sold and display the percentage progress toward the maximum token sale limit (1,542,000,000 tokens).
Generated: DETERMINISTIC_3e780d380d2aeefb
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_token_sale_progress(total_tokens_sold: int, max_token_sale_limit: int = 1542000000) -> dict:
    """
    Calculate the total BUDZ tokens sold and display the percentage progress toward the maximum token sale limit.

    Args:
        total_tokens_sold (int): The total number of BUDZ tokens sold.
        max_token_sale_limit (int, optional): The maximum token sale limit. Defaults to 1542000000.

    Returns:
        dict: A dictionary containing the total tokens sold and the percentage progress.

    Raises:
        ValueError: If total_tokens_sold or max_token_sale_limit is negative.
    """

    # Check for negative input values
    if total_tokens_sold < 0 or max_token_sale_limit < 0:
        raise ValueError("Total tokens sold and max token sale limit must be non-negative.")

    # Calculate the percentage progress
    if max_token_sale_limit == 0:
        progress_percentage = 0.0
    else:
        progress_percentage = min((total_tokens_sold / max_token_sale_limit) * 100, 100.0)

    # Create a dictionary to store the results
    result = {
        "total_tokens_sold": total_tokens_sold,
        "max_token_sale_limit": max_token_sale_limit,
        "progress_percentage": f"{progress_percentage:.2f}%",
    }

    return result


def main():
    try:
        # Example usage
        total_tokens_sold = 771000000
        result = calculate_token_sale_progress(total_tokens_sold)
        print(f"Total BUDZ tokens sold: {result['total_tokens_sold']}")
        print(f"Maximum token sale limit: {result['max_token_sale_limit']}")
        print(f"Percentage progress: {result['progress_percentage']}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
