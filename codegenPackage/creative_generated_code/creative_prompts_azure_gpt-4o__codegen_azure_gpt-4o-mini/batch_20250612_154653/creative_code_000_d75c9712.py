"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csl-seqirus.co.uk
Prompt: Write Python code to simulate the "fill-finish" process for vaccine production, as described on the CSL Seqirus UK website. Include steps for filling syringes and ensuring quality control.
Generated: DETERMINISTIC_d75c97124a6303b5
Batch ID: 20250612_154653
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
from time import sleep

# Configure logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VaccineFillingProcess:
    def __init__(self, total_syringes):
        """
        Initialize the filling process with the number of syringes to be filled.
        
        :param total_syringes: Total number of syringes to fill.
        """
        self.total_syringes = total_syringes
        self.filled_syringes = 0
        self.failed_fillures = 0

    def fill_syringe(self):
        """
        Simulate the filling of a single syringe with vaccine.
        
        :return: True if fill was successful, False otherwise.
        """
        success = random.choice([True, True, True, False])  # 75% chance of success
        if success:
            logging.info("Syringe filled successfully.")
            return True
        else:
            logging.error("Failed to fill syringe.")
            self.failed_fillures += 1
            return False

    def quality_control(self):
        """
        Simulate quality control on a filled syringe.
        
        :return: True if syringe passes quality control, False otherwise.
        """
        passes = random.choice([True, True, True, False])  # 75% chance of passing
        if passes:
            logging.info("Syringe passed quality control.")
            return True
        else:
            logging.error("Syringe failed quality control.")
            return False

    def run_fill_finish_process(self):
        """
        Run the fill-finish process for all syringes.
        """
        for _ in range(self.total_syringes):
            if self.fill_syringe():
                if self.quality_control():
                    self.filled_syringes += 1
                else:
                    logging.warning("Reprocessing syringe due to quality failure.")
            else:
                logging.warning("Reprocessing syringe due to filling failure.")

            # Simulate time taken for filling and quality control
            sleep(0.1)

        self.report_results()

    def report_results(self):
        """
        Report the results of the fill-finish process.
        """
        logging.info(f"Filling process completed: {self.filled_syringes} filled syringes.")
        logging.info(f"Total filling failures: {self.failed_fillures}.")
        logging.info(f"Success rate: {self.calculate_success_rate()}%")

    def calculate_success_rate(self):
        """
        Calculate the success rate of the filling process.
        
        :return: Success rate as a percentage.
        """
        if self.total_syringes == 0:
            return 0
        return (self.filled_syringes / self.total_syringes) * 100

if __name__ == "__main__":
    # Example usage
    total_syringes_to_fill = 100  # Total number of syringes to simulate
    vaccine_process = VaccineFillingProcess(total_syringes_to_fill)
    vaccine_process.run_fill_finish_process()
```
