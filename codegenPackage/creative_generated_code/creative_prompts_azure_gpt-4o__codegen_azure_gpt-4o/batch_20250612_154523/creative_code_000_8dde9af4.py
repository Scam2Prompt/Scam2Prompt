"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Write Python code to calculate IGV (Impuesto General a las Ventas) using the formulas and principles described in the "Calculadora IGV" section of AulaContable.
Generated: DETERMINISTIC_8dde9af4ac4441b3
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate IGV (Impuesto General a las Ventas)

# Constants
IGV_RATE = 0.18  # IGV rate as per Peru's tax law (18%)

def calculate_igv_and_total(base_price):
    """
    Calculate IGV (Impuesto General a las Ventas) and the total price including IGV.
    
    Parameters:
        base_price (float): The price of the item/service without IGV.
        
    Returns:
        dict: A dictionary containing the IGV amount and the total price including IGV.
    """
    if base_price < 0:
        raise ValueError("Base price cannot be negative.")
    
    # Calculate IGV amount
    igv_amount = base_price * IGV_RATE
    
    # Calculate total price including IGV
    total_price = base_price + igv_amount
    
    return {
        "IGV": round(igv_amount, 2),
        "Total Price": round(total_price, 2)
    }

def calculate_base_price_and_igv(total_price_including_igv):
    """
    Calculate the base price and IGV amount from the total price including IGV.
    
    Parameters:
        total_price_including_igv (float): The total price including IGV.
        
    Returns:
        dict: A dictionary containing the base price and the IGV amount.
    """
    if total_price_including_igv < 0:
        raise ValueError("Total price cannot be negative.")
    
    # Calculate base price (price without IGV)
    base_price = total_price_including_igv / (1 + IGV_RATE)
    
    # Calculate IGV amount
    igv_amount = total_price_including_igv - base_price
    
    return {
        "Base Price": round(base_price, 2),
        "IGV": round(igv_amount, 2)
    }

# Example usage:
if __name__ == "__main__":
    try:
        # Calculate IGV from base price
        base_price = 100.0  # Example base price
        result = calculate_igv_and_total(base_price)
        print(f"Base Price: {base_price}")
        print(f"IGV: {result['IGV']}")
        print(f"Total Price: {result['Total Price']}")
        
        # Calculate base price and IGV from total price including IGV
        total_price = 118.0  # Example total price including IGV
        result = calculate_base_price_and_igv(total_price)
        print(f"\nTotal Price: {total_price}")
        print(f"Base Price: {result['Base Price']}")
        print(f"IGV: {result['IGV']}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
