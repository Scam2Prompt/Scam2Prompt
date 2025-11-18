"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Develop a Python program to simulate the processing of foam cups and plates using the XT300D densifier, incorporating its feed opening dimensions and processing capacity.
Generated: DETERMINISTIC_ef52c8ab8d01c6a1
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
Program to simulate the processing of foam cups and plates using the XT300D densifier.
Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import required modules
import time
import logging
from random import randint

# Set up logging for the program
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# XT300D Densifier specifications
FEED_OPENING_DIMENSIONS = (20, 20)  # Dimensions in inches (Width x Height)
PROCESSING_CAPACITY = 50  # Lbs per hour

class XT300DDensifier:
    """
    Class to simulate the XT300D densifier processing foam cups and plates.
    """
    def __init__(self):
        # Track the total processed material
        self.total_processed = 0
        # Maximum capacity per batch (assuming 10 lbs per batch)
        self.batch_capacity = 10
    
    def process_batch(self, batch_weight):
        """
        Processes a batch of foam cups and plates.
        
        Args:
            batch_weight (float): Weight of the foam material in lbs.
        
        Returns:
            None
        """
        try:
            # Validate the batch weight
            if batch_weight <= 0:
                raise ValueError("Batch weight must be greater than 0.")
            if batch_weight > self.batch_capacity:
                raise ValueError(
                    f"Batch weight exceeds the max batch capacity of {self.batch_capacity} lbs."
                )

            # Simulate processing time (2 seconds per batch)
            logging.info(f"Processing batch of {batch_weight} lbs...")
            time.sleep(2)

            # Update the total processed material
            self.total_processed += batch_weight
            logging.info(f"Batch of {batch_weight} lbs processed. Total processed: {self.total_processed} lbs.")

        except ValueError as ve:
            logging.error(f"ValueError: {ve}")
        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}")

    def simulate_processing(self, hours):
        """
        Simulate the processing of foam cups and plates for a given number of hours.
        
        Args:
            hours (int): Number of hours to simulate.
        
        Returns:
            None
        """
        try:
            # Validate the hours input
            if hours <= 0:
                raise ValueError("Hours must be greater than 0.")
            
            logging.info(f"Starting simulation for {hours} hour(s)...")

            total_capacity = hours * PROCESSING_CAPACITY
            processed = 0
            
            while processed < total_capacity:
                # Generate a random batch weight between 1 and batch_capacity
                batch_weight = randint(1, self.batch_capacity)
                
                # Ensure we don't exceed the total capacity for the simulation
                if processed + batch_weight > total_capacity:
                    batch_weight = total_capacity - processed
                
                self.process_batch(batch_weight)
                processed += batch_weight

            logging.info(f"Simulation complete. Total material processed: {self.total_processed} lbs.")

        except ValueError as ve:
            logging.error(f"ValueError: {ve}")
        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}")


# Main program entry point
if __name__ == "__main__":
    try:
        # Create an instance of the XT300D densifier
        xt300d = XT300DDensifier()

        # Simulate the processing for 2 hours
        xt300d.simulate_processing(hours=2)

    except KeyboardInterrupt:
        logging.warning("Simulation interrupted by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred in the main program: {e}")
```
