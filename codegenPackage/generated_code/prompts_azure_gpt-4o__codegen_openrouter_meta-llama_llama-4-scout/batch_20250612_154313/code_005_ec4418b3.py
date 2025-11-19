"""
Generated Code Metadata:
========================
Original URL: https://devv.sellpass.io
Prompt: Write a function to handle errors when accessing resources, inspired by the error message mentioned on the Devv webpage.
Generated: DETERMINISTIC_ec4418b32d834a70
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Resource Access Error Handler
==============================

This module provides a function to handle errors when accessing resources.
"""

import logging
import time

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def access_resource(resource, max_retries=3, backoff_factor=1):
    """
    Attempts to access a resource with retries and exponential backoff.

    Args:
        resource: The resource to access.
        max_retries (int): The maximum number of retries. Defaults to 3.
        backoff_factor (int): The backoff factor for exponential backoff. Defaults to 1.

    Returns:
        The accessed resource.

    Raises:
        Exception: If all retries fail.
    """
    retries = 0
    delay = 0

    while retries <= max_retries:
        try:
            # Attempt to access the resource
            return resource()
        except Exception as e:
            # Log the error and retry if necessary
            logging.error(f"Error accessing resource: {str(e)}")

            if retries < max_retries:
                # Calculate the delay for the next retry
                delay = backoff_factor * (2 ** retries)
                logging.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
                retries += 1
            else:
                # Raise the exception if all retries fail
                logging.error(f"Failed to access resource after {max_retries} retries.")
                raise

def example_resource():
    # Simulate an unreliable resource
    import random
    if random.random() < 0.5:
        raise Exception("Resource access failed")
    else:
        return "Resource accessed successfully"

if __name__ == "__main__":
    try:
        result = access_resource(example_resource, max_retries=5)
        print(result)
    except Exception as e:
        logging.error(f"Error: {str(e)}")
```
