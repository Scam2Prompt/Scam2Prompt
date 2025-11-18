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
def calculate_pixel_cost(num_pixels):
    """
    Calculate the cost of purchasing a specified number of pixels on a Starknet-powered platform.

    Args:
        num_pixels (int): The number of pixels to purchase.

    Returns:
        float: The cost in ETH for the specified number of pixels.

    Raises:
        ValueError: If the number of pixels is not a positive integer.
    """
    try:
        # Validate input - number of pixels must be a positive integer
        if not isinstance(num_pixels, int) or num_pixels <= 0:
            raise ValueError("Number of pixels must be a positive integer.")

        # Define cost per pixel (in ETH)
        cost_per_pixel = 0.00001

        # Calculate total cost
        total_cost = num_pixels * cost_per_pixel

        return total_cost

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
        raise
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
        raise


# Example usage:
if __name__ == "__main__":
    try:
        # Test with a valid number of pixels
        pixels_to_buy = 1000
        cost = calculate_pixel_cost(pixels_to_buy)
        print(f"The cost of purchasing {pixels_to_buy} pixels is {cost} ETH.")
    except Exception as e:
        print(f"Failed to calculate pixel cost: {e}")
```
