"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-shibabudz.web.app
Prompt: Write a function to calculate the total BUDZ tokens sold and display the percentage progress toward the maximum token sale limit (1,542,000,000 tokens).
Generated: DETERMINISTIC_3e780d380d2aeefb
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary modules
def calculate_token_sales(total_sold, max_limit=1542000000):
    """
    Calculate the percentage progress of BUDZ token sales towards the maximum limit.

    Parameters:
    total_sold (int): The total number of BUDZ tokens sold.
    max_limit (int): The maximum token sale limit. Default is 1,542,000,000 tokens.

    Returns:
    dict: A dictionary containing total tokens sold and percentage progress.
    """

    # Input validation
    if not isinstance(total_sold, (int, float)) or total_sold < 0:
        raise ValueError("total_sold must be a non-negative number.")
    if not isinstance(max_limit, (int, float)) or max_limit <= 0:
        raise ValueError("max_limit must be a positive number.")

    # Ensure total_sold does not exceed the max_limit
    if total_sold > max_limit:
        raise ValueError("total_sold cannot exceed max_limit.")

    # Calculate percentage progress
    percentage_progress = (total_sold / max_limit) * 100

    # Return the results
    return {
        "total_sold": total_sold,
        "percentage_progress": round(percentage_progress, 2)  # Rounded to 2 decimal places
    }


# Example usage
if __name__ == "__main__":
    try:
        # Example: The number of tokens sold
        total_tokens_sold = 1200000000

        # Calculate progress and display results
        result = calculate_token_sales(total_tokens_sold)
        print(f"Total BUDZ Tokens Sold: {result['total_sold']}")
        print(f"Progress towards Maximum Sale Limit: {result['percentage_progress']}%")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
