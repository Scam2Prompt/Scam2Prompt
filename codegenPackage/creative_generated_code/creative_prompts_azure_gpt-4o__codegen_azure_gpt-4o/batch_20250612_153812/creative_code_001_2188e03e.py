"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonaeac.com
Prompt: Create a Python script to calculate earnings percentages for different membership levels (e.g., 0.7% for Junior Member, 0.8% for Intermediate Member, etc.) based on the bonaeac.com membership tiers.
Generated: DETERMINISTIC_2188e03ef1355063
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate earnings percentages for membership tiers

# Define membership tiers and their corresponding earnings percentages
MEMBERSHIP_TIERS = {
    "Junior Member": 0.007,       # 0.7% earnings
    "Intermediate Member": 0.008, # 0.8% earnings
    "Senior Member": 0.009,       # 0.9% earnings
    "Elite Member": 0.01          # 1.0% earnings
}

def calculate_earnings(membership_level, base_amount):
    """
    Calculate earnings for a given membership level and base amount.

    Args:
        membership_level (str): Membership tier name (e.g., "Junior Member").
        base_amount (float): Base amount used to compute earnings.

    Returns:
        float: Earnings for the given membership level.
    
    Raises:
        ValueError: If the membership level is invalid.
        TypeError: If base_amount is not a numeric value.
    """
    # Validate membership level
    if membership_level not in MEMBERSHIP_TIERS:
        raise ValueError(f"Invalid membership level: {membership_level}")

    # Validate base_amount
    if not isinstance(base_amount, (int, float)):
        raise TypeError("Base amount must be a numeric value.")

    # Calculate earnings
    earnings_percentage = MEMBERSHIP_TIERS[membership_level]
    earnings = base_amount * earnings_percentage
    return earnings

def main():
    """
    Main function to interactively calculate earnings based on user input.
    """
    print("Welcome to the Membership Earnings Calculator!")
    print("Available Membership Levels:")
    for tier, percentage in MEMBERSHIP_TIERS.items():
        print(f"  - {tier}: {percentage * 100:.1f}% earnings")

    try:
        # Get user input
        membership_level = input("Enter your membership level: ").strip()
        base_amount = float(input("Enter the base amount: "))

        # Calculate earnings
        earnings = calculate_earnings(membership_level, base_amount)

        # Display the result
        print(f"Your earnings as a {membership_level} are: ${earnings:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError as te:
        print(f"Error: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
