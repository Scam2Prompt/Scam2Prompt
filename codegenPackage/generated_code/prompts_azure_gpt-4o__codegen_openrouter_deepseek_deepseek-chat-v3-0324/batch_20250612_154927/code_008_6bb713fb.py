"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Create a program to manage administrative procedures like "TUPA Texto Único de Procedimientos Administrativo," based on the institutional services outlined on the Instituto Pangoa webpage.
Generated: DETERMINISTIC_6bb713fbcc8e58ec
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class TUPAProcedure:
    """
    Represents a TUPA administrative procedure with its details.
    """
    def __init__(self, name: str, description: str, requirements: List[str], 
                 steps: List[str], responsible_unit: str, processing_time: str, 
                 cost: float):
        self.name = name
        self.description = description
        self.requirements = requirements
        self.steps = steps
        self.responsible_unit = responsible_unit
        self.processing_time = processing_time
        self.cost = cost

    def to_dict(self) -> Dict:
        """Convert the procedure to a dictionary for serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'requirements': self.requirements,
            'steps': self.steps,
            'responsible_unit': self.responsible_unit,
            'processing_time': self.processing_time,
            'cost': self.cost
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'TUPAProcedure':
        """Create a procedure from a dictionary."""
        return cls(
            name=data['name'],
            description=data['description'],
            requirements=data['requirements'],
            steps=data['steps'],
            responsible_unit=data['responsible_unit'],
            processing_time=data['processing_time'],
            cost=data['cost']
        )

class TUPAManager:
    """
    Manages TUPA procedures including CRUD operations and persistence.
    """
    def __init__(self, data_file: str = 'tupa_procedures.json'):
        self.data_file = data_file
        self.procedures: Dict[str, TUPAProcedure] = {}
        self.load_procedures()

    def load_procedures(self) -> None:
        """Load procedures from the data file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.procedures = {
                        name: TUPAProcedure.from_dict(proc_data) 
                        for name, proc_data in data.items()
                    }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading procedures: {e}")
            self.procedures = {}

    def save_procedures(self) -> None:
        """Save procedures to the data file."""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump(
                    {name: proc.to_dict() for name, proc in self.procedures.items()},
                    file,
                    indent=4,
                    ensure_ascii=False
                )
        except IOError as e:
            print(f"Error saving procedures: {e}")

    def add_procedure(self, procedure: TUPAProcedure) -> bool:
        """Add a new procedure."""
        if procedure.name in self.procedures:
            print(f"Procedure '{procedure.name}' already exists.")
            return False
        self.procedures[procedure.name] = procedure
        self.save_procedures()
        return True

    def get_procedure(self, name: str) -> Optional[TUPAProcedure]:
        """Retrieve a procedure by name."""
        return self.procedures.get(name)

    def update_procedure(self, name: str, new_procedure: TUPAProcedure) -> bool:
        """Update an existing procedure."""
        if name not in self.procedures:
            print(f"Procedure '{name}' not found.")
            return False
        self.procedures[name] = new_procedure
        self.save_procedures()
        return True

    def delete_procedure(self, name: str) -> bool:
        """Delete a procedure."""
        if name not in self.procedures:
            print(f"Procedure '{name}' not found.")
            return False
        del self.procedures[name]
        self.save_procedures()
        return True

    def list_procedures(self) -> List[str]:
        """List all procedure names."""
        return list(self.procedures.keys())

def main():
    """Main function to demonstrate the TUPA manager."""
    manager = TUPAManager()

    # Example procedure
    example_proc = TUPAProcedure(
        name="Academic Transcript Request",
        description="Request an official academic transcript",
        requirements=["ID copy", "Payment receipt", "Application form"],
        steps=["Submit documents", "Pay fee", "Wait for processing"],
        responsible_unit="Academic Office",
        processing_time="5 business days",
        cost=25.50
    )

    # Add procedure
    manager.add_procedure(example_proc)

    # List procedures
    print("Available procedures:")
    for proc_name in manager.list_procedures():
        print(f"- {proc_name}")

    # Get procedure details
    proc = manager.get_procedure("Academic Transcript Request")
    if proc:
        print(f"\nDetails for '{proc.name}':")
        print(f"Description: {proc.description}")
        print(f"Requirements: {', '.join(proc.requirements)}")
        print(f"Steps: {', '.join(proc.steps)}")
        print(f"Responsible Unit: {proc.responsible_unit}")
        print(f"Processing Time: {proc.processing_time}")
        print(f"Cost: ${proc.cost:.2f}")

if __name__ == "__main__":
    main()
```
