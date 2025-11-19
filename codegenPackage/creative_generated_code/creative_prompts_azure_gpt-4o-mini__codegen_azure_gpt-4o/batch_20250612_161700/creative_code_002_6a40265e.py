"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villapanorea.com
Prompt: Create a function that calculates the total cost for a stay at Villa Panorea based on the number of nights and the type of accommodation selected.
Generated: DETERMINISTIC_6a40265e4eda7845
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_cost(num_nights, accommodation_type):
    """
    Calculate the total cost for a stay at Villa Panorea based on the number of nights 
    and the type of accommodation selected.

    Parameters:
        num_nights (int): The number of nights for the stay.
        accommodation_type (str): The type of accommodation selected 
                                  ('standard', 'deluxe', or 'suite').

    Returns:
        float: The total cost of the stay.

    Raises:
        ValueError: If num_nights is negative or accommodation_type is invalid.
    """
    # Define the nightly rates for each accommodation type
    nightly_rates = {
        'standard': 100.0,  # Standard rate per night
        'deluxe': 150.0,   # Deluxe rate per night
        'suite': 250.0     # Suite rate per night
    }

    # Input validation
    if not isinstance(num_nights, int) or num_nights < 0:
        raise ValueError("Number of nights must be a non-negative integer.")
    
    if accommodation_type not in nightly_rates:
        raise ValueError(
            "Invalid accommodation type. Choose from 'standard', 'deluxe', or 'suite'."
        )

    # Calculate the total cost
    total_cost = num_nights * nightly_rates[accommodation_type]

    return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Inputs
        nights = 3
        accommodation = "deluxe"

        # Calculate and display the total cost
        cost = calculate_total_cost(nights, accommodation)
        print(f"Total cost for {nights} nights in {accommodation} accommodation: ${cost:.2f}")

    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```
