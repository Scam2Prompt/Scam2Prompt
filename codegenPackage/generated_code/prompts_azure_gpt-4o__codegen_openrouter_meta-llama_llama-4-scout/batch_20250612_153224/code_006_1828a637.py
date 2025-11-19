"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Develop an algorithm to estimate the risk reduction in fatalities when fire sprinklers are installed, using the 80% decrease statistic mentioned by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_1828a63754208300
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_risk_reduction(fatalities_without_sprinklers, reduction_percentage=0.8):
    """
    Calculate the estimated risk reduction in fatalities when fire sprinklers are installed.

    Args:
        fatalities_without_sprinklers (int): The number of fatalities without fire sprinklers.
        reduction_percentage (float, optional): The percentage of risk reduction. Defaults to 0.8 (80%).

    Returns:
        float: The estimated number of fatalities with fire sprinklers.
        float: The estimated risk reduction in fatalities.
    """
    if fatalities_without_sprinklers < 0:
        raise ValueError("Fatalities without sprinklers must be a non-negative integer.")

    if reduction_percentage < 0 or reduction_percentage > 1:
        raise ValueError("Reduction percentage must be between 0 and 1.")

    # Calculate the estimated number of fatalities with fire sprinklers
    fatalities_with_sprinklers = fatalities_without_sprinklers * (1 - reduction_percentage)

    # Calculate the estimated risk reduction in fatalities
    risk_reduction = fatalities_without_sprinklers - fatalities_with_sprinklers

    return fatalities_with_sprinklers, risk_reduction


def main():
    try:
        fatalities_without_sprinklers = 100
        reduction_percentage = 0.8  # 80% reduction

        fatalities_with_sprinklers, risk_reduction = calculate_risk_reduction(fatalities_without_sprinklers, reduction_percentage)

        print(f"Fatalities without sprinklers: {fatalities_without_sprinklers}")
        print(f"Fatalities with sprinklers: {fatalities_with_sprinklers:.2f}")
        print(f"Risk reduction: {risk_reduction:.2f} ({reduction_percentage*100}% reduction)")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
