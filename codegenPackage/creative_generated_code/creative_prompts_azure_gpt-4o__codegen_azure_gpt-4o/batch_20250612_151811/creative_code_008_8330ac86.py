"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Generate code to calculate the cost reductions achieved by outsourcing credit valuation and collections, inspired by Summar Financial's factoring services.
Generated: DETERMINISTIC_8330ac866bd164bb
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_cost_reduction(internal_cost, outsourced_cost):
    """
    Calculate the cost reductions achieved by outsourcing services.
    
    Parameters:
        internal_cost (float): The cost associated with performing credit valuation and collections in-house.
        outsourced_cost (float): The cost associated with outsourcing these services.

    Returns:
        float: The cost reduction achieved through outsourcing.
    """
    try:
        # Validate input parameters
        if internal_cost < 0 or outsourced_cost < 0:
            raise ValueError("Costs cannot be negative.")

        # Calculate cost reduction
        cost_reduction = internal_cost - outsourced_cost
        return cost_reduction

    except TypeError as e:
        logging.error("Invalid input type: %s", e)
        raise TypeError("Both internal_cost and outsourced_cost must be numbers.") from e

    except ValueError as e:
        logging.error("Invalid input value: %s", e)
        raise

def main():
    """
    Main function to demonstrate the cost reduction calculation.
    """
    try:
        # Example costs (replace these with actual values or gather from user input/database)
        internal_cost = float(input("Enter the internal cost for credit valuation and collections: "))
        outsourced_cost = float(input("Enter the outsourced cost for these services: "))

        # Calculate cost reduction
        cost_reduction = calculate_cost_reduction(internal_cost, outsourced_cost)
        
        # Log and display the result
        logging.info("Internal cost: $%.2f", internal_cost)
        logging.info("Outsourced cost: $%.2f", outsourced_cost)
        logging.info("Cost reduction achieved: $%.2f", cost_reduction)

        print(f"Cost reduction achieved by outsourcing: ${cost_reduction:.2f}")

    except Exception as e:
        logging.error("An error occurred: %s", e)
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
