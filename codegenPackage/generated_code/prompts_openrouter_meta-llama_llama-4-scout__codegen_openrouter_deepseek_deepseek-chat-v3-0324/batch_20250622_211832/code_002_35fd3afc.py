"""
Generated Code Metadata:
========================
Original URL: https://you-trip.ru
Prompt: Generate a code snippet to calculate the cost of a tour package, considering the 30% upfront payment and 70% payment 21 days before departure, as described on the YouTrip website.
Generated: DETERMINISTIC_35fd3afc8db06360
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_tour_cost(total_cost, days_until_departure):
    """
    Calculate the payment schedule for a tour package based on YouTrip's payment policy.
    
    Args:
        total_cost (float): Total cost of the tour package.
        days_until_departure (int): Number of days until the departure date.
    
    Returns:
        dict: A dictionary containing the upfront and final payment amounts,
              along with a message if the final payment is due.
    
    Raises:
        ValueError: If total_cost is negative or days_until_departure is invalid.
    """
    # Validate inputs
    if total_cost < 0:
        raise ValueError("Total cost cannot be negative.")
    if days_until_departure < 0:
        raise ValueError("Days until departure cannot be negative.")
    
    # Calculate payments
    upfront_payment = total_cost * 0.3
    final_payment = total_cost * 0.7
    
    payment_schedule = {
        'upfront_payment': upfront_payment,
        'final_payment': final_payment,
        'message': None
    }
    
    # Check if final payment is due
    if days_until_departure <= 21:
        payment_schedule['message'] = "Final payment is due now."
    
    return payment_schedule

# Example usage
if __name__ == "__main__":
    try:
        total_cost = 1000.0  # Example total cost
        days_until_departure = 30  # Example days until departure
        
        schedule = calculate_tour_cost(total_cost, days_until_departure)
        print(f"Upfront Payment (30%): ${schedule['upfront_payment']:.2f}")
        print(f"Final Payment (70%): ${schedule['final_payment']:.2f}")
        if schedule['message']:
            print(schedule['message'])
    except ValueError as e:
        print(f"Error: {e}")
```
