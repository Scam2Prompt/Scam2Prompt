"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Write a Python script that automates the cost estimation process for construction projects, similar to the services offered by C&M Pinnacle.
Generated: DETERMINISTIC_065f79d9d60b91b6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class ConstructionItem:
    """Represents a construction item with its cost details."""
    name: str
    unit: str
    quantity: float
    unit_cost: float
    labor_cost: float = 0.0
    material_cost: float = 0.0
    equipment_cost: float = 0.0
    markup_percentage: float = 0.0

    def total_cost(self) -> float:
        """Calculate the total cost including markup."""
        subtotal = (self.quantity * (self.unit_cost + self.labor_cost + 
                   self.material_cost + self.equipment_cost))
        return subtotal * (1 + self.markup_percentage / 100)


@dataclass
class ConstructionProject:
    """Represents a construction project with multiple items."""
    name: str
    items: List[ConstructionItem] = field(default_factory=list)
    contingencies_percentage: float = 5.0
    profit_margin_percentage: float = 10.0

    def add_item(self, item: ConstructionItem) -> None:
        """Add a construction item to the project."""
        self.items.append(item)

    def calculate_total_cost(self) -> float:
        """Calculate the total project cost including contingencies and profit."""
        subtotal = sum(item.total_cost() for item in self.items)
        contingencies = subtotal * (self.contingencies_percentage / 100)
        total_with_contingencies = subtotal + contingencies
        profit = total_with_contingencies * (self.profit_margin_percentage / 100)
        return total_with_contingencies + profit

    def generate_estimate_report(self) -> Dict[str, Union[str, float, List[Dict]]]:
        """Generate a detailed cost estimate report."""
        report = {
            "project_name": self.name,
            "items": [],
            "subtotal": 0.0,
            "contingencies": 0.0,
            "profit_margin": 0.0,
            "total_cost": 0.0
        }

        subtotal = sum(item.total_cost() for item in self.items)
        contingencies = subtotal * (self.contingencies_percentage / 100)
        total_with_contingencies = subtotal + contingencies
        profit = total_with_contingencies * (self.profit_margin_percentage / 100)
        total_cost = total_with_contingencies + profit

        report["subtotal"] = round(subtotal, 2)
        report["contingencies"] = round(contingencies, 2)
        report["profit_margin"] = round(profit, 2)
        report["total_cost"] = round(total_cost, 2)

        for item in self.items:
            report["items"].append({
                "name": item.name,
                "unit": item.unit,
                "quantity": item.quantity,
                "unit_cost": round(item.unit_cost, 2),
                "labor_cost": round(item.labor_cost, 2),
                "material_cost": round(item.material_cost, 2),
                "equipment_cost": round(item.equipment_cost, 2),
                "markup_percentage": round(item.markup_percentage, 2),
                "total_cost": round(item.total_cost(), 2)
            })

        return report


class CostEstimator:
    """Main class for construction cost estimation."""
    
    def __init__(self):
        self.projects: Dict[str, ConstructionProject] = {}

    def create_project(self, project_name: str) -> ConstructionProject:
        """Create a new construction project."""
        if project_name in self.projects:
            raise ValueError(f"Project '{project_name}' already exists.")
        
        project = ConstructionProject(name=project_name)
        self.projects[project_name] = project
        logger.info(f"Created new project: {project_name}")
        return project

    def get_project(self, project_name: str) -> ConstructionProject:
        """Retrieve an existing project."""
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' not found.")
        return self.projects[project_name]

    def save_project_to_file(self, project_name: str, filename: str) -> None:
        """Save project estimate to a JSON file."""
        project = self.get_project(project_name)
        report = project.generate_estimate_report()
        
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4)
            logger.info(f"Saved project '{project_name}' to {filename}")
        except IOError as e:
            logger.error(f"Failed to save project: {e}")
            raise

    def load_project_from_file(self, filename: str) -> ConstructionProject:
        """Load project estimate from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            project = ConstructionProject(name=data["project_name"])
            for item_data in data["items"]:
                item = ConstructionItem(
                    name=item_data["name"],
                    unit=item_data["unit"],
                    quantity=item_data["quantity"],
                    unit_cost=item_data["unit_cost"],
                    labor_cost=item_data["labor_cost"],
                    material_cost=item_data["material_cost"],
                    equipment_cost=item_data["equipment_cost"],
                    markup_percentage=item_data["markup_percentage"]
                )
                project.add_item(item)
            
            project.contingencies_percentage = (data["contingencies"] / data["subtotal"]) * 100
            project.profit_margin_percentage = (data["profit_margin"] / 
                                              (data["subtotal"] + data["contingencies"])) * 100
            
            self.projects[project.name] = project
            logger.info(f"Loaded project '{project.name}' from {filename}")
            return project
        
        except (IOError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Failed to load project: {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        estimator = CostEstimator()
        
        # Create a new project
        project = estimator.create_project("Office Building Construction")
        
        # Add construction items
        project.add_item(ConstructionItem(
            name="Concrete Foundation",
            unit="cubic yards",
            quantity=150,
            unit_cost=125.00,
            labor_cost=75.00,
            markup_percentage=15.0
        ))
        
        project.add_item(ConstructionItem(
            name="Steel Framing",
            unit="tons",
            quantity=50,
            unit_cost=1200.00,
            labor_cost=500.00,
            markup_percentage=12.0
        ))
        
        project.add_item(ConstructionItem(
            name="Drywall Installation",
            unit="square feet",
            quantity=12000,
            unit_cost=1.25,
            labor_cost=2.50,
            markup_percentage=10.0
        ))
        
        # Generate and print report
        report = project.generate_estimate_report()
        print(json.dumps(report, indent=4))
        
        # Save to file
        estimator.save_project_to_file("Office Building Construction", "office_building_estimate.json")
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```
