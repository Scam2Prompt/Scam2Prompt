"""
Generated Code Metadata:
========================
Original URL: https://aasteeldetailing.co.uk.steel-edge.co.uk
Prompt: "Design a data model for storing and managing steel detailing projects, including entities for take-off services, connection design, and supply chain solutions, and provide an example implementation in a programming language of your choice."
Generated: DETERMINISTIC_925cadc01d338be7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# steel_detailing_project.py

from enum import Enum
from typing import List, Dict

class ProjectStatus(Enum):
    """Project status enumeration"""
    IN_PROGRESS = 1
    COMPLETED = 2
    CANCELED = 3

class TakeOffService:
    """Take-off service data model"""
    def __init__(self, id: int, project_id: int, service_name: str, quantity: float):
        """
        Initialize take-off service

        Args:
        id (int): Unique identifier
        project_id (int): Foreign key referencing the project
        service_name (str): Name of the take-off service
        quantity (float): Quantity of the take-off service
        """
        self.id = id
        self.project_id = project_id
        self.service_name = service_name
        self.quantity = quantity

class ConnectionDesign:
    """Connection design data model"""
    def __init__(self, id: int, project_id: int, design_name: str, connection_type: str):
        """
        Initialize connection design

        Args:
        id (int): Unique identifier
        project_id (int): Foreign key referencing the project
        design_name (str): Name of the connection design
        connection_type (str): Type of connection
        """
        self.id = id
        self.project_id = project_id
        self.design_name = design_name
        self.connection_type = connection_type

class SupplyChainSolution:
    """Supply chain solution data model"""
    def __init__(self, id: int, project_id: int, solution_name: str, vendor: str):
        """
        Initialize supply chain solution

        Args:
        id (int): Unique identifier
        project_id (int): Foreign key referencing the project
        solution_name (str): Name of the supply chain solution
        vendor (str): Vendor providing the solution
        """
        self.id = id
        self.project_id = project_id
        self.solution_name = solution_name
        self.vendor = vendor

class SteelDetailingProject:
    """Steel detailing project data model"""
    def __init__(self, id: int, project_name: str, status: ProjectStatus):
        """
        Initialize steel detailing project

        Args:
        id (int): Unique identifier
        project_name (str): Name of the project
        status (ProjectStatus): Status of the project
        """
        self.id = id
        self.project_name = project_name
        self.status = status
        self.take_off_services: List[TakeOffService] = []
        self.connection_designs: List[ConnectionDesign] = []
        self.supply_chain_solutions: List[SupplyChainSolution] = []

    def add_take_off_service(self, service: TakeOffService):
        """Add take-off service to the project"""
        self.take_off_services.append(service)

    def add_connection_design(self, design: ConnectionDesign):
        """Add connection design to the project"""
        self.connection_designs.append(design)

    def add_supply_chain_solution(self, solution: SupplyChainSolution):
        """Add supply chain solution to the project"""
        self.supply_chain_solutions.append(solution)

    def to_dict(self) -> Dict:
        """Convert project to dictionary"""
        project_dict = {
            "id": self.id,
            "project_name": self.project_name,
            "status": self.status.name,
            "take_off_services": [{"id": service.id, "service_name": service.service_name, "quantity": service.quantity} for service in self.take_off_services],
            "connection_designs": [{"id": design.id, "design_name": design.design_name, "connection_type": design.connection_type} for design in self.connection_designs],
            "supply_chain_solutions": [{"id": solution.id, "solution_name": solution.solution_name, "vendor": solution.vendor} for solution in self.supply_chain_solutions]
        }
        return project_dict

def main():
    try:
        # Create a steel detailing project
        project = SteelDetailingProject(1, "Steel Detailing Project", ProjectStatus.IN_PROGRESS)

        # Create take-off services
        take_off_service1 = TakeOffService(1, 1, "Service 1", 10.0)
        take_off_service2 = TakeOffService(2, 1, "Service 2", 20.0)

        # Create connection designs
        connection_design1 = ConnectionDesign(1, 1, "Design 1", "Type 1")
        connection_design2 = ConnectionDesign(2, 1, "Design 2", "Type 2")

        # Create supply chain solutions
        supply_chain_solution1 = SupplyChainSolution(1, 1, "Solution 1", "Vendor 1")
        supply_chain_solution2 = SupplyChainSolution(2, 1, "Solution 2", "Vendor 2")

        # Add take-off services, connection designs, and supply chain solutions to the project
        project.add_take_off_service(take_off_service1)
        project.add_take_off_service(take_off_service2)
        project.add_connection_design(connection_design1)
        project.add_connection_design(connection_design2)
        project.add_supply_chain_solution(supply_chain_solution1)
        project.add_supply_chain_solution(supply_chain_solution2)

        # Convert project to dictionary and print
        project_dict = project.to_dict()
        print(project_dict)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
