"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Write a script to calculate the average property loss reduction per fire when sprinklers are present, referencing the 71% statistic from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_812a063546356822
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
Script to calculate the average property loss reduction per fire when sprinklers are present.
References the 71% statistic from Independence Fire Sprinkler Company.

Requirements:
- Input: Average property loss per fire without sprinklers.
- Output: Average property loss with sprinklers and the reduction in percentage.
"""

def calculate_loss_with_sprinklers(loss_without_sprinklers):
    """
    Calculate the property loss when sprinklers are present based on the 71% reduction statistic.

    Parameters:
        loss_without_sprinklers (float): Average property loss per fire without sprinklers.

    Returns:
        tuple: A tuple containing:
            - loss_with_sprinklers (float): Average property loss with sprinklers.
            - reduction_percentage (float): Percentage reduction in property loss.
    """
    # Validate input
    if loss_without_sprinklers < 0:
        raise ValueError("Property loss cannot be negative.")

    # Calculate loss with sprinklers
    reduction_percentage = 71  # Reduction percentage as per statistic
    loss_with_sprinklers = loss_without_sprinklers * (1 - reduction_percentage / 100)

    return loss_with_sprinklers, reduction_percentage


def main():
    """
    Main function to run the script. Prompts the user for input and calculates the property
    loss with sprinklers present.
    """
    try:
        # Prompt user for input
        loss_without_sprinklers = float(input("Enter the average property loss per fire without sprinklers ($): "))

        # Perform calculation
        loss_with_sprinklers, reduction_percentage = calculate_loss_with_sprinklers(loss_without_sprinklers)

        # Display results
        print(f"\nAverage property loss without sprinklers: ${loss_without_sprinklers:,.2f}")
        print(f"Average property loss with sprinklers: ${loss_with_sprinklers:,.2f}")
        print(f"Reduction in property loss: {reduction_percentage}%")

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
