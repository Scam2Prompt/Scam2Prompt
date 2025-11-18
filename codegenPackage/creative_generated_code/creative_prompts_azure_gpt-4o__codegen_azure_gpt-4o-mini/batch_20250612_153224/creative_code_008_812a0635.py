"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Write a script to calculate the average property loss reduction per fire when sprinklers are present, referencing the 71% statistic from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_812a063546356822
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

# Configure logging for better error tracking and information output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_average_property_loss_reduction():
    """
    Calculate the average property loss reduction per fire when sprinklers are present.

    Returns:
        float: The average property loss reduction as a percentage.
    """
    try:
        # Statistic from Independence Fire Sprinkler Company
        reduction_percentage = 71.0  # Represents 71% property loss reduction
        logging.info(f"Calculated average property loss reduction: {reduction_percentage}%")
        
        return reduction_percentage

    except Exception as e:
        logging.error("An error occurred while calculating property loss reduction: %s", e)
        return None

if __name__ == "__main__":
    # Entry point of the script
    average_loss_reduction = calculate_average_property_loss_reduction()
    
    if average_loss_reduction is not None:
        print(f"The average property loss reduction per fire when sprinklers are present is: {average_loss_reduction}%")
    else:
        print("Failed to calculate the average property loss reduction.")
```
