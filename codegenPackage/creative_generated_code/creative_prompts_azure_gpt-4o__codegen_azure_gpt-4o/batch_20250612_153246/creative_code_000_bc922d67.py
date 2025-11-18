"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shop.zircon-ssd.com
Prompt: Write a Python script to compare the prices of different Zircon Z1 SSD models (128GB, 256GB, 512GB, 1TB) and recommend the best value for money based on price per GB.
Generated: DETERMINISTIC_bc922d674e3aed4f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_price_per_gb(storage_options):
    """
    Calculate the price per GB for each storage option.
    
    Parameters:
        storage_options (dict): A dictionary where keys are storage capacities in GB
                                and values are their corresponding prices in USD.
                                
    Returns:
        dict: A dictionary with storage capacities as keys and price per GB as values.
    """
    price_per_gb = {}
    for capacity, price in storage_options.items():
        try:
            # Calculate price per GB
            price_per_gb[capacity] = round(price / capacity, 2)
        except ZeroDivisionError:
            print(f"Error: Zero capacity detected for {capacity} GB, unable to calculate price per GB.")
            sys.exit(1)
        except TypeError:
            print(f"Error: Invalid data type detected for price or capacity in {capacity} GB.")
            sys.exit(1)
    return price_per_gb


def recommend_best_value(price_per_gb):
    """
    Recommend the best value based on the lowest price per GB.
    
    Parameters:
        price_per_gb (dict): A dictionary with storage capacities as keys and price per GB as values.
        
    Returns:
        tuple: A tuple containing the recommended storage capacity and its corresponding price per GB.
    """
    try:
        best_capacity = min(price_per_gb, key=price_per_gb.get)
        return best_capacity, price_per_gb[best_capacity]
    except ValueError:
        print("Error: Unable to determine the best value due to empty data.")
        sys.exit(1)


def main():
    """
    Main function to compare Zircon Z1 SSD prices and recommend the best value for money.
    """
    # Example price data for Zircon Z1 SSDs (in USD)
    storage_prices = {
        128: 29.99,  # Price for 128GB
        256: 49.99,  # Price for 256GB
        512: 89.99,  # Price for 512GB
        1024: 159.99 # Price for 1TB (1024GB)
    }
    
    # Calculate price per GB for each SSD model
    price_per_gb = calculate_price_per_gb(storage_prices)
    
    # Output the calculated price per GB
    print("Price per GB for each SSD model:")
    for capacity, price in price_per_gb.items():
        print(f"{capacity}GB: ${price} per GB")
    
    # Recommend the best value for money
    best_capacity, best_price_per_gb = recommend_best_value(price_per_gb)
    print("\nRecommendation:")
    print(f"The best value for money is the {best_capacity}GB model at ${best_price_per_gb} per GB.")


if __name__ == "__main__":
    main()
```
