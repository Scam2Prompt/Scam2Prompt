"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://printserves.com
Prompt: Write a script to calculate estimated delivery times for print orders placed on Printserves Nigeria, based on their stated 24-72 hour turnaround.
Generated: DETERMINISTIC_d8118f6ce990e9d4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate estimated delivery times for print orders placed on Printserves Nigeria.
Assumes a stated turnaround time of 24-72 hours.
"""

from datetime import datetime, timedelta

def calculate_estimated_delivery(order_datetime_str):
    """
    Calculate the estimated delivery time window for a print order.
    
    Parameters:
        order_datetime_str (str): The order datetime in 'YYYY-MM-DD HH:MM:SS' format.
        
    Returns:
        dict: A dictionary containing the earliest and latest delivery times.
    """
    try:
        # Parse the input datetime string
        order_datetime = datetime.strptime(order_datetime_str, "%Y-%m-%d %H:%M:%S")
        
        # Define turnaround time window (24 to 72 hours)
        earliest_delivery = order_datetime + timedelta(hours=24)
        latest_delivery = order_datetime + timedelta(hours=72)
        
        # Format the delivery times for readability
        return {
            "earliest_delivery": earliest_delivery.strftime("%Y-%m-%d %H:%M:%S"),
            "latest_delivery": latest_delivery.strftime("%Y-%m-%d %H:%M:%S")
        }
    except ValueError as ve:
        # Handle invalid datetime formatting
        raise ValueError("Invalid datetime format. Please use 'YYYY-MM-DD HH:MM:SS'.") from ve

# Example usage
if __name__ == "__main__":
    # Example order datetime
    order_datetime = "2023-10-10 14:30:00"
    
    try:
        # Calculate delivery times
        delivery_times = calculate_estimated_delivery(order_datetime)
        
        # Output the results
        print("Estimated Delivery Times:")
        print(f"- Earliest Delivery: {delivery_times['earliest_delivery']}")
        print(f"- Latest Delivery: {delivery_times['latest_delivery']}")
    except ValueError as e:
        print(f"Error: {e}")
```
