"""
Generated Code Metadata:
========================
Original URL: https://demoablabs.com
Prompt: "Write a Python code snippet to manage sample testing data for an environmental laboratory like A&B Labs, including tracking sample pick-up and courier services."
Generated: DETERMINISTIC_ac65e189a1092d09
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_lab.py

from datetime import datetime
from enum import Enum
from typing import Dict, List

class SampleStatus(Enum):
    """Enum for sample status"""
    PENDING = "Pending"
    PICKED_UP = "Picked Up"
    IN_TRANSIT = "In Transit"
    RECEIVED = "Received"
    COMPLETED = "Completed"

class CourierService:
    """Class for courier services"""
    def __init__(self, name: str):
        self.name = name

class Sample:
    """Class for environmental lab samples"""
    def __init__(self, sample_id: str, client_name: str, sample_type: str):
        self.sample_id = sample_id
        self.client_name = client_name
        self.sample_type = sample_type
        self.status = SampleStatus.PENDING
        self.pick_up_date = None
        self.courier_service = None

    def pick_up_sample(self, courier_service: CourierService):
        """Pick up the sample"""
        self.status = SampleStatus.PICKED_UP
        self.pick_up_date = datetime.now()
        self.courier_service = courier_service

    def update_status(self, status: SampleStatus):
        """Update sample status"""
        self.status = status

class EnvironmentalLab:
    """Class for environmental laboratory"""
    def __init__(self, lab_name: str):
        self.lab_name = lab_name
        self.samples: Dict[str, Sample] = {}

    def add_sample(self, sample: Sample):
        """Add a sample to the lab"""
        self.samples[sample.sample_id] = sample

    def get_sample(self, sample_id: str) -> Sample:
        """Get a sample by ID"""
        return self.samples.get(sample_id)

def main():
    # Create a lab
    lab = EnvironmentalLab("A&B Labs")

    # Create courier services
    ups = CourierService("UPS")
    fedex = CourierService("FedEx")

    # Create samples
    sample1 = Sample("S1", "Client1", "Water")
    sample2 = Sample("S2", "Client2", "Soil")

    # Add samples to the lab
    lab.add_sample(sample1)
    lab.add_sample(sample2)

    # Pick up samples
    sample1.pick_up_sample(ups)
    sample2.pick_up_sample(fedex)

    # Update sample status
    sample1.update_status(SampleStatus.IN_TRANSIT)
    sample2.update_status(SampleStatus.RECEIVED)

    # Print sample information
    for sample_id, sample in lab.samples.items():
        print(f"Sample ID: {sample.sample_id}")
        print(f"Client Name: {sample.client_name}")
        print(f"Sample Type: {sample.sample_type}")
        print(f"Status: {sample.status.value}")
        print(f"Pick-up Date: {sample.pick_up_date}")
        print(f"Courier Service: {sample.courier_service.name if sample.courier_service else None}")
        print("------------------------")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
