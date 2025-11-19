"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: Write a Python script that calculates the cost of making a custom t-shirt quilt based on the number of shirts provided, inspired by the pricing model on Panic in Polkadots.
Generated: DETERMINISTIC_61f849333caf6bd3
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the cost of making a custom t-shirt quilt based on the number of shirts provided.
Pricing model inspired by Panic in Polkadots.

Pricing Model:
- Base cost: $100 (includes labor and materials for up to 4 shirts)
- Additional cost per shirt beyond 4: $20 per shirt
- Optional border: $50
- Optional backing upgrade: $75
"""

def calculate_quilt_cost(num_shirts, add_border=False, upgrade_backing=False):
    """
    Calculate the cost of a custom t-shirt quilt.

    Parameters:
        num_shirts (int): Number of t-shirts to be used in the quilt.
        add_border (bool): Whether to add a decorative border to the quilt (default: False).
        upgrade_backing (bool): Whether to upgrade the backing material (default: False).

    Returns:
        float: Total cost of the quilt.
    """
    try:
        # Validate input
        if not isinstance(num_shirts, int) or num_shirts <= 0:
            raise ValueError("Number of shirts must be a positive integer.")

        # Base cost for up to 4 shirts
        base_cost = 100

        # Additional cost for shirts beyond 4
        additional_shirts = max(0, num_shirts - 4)
        additional_cost = additional_shirts * 20

        # Optional features
        border_cost = 50 if add_border else 0
        backing_cost = 75 if upgrade_backing else 0

        # Calculate total cost
        total_cost = base_cost + additional_cost + border_cost + backing_cost
        return total_cost

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    print("Welcome to the T-Shirt Quilt Cost Calculator!")
    
    try:
        # Get user input
        num_shirts = int(input("Enter the number of t-shirts to be used in the quilt: "))
        add_border = input("Do you want to add a decorative border? (yes/no): ").strip().lower() == "yes"
        upgrade_backing = input("Do you want to upgrade the backing material? (yes/no): ").strip().lower() == "yes"

        # Calculate cost
        total_cost = calculate_quilt_cost(num_shirts, add_border, upgrade_backing)

        if total_cost is not None:
            print(f"The total cost of your custom t-shirt quilt is: ${total_cost:.2f}")
        else:
            print("Failed to calculate the cost due to invalid input.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
