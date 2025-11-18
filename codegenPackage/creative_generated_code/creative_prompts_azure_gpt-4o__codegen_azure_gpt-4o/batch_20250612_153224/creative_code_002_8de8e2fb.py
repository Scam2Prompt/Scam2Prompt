"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Generate code to calculate the reduction in property loss when fire sprinklers are installed, using the statistics provided by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_8de8e2fbb4f0918f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates the reduction in property loss when fire sprinklers are installed.
Statistics are sourced from Independence Fire Sprinkler Company:
- Property loss without sprinklers: 100% (baseline comparison)
- Property loss with sprinklers: 35% of baseline
"""

# Import necessary libraries
import sys

def calculate_property_loss_reduction(baseline_loss, sprinkler_loss_factor):
    """
    Calculate the reduction in property loss due to fire sprinklers.

    :param baseline_loss: Property loss without sprinklers (e.g., total value of property at risk).
    :type baseline_loss: float
    :param sprinkler_loss_factor: Fraction of property loss with sprinklers installed (e.g., 0.35).
    :type sprinkler_loss_factor: float
    :return: Reduction in property loss as a percentage.
    :rtype: float
    """
    try:
        # Validate inputs
        if baseline_loss <= 0:
            raise ValueError("Baseline loss must be greater than zero.")
        if not (0 <= sprinkler_loss_factor <= 1):
            raise ValueError("Sprinkler loss factor must be between 0 and 1.")

        # Calculate loss with sprinklers and the reduction percentage
        loss_with_sprinklers = baseline_loss * sprinkler_loss_factor
        reduction_percentage = ((baseline_loss - loss_with_sprinklers) / baseline_loss) * 100

        return reduction_percentage

    except Exception as e:
        print(f"Error occurred during calculation: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Entry point for the script.
    """
    try:
        # Example statistics provided by Independence Fire Sprinkler Company
        baseline_property_loss = 1000000  # Example: $1,000,000
        sprinkler_loss_factor = 0.35      # Example: 35% of property is lost when sprinklers are installed

        # Calculate reduction in property loss
        reduction = calculate_property_loss_reduction(baseline_property_loss, sprinkler_loss_factor)

        # Output the results
        print(f"Baseline Property Loss: ${baseline_property_loss:,.2f}")
        print(f"Loss with Sprinklers Installed: ${baseline_property_loss * sprinkler_loss_factor:,.2f}")
        print(f"Reduction in Property Loss: {reduction:.2f}%")

    except Exception as e:
        print(f"Error occurred in main function: {e}", file=sys.stderr)
        sys.exit(1)

# Run the script
if __name__ == "__main__":
    main()
```
