"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: Create a script to generate a detailed production report for customized packaging boxes, including material usage, processing steps (e.g., embossing, UV coating), and estimated delivery times, based on Metis's service model.
Generated: DETERMINISTIC_8ca42a6eb196fdea
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# production_report_generator.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class MaterialType(str, Enum):
    """Material types for packaging boxes"""
    PAPER = "paper"
    CARDBOARD = "cardboard"
    PLASTIC = "plastic"

class ProcessingStep(str, Enum):
    """Processing steps for packaging boxes"""
    EMBOSSING = "embossing"
    UV_COATING = "uv coating"
    CUTTING = "cutting"

@dataclass
class Material:
    """Material usage details"""
    material_type: MaterialType
    quantity: float  # in square meters

@dataclass
class Processing:
    """Processing steps details"""
    step: ProcessingStep
    description: str

@dataclass
class ProductionReport:
    """Production report details"""
    material_usages: List[Material]
    processing_steps: List[Processing]
    estimated_delivery_time: str

class ProductionReportGenerator:
    """Generates production reports for customized packaging boxes"""

    def __init__(self, service_model: str):
        """
        Initializes the production report generator with Metis's service model

        Args:
        - service_model (str): Metis's service model
        """
        self.service_model = service_model

    def generate_report(self, material_usages: List[Material], processing_steps: List[Processing]) -> ProductionReport:
        """
        Generates a detailed production report

        Args:
        - material_usages (List[Material]): Material usage details
        - processing_steps (List[Processing]): Processing steps details

        Returns:
        - ProductionReport: Production report details
        """
        estimated_delivery_time = self.estimate_delivery_time(material_usages, processing_steps)
        return ProductionReport(material_usages, processing_steps, estimated_delivery_time)

    def estimate_delivery_time(self, material_usages: List[Material], processing_steps: List[Processing]) -> str:
        """
        Estimates delivery time based on material usages and processing steps

        Args:
        - material_usages (List[Material]): Material usage details
        - processing_steps (List[Processing]): Processing steps details

        Returns:
        - str: Estimated delivery time
        """
        # Assuming a base delivery time of 3-5 business days
        base_delivery_time = 3

        # Add 1-2 business days for each processing step
        processing_time = len(processing_steps) * 2

        # Add 1-2 business days for each material usage
        material_time = len(material_usages) * 1

        estimated_delivery_time = base_delivery_time + processing_time + material_time
        return f"{estimated_delivery_time} business days"

def main():
    try:
        # Create a production report generator with Metis's service model
        generator = ProductionReportGenerator("metis_service_model")

        # Define material usages
        material_usages = [
            Material(MaterialType.PAPER, 10.0),
            Material(MaterialType.CARDBOARD, 5.0)
        ]

        # Define processing steps
        processing_steps = [
            Processing(ProcessingStep.EMBOSSING, "Embossing logo on the box"),
            Processing(ProcessingStep.UV_COATING, "UV coating on the box surface")
        ]

        # Generate production report
        report = generator.generate_report(material_usages, processing_steps)

        # Print production report
        print("Production Report:")
        print("--------------------")
        print("Material Usages:")
        for material in report.material_usages:
            print(f"- {material.material_type.value}: {material.quantity} sqm")
        print("Processing Steps:")
        for processing in report.processing_steps:
            print(f"- {processing.step.value}: {processing.description}")
        print(f"Estimated Delivery Time: {report.estimated_delivery_time}")

    except Exception as e:
        print(f"Error generating production report: {str(e)}")

if __name__ == "__main__":
    main()
```
