"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Write Python code to simulate the "fill-finish" process for vaccine production, as described on the CSL Seqirus UK website. Include steps for filling syringes and ensuring quality control.
Generated: DETERMINISTIC_d75c97124a6303b5
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import List, Dict, Optional

class VaccineBatch:
    """Represents a batch of vaccine doses being produced."""
    
    def __init__(self, batch_id: str, dose_count: int):
        self.batch_id = batch_id
        self.dose_count = dose_count
        self.filled_doses = 0
        self.defective_doses = 0
        self.status = "Pending"
        self.quality_checks = {
            "volume_check": False,
            "sterility_check": False,
            "label_check": False,
            "visual_inspection": False
        }
    
    def __str__(self) -> str:
        return (f"Batch {self.batch_id}: {self.filled_doses}/{self.dose_count} doses filled, "
                f"{self.defective_doses} defective, Status: {self.status}")

class FillFinishSimulator:
    """Simulates the fill-finish process for vaccine production."""
    
    def __init__(self):
        self.batches: Dict[str, VaccineBatch] = {}
        self.current_batch_id = 1
    
    def create_batch(self, dose_count: int) -> VaccineBatch:
        """Create a new vaccine batch with specified number of doses."""
        batch_id = f"VB{self.current_batch_id:04d}"
        self.current_batch_id += 1
        batch = VaccineBatch(batch_id, dose_count)
        self.batches[batch_id] = batch
        batch.status = "Created"
        print(f"Created new batch {batch_id} with {dose_count} doses")
        return batch
    
    def fill_syringes(self, batch_id: str) -> bool:
        """Simulate filling syringes for a batch."""
        batch = self.batches.get(batch_id)
        if not batch:
            print(f"Error: Batch {batch_id} not found")
            return False
        
        if batch.status != "Created":
            print(f"Error: Batch {batch_id} is not in 'Created' state")
            return False
        
        batch.status = "Filling"
        print(f"Starting syringe filling for batch {batch_id}")
        
        # Simulate filling process
        for i in range(batch.dose_count):
            time.sleep(0.1)  # Simulate time to fill one syringe
            if random.random() < 0.01:  # 1% chance of defect
                batch.defective_doses += 1
            else:
                batch.filled_doses += 1
            if (i + 1) % 100 == 0:
                print(f"Filled {i + 1}/{batch.dose_count} syringes")
        
        batch.status = "Filled"
        print(f"Completed filling for batch {batch_id}")
        return True
    
    def perform_quality_checks(self, batch_id: str) -> bool:
        """Perform quality control checks on a filled batch."""
        batch = self.batches.get(batch_id)
        if not batch:
            print(f"Error: Batch {batch_id} not found")
            return False
        
        if batch.status != "Filled":
            print(f"Error: Batch {batch_id} is not in 'Filled' state")
            return False
        
        batch.status = "Quality Control"
        print(f"Starting quality checks for batch {batch_id}")
        
        # Simulate quality checks
        time.sleep(1)  # Simulate time for checks
        batch.quality_checks["volume_check"] = random.random() > 0.05
        batch.quality_checks["sterility_check"] = random.random() > 0.02
        batch.quality_checks["label_check"] = random.random() > 0.03
        batch.quality_checks["visual_inspection"] = random.random() > 0.04
        
        all_passed = all(batch.quality_checks.values())
        if all_passed:
            batch.status = "Approved"
            print(f"Batch {batch_id} passed all quality checks")
        else:
            batch.status = "Rejected"
            print(f"Batch {batch_id} failed quality checks")
        
        return all_passed
    
    def package_batch(self, batch_id: str) -> bool:
        """Package an approved batch for distribution."""
        batch = self.batches.get(batch_id)
        if not batch:
            print(f"Error: Batch {batch_id} not found")
            return False
        
        if batch.status != "Approved":
            print(f"Error: Batch {batch_id} is not approved for packaging")
            return False
        
        batch.status = "Packaging"
        print(f"Packaging batch {batch_id}")
        
        time.sleep(2)  # Simulate packaging time
        batch.status = "Completed"
        print(f"Batch {batch_id} packaging completed and ready for distribution")
        return True
    
    def run_full_process(self, dose_count: int) -> bool:
        """Run the complete fill-finish process for a new batch."""
        batch = self.create_batch(dose_count)
        if not self.fill_syringes(batch.batch_id):
            return False
        if not self.perform_quality_checks(batch.batch_id):
            return False
        if batch.status == "Approved":
            return self.package_batch(batch.batch_id)
        return False
    
    def get_batch_status(self, batch_id: str) -> Optional[Dict]:
        """Get detailed status of a batch."""
        batch = self.batches.get(batch_id)
        if not batch:
            return None
        
        return {
            "batch_id": batch.batch_id,
            "dose_count": batch.dose_count,
            "filled_doses": batch.filled_doses,
            "defective_doses": batch.defective_doses,
            "status": batch.status,
            "quality_checks": batch.quality_checks
        }

# Example usage
if __name__ == "__main__":
    simulator = FillFinishSimulator()
    simulator.run_full_process(1000)
```
