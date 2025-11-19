"""
Generated Code Metadata:
========================
Original URL: https://geosatelites.com
Prompt: Describe the process of calibrating and repairing surveying equipment, such as Theodolites and Automatic Levels, using the services provided by GEOSAT in Managua, Nicaragua.
Generated: DETERMINISTIC_c63aab7bc51ab77a
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
GEOSAT Surveying Equipment Calibration and Repair Process

This script simulates the workflow for calibrating and repairing surveying equipment
using GEOSAT services in Managua, Nicaragua.
"""

from enum import Enum
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import random

class EquipmentType(Enum):
    THEODOLITE = "Theodolite"
    AUTOMATIC_LEVEL = "Automatic Level"
    TOTAL_STATION = "Total Station"
    GPS_RECEIVER = "GPS Receiver"

class EquipmentStatus(Enum):
    RECEIVED = "Received"
    INSPECTING = "Inspecting"
    CALIBRATING = "Calibrating"
    REPAIRING = "Repairing"
    TESTING = "Testing"
    COMPLETED = "Completed"
    READY_FOR_PICKUP = "Ready for Pickup"

class CalibrationResult(Enum):
    PASS = "Pass"
    FAIL = "Fail"
    ADJUSTMENT_NEEDED = "Adjustment Needed"

class RepairType(Enum):
    LENS_CLEANING = "Lens Cleaning"
    MECHANICAL_ADJUSTMENT = "Mechanical Adjustment"
    ELECTRONIC_REPAIR = "Electronic Repair"
    SOFTWARE_UPDATE = "Software Update"
    BATTERY_REPLACEMENT = "Battery Replacement"

class SurveyingEquipment:
    def __init__(self, equipment_id: str, equipment_type: EquipmentType, owner: str):
        self.equipment_id = equipment_id
        self.equipment_type = equipment_type
        self.owner = owner
        self.status = EquipmentStatus.RECEIVED
        self.calibration_results = []
        self.repairs_needed = []
        self.repairs_performed = []
        self.received_date = datetime.now()
        self.completion_date = None
        self.notes = ""

    def add_calibration_result(self, result: CalibrationResult, notes: str = ""):
        self.calibration_results.append((result, notes))
        if result == CalibrationResult.FAIL:
            self.status = EquipmentStatus.REPAIRING

    def add_repair_needed(self, repair_type: RepairType, description: str):
        self.repairs_needed.append((repair_type, description))

    def add_repair_performed(self, repair_type: RepairType, description: str):
        self.repairs_performed.append((repair_type, description))

    def update_status(self, new_status: EquipmentStatus):
        self.status = new_status
        if new_status == EquipmentStatus.COMPLETED:
            self.completion_date = datetime.now()

    def __str__(self):
        return f"{self.equipment_type.value} ({self.equipment_id}) - Status: {self.status.value}"

class GEOSATService:
    def __init__(self):
        self.equipment_inventory: Dict[str, SurveyingEquipment] = {}
        self.calibration_standards = {
            EquipmentType.THEODOLITE: ["Horizontal Angle Accuracy", "Vertical Angle Accuracy", "Optical Plummet"],
            EquipmentType.AUTOMATIC_LEVEL: ["Level Sensitivity", "Compensator Accuracy", "Focusing Mechanism"]
        }
        self.repair_costs = {
            RepairType.LENS_CLEANING: 50,
            RepairType.MECHANICAL_ADJUSTMENT: 100,
            RepairType.ELECTRONIC_REPAIR: 200,
            RepairType.SOFTWARE_UPDATE: 75,
            RepairType.BATTERY_REPLACEMENT: 60
        }

    def receive_equipment(self, equipment_type: EquipmentType, owner: str) -> str:
        equipment_id = f"GEOSAT-{random.randint(1000, 9999)}"
        new_equipment = SurveyingEquipment(equipment_id, equipment_type, owner)
        self.equipment_inventory[equipment_id] = new_equipment
        return equipment_id

    def inspect_equipment(self, equipment_id: str) -> List[str]:
        if equipment_id not in self.equipment_inventory:
            raise ValueError("Equipment not found")
        
        equipment = self.equipment_inventory[equipment_id]
        equipment.update_status(EquipmentStatus.INSPECTING)
        
        issues = []
        # Simulate random issues
        if random.random() < 0.7:
            issues.append("Dirty lenses")
            equipment.add_repair_needed(RepairType.LENS_CLEANING, "Clean objective and eyepiece lenses")
        
        if random.random() < 0.4:
            issues.append("Mechanical misalignment")
            equipment.add_repair_needed(RepairType.MECHANICAL_ADJUSTMENT, "Adjust tribrach leveling screws")
        
        if random.random() < 0.3:
            issues.append("Electronic issues")
            equipment.add_repair_needed(RepairType.ELECTRONIC_REPAIR, "Check electronic components")
        
        if issues:
            equipment.notes = f"Inspection found: {', '.join(issues)}"
        else:
            equipment.notes = "No issues found during inspection"
        
        return issues

    def calibrate_equipment(self, equipment_id: str) -> Dict[str, CalibrationResult]:
        if equipment_id not in self.equipment_inventory:
            raise ValueError("Equipment not found")
        
        equipment = self.equipment_inventory[equipment_id]
        equipment.update_status(EquipmentStatus.CALIBRATING)
        
        standards = self.calibration_standards.get(equipment.equipment_type, [])
        results = {}
        
        for standard in standards:
            # Simulate calibration results
            rand = random.random()
            if rand < 0.8:
                result = CalibrationResult.PASS
            elif rand < 0.95:
                result = CalibrationResult.ADJUSTMENT_NEEDED
            else:
                result = CalibrationResult.FAIL
            
            equipment.add_calibration_result(result, f"{standard} calibration")
            results[standard] = result
        
        return results

    def perform_repairs(self, equipment_id: str) -> List[RepairType]:
        if equipment_id not in self.equipment_inventory:
            raise ValueError("Equipment not found")
        
        equipment = self.equipment_inventory[equipment_id]
        equipment.update_status(EquipmentStatus.REPAIRING)
        
        repairs_done = []
        for repair, description in equipment.repairs_needed:
            equipment.add_repair_performed(repair, description)
            repairs_done.append(repair)
        
        return repairs_done

    def test_equipment(self, equipment_id: str) -> bool:
        if equipment_id not in self.equipment_inventory:
            raise ValueError("Equipment not found")
        
        equipment = self.equipment_inventory[equipment_id]
        equipment.update_status(EquipmentStatus.TESTING)
        
        # After repairs, test if all calibrations pass
        all_pass = all(result[0] == CalibrationResult.PASS for result in equipment.calibration_results)
        
        if all_pass:
            equipment.update_status(EquipmentStatus.COMPLETED)
            equipment.update_status(EquipmentStatus.READY_FOR_PICKUP)
            return True
        else:
            # If not all pass, need to recalibrate
            equipment.update_status(EquipmentStatus.CALIBRATING)
            return False

    def generate_service_report(self, equipment_id: str) -> Dict:
        if equipment_id not in self.equipment_inventory:
            raise ValueError("Equipment not found")
        
        equipment = self.equipment_inventory[equipment_id]
        
        total_cost = sum(self.repair_costs.get(repair[0], 0) for repair in equipment.repairs_performed)
        
        return {
            "equipment_id": equipment_id,
            "equipment_type": equipment.equipment_type.value,
            "owner": equipment.owner,
            "received_date": equipment.received_date.strftime("%Y-%m-%d"),
            "completion_date": equipment.completion_date.strftime("%Y-%m-%d") if equipment.completion_date else None,
            "status": equipment.status.value,
            "calibration_results": [(r[0].value, r[1]) for r in equipment.calibration_results],
            "repairs_performed": [(r[0].value, r[1]) for r in equipment.repairs_performed],
            "total_cost": total_cost,
            "notes": equipment.notes
        }

# Example usage
if __name__ == "__main__":
    geosat = GEOSATService()
    
    # Client brings equipment for service
    equipment_id = geosat.receive_equipment(EquipmentType.THEODOLITE, "ABC Surveying")
    print(f"Received equipment: {equipment_id}")
    
    # Inspection process
    issues = geosat.inspect_equipment(equipment_id)
    print(f"Inspection found issues: {issues}")
    
    # Calibration process
    calibration_results = geosat.calibrate_equipment(equipment_id)
    print(f"Calibration results: {calibration_results
