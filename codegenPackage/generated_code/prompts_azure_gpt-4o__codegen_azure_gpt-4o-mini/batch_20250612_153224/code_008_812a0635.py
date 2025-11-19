"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Write a script to calculate the average property loss reduction per fire when sprinklers are present, referencing the 71% statistic from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_812a063546356822
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# average_loss_reduction.py

def calculate_average_loss_reduction(total_losses: float, number_of_fires: int, reduction_percentage: float) -> float:
    """
    Calculate the average property loss reduction per fire when sprinklers are present.

    Parameters:
    total_losses (float): The total property losses incurred without sprinklers.
    number_of_fires (int): The total number of fires that occurred.
    reduction_percentage (float): The percentage reduction in property loss due to sprinklers.

    Returns:
    float: The average property loss reduction per fire when sprinklers are present.
    
    Raises:
    ValueError: If number_of_fires is less than or equal to zero or total_losses is negative.
    """
    if number_of_fires <= 0:
        raise ValueError("Number of fires must be greater than zero.")
    if total_losses < 0:
        raise ValueError("Total losses cannot be negative.")

    # Calculate the total loss reduction based on the reduction percentage
    total_loss_reduction = total_losses * (reduction_percentage / 100)

    # Calculate the average loss reduction per fire
    average_loss_reduction = total_loss_reduction / number_of_fires

    return average_loss_reduction


def main():
    """
    Main function to execute the average loss reduction calculation.
    """
    # Constants
    REDUCTION_PERCENTAGE = 71.0  # Percentage reduction in property loss due to sprinklers

    # Example data (these values can be modified as needed)
    total_losses = 1000000.0  # Total property losses in dollars
    number_of_fires = 50       # Total number of fires

    try:
        # Calculate the average loss reduction
        average_reduction = calculate_average_loss_reduction(total_losses, number_of_fires, REDUCTION_PERCENTAGE)
        print(f"Average property loss reduction per fire with sprinklers: ${average_reduction:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
