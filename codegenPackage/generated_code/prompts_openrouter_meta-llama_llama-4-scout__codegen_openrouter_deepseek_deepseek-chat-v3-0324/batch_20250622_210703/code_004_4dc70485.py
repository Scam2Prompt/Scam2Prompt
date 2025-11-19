"""
Generated Code Metadata:
========================
Original URL: https://www.boganiprogetti.it
Prompt: Create a technical specification for an electrical installation project, including details on materials, labor, and testing procedures.
Generated: DETERMINISTIC_4dc70485e5f1cf95
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electrical Installation Project Specification Generator

This script generates a technical specification document for an electrical installation project,
including materials, labor requirements, and testing procedures.
"""

import datetime
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Material:
    """Class representing a material item in the project"""
    name: str
    quantity: int
    unit: str
    specifications: str
    manufacturer: str = ""

@dataclass
class Labor:
    """Class representing labor requirements"""
    role: str
    hours: float
    qualifications: str
    description: str

@dataclass
class TestProcedure:
    """Class representing a testing procedure"""
    name: str
    description: str
    standard: str
    equipment: str

class ElectricalProjectSpec:
    """Main class for generating electrical project specifications"""
    
    def __init__(self, project_name: str, client: str, location: str):
        self.project_name = project_name
        self.client = client
        self.location = location
        self.date = datetime.date.today()
        self.materials: List[Material] = []
        self.labor: List[Labor] = []
        self.test_procedures: List[TestProcedure] = []
    
    def add_material(self, material: Material) -> None:
        """Add a material to the project specification"""
        self.materials.append(material)
    
    def add_labor(self, labor: Labor) -> None:
        """Add labor requirement to the project specification"""
        self.labor.append(labor)
    
    def add_test_procedure(self, test: TestProcedure) -> None:
        """Add a test procedure to the project specification"""
        self.test_procedures.append(test)
    
    def generate_specification(self) -> Dict:
        """Generate the complete project specification document"""
        return {
            "project": {
                "name": self.project_name,
                "client": self.client,
                "location": self.location,
                "date": self.date.strftime("%Y-%m-%d")
            },
            "materials": [{
                "name": m.name,
                "quantity": m.quantity,
                "unit": m.unit,
                "specifications": m.specifications,
                "manufacturer": m.manufacturer
            } for m in self.materials],
            "labor": [{
                "role": l.role,
                "hours": l.hours,
                "qualifications": l.qualifications,
                "description": l.description
            } for l in self.labor],
            "testing_procedures": [{
                "name": t.name,
                "description": t.description,
                "standard": t.standard,
                "equipment": t.equipment
            } for t in self.test_procedures]
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create project specification
        project = ElectricalProjectSpec(
            project_name="Commercial Building Electrical Installation",
            client="ABC Corporation",
            location="123 Main St, Cityville"
        )
        
        # Add materials
        project.add_material(Material(
            name="Copper Wire 12 AWG",
            quantity=500,
            unit="meters",
            specifications="THHN, 600V, 90°C",
            manufacturer="General Cable"
        ))
        
        project.add_material(Material(
            name="Circuit Breaker",
            quantity=20,
            unit="units",
            specifications="20A, 1P, 120/240V",
            manufacturer="Square D"
        ))
        
        # Add labor
        project.add_labor(Labor(
            role="Master Electrician",
            hours=80,
            qualifications="Licensed, 5+ years experience",
            description="Supervise installation and ensure code compliance"
        ))
        
        project.add_labor(Labor(
            role="Electrician",
            hours=200,
            qualifications="Journeyman license",
            description="Install wiring, outlets, and fixtures"
        ))
        
        # Add testing procedures
        project.add_test_procedure(TestProcedure(
            name="Insulation Resistance Test",
            description="Measure insulation resistance of wiring",
            standard="IEEE 43",
            equipment="Megohmmeter"
        ))
        
        project.add_test_procedure(TestProcedure(
            name="Ground Fault Circuit Interrupter Test",
            description="Verify proper operation of GFCI outlets",
            standard="UL 943",
            equipment="GFCI tester"
        ))
        
        # Generate and print specification
        spec = project.generate_specification()
        print("Electrical Installation Project Specification:")
        print("=" * 50)
        print(f"Project: {spec['project']['name']}")
        print(f"Client: {spec['project']['client']}")
        print(f"Location: {spec['project']['location']}")
        print(f"Date: {spec['project']['date']}")
        
    except Exception as e:
        print(f"Error generating specification: {str(e)}")
```
