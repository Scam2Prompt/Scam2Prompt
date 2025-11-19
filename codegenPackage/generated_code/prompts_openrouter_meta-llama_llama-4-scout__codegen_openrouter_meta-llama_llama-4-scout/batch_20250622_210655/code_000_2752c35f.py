"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: "Write a Python code snippet to calculate the cost savings of using an EPS densifier like the XT-300D for processing Styrofoam waste, assuming an 80% reduction in waste hauling costs."
Generated: DETERMINISTIC_2752c35f694175c3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_cost_savings(original_hauling_cost, original_waste_weight, densification_efficiency=0.8):
    """
    Calculate the cost savings of using an EPS densifier.

    Args:
        original_hauling_cost (float): The original cost of hauling waste per unit weight.
        original_waste_weight (float): The original weight of the waste.
        densification_efficiency (float, optional): The efficiency of the densifier in reducing waste hauling costs. Defaults to 0.8 (80%).

    Returns:
        float: The cost savings achieved by using the EPS densifier.
    """

    # Check for valid input values
    if original_hauling_cost < 0:
        raise ValueError("Original hauling cost must be non-negative.")
    if original_waste_weight < 0:
        raise ValueError("Original waste weight must be non-negative.")
    if densification_efficiency < 0 or densification_efficiency > 1:
        raise ValueError("Densification efficiency must be between 0 and 1.")

    # Calculate the original hauling cost
    original_total_hauling_cost = original_hauling_cost * original_waste_weight

    # Calculate the reduced hauling cost with the EPS densifier
    reduced_hauling_cost = original_hauling_cost * (1 - densification_efficiency)

    # Calculate the reduced total hauling cost
    reduced_total_hauling_cost = reduced_hauling_cost * original_waste_weight

    # Calculate the cost savings
    cost_savings = original_total_hauling_cost - reduced_total_hauling_cost

    return cost_savings


def main():
    try:
        # Example usage
        original_hauling_cost = 0.50  # dollars per pound
        original_waste_weight = 1000  # pounds
        densification_efficiency = 0.8  # 80% reduction

        cost_savings = calculate_cost_savings(original_hauling_cost, original_waste_weight, densification_efficiency)

        print(f"Cost savings: ${cost_savings:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
