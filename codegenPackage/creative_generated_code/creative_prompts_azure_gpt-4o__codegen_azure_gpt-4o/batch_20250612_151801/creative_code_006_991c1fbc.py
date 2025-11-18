"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kubitz.com.br
Prompt: Develop code for a recycling plant that processes up to 150 tons/day, incorporating components like sack shredders, compactors, and magnetic separators, as described in Kubitz's automated plant configurations.
Generated: DETERMINISTIC_991c1fbcceb317c0
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Recycling Plant Processing System

This script simulates a recycling plant that processes up to 150 tons/day.
The system incorporates components such as sack shredders, compactors, and magnetic separators.
Each stage of processing is modeled as a function, ensuring modularity, scalability, and error handling.
"""

import logging

# Configure logging for monitoring and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
MAX_DAILY_CAPACITY = 150  # in tons

class ProcessingError(Exception):
    """Custom exception for handling processing errors."""
    pass

def check_capacity(input_tons):
    """
    Validate the input tons against the maximum daily capacity.

    Args:
        input_tons (float): Amount of material to be processed (in tons).

    Returns:
        float: Validated input tons.

    Raises:
        ProcessingError: If the input exceeds the maximum daily capacity.
    """
    if input_tons > MAX_DAILY_CAPACITY:
        raise ProcessingError("Input exceeds the maximum daily capacity of the plant.")
    if input_tons <= 0:
        raise ProcessingError("Input material must be greater than zero.")
    logging.info(f"Input validated: {input_tons} tons will be processed.")
    return input_tons

def sack_shredder(input_tons):
    """
    Simulate the sack shredding process.

    Args:
        input_tons (float): Amount of material to be processed (in tons).

    Returns:
        float: Amount of shredded material.

    Raises:
        ProcessingError: If shredding fails.
    """
    try:
        shredded_tons = input_tons * 0.95  # Assume 95% efficiency in shredding
        logging.info(f"Sack shredding completed: {shredded_tons:.2f} tons shredded.")
        return shredded_tons
    except Exception as e:
        raise ProcessingError(f"Sack shredding failed: {e}")

def magnetic_separator(input_tons):
    """
    Simulate the magnetic separation process.

    Args:
        input_tons (float): Amount of material to be processed (in tons).

    Returns:
        float: Amount of material after magnetic separation.

    Raises:
        ProcessingError: If magnetic separation fails.
    """
    try:
        separated_tons = input_tons * 0.90  # Assume 90% efficiency in separation
        logging.info(f"Magnetic separation completed: {separated_tons:.2f} tons separated.")
        return separated_tons
    except Exception as e:
        raise ProcessingError(f"Magnetic separation failed: {e}")

def compactor(input_tons):
    """
    Simulate the compacting process.

    Args:
        input_tons (float): Amount of material to be processed (in tons).

    Returns:
        float: Amount of compacted material.

    Raises:
        ProcessingError: If compacting fails.
    """
    try:
        compacted_tons = input_tons * 0.85  # Assume 85% efficiency in compacting
        logging.info(f"Compacting completed: {compacted_tons:.2f} tons compacted.")
        return compacted_tons
    except Exception as e:
        raise ProcessingError(f"Compacting failed: {e}")

def process_material(input_tons):
    """
    Simulate the entire recycling plant process.

    Args:
        input_tons (float): Amount of material to be processed (in tons).

    Returns:
        float: Final output of processed material.

    Raises:
        ProcessingError: If any stage fails.
    """
    try:
        input_tons = check_capacity(input_tons)
        shredded_tons = sack_shredder(input_tons)
        separated_tons = magnetic_separator(shredded_tons)
        compacted_tons = compactor(separated_tons)
        logging.info(f"Recycling process completed: {compacted_tons:.2f} tons fully processed.")
        return compacted_tons
    except ProcessingError as e:
        logging.error(f"Processing error: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    try:
        input_material = 120  # Input material in tons
        final_output = process_material(input_material)
        print(f"Final output: {final_output:.2f} tons")
    except ProcessingError as error:
        print(f"Failed to process material: {error}")
```
