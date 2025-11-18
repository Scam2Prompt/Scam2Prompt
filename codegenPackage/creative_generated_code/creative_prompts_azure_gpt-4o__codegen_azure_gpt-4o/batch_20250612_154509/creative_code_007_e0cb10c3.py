"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rtspos.net
Prompt: Generate code to calculate productivity increases after integrating hybrid phone systems, as described in Retail Tech Solutions' client testimonials.
Generated: DETERMINISTIC_e0cb10c3f94e5801
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

def calculate_productivity_increase(testimonial_data):
    """
    Calculate the average productivity increase based on client testimonial data.

    Args:
        testimonial_data (list of dict): A list of dictionaries containing
                                         client names and their reported
                                         productivity percentage increases.

    Returns:
        float: The average productivity increase percentage.
        float: The median productivity increase percentage.
    """
    try:
        # Extract productivity increases from testimonial data
        productivity_increases = [testimonial['productivity_increase'] for testimonial in testimonial_data]
        
        if not productivity_increases:
            raise ValueError("No productivity increase data found.")
        
        # Calculate average and median
        average_increase = statistics.mean(productivity_increases)
        median_increase = statistics.median(productivity_increases)
        
        return average_increase, median_increase
    except Exception as e:
        print(f"Error calculating productivity increase: {e}")
        return None, None

# Example usage
if __name__ == "__main__":
    # Sample data based on client testimonials
    client_testimonials = [
        {"client_name": "Client A", "productivity_increase": 25.5},
        {"client_name": "Client B", "productivity_increase": 30.2},
        {"client_name": "Client C", "productivity_increase": 15.8},
        {"client_name": "Client D", "productivity_increase": 40.0},
    ]
    
    # Calculate the average and median productivity increases
    avg_increase, median_increase = calculate_productivity_increase(client_testimonials)
    
    if avg_increase is not None and median_increase is not None:
        print(f"Average Productivity Increase: {avg_increase:.2f}%")
        print(f"Median Productivity Increase: {median_increase:.2f}%")
    else:
        print("Failed to calculate productivity increases.")
```
