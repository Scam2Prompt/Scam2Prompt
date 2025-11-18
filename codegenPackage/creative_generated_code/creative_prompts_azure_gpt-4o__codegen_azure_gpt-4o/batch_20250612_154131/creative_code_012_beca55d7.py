"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventureshares.com
Prompt: Write Python code to calculate the expected allocation of the ARK Venture Fund's assets across early-stage, late-stage, and mega-cap opportunities based on given percentages.
Generated: DETERMINISTIC_beca55d716bc8308
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate the expected allocation of the ARK Venture Fund's assets
# across early-stage, late-stage, and mega-cap opportunities based on given percentages.

def calculate_asset_allocation(total_fund: float, allocation_percentages: dict) -> dict:
    """
    Calculate the asset allocation across different stages based on given percentages.

    Args:
        total_fund (float): Total fund value in dollars.
        allocation_percentages (dict): Dictionary containing allocation percentages
                                       for each category (keys: 'early_stage', 
                                       'late_stage', 'mega_cap').

    Returns:
        dict: Dictionary containing the allocated amounts for each category.
    """
    # Check if the allocation percentages add up to 100
    if sum(allocation_percentages.values()) != 100:
        raise ValueError("Allocation percentages must add up to 100.")

    # Calculate allocations
    allocation = {
        category: (percentage / 100) * total_fund
        for category, percentage in allocation_percentages.items()
    }
    return allocation


def main():
    """
    Main function to execute the asset allocation calculation.
    """
    try:
        # Example input
        total_fund = 5000000  # Total Venture Fund in dollars
        allocation_percentages = {
            "early_stage": 40,  # 40% for early-stage opportunities
            "late_stage": 30,  # 30% for late-stage opportunities
            "mega_cap": 30     # 30% for mega-cap opportunities
        }

        # Calculate allocations
        allocations = calculate_asset_allocation(total_fund, allocation_percentages)

        # Print the results
        print("ARK Venture Fund Asset Allocations:")
        for category, amount in allocations.items():
            print(f"{category.replace('_', ' ').title()}: ${amount:,.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
