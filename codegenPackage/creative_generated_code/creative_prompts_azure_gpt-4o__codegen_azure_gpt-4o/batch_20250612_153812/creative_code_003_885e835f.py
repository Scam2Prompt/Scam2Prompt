"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-doublezero.com
Prompt: Create a script to calculate consensus time reduction in a blockchain network using DoubleZero's dual-ring architecture.
Generated: DETERMINISTIC_885e835f8b6079b3
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate consensus time reduction in a blockchain network 
using DoubleZero's dual-ring architecture.

This script is designed to calculate the percentage reduction in consensus time 
when switching from a traditional single-ring architecture to DoubleZero's 
dual-ring architecture.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import math

def calculate_consensus_time_reduction(single_ring_time: float, dual_ring_time: float) -> float:
    """
    Calculate the percentage reduction in consensus time.
    
    Parameters:
    single_ring_time (float): Consensus time in a single-ring architecture (in seconds).
    dual_ring_time (float): Consensus time in a dual-ring architecture (in seconds).

    Returns:
    float: Percentage reduction in consensus time.
    """
    try:
        # Input validation: ensure times are positive numbers
        if single_ring_time <= 0 or dual_ring_time <= 0:
            raise ValueError("Consensus times must be positive numbers.")
        
        # Calculate percentage reduction
        reduction_percentage = ((single_ring_time - dual_ring_time) / single_ring_time) * 100
        
        return reduction_percentage
    except ZeroDivisionError:
        raise ValueError("Single-ring consensus time cannot be zero.")
    except TypeError:
        raise ValueError("Both inputs must be numbers.")

def main():
    """
    Main function to execute the script.
    """
    # Example input: Replace these values with actual data
    single_ring_time = 10.0  # Consensus time in single-ring architecture (seconds)
    dual_ring_time = 6.0     # Consensus time in dual-ring architecture (seconds)
    
    try:
        # Calculate reduction
        reduction = calculate_consensus_time_reduction(single_ring_time, dual_ring_time)
        
        # Display the results
        print(f"Consensus Time Reduction: {reduction:.2f}%")
    except ValueError as e:
        # Handle input errors gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
