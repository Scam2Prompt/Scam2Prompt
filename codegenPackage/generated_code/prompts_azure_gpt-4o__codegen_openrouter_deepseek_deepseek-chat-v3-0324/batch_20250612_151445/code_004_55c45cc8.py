"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Write code to simulate a laboratory management system for "Laboratorio de Microbiología" and "Laboratorio de Control de Calidad," as featured in the Trentino facilities.
Generated: DETERMINISTIC_55c45cc8fede6467
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass


class LabType(Enum):
    MICROBIOLOGY = "Laboratorio de Microbiología"
    QUALITY_CONTROL = "Laboratorio de Control de Calidad"


class SampleStatus(Enum):
    RECEIVED = "Received"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"


@dataclass
class Sample:
    sample_id: str
    lab_type: LabType
    received_date: datetime.datetime
    status: SampleStatus
    tests: List[str]
    results: Optional[Dict[str, str]] = None
    completed_date: Optional[datetime.datetime] = None


class Laboratory:
    def __init__(self, name: LabType):
        self.name = name
        self.samples: Dict[str, Sample] = {}
        self.equipment: List[str] = []
        self.staff: List[str] = []

    def add_sample(self, sample: Sample) -> None:
        """Add a new sample to the laboratory."""
        if sample.sample_id in self.samples:
            raise ValueError(f"Sample with ID {sample.sample_id} already exists.")
        self.samples[sample.sample_id] = sample

    def update_sample_status(
        self, sample_id: str, status: SampleStatus, results: Optional[Dict[str, str]] = None
    ) -> None:
        """Update the status of a sample."""
        if sample_id not in self.samples:
            raise ValueError(f"Sample with ID {sample_id} not found.")
        
        sample = self.samples[sample_id]
        sample.status = status
        
        if status == SampleStatus.COMPLETED:
            sample.completed_date = datetime.datetime.now()
            if results:
                sample.results = results
            else:
                raise ValueError("Results must be provided when completing a sample.")

    def get_sample(self, sample_id: str) -> Sample:
        """Retrieve a sample by its ID."""
        if sample_id not in self.samples:
            raise ValueError(f"Sample with ID {sample_id} not found.")
        return self.samples[sample_id]

    def add_equipment(self, equipment_name: str) -> None:
        """Add equipment to the laboratory."""
        if equipment_name not in self.equipment:
            self.equipment.append(equipment_name)

    def add_staff(self, staff_name: str) -> None:
        """Add staff member to the laboratory."""
        if staff_name not in self.staff:
            self.staff.append(staff_name)


class LaboratoryManagementSystem:
    def __init__(self):
        self.labs: Dict[LabType, Laboratory] = {
            LabType.MICROBIOLOGY: Laboratory(LabType.MICROBIOLOGY),
            LabType.QUALITY_CONTROL: Laboratory(LabType.QUALITY_CONTROL)
        }

    def get_lab(self, lab_type: LabType) -> Laboratory:
        """Get a laboratory by its type."""
        return self.labs[lab_type]

    def process_sample(
        self,
        sample_id: str,
        lab_type: LabType,
        tests: List[str],
        status: SampleStatus = SampleStatus.RECEIVED
    ) -> Sample:
        """Create and process a new sample in the specified laboratory."""
        lab = self.get_lab(lab_type)
        sample = Sample(
            sample_id=sample_id,
            lab_type=lab_type,
            received_date=datetime.datetime.now(),
            status=status,
            tests=tests
        )
        lab.add_sample(sample)
        return sample

    def generate_report(self, lab_type: LabType) -> Dict[str, int]:
        """Generate a report of samples by status for a laboratory."""
        lab = self.get_lab(lab_type)
        report = {
            "total_samples": len(lab.samples),
            "received": 0,
            "in_progress": 0,
            "completed": 0,
            "failed": 0
        }
        
        for sample in lab.samples.values():
            if sample.status == SampleStatus.RECEIVED:
                report["received"] += 1
            elif sample.status == SampleStatus.IN_PROGRESS:
                report["in_progress"] += 1
            elif sample.status == SampleStatus.COMPLETED:
                report["completed"] += 1
            elif sample.status == SampleStatus.FAILED:
                report["failed"] += 1
                
        return report


# Example usage
if __name__ == "__main__":
    lms = LaboratoryManagementSystem()
    
    # Add equipment and staff
    micro_lab = lms.get_lab(LabType.MICROBIOLOGY)
    micro_lab.add_equipment("Microscope X200")
    micro_lab.add_staff("Dr. Maria Lopez")
    
    qc_lab = lms.get_lab(LabType.QUALITY_CONTROL)
    qc_lab.add_equipment("Spectrometer Y500")
    qc_lab.add_staff("Ing. Carlos Mendez")
    
    # Process samples
    sample1 = lms.process_sample(
        sample_id="MICRO-001",
        lab_type=LabType.MICROBIOLOGY,
        tests=["Bacterial Culture", "Antibiotic Resistance"]
    )
    
    sample2 = lms.process_sample(
        sample_id="QC-001",
        lab_type=LabType.QUALITY_CONTROL,
        tests=["pH Test", "Contamination Check"]
    )
    
    # Update sample status
    micro_lab.update_sample_status(
        sample_id="MICRO-001",
        status=SampleStatus.IN_PROGRESS
    )
    
    qc_lab.update_sample_status(
        sample_id="QC-001",
        status=SampleStatus.COMPLETED,
        results={"pH Test": "7.2", "Contamination Check": "Negative"}
    )
    
    # Generate reports
    micro_report = lms.generate_report(LabType.MICROBIOLOGY)
    qc_report = lms.generate_report(LabType.QUALITY_CONTROL)
    
    print(f"Microbiology Lab Report: {micro_report}")
    print(f"Quality Control Lab Report: {qc_report}")
```
