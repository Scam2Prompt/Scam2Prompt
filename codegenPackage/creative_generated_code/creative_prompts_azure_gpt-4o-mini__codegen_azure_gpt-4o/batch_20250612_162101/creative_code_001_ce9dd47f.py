"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Write a script to calculate the total cost of building a Londritech computer with specified components like the RTX3050 and 16GB RAM.
Generated: DETERMINISTIC_ce9dd47faabcf397
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Londritech Computer Cost Calculator
# This script calculates the total cost of building a Londritech computer based on specified components.

def calculate_total_cost(components, prices):
    """
    Calculate the total cost of the computer build.
    
    Parameters:
        components (list): A list of component names to be included in the build.
        prices (dict): A dictionary mapping component names to their respective prices.
        
    Returns:
        float: The total cost of the build.
    """
    total_cost = 0.0
    
    for component in components:
        if component in prices:
            total_cost += prices[component]
        else:
            raise ValueError(f"Component '{component}' not found in price list.")
    
    return total_cost


def main():
    """
    Main function to execute the Londritech computer cost calculation.
    """
    # Define prices for each component (example pricing)
    component_prices = {
        "RTX3050": 349.99,     # Price in USD
        "16GB RAM": 79.99,     # Price in USD
        "Intel i7 Processor": 319.99,  # Price in USD
        "512GB SSD": 69.99,    # Price in USD
        "750W PSU": 89.99,     # Price in USD
        "Case": 59.99          # Price in USD
    }
    
    # Components requested by the user
    selected_components = [
        "RTX3050",
        "16GB RAM",
        "Intel i7 Processor",
        "512GB SSD",
        "750W PSU",
        "Case"
    ]
    
    try:
        # Calculate the total cost
        total_cost = calculate_total_cost(selected_components, component_prices)
        print(f"The total cost of building the Londritech computer is: ${total_cost:.2f}")
    except ValueError as e:
        # Handle missing components gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
