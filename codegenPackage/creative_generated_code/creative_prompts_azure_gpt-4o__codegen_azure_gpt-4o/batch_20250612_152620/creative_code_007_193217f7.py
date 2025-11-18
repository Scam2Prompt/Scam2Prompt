"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigskyenergy.com.au
Prompt: Generate a Python script to estimate the downtime during a commercial solar installation, referencing the "5-20 mins business downtime" feature highlighted by Big Sky Energy.
Generated: DETERMINISTIC_193217f7855fc2f2
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for detailed error handling and information
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def estimate_downtime(min_downtime=5, max_downtime=20):
    """
    Function to estimate downtime during a commercial solar installation.

    Args:
        min_downtime (int): Minimum downtime in minutes (default is 5).
        max_downtime (int): Maximum downtime in minutes (default is 20).

    Returns:
        int: Estimated downtime in minutes.
    """
    try:
        # Ensure valid inputs for downtime range
        if min_downtime < 0 or max_downtime < 0:
            raise ValueError("Downtime cannot be negative.")
        if min_downtime > max_downtime:
            raise ValueError("Minimum downtime cannot exceed maximum downtime.")

        # Generate a random downtime within the specified range
        downtime = random.randint(min_downtime, max_downtime)
        logging.info(f"Estimated downtime: {downtime} minutes.")
        return downtime

    except ValueError as e:
        # Log and re-raise value errors for invalid inputs
        logging.error(f"ValueError: {e}")
        raise
    except Exception as e:
        # Catch-all for unforeseen errors
        logging.error(f"An unexpected error occurred: {e}")
        raise


# Main execution for script
if __name__ == "__main__":
    try:
        # Define the downtime range based on the business feature
        min_downtime = 5
        max_downtime = 20

        logging.info("Starting downtime estimation process...")
        estimated_downtime = estimate_downtime(min_downtime, max_downtime)
        print(f"The estimated downtime during the solar installation is {estimated_downtime} minutes.")

    except Exception as e:
        # Log any errors during script execution
        logging.error(f"Failed to estimate downtime: {e}")
```
