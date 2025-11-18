"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmining.website
Prompt: Create a program to compare the cost and benefits of upgrading to Tier4 versus staying on the free mining plan, using the earning rates and affiliate bonuses provided on the Coinmining website.
Generated: DETERMINISTIC_11f7b955a6619ecf
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_earnings(plan_rate, hours, affiliate_bonus=0):
    """
    Calculate earnings based on mining rate and affiliate bonus.

    Args:
        plan_rate (float): The earning rate of the plan (per hour).
        hours (int): The number of hours to calculate earnings for.
        affiliate_bonus (float): Additional bonus rate from affiliates (default: 0).

    Returns:
        float: Total earnings over the specified hours.
    """
    try:
        if plan_rate < 0 or hours < 0 or affiliate_bonus < 0:
            raise ValueError("Earning rate, hours, and affiliate bonus must be non-negative.")
        return (plan_rate + affiliate_bonus) * hours
    except Exception as e:
        print(f"Error calculating earnings: {e}")
        sys.exit(1)


def compare_plans(free_rate, tier4_rate, tier4_cost, hours, affiliate_bonus=0):
    """
    Compare the cost and benefits of upgrading to Tier4 versus staying on the free plan.

    Args:
        free_rate (float): The earning rate of the free plan (per hour).
        tier4_rate (float): The earning rate of the Tier4 plan (per hour).
        tier4_cost (float): The cost of Tier4 plan (one-time cost).
        hours (int): The number of hours to calculate for.
        affiliate_bonus (float): Additional bonus rate from affiliates (default: 0).

    Returns:
        dict: Summary of free plan earnings, Tier4 plan earnings, and net profit/loss.
    """
    try:
        # Calculate earnings for both plans
        free_plan_earnings = calculate_earnings(free_rate, hours, affiliate_bonus)
        tier4_plan_earnings = calculate_earnings(tier4_rate, hours, affiliate_bonus) - tier4_cost

        # Net difference in earning
        net_difference = tier4_plan_earnings - free_plan_earnings

        return {
            "Free Plan Earnings": free_plan_earnings,
            "Tier4 Plan Earnings (after cost)": tier4_plan_earnings,
            "Net Difference": net_difference
        }
    except Exception as e:
        print(f"Error comparing plans: {e}")
        sys.exit(1)


def main():
    """
    Entry point of the program. Collects user input and displays the comparison results.
    """
    try:
        print("Mining Plan Comparison Tool\n")

        # User inputs
        free_rate = float(input("Enter the earning rate for the Free Plan (per hour): "))
        tier4_rate = float(input("Enter the earning rate for the Tier4 Plan (per hour): "))
        tier4_cost = float(input("Enter the cost of the Tier4 Plan (one-time): "))
        hours = int(input("Enter the number of hours to calculate earnings for: "))
        affiliate_bonus = float(input("Enter the affiliate bonus rate (if any, default is 0): ") or 0)

        # Validate inputs
        if hours <= 0:
            raise ValueError("Hours must be a positive integer.")
        if free_rate < 0 or tier4_rate < 0 or tier4_cost < 0 or affiliate_bonus < 0:
            raise ValueError("Rates, cost, and bonuses must be non-negative values.")

        # Compare plans
        comparison = compare_plans(free_rate, tier4_rate, tier4_cost, hours, affiliate_bonus)

        # Display results
        print("\nComparison Results:")
        print(f"Free Plan Earnings: ${comparison['Free Plan Earnings']:.2f}")
        print(f"Tier4 Plan Earnings (after cost): ${comparison['Tier4 Plan Earnings (after cost)']:.2f}")
        print(f"Net Difference: ${comparison['Net Difference']:.2f}")

        if comparison["Net Difference"] > 0:
            print("\nUpgrading to Tier4 is beneficial.")
        elif comparison["Net Difference"] < 0:
            print("\nStaying on the Free Plan is better.")
        else:
            print("\nBoth plans yield the same net earnings.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
