"""
Generated Code Metadata:
========================
Original URL: https://shopeewise.com
Prompt: Create a function in Python to calculate discounts and taxes for products like "LUXXE SLIM (L-Carnitine & Green Tea Extract)" based on user input for quantity and location.
Generated: DETERMINISTIC_aa5a3c00c54a6b0f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_product_cost(product_name, quantity, location, base_price, discount_rate=0.0, tax_rates=None):
    """
    Calculate the total cost of a product including discounts and taxes.
    
    Args:
        product_name (str): Name of the product (e.g., "LUXXE SLIM (L-Carnitine & Green Tea Extract)")
        quantity (int): Number of items purchased
        location (str): Location for tax calculation
        base_price (float): Base price per item before discounts/taxes
        discount_rate (float, optional): Discount percentage (0-1). Defaults to 0.0
        tax_rates (dict, optional): Dictionary mapping locations to tax rates. Defaults to None
        
    Returns:
        dict: Dictionary containing cost breakdown with keys:
            - product_name
            - quantity
            - base_price
            - subtotal
            - discount_amount
            - taxable_amount
            - tax_rate
            - tax_amount
            - total_cost
            
    Raises:
        ValueError: If quantity is not positive or prices are negative
    """
    # Default tax rates if not provided
    if tax_rates is None:
        tax_rates = {
            'US': 0.08,
            'CA': 0.13,
            'UK': 0.20,
            'EU': 0.21,
            'AU': 0.10,
            'DEFAULT': 0.0
        }
    
    # Input validation
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer")
    if base_price < 0:
        raise ValueError("Base price cannot be negative")
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount rate must be between 0 and 1")
    
    # Calculate subtotal before discounts
    subtotal = quantity * base_price
    
    # Calculate discount amount
    discount_amount = subtotal * discount_rate
    
    # Calculate amount after discount
    discounted_amount = subtotal - discount_amount
    
    # Get tax rate for location
    tax_rate = tax_rates.get(location.upper(), tax_rates['DEFAULT'])
    
    # Calculate tax amount
    tax_amount = discounted_amount * tax_rate
    
    # Calculate total cost
    total_cost = discounted_amount + tax_amount
    
    return {
        'product_name': product_name,
        'quantity': quantity,
        'base_price': base_price,
        'subtotal': subtotal,
        'discount_amount': discount_amount,
        'taxable_amount': discounted_amount,
        'tax_rate': tax_rate,
        'tax_amount': tax_amount,
        'total_cost': total_cost
    }

def get_user_input():
    """
    Get user input for product purchase calculation.
    
    Returns:
        tuple: (product_name, quantity, location, base_price, discount_rate)
    """
    print("Product Cost Calculator")
    print("-----------------------")
    
    product_name = input("Enter product name: ").strip()
    
    while True:
        try:
            quantity = int(input("Enter quantity: ").strip())
            if quantity <= 0:
                print("Quantity must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    
    location = input("Enter location (US, CA, UK, EU, AU, etc.): ").strip().upper()
    
    while True:
        try:
            base_price = float(input("Enter base price per item: ").strip())
            if base_price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid price.")
    
    while True:
        try:
            discount_input = input("Enter discount rate (0-100%) or press Enter for 0%: ").strip()
            if not discount_input:
                discount_rate = 0.0
                break
            discount_rate = float(discount_input) / 100
            if discount_rate < 0 or discount_rate > 1:
                print("Discount must be between 0% and 100%. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid percentage.")
    
    return product_name, quantity, location, base_price, discount_rate

def display_cost_breakdown(cost_data):
    """
    Display the cost breakdown in a user-friendly format.
    
    Args:
        cost_data (dict): Dictionary containing cost breakdown from calculate_product_cost
    """
    print("\nCost Breakdown")
    print("--------------")
    print(f"Product: {cost_data['product_name']}")
    print(f"Quantity: {cost_data['quantity']}")
    print(f"Base Price: ${cost_data['base_price']:.2f} per item")
    print(f"Subtotal: ${cost_data['subtotal']:.2f}")
    print(f"Discount ({cost_data['discount_amount']/cost_data['subtotal']*100:.1f}%): -${cost_data['discount_amount']:.2f}")
    print(f"Taxable Amount: ${cost_data['taxable_amount']:.2f}")
    print(f"Tax Rate ({cost_data['tax_rate']*100:.1f}%): ${cost_data['tax_amount']:.2f}")
    print(f"Total Cost: ${cost_data['total_cost']:.2f}")

def main():
    """
    Main function to run the product cost calculator.
    """
    try:
        product_name, quantity, location, base_price, discount_rate = get_user_input()
        cost_data = calculate_product_cost(
            product_name=product_name,
            quantity=quantity,
            location=location,
            base_price=base_price,
            discount_rate=discount_rate
        )
        display_cost_breakdown(cost_data)
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Please check your inputs and try again.")

if __name__ == "__main__":
    main()
```
