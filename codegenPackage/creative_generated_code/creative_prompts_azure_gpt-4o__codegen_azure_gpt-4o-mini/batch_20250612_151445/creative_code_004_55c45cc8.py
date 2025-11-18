"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Write code to simulate a laboratory management system for "Laboratorio de Microbiología" and "Laboratorio de Control de Calidad," as featured in the Trentino facilities.
Generated: DETERMINISTIC_55c45cc8fede6467
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Laboratory:
    """Base class for laboratories."""
    
    def __init__(self, name: str):
        self.name = name
        self.samples: List[Dict] = []  # List to hold sample information

    def add_sample(self, sample_id: str, description: str, date_collected: Optional[datetime.date] = None):
        """Add a new sample to the laboratory."""
        if not sample_id or not description:
            raise ValueError("Sample ID and description cannot be empty.")
        
        if date_collected is None:
            date_collected = datetime.date.today()
        
        sample = {
            "sample_id": sample_id,
            "description": description,
            "date_collected": date_collected,
            "results": None
        }
        self.samples.append(sample)
        print(f"Sample {sample_id} added to {self.name}.")

    def record_results(self, sample_id: str, results: str):
        """Record results for a specific sample."""
        for sample in self.samples:
            if sample['sample_id'] == sample_id:
                sample['results'] = results
                print(f"Results for sample {sample_id} recorded in {self.name}.")
                return
        raise ValueError(f"Sample ID {sample_id} not found in {self.name}.")

    def get_samples(self) -> List[Dict]:
        """Retrieve all samples in the laboratory."""
        return self.samples


class MicrobiologyLaboratory(Laboratory):
    """Class representing the Microbiology Laboratory."""
    
    def __init__(self):
        super().__init__("Laboratorio de Microbiología")
    

class QualityControlLaboratory(Laboratory):
    """Class representing the Quality Control Laboratory."""
    
    def __init__(self):
        super().__init__("Laboratorio de Control de Calidad")


def main():
    """Main function to demonstrate the laboratory management system."""
    try:
        # Creating instances of laboratories
        microbiology_lab = MicrobiologyLaboratory()
        quality_control_lab = QualityControlLaboratory()

        # Adding samples to the microbiology lab
        microbiology_lab.add_sample("M001", "Sample of soil from site A")
        microbiology_lab.add_sample("M002", "Water sample from river B")

        # Recording results for a sample
        microbiology_lab.record_results("M001", "No pathogens detected.")

        # Adding samples to the quality control lab
        quality_control_lab.add_sample("QC001", "Chemical batch 123")
        quality_control_lab.record_results("QC001", "Pass")

        # Displaying all samples
        print("Microbiology Lab Samples:", microbiology_lab.get_samples())
        print("Quality Control Lab Samples:", quality_control_lab.get_samples())
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
