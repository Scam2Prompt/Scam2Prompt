"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-homepage-kappa.vercel.app
Prompt: Write a function to calculate the cost of purchasing a specific number of pixels on a Starknet-powered platform, given a price of 0.00001 ETH per pixel.
Generated: DETERMINISTIC_f9313af48c83a335
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PixelPurchaseError(Exception):
    """Custom exception for errors related to pixel purchases."""
    pass

def calculate_pixel_cost(num_pixels: int, price_per_pixel: float = 0.00001) -> float:
    """
    Calculate the total cost of purchasing a specific number of pixels on a Starknet-powered platform.

    Parameters:
    num_pixels (int): The number of pixels to purchase.
    price_per_pixel (float): The price of each pixel in ETH (default is 0.00001 ETH).

    Returns:
    float: The total cost in ETH.

    Raises:
    PixelPurchaseError: If the number of pixels is negative or not an integer.
    """
    
    # Validate the input
    if not isinstance(num_pixels, int):
        raise PixelPurchaseError("Number of pixels must be an integer.")
    if num_pixels < 0:
        raise PixelPurchaseError("Number of pixels cannot be negative.")
    
    # Calculate total cost
    total_cost = num_pixels * price_per_pixel
    
    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        num_pixels_to_purchase = 1000  # Example input
        total_cost = calculate_pixel_cost(num_pixels_to_purchase)
        print(f"The total cost for purchasing {num_pixels_to_purchase} pixels is: {total_cost} ETH")
    except PixelPurchaseError as e:
        print(f"Error: {e}")
```
