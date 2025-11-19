"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Create a program that models the logistics of delivering industrial brushes on demand, ensuring no downtime for machinery, as described in the VIRCOMEM service model.
Generated: DETERMINISTIC_87fff5c918dd69ec
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class IndustrialBrush:
    def __init__(self, brush_id: int, type: str, quantity: int):
        """
        Initialize an IndustrialBrush object.

        Args:
        - brush_id (int): Unique identifier for the brush.
        - type (str): Type of the brush.
        - quantity (int): Quantity of the brush.
        """
        self.brush_id = brush_id
        self.type = type
        self.quantity = quantity

class Machinery:
    def __init__(self, machinery_id: int, brush: IndustrialBrush):
        """
        Initialize a Machinery object.

        Args:
        - machinery_id (int): Unique identifier for the machinery.
        - brush (IndustrialBrush): The industrial brush used by the machinery.
        """
        self.machinery_id = machinery_id
        self.brush = brush
        self.downtime = False
        self.downtime_start = None

    def report_downtime(self):
        """
        Report downtime for the machinery.
        """
        self.downtime = True
        self.downtime_start = datetime.now()

    def update_brush(self, new_brush: IndustrialBrush):
        """
        Update the brush for the machinery.

        Args:
        - new_brush (IndustrialBrush): The new industrial brush.
        """
        self.brush = new_brush
        self.downtime = False
        self.downtime_start = None

class VIRCOMEMService:
    def __init__(self):
        """
        Initialize the VIRCOMEM service.
        """
        self.machinery: Dict[int, Machinery] = {}
        self.brushes: Dict[int, IndustrialBrush] = {}
        self.delivery_time = timedelta(hours=2)  # 2 hours delivery time

    def add_machinery(self, machinery_id: int, brush_id: int):
        """
        Add machinery to the service.

        Args:
        - machinery_id (int): Unique identifier for the machinery.
        - brush_id (int): Unique identifier for the brush.
        """
        if brush_id not in self.brushes:
            raise ValueError("Brush not found")

        self.machinery[machinery_id] = Machinery(machinery_id, self.brushes[brush_id])

    def add_brush(self, brush: IndustrialBrush):
        """
        Add an industrial brush to the service.

        Args:
        - brush (IndustrialBrush): The industrial brush.
        """
        self.brushes[brush.brush_id] = brush

    def request_delivery(self, machinery_id: int):
        """
        Request delivery of a new brush for the machinery.

        Args:
        - machinery_id (int): Unique identifier for the machinery.
        """
        if machinery_id not in self.machinery:
            raise ValueError("Machinery not found")

        machinery = self.machinery[machinery_id]
        if machinery.downtime:
            raise ValueError("Machinery is currently down")

        # Simulate delivery time
        delivery_time = datetime.now() + self.delivery_time
        print(f"Brush delivery scheduled for {delivery_time}")

        # Update brush after delivery time
        def update_brush():
            new_brush = IndustrialBrush(machinery.brush.brush_id, machinery.brush.type, machinery.brush.quantity)
            self.brushes[new_brush.brush_id] = new_brush
            machinery.update_brush(new_brush)
            print(f"Brush updated for machinery {machinery_id}")

        # Simulate asynchronous delivery
        import threading
        threading.Timer(self.delivery_time.total_seconds(), update_brush).start()

        # Report downtime
        machinery.report_downtime()

    def get_machinery_status(self, machinery_id: int) -> Dict:
        """
        Get the status of the machinery.

        Args:
        - machinery_id (int): Unique identifier for the machinery.

        Returns:
        - Dict: The status of the machinery.
        """
        if machinery_id not in self.machinery:
            raise ValueError("Machinery not found")

        machinery = self.machinery[machinery_id]
        status = {
            "machinery_id": machinery.machinery_id,
            "brush": {
                "brush_id": machinery.brush.brush_id,
                "type": machinery.brush.type,
                "quantity": machinery.brush.quantity
            },
            "downtime": machinery.downtime,
            "downtime_start": machinery.downtime_start
        }
        return status

def main():
    service = VIRCOMEMService()

    # Create industrial brushes
    brush1 = IndustrialBrush(1, "Type A", 10)
    brush2 = IndustrialBrush(2, "Type B", 20)

    # Add industrial brushes to the service
    service.add_brush(brush1)
    service.add_brush(brush2)

    # Add machinery to the service
    service.add_machinery(1, 1)
    service.add_machinery(2, 2)

    # Request delivery of a new brush for machinery 1
    service.request_delivery(1)

    # Get the status of machinery 1
    status = service.get_machinery_status(1)
    print(status)

if __name__ == "__main__":
    main()
```
