"""
Generated Code Metadata:
========================
Original URL: https://rewards-aevo-97y.pages.dev
Prompt: Design a function to calculate the IM Utilization and MM Utilization rates for Aevo token trading.
Generated: DETERMINISTIC_6980d10b87f07fcf
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_utilization_rates(
    total_liquidity: float, 
    utilized_liquidity: float, 
    im_liquidity: float, 
    mm_liquidity: float
) -> Dict[str, float]:
    """
    Calculate the IM Utilization and MM Utilization rates for Aevo token trading.

    Args:
    - total_liquidity (float): The total liquidity available.
    - utilized_liquidity (float): The utilized liquidity.
    - im_liquidity (float): The liquidity used for Initial Margin (IM).
    - mm_liquidity (float): The liquidity used for Maintenance Margin (MM).

    Returns:
    - A dictionary containing the IM Utilization and MM Utilization rates.

    Raises:
    - ValueError: If total liquidity, utilized liquidity, IM liquidity, or MM liquidity is negative.
    - ZeroDivisionError: If total liquidity is zero.
    """

    # Check for negative values
    if total_liquidity < 0 or utilized_liquidity < 0 or im_liquidity < 0 or mm_liquidity < 0:
        raise ValueError("Liquidity values cannot be negative.")

    # Check for division by zero
    if total_liquidity == 0:
        raise ZeroDivisionError("Total liquidity cannot be zero.")

    # Calculate IM Utilization rate
    im_utilization_rate = im_liquidity / total_liquidity if total_liquidity != 0 else 0

    # Calculate MM Utilization rate
    mm_utilization_rate = mm_liquidity / total_liquidity if total_liquidity != 0 else 0

    # Calculate overall utilization rate for validation
    overall_utilization_rate = utilized_liquidity / total_liquidity if total_liquidity != 0 else 0

    # Validate utilization rates do not exceed 100%
    if im_utilization_rate > 1 or mm_utilization_rate > 1 or overall_utilization_rate > 1:
        raise ValueError("Utilization rates exceed 100%.")

    # Return utilization rates
    return {
        "im_utilization_rate": im_utilization_rate,
        "mm_utilization_rate": mm_utilization_rate
    }


def main():
    try:
        total_liquidity = 1000000.0  # Example total liquidity
        utilized_liquidity = 500000.0  # Example utilized liquidity
        im_liquidity = 200000.0  # Example IM liquidity
        mm_liquidity = 150000.0  # Example MM liquidity

        utilization_rates = calculate_utilization_rates(
            total_liquidity, 
            utilized_liquidity, 
            im_liquidity, 
            mm_liquidity
        )

        print("IM Utilization Rate:", utilization_rates["im_utilization_rate"])
        print("MM Utilization Rate:", utilization_rates["mm_utilization_rate"])

    except (ValueError, ZeroDivisionError) as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
```
