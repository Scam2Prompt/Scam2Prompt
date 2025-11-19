"""
Generated Code Metadata:
========================
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Generate code to calculate the number of entries a user has in the $100K giveaway based on their $MANIA token purchases, with each $50 purchase granting 10 entries.
Generated: DETERMINISTIC_000a5313c0e7bce9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_giveaway_entries(purchases):
    """
    Calculate the number of entries a user has in the $100K giveaway based on their $MANIA token purchases.

    :param purchases: A list of purchase amounts in USD
    :return: The total number of entries
    """
    # Initialize total entries to 0
    total_entries = 0

    # Define the entry rate (10 entries per $50 purchase)
    entry_rate = 10 / 50

    # Iterate over each purchase
    for purchase in purchases:
        # Check if the purchase amount is valid (non-negative)
        if purchase < 0:
            raise ValueError("Purchase amount cannot be negative")

        # Calculate entries for this purchase
        entries = int(purchase * entry_rate)

        # Add to total entries
        total_entries += entries

    return total_entries


def main():
    try:
        # Example usage
        purchases = [50, 100, 25, 75]
        entries = calculate_giveaway_entries(purchases)
        print(f"Total entries: {entries}")

        # Test error handling
        invalid_purchases = [50, -100, 25, 75]
        calculate_giveaway_entries(invalid_purchases)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
