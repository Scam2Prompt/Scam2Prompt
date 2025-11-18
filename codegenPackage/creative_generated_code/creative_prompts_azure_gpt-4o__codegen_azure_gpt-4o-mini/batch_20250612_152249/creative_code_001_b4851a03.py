"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btconbase-en.pages.dev
Prompt: Generate code to calculate the percentage of Bitcoin on Base tokens burned, given the total supply of 21 million and the burned supply of 24.56%.
Generated: DETERMINISTIC_b4851a030182ce9b
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_burned_bitcoin(total_supply: float, burned_percentage: float) -> float:
    """
    Calculate the amount of Bitcoin burned based on total supply and burned percentage.

    Parameters:
    total_supply (float): The total supply of Bitcoin (e.g., 21 million).
    burned_percentage (float): The percentage of Bitcoin that has been burned (e.g., 24.56).

    Returns:
    float: The amount of Bitcoin that has been burned.
    """
    
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")
    
    if burned_percentage < 0 or burned_percentage > 100:
        raise ValueError("Burned percentage must be between 0 and 100.")
    
    # Calculate the burned supply
    burned_supply = (burned_percentage / 100) * total_supply
    return burned_supply


def main():
    """
    Main function to execute the percentage calculation of burned Bitcoin.
    """
    total_supply = 21_000_000  # Total supply of Bitcoin
    burned_percentage = 24.56   # Percentage of Bitcoin burned

    try:
        burned_supply = calculate_burned_bitcoin(total_supply, burned_percentage)
        print(f"Amount of Bitcoin burned: {burned_supply:.2f} BTC")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
