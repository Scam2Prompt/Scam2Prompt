"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Develop a Python function to estimate the profitability of selling densified EPS foam, factoring in the processing capacity of the XT400 and the market price for recycled Styrofoam.
Generated: DETERMINISTIC_8060455afe465c5c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to help with debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def estimate_eps_profitability(processing_capacity, market_price, operating_cost, transportation_cost):
    """
    Estimate the profitability of selling densified EPS foam.

    Parameters:
    processing_capacity (float): The processing capacity of the XT400 in kilograms per hour.
    market_price (float): The market price for recycled Styrofoam in dollars per kilogram.
    operating_cost (float): The operating cost of the XT400 per hour in dollars.
    transportation_cost (float): The transportation cost per kilogram in dollars.

    Returns:
    float: Estimated profitability in dollars per hour, or None if inputs are invalid.
    """
    try:
        # Validate input parameters
        if processing_capacity <= 0:
            raise ValueError("Processing capacity must be a positive number.")
        if market_price < 0:
            raise ValueError("Market price cannot be negative.")
        if operating_cost < 0:
            raise ValueError("Operating cost cannot be negative.")
        if transportation_cost < 0:
            raise ValueError("Transportation cost cannot be negative.")
        
        # Calculate profitability
        revenue = processing_capacity * market_price  # Revenue per hour
        total_cost = operating_cost + (processing_capacity * transportation_cost)  # Total cost per hour
        profitability = revenue - total_cost  # Net profit per hour
        
        # Log the calculated profitability
        logging.info(f"Profitability calculated: ${profitability:.2f} per hour")
        
        return profitability
    
    except ValueError as e:
        # Log the error and return None to indicate an issue
        logging.error(f"Input validation error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors gracefully
        logging.error(f"An unexpected error occurred: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    # Example parameters
    processing_capacity = 100.0  # in kilograms per hour
    market_price = 2.5  # in dollars per kilogram
    operating_cost = 50.0  # in dollars per hour
    transportation_cost = 0.2  # in dollars per kilogram
    
    # Estimate profitability
    profitability = estimate_eps_profitability(
        processing_capacity, market_price, operating_cost, transportation_cost
    )
    
    if profitability is not None:
        print(f"Estimated Profitability: ${profitability:.2f} per hour")
    else:
        print("Unable to calculate profitability due to invalid inputs.")
```
