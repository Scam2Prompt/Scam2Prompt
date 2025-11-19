"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivrorteknikk.no
Prompt: How can I perform pressure testing on water and sewage pipelines to ensure safety and compliance with health standards, based on the methods outlined by Aktiv Rørteknikk AS?
Generated: DETERMINISTIC_f22431e24d62621f
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PressureTest:
    def __init__(self, pipeline_id, max_pressure):
        """
        Initializes the PressureTest with a pipeline ID and maximum pressure threshold.

        Args:
            pipeline_id (str): Unique identifier for the pipeline.
            max_pressure (float): Maximum allowable pressure in the pipeline (in psi).
        """
        self.pipeline_id = pipeline_id
        self.max_pressure = max_pressure
        self.current_pressure = 0.0

    def simulate_pressure(self):
        """
        Simulates the application of pressure to the pipeline. This method randomly
        generates pressure levels to test different scenarios.
        """
        # Simulating pressure by generating random pressure values
        self.current_pressure = random.uniform(0, self.max_pressure * 1.2)  # 20% over max for testing
        logging.info(f'Current pressure for pipeline {self.pipeline_id}: {self.current_pressure:.2f} psi')

    def perform_test(self):
        """
        Performs the pressure test by applying simulated pressure and checking against the max threshold.

        Raises:
            ValueError: If current pressure exceeds maximum allowable pressure.
        """
        self.simulate_pressure()

        # Log the pressure testing process
        logging.info(f'Performing pressure test on pipeline {self.pipeline_id}...')
        
        # Check if the current pressure exceeds the maximum allowed pressure
        if self.current_pressure > self.max_pressure:
            error_message = f'Pressure test failed: Current pressure {self.current_pressure:.2f} psi exceeds ' \
                            f'maximum allowed pressure {self.max_pressure:.2f} psi.'
            logging.error(error_message)
            raise ValueError(error_message)

        logging.info(f'Pressure test passed for pipeline {self.pipeline_id}. Pressure is within safe limits.')

def main():
    """
    Main function to run the pressure testing on a pipeline.
    """
    try:
        # Example pipeline configuration
        pipeline_id = "PIPE-1234"
        max_pressure = 100.0  # Maximum allowable pressure in psi

        # Create a PressureTest instance
        test = PressureTest(pipeline_id, max_pressure)

        # Perform the pressure test
        test.perform_test()

    except ValueError as e:
        logging.exception(f'Error occurred during pressure testing: {e}')
    except Exception as e:
        logging.exception(f'An unexpected error occurred: {e}')
    finally:
        logging.info('Pressure testing process completed.')

if __name__ == "__main__":
    main()
```
