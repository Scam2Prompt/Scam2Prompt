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
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_delivery_time(order_time: str) -> dict:
    """
    Calculate estimated delivery times for print orders.
    
    Args:
        order_time (str): The time the order was placed in the format 'YYYY-MM-DD HH:MM:SS'.
        
    Returns:
        dict: A dictionary containing the order time, 
              and estimated delivery times for minimum and maximum turnaround.
              
    Raises:
        ValueError: If the order_time is not in the correct format.
    """
    # Define turnaround time limits in hours
    MIN_TURNAROUND_HOURS = 24
    MAX_TURNAROUND_HOURS = 72
    
    try:
        # Parse the order time
        order_datetime = datetime.strptime(order_time, '%Y-%m-%d %H:%M:%S')
        
        # Calculate estimated delivery times
        min_delivery_time = order_datetime + timedelta(hours=MIN_TURNAROUND_HOURS)
        max_delivery_time = order_datetime + timedelta(hours=MAX_TURNAROUND_HOURS)
        
        # Create a result dictionary
        delivery_times = {
            'order_time': order_datetime.strftime('%Y-%m-%d %H:%M:%S'),
            'min_delivery_time': min_delivery_time.strftime('%Y-%m-%d %H:%M:%S'),
            'max_delivery_time': max_delivery_time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Log the calculated delivery times
        logging.info(f"Calculated delivery times: {delivery_times}")
        
        return delivery_times
    
    except ValueError as e:
        logging.error(f"Error in calculating delivery time: {e}")
        raise ValueError("Invalid order time format. Please use 'YYYY-MM-DD HH:MM:SS'.")

# Example usage
if __name__ == "__main__":
    order_time_input = '2023-10-01 14:30:00'  # Example order time
    try:
        delivery_estimates = calculate_delivery_time(order_time_input)
        print(delivery_estimates)
    except ValueError as e:
        print(e)
```
