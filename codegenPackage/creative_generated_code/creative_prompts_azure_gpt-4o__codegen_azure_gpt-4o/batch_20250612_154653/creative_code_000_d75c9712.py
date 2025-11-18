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

class VaccineProduction:
    def __init__(self, batch_size):
        """
        Initialize vaccine production parameters.
        :param batch_size: Number of syringes to process in the batch.
        """
        self.batch_size = batch_size
        self.syringes = []
        self.quality_control_passed = []

    def fill_syringe(self):
        """
        Simulates the filling of a syringe with vaccine.
        Each syringe is assigned a random volume to simulate variability.
        Returns a dictionary representing a filled syringe.
        """
        syringe = {
            "id": len(self.syringes) + 1,
            "volume": round(random.uniform(0.95, 1.05), 3)  # Volume in milliliters
        }
        return syringe

    def quality_control(self, syringe):
        """
        Simulates a quality control check.
        A syringe passes if its volume is within the acceptable range (0.98 - 1.02 ml).
        :param syringe: Dictionary representing a syringe.
        :return: Boolean indicating whether the syringe passes quality control.
        """
        return 0.98 <= syringe["volume"] <= 1.02

    def simulate_fill_finish(self):
        """
        Simulates the fill-finish process for vaccine production.
        Includes filling syringes and performing quality control.
        """
        print(f"Starting fill-finish process for {self.batch_size} syringes...\n")

        # Filling syringes
        for _ in range(self.batch_size):
            syringe = self.fill_syringe()
            self.syringes.append(syringe)
            print(f"Syringe {syringe['id']} filled with {syringe['volume']} ml.")

        print("\nPerforming quality control...\n")

        # Quality control
        for syringe in self.syringes:
            if self.quality_control(syringe):
                self.quality_control_passed.append(syringe)
                print(f"Syringe {syringe['id']} passed quality control.")
            else:
                print(f"Syringe {syringe['id']} failed quality control (Volume: {syringe['volume']} ml).")

        # Final summary
        print("\nFill-finish process completed.")
        print(f"Syringes processed: {len(self.syringes)}")
        print(f"Syringes passing quality control: {len(self.quality_control_passed)}")
        print(f"Syringes failing quality control: {len(self.syringes) - len(self.quality_control_passed)}")

    def get_results(self):
        """
        Provides the results of the simulation.
        :return: Dictionary containing details of the syringes.
        """
        return {
            "total_syringes": len(self.syringes),
            "passed_quality_control": len(self.quality_control_passed),
            "failed_quality_control": len(self.syringes) - len(self.quality_control_passed),
            "details": self.syringes
        }


if __name__ == "__main__":
    try:
        # Set batch size for simulation
        batch_size = 10  # Example: Process 10 syringes

        # Initialize and run the simulation
        production = VaccineProduction(batch_size)
        production.simulate_fill_finish()

        # Optionally, retrieve detailed results
        results = production.get_results()
        print("\nDetailed Results:")
        print(results)

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
```
