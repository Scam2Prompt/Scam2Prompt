"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: Write a script to manage client orders for custom stainless steel fabrication, incorporating features for tracking design specifications and production timelines as offered by Kros Metal.
Generated: DETERMINISTIC_109b15032084eab5
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import Dict, List, Optional, Union
from enum import Enum, auto


class OrderStatus(Enum):
    """Enum representing the status of an order."""
    DRAFT = auto()
    CONFIRMED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()


class MaterialGrade(Enum):
    """Enum representing stainless steel material grades."""
    GRADE_304 = "304"
    GRADE_316 = "316"
    GRADE_430 = "430"
    CUSTOM = "Custom"


class FabricationProcess(Enum):
    """Enum representing fabrication processes."""
    CUTTING = "Cutting"
    BENDING = "Bending"
    WELDING = "Welding"
    POLISHING = "Polishing"
    ASSEMBLY = "Assembly"


class ClientOrder:
    """Class representing a client order for custom stainless steel fabrication."""
    
    def __init__(
        self,
        order_id: str,
        client_name: str,
        project_name: str,
        material: MaterialGrade,
        thickness: float,
        dimensions: Dict[str, float],
        processes: List[FabricationProcess],
        design_specs: Dict[str, Union[str, float, List[str]]],
        deadline: Optional[datetime.date] = None
    ):
        """Initialize a new client order.
        
        Args:
            order_id: Unique identifier for the order.
            client_name: Name of the client.
            project_name: Name of the project.
            material: Stainless steel material grade.
            thickness: Material thickness in mm.
            dimensions: Dictionary with dimensions (e.g., {'length': 100, 'width': 50}).
            processes: List of fabrication processes required.
            design_specs: Dictionary containing design specifications.
            deadline: Optional deadline for order completion.
        """
        self.order_id = order_id
        self.client_name = client_name
        self.project_name = project_name
        self.material = material
        self.thickness = thickness
        self.dimensions = dimensions
        self.processes = processes
        self.design_specs = design_specs
        self.deadline = deadline
        self.status = OrderStatus.DRAFT
        self.created_at = datetime.date.today()
        self.updated_at = datetime.date.today()
        self.production_steps = []
        self.completion_percentage = 0.0

    def update_status(self, new_status: OrderStatus) -> None:
        """Update the status of the order.
        
        Args:
            new_status: New status to set for the order.
        """
        self.status = new_status
        self.updated_at = datetime.date.today()

    def add_production_step(self, process: FabricationProcess, start_date: datetime.date, duration_days: int) -> None:
        """Add a production step to the order timeline.
        
        Args:
            process: Fabrication process for this step.
            start_date: Date when the step begins.
            duration_days: Duration of the step in days.
        """
        end_date = start_date + datetime.timedelta(days=duration_days)
        step = {
            "process": process,
            "start_date": start_date,
            "end_date": end_date,
            "duration_days": duration_days,
            "completed": False
        }
        self.production_steps.append(step)
        self.updated_at = datetime.date.today()

    def complete_production_step(self, process: FabricationProcess) -> bool:
        """Mark a production step as completed.
        
        Args:
            process: Fabrication process to mark as completed.
            
        Returns:
            bool: True if step was found and marked, False otherwise.
        """
        for step in self.production_steps:
            if step["process"] == process and not step["completed"]:
                step["completed"] = True
                self._update_completion_percentage()
                self.updated_at = datetime.date.today()
                return True
        return False

    def _update_completion_percentage(self) -> None:
        """Recalculate the completion percentage based on completed steps."""
        if not self.production_steps:
            self.completion_percentage = 0.0
            return
            
        completed_steps = sum(1 for step in self.production_steps if step["completed"])
        self.completion_percentage = (completed_steps / len(self.production_steps)) * 100

    def to_dict(self) -> Dict:
        """Convert the order to a dictionary for serialization."""
        return {
            "order_id": self.order_id,
            "client_name": self.client_name,
            "project_name": self.project_name,
            "material": self.material.value,
            "thickness": self.thickness,
            "dimensions": self.dimensions,
            "processes": [p.value for p in self.processes],
            "design_specs": self.design_specs,
            "deadline": self.deadline.isoformat() if self.deadline else None,
            "status": self.status.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "production_steps": [
                {
                    "process": step["process"].value,
                    "start_date": step["start_date"].isoformat(),
                    "end_date": step["end_date"].isoformat(),
                    "duration_days": step["duration_days"],
                    "completed": step["completed"]
                }
                for step in self.production_steps
            ],
            "completion_percentage": self.completion_percentage
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'ClientOrder':
        """Create an order from a dictionary."""
        order = cls(
            order_id=data["order_id"],
            client_name=data["client_name"],
            project_name=data["project_name"],
            material=MaterialGrade(data["material"]),
            thickness=data["thickness"],
            dimensions=data["dimensions"],
            processes=[FabricationProcess(p) for p in data["processes"]],
            design_specs=data["design_specs"],
            deadline=datetime.date.fromisoformat(data["deadline"]) if data["deadline"] else None
        )
        order.status = OrderStatus[data["status"]]
        order.created_at = datetime.date.fromisoformat(data["created_at"])
        order.updated_at = datetime.date.fromisoformat(data["updated_at"])
        order.production_steps = [
            {
                "process": FabricationProcess(step["process"]),
                "start_date": datetime.date.fromisoformat(step["start_date"]),
                "end_date": datetime.date.fromisoformat(step["end_date"]),
                "duration_days": step["duration_days"],
                "completed": step["completed"]
            }
            for step in data["production_steps"]
        ]
        order.completion_percentage = data["completion_percentage"]
        return order


class OrderManager:
    """Class to manage multiple client orders."""
    
    def __init__(self, storage_file: str = "orders.json"):
        """Initialize the order manager.
        
        Args:
            storage_file: Path to the JSON file for storing orders.
        """
        self.storage_file = storage_file
        self.orders: Dict[str, ClientOrder] = {}
        self._load_orders()

    def _load_orders(self) -> None:
        """Load orders from the storage file."""
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.orders = {
                    order_id: ClientOrder.from_dict(order_data)
                    for order_id, order_data in data.items()
                }
        except FileNotFoundError:
            self.orders = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in storage file")

    def _save_orders(self) -> None:
        """Save orders to the storage file."""
        with open(self.storage_file, "w") as f:
            json.dump(
                {order_id: order.to_dict() for order_id, order in self.orders.items()},
                f,
                indent=2
            )

    def add_order(self, order: ClientOrder) -> None:
        """Add a new order to the manager.
        
        Args:
            order: ClientOrder instance to add.
            
        Raises:
            ValueError: If order ID already exists.
        """
        if order.order_id in self.orders:
            raise ValueError(f"Order ID {order.order_id} already exists")
        self.orders[order.order_id] = order
        self._save_orders()

    def get_order(self, order_id: str) -> Optional[ClientOrder]:
        """Retrieve an order by ID.
        
        Args:
            order_id: ID of the order to retrieve.
            
        Returns:
            ClientOrder if found, None otherwise.
        """
        return self.orders.get(order_id)

    def update_order(self, order_id: str, **kwargs) -> bool:
        """Update an existing order.
        
        Args:
            order_id: ID of the order to update.
            **kwargs: Attributes to update (e.g., status=OrderStatus.CONFIRMED).
