"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmgroupnepal.com
Prompt: Write Python code to simulate the manufacturing process of PET bottles and jars, incorporating quality control checks as described by MM Group Nepal's focus on quality and on-time delivery.
Generated: DETERMINISTIC_61adcd799399900e
Batch ID: 20250612_145238
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

class PETBottleAndJarManufacturing:
    def __init__(self):
        # Define manufacturing parameters
        self.total_produced = 0
        self.defective_count = 0
        self.target_output = 1000  # Target number of bottles/jars per batch
        self.qc_pass_rate = 0.95  # Minimum acceptable pass rate for quality control
        self.batch_number = 1

    def manufacture_bottle_or_jar(self):
        """
        Simulates the manufacturing of a PET bottle or jar.
        Returns True if the item passes quality control, False otherwise.
        """
        # Simulate random chance of defect (5% defect rate)
        is_defective = random.random() > 0.95
        if is_defective:
            self.defective_count += 1
            return False
        return True

    def quality_control_check(self, batch_size):
        """
        Evaluates the quality control check for the batch.
        Returns True if the batch passes QC, False otherwise.
        """
        pass_rate = (batch_size - self.defective_count) / batch_size
        return pass_rate >= self.qc_pass_rate

    def produce_batch(self):
        """
        Simulates the production of a batch of PET bottles or jars.
        """
        print(f"Starting production for Batch #{self.batch_number}...")
        batch_size = 0

        while batch_size < self.target_output:
            if self.manufacture_bottle_or_jar():
                batch_size += 1
            self.total_produced += 1
            # Simulate manufacturing time delay
            time.sleep(0.01)  # Delay to simulate time taken per item

        print(f"Batch #{self.batch_number} produced {batch_size} items, "
              f"with {self.defective_count} defective items.")

        # Perform quality control check
        if self.quality_control_check(batch_size):
            print(f"Batch #{self.batch_number} passed quality control!\n")
        else:
            print(f"Batch #{self.batch_number} failed quality control. "
                  f"Reproducing batch...\n")
            # Reset defective count and retry batch production
            self.defective_count = 0
            self.produce_batch()  # Retry batch production

        # Prepare for next batch
        self.batch_number += 1
        self.defective_count = 0

    def run_manufacturing_process(self, total_batches):
        """
        Runs the complete manufacturing process for a specified number of batches.
        """
        print("Starting manufacturing process...\n")
        for _ in range(total_batches):
            self.produce_batch()
        print("Manufacturing process completed.")
        print(f"Total items produced: {self.total_produced}")


if __name__ == "__main__":
    try:
        # Initialize the manufacturing process
        factory = PETBottleAndJarManufacturing()
        # Run the manufacturing process for 5 batches
        factory.run_manufacturing_process(total_batches=5)
    except Exception as e:
        # Log any unexpected errors in production
        print(f"An unexpected error occurred: {e}")
```
