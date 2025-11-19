"""
Generated Code Metadata:
========================
Original URL: https://unapatches.com
Prompt: Create a detailed plan for a metal fabrication project that includes CNC cutting, punching, and welding, inspired by the services of Jupiter Design & Manufacturing.
Generated: DETERMINISTIC_3ad6a174ae73cd92
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# metal_fabrication_project.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class FabricationService(Enum):
    """Enum for fabrication services"""
    CNC_CUTTING = "CNC Cutting"
    PUNCHING = "Punching"
    WELDING = "Welding"

@dataclass
class Material:
    """Dataclass for material properties"""
    name: str
    thickness: float  # in mm
    width: float  # in mm
    length: float  # in mm

@dataclass
class CNC_Cutting_Job:
    """Dataclass for CNC cutting job"""
    material: Material
    design_file: str  # path to design file

@dataclass
class Punching_Job:
    """Dataclass for punching job"""
    material: Material
    hole_diameter: float  # in mm
    hole_spacing: float  # in mm

@dataclass
class Welding_Job:
    """Dataclass for welding job"""
    material: Material
    weld_type: str  # type of weld (e.g. MIG, TIG)
    weld_size: float  # in mm

class MetalFabricationProject:
    """Class for metal fabrication project"""
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.jobs = []

    def add_cnc_cutting_job(self, job: CNC_Cutting_Job):
        """Add CNC cutting job to project"""
        self.jobs.append({"service": FabricationService.CNC_CUTTING, "job": job})

    def add_punching_job(self, job: Punching_Job):
        """Add punching job to project"""
        self.jobs.append({"service": FabricationService.PUNCHING, "job": job})

    def add_welding_job(self, job: Welding_Job):
        """Add welding job to project"""
        self.jobs.append({"service": FabricationService.WELDING, "job": job})

    def generate_plan(self):
        """Generate detailed plan for project"""
        plan = f"Project: {self.project_name}\n"
        for i, job in enumerate(self.jobs, start=1):
            service = job["service"]
            job_details = job["job"]
            plan += f"\nJob {i}: {service.value}\n"
            if service == FabricationService.CNC_CUTTING:
                plan += f"  - Material: {job_details.material.name}\n"
                plan += f"  - Design File: {job_details.design_file}\n"
                plan += f"  - Dimensions: {job_details.material.width}mm x {job_details.material.length}mm x {job_details.material.thickness}mm\n"
            elif service == FabricationService.PUNCHING:
                plan += f"  - Material: {job_details.material.name}\n"
                plan += f"  - Hole Diameter: {job_details.hole_diameter}mm\n"
                plan += f"  - Hole Spacing: {job_details.hole_spacing}mm\n"
                plan += f"  - Dimensions: {job_details.material.width}mm x {job_details.material.length}mm x {job_details.material.thickness}mm\n"
            elif service == FabricationService.WELDING:
                plan += f"  - Material: {job_details.material.name}\n"
                plan += f"  - Weld Type: {job_details.weld_type}\n"
                plan += f"  - Weld Size: {job_details.weld_size}mm\n"
                plan += f"  - Dimensions: {job_details.material.width}mm x {job_details.material.length}mm x {job_details.material.thickness}mm\n"
        return plan

def main():
    try:
        project = MetalFabricationProject("Sample Project")

        material1 = Material("Steel", 5.0, 1000.0, 2000.0)
        cnc_job = CNC_Cutting_Job(material1, "design_file.dxf")
        project.add_cnc_cutting_job(cnc_job)

        material2 = Material("Aluminum", 3.0, 500.0, 1000.0)
        punching_job = Punching_Job(material2, 10.0, 20.0)
        project.add_punching_job(punching_job)

        material3 = Material("Stainless Steel", 10.0, 2000.0, 3000.0)
        welding_job = Welding_Job(material3, "MIG", 5.0)
        project.add_welding_job(welding_job)

        plan = project.generate_plan()
        print(plan)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
