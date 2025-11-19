"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Write a Python function that calculates the appropriate dumpster size needed for various types of waste removal, referencing the 10, 15, and 20 yard options from Junk in The Box ATL.
Generated: DETERMINISTIC_e144847f06fd3f57
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Tuple

def calculate_dumpster_size(waste_type: str, estimated_volume: float) -> Tuple[str, str]:
    """
    Calculate the appropriate dumpster size for waste removal.

    Parameters:
        waste_type (str): The type of waste (e.g., "household", "construction", "yard").
        estimated_volume (float): The estimated volume of waste in cubic yards.

    Returns:
        Tuple[str, str]: A tuple containing the recommended dumpster size and a message.
    """
    # Define available dumpster sizes
    dumpster_sizes = {
        "10 yard": 10,
        "15 yard": 15,
        "20 yard": 20
    }

    # Validate inputs
    if not isinstance(waste_type, str) or not isinstance(estimated_volume, (int, float)):
        return ("Error", "Invalid input. Please provide a valid waste type and estimated volume.")

    if estimated_volume <= 0:
        return ("Error", "Estimated volume must be greater than zero.")

    # Determine the appropriate dumpster size
    if estimated_volume <= dumpster_sizes["10 yard"]:
        return ("10 yard", "Recommended for small projects like household cleanouts or light yard waste.")
    elif estimated_volume <= dumpster_sizes["15 yard"]:
        return ("15 yard", "Recommended for medium projects like small construction jobs or moderate yard waste.")
    elif estimated_volume <= dumpster_sizes["20 yard"]:
        return ("20 yard", "Recommended for larger projects like major construction jobs or heavy yard waste.")
    else:
        return ("Error", "Estimated volume exceeds available dumpster sizes. Consider multiple dumpsters or consult Junk in The Box ATL.")

# Example usage
if __name__ == "__main__":
    # Test the function with sample inputs
    waste_type = "construction"
    estimated_volume = 12.5
    size, message = calculate_dumpster_size(waste_type, estimated_volume)
    print(f"Recommended Dumpster Size: {size}")
    print(f"Message: {message}")
```
