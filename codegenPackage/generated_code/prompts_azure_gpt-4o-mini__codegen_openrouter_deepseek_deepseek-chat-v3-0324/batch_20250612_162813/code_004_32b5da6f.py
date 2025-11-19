"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: Create a checklist for conducting NDT inspections on marine vessels, inspired by the quality service principles of Marine NDT & Engineering Works.
Generated: DETERMINISTIC_32b5da6f229cb91b
Batch ID: 20250612_162813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python implementation for a marine vessel NDT inspection checklist system:

```python
import json
from datetime import datetime
from enum import Enum, auto


class InspectionType(Enum):
    VISUAL = auto()
    ULTRASONIC = auto()
    RADIOGRAPHIC = auto()
    MAGNETIC_PARTICLE = auto()
    DYE_PENETRANT = auto()


class VesselComponent(Enum):
    HULL = "Hull Plates and Structure"
    WELDS = "Welds and Joints"
    TANKS = "Cargo Tanks"
    PIPING = "Piping Systems"
    PROPELLER = "Propeller and Shaft"
    RUDDER = "Rudder and Steering"
    DECK = "Deck Equipment"


class InspectionStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed - Requires Attention"


class NDTInspectionChecklist:
    """
    A comprehensive checklist for conducting NDT inspections on marine vessels
    following Marine NDT & Engineering Works quality service principles.
    """
    
    def __init__(self, vessel_name: str, vessel_id: str):
        self.vessel_name = vessel_name
        self.vessel_id = vessel_id
        self.inspection_date = datetime.now().strftime("%Y-%m-%d")
        self.checklist_items = []
        self.overall_status = InspectionStatus.PENDING
        self.inspection_type = None
        self.component = None
        
    def add_checklist_item(self, component: VesselComponent, inspection_type: InspectionType,
                          standard: str, procedure: str, acceptance_criteria: str):
        """
        Add an item to the inspection checklist.
        
        Args:
            component: Vessel component being inspected
            inspection_type: Type of NDT inspection
            standard: Reference standard (e.g., ASTM, ISO, etc.)
            procedure: Procedure reference number
            acceptance_criteria: Criteria for passing inspection
        """
        item = {
            "component": component,
            "type": inspection_type,
            "standard": standard,
            "procedure": procedure,
            "criteria": acceptance_criteria,
            "status": InspectionStatus.PENDING,
            "findings": "",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.checklist_items.append(item)
        
    def update_item_status(self, item_index: int, status: InspectionStatus, findings: str = ""):
        """
        Update the status of a checklist item.
        
        Args:
            item_index: Index of the item in the checklist
            status: New status of the inspection item
            findings: Any findings from the inspection
        """
        if 0 <= item_index < len(self.checklist_items):
            self.checklist_items[item_index]["status"] = status
            self.checklist_items[item_index]["findings"] = findings
            self.checklist_items[item_index]["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            raise IndexError("Checklist item index out of range")
        
    def generate_report(self) -> dict:
        """
        Generate a comprehensive inspection report.
        
        Returns:
            Dictionary containing all inspection data
        """
        completed_items = sum(1 for item in self.checklist_items 
                            if item["status"] == InspectionStatus.COMPLETED)
        total_items = len(self.checklist_items)
        
        # Update overall status
        if total_items == 0:
            self.overall_status = InspectionStatus.PENDING
        elif completed_items == total_items:
            self.overall_status = InspectionStatus.COMPLETED
        else:
            self.overall_status = InspectionStatus.IN_PROGRESS
            
        return {
            "vessel_info": {
                "name": self.vessel_name,
                "id": self.vessel_id,
                "inspection_date": self.inspection_date
            },
            "inspection_summary": {
                "total_items": total_items,
                "completed": completed_items,
                "pending": total_items - completed_items,
                "overall_status": self.overall_status.value
            },
            "checklist_items": self.checklist_items
        }
        
    def save_report(self, filename: str):
        """
        Save the inspection report to a JSON file.
        
        Args:
            filename: Path to the output file
        """
        report = self.generate_report()
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4, default=str)
        except IOError as e:
            raise IOError(f"Failed to save report: {str(e)}")
    
    @classmethod
    def create_standard_checklist(cls, vessel_name: str, vessel_id: str) -> 'NDTInspectionChecklist':
        """
        Create a standard checklist based on typical marine inspection requirements.
        
        Args:
            vessel_name: Name of the vessel
            vessel_id: Unique identifier for the vessel
            
        Returns:
            Pre-configured NDT inspection checklist
        """
        checklist = cls(vessel_name, vessel_id)
        
        # Standard inspection items
        standard_items = [
            (VesselComponent.HULL, InspectionType.VISUAL, "ISO 8502", "VIS-01", "No visible cracks or deformations"),
            (VesselComponent.HULL, InspectionType.ULTRASONIC, "ASTM E114", "UT-03", "Thickness within 10% of design spec"),
            (VesselComponent.WELDS, InspectionType.RADIOGRAPHIC, "ASME V", "RT-02", "No indications exceeding Level B"),
            (VesselComponent.WELDS, InspectionType.MAGNETIC_PARTICLE, "ASTM E709", "MT-01", "No relevant indications"),
            (VesselComponent.TANKS, InspectionType.VISUAL, "IMO MSPC", "VIS-02", "No coating breakdown or wastage"),
            (VesselComponent.TANKS, InspectionType.ULTRASONIC, "API 650", "UT-04", "Thickness > minimum required"),
            (VesselComponent.PIPING, InspectionType.DYE_PENETRANT, "ASTM E165", "PT-01", "No surface-breaking defects"),
            (VesselComponent.PROPELLER, InspectionType.MAGNETIC_PARTICLE, "ASTM E709", "MT-02", "No cracks detected"),
            (VesselComponent.RUDDER, InspectionType.ULTRASONIC, "ABS Ch7", "UT-05", "No void areas detected"),
            (VesselComponent.DECK, InspectionType.VISUAL, "ISO 8502", "VIS-03", "No structural deformations")
        ]
        
        for component, insp_type, standard, procedure, criteria in standard_items:
            checklist.add_checklist_item(component, insp_type, standard, procedure, criteria)
            
        return checklist


# Example usage
if __name__ == "__main__":
    # Create a standard checklist for a vessel
    checklist = NDTInspectionChecklist.create_standard_checklist(
        vessel_name="MV Ocean Carrier",
        vessel_id="OC-2023-001"
    )
    
    # Simulate completing some inspections
    try:
        checklist.update_item_status(0, InspectionStatus.COMPLETED, "No defects found")
        checklist.update_item_status(1, InspectionStatus.COMPLETED, "Thickness measurements within spec")
        checklist.update_item_status(2, InspectionStatus.FAILED, "Porosity detected in weld area RT-12-45")
        
        # Generate and save report
        report = checklist.generate_report()
        checklist.save_report("vessel_inspection_report.json")
        
        print(f"Inspection report generated for {checklist.vessel_name}")
        print(f"Overall status: {checklist.overall_status.value}")
        
    except Exception as e:
        print(f"Error during inspection process: {str(e)}")
```
