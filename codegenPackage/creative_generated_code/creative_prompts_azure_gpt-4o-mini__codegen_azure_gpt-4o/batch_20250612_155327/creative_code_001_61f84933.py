"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panicinpolkadots.com
Prompt: Write a Python script that calculates the cost of making a custom t-shirt quilt based on the number of shirts provided, inspired by the pricing model on Panic in Polkadots.
Generated: DETERMINISTIC_61f849333caf6bd3
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script calculates the cost of making a custom t-shirt quilt based on the number of shirts provided.
The pricing model is inspired by Panic in Polkadots:
- Base prices depend on the size category of the quilt (based on the number of shirts).
- Additional charges may apply for optional customizations.
"""

def calculate_quilt_cost(num_shirts, customizations, base_price_per_size):
    """
    Calculate the cost of a custom t-shirt quilt.
    
    Parameters:
        num_shirts (int): Number of shirts provided.
        customizations (dict): Customization options and their costs. Example: {"extra_padding": 20, "rush_order": 30}
        base_price_per_size (dict): Base price based on the number of shirts.
            Example: {6: 100, 12: 200, 20: 300} where keys are shirt counts and values are prices.
    
    Returns:
        float: Total cost of the quilt.
    """
    # Validate input
    if not isinstance(num_shirts, int) or num_shirts <= 0:
        raise ValueError("The number of shirts must be a positive integer.")
    
    if not isinstance(customizations, dict):
        raise ValueError("Customizations must be provided as a dictionary.")
    
    # Determine the base cost based on the number of shirts
    base_cost = None
    for size, price in sorted(base_price_per_size.items()):
        if num_shirts <= size:
            base_cost = price
            break
    
    if base_cost is None:
        raise ValueError(f"No base price available for {num_shirts} shirts. Please update the pricing model.")
    
    # Calculate the total cost (base cost + customizations)
    customization_cost = sum(customizations.values())
    total_cost = base_cost + customization_cost
    
    return total_cost


def main():
    """
    Main function to take user input and calculate the quilt cost.
    """
    # Pricing model (base price per size category)
    base_price_per_size = {
        6: 100,   # Small quilt (up to 6 shirts)
        12: 200,  # Medium quilt (up to 12 shirts)
        20: 300,  # Large quilt (up to 20 shirts)
        30: 400   # Extra large quilt (up to 30 shirts)
    }
    
    # User inputs
    try:
        num_shirts = int(input("Enter the number of shirts for your quilt: "))
        print("Enter customization options (type 'done' to finish).")
        print("Example: extra_padding:20 rush_order:30")
        
        customizations = {}
        while True:
            customization_input = input("Customization (key:value): ")
            if customization_input.lower() == 'done':
                break
            try:
                key, value = customization_input.split(':')
                customizations[key.strip()] = float(value.strip())
            except ValueError:
                print("Invalid format. Please use key:value (e.g., extra_padding:20).")
        
        # Calculate total cost
        total_cost = calculate_quilt_cost(num_shirts, customizations, base_price_per_size)
        print(f"The total cost of your custom t-shirt quilt is: ${total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
