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
from dataclasses import dataclass
from enum import Enum
from typing import List

class VaccineStatus(Enum):
    """Enum for vaccine status"""
    AVAILABLE = 1
    IN_PROCESS = 2
    COMPLETE = 3
    REJECTED = 4

@dataclass
class Syringe:
    """Class to represent a syringe"""
    id: int
    vaccine_status: VaccineStatus
    volume: float  # in ml

class FillFinishProcess:
    """Class to simulate fill-finish process for vaccine production"""

    def __init__(self):
        self.syringes: List[Syringe] = []
        self.next_syringe_id: int = 1

    def fill_syringe(self, volume: float) -> Syringe:
        """Fill a syringe with vaccine"""
        if volume <= 0:
            raise ValueError("Volume must be greater than zero")

        syringe = Syringe(self.next_syringe_id, VaccineStatus.IN_PROCESS, volume)
        self.syringes.append(syringe)
        self.next_syringe_id += 1
        return syringe

    def quality_control(self, syringe_id: int) -> bool:
        """Perform quality control on a syringe"""
        for syringe in self.syringes:
            if syringe.id == syringe_id:
                if syringe.vaccine_status == VaccineStatus.IN_PROCESS:
                    # Simulate quality control check
                    if syringe.volume > 0.9 and syringe.volume < 1.1:  # assume 1ml +/- 10%
                        syringe.vaccine_status = VaccineStatus.COMPLETE
                        return True
                    else:
                        syringe.vaccine_status = VaccineStatus.REJECTED
                        return False
                else:
                    raise ValueError("Syringe is not in process")
        raise ValueError("Syringe not found")

    def get_syringe_status(self, syringe_id: int) -> VaccineStatus:
        """Get the status of a syringe"""
        for syringe in self.syringes:
            if syringe.id == syringe_id:
                return syringe.vaccine_status
        raise ValueError("Syringe not found")

def main():
    process = FillFinishProcess()

    try:
        # Fill 10 syringes
        for _ in range(10):
            syringe = process.fill_syringe(1.0)  # fill with 1ml
            print(f"Syringe {syringe.id} filled")

        # Perform quality control on syringes
        for syringe in process.syringes:
            if process.quality_control(syringe.id):
                print(f"Syringe {syringe.id} passed quality control")
            else:
                print(f"Syringe {syringe.id} failed quality control")

        # Print final status of syringes
        for syringe in process.syringes:
            print(f"Syringe {syringe.id} status: {syringe.vaccine_status.name}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
