"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaperiyadh2.com
Prompt: Create a function that calculates the discounted price for products on Vape Riyadh 2, such as the Juul Pods and ELF BAR devices.
Generated: DETERMINISTIC_4fa8ada06e335eab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    """
    Calculate the discounted price of a product.

    Parameters:
    original_price (float): The original price of the product.
    discount_percentage (float): The discount percentage to be applied.

    Returns:
    float: The discounted price after applying the discount.

    Raises:
    ValueError: If the original price or discount percentage is negative.
    """
    # Validate input parameters
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative.")

    # Calculate the discount amount
    discount_amount = (discount_percentage / 100) * original_price
    
    # Calculate the final discounted price
    discounted_price = original_price - discount_amount
    
    # Ensure the discounted price does not go below zero
    return max(discounted_price, 0)


# Example usage:
if __name__ == "__main__":
    try:
        # Original prices of products (Juul Pods and ELF BAR devices)
        juul_pods_price = 20.00  # Example price for Juul Pods
        elf_bar_price = 15.00     # Example price for ELF BAR devices

        # Example discount percentages
        juul_discount = 10         # 10% discount
        elf_discount = 25          # 25% discount

        # Calculate discounted prices
        juul_discounted_price = calculate_discounted_price(juul_pods_price, juul_discount)
        elf_discounted_price = calculate_discounted_price(elf_bar_price, elf_discount)

        # Output results
        print(f"Discounted price for Juul Pods: ${juul_discounted_price:.2f}")
        print(f"Discounted price for ELF BAR: ${elf_discounted_price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
