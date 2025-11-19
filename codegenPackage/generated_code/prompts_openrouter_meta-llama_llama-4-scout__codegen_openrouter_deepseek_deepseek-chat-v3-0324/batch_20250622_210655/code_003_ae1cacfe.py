"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: "Design a data cabling and LAN infrastructure for a commercial building, considering factors such as scalability, security, and performance, as per the expertise of Vivek Enterprises."
Generated: DETERMINISTIC_ae1cacfe057ac8e9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Data Cabling and LAN Infrastructure Design for Commercial Buildings
Author: Vivek Enterprises
Date: [Current Date]
Version: 1.0
"""

import json
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import math

class CableType(Enum):
    CAT6 = "CAT6"
    CAT6A = "CAT6A"
    FIBER_OM3 = "Fiber OM3"
    FIBER_OM4 = "Fiber OM4"

class TerminationType(Enum):
    RJ45 = "RJ45"
    LC = "LC"
    SC = "SC"

class NetworkDeviceType(Enum):
    SWITCH = "Switch"
    ROUTER = "Router"
    FIREWALL = "Firewall"
    ACCESS_POINT = "Access Point"

@dataclass
class NetworkDevice:
    id: str
    type: NetworkDeviceType
    model: str
    ports: int
    uplink_speed: int  # in Gbps
    location: str
    security_features: List[str]

@dataclass
class CableRun:
    id: str
    source_device: str
    destination_device: str
    cable_type: CableType
    length: float  # in meters
    termination_a: TerminationType
    termination_b: TerminationType
    label: str

@dataclass
class FloorPlan:
    floor_number: int
    rooms: List[str]
    network_closets: List[str]
    cable_runs: List[CableRun]

@dataclass
class BuildingDesign:
    name: str
    floors: int
    floor_plans: List[FloorPlan]
    network_devices: List[NetworkDevice]
    security_policy: Dict[str, str]
    scalability_factors: Dict[str, str]

class LANDesigner:
    def __init__(self, building_name: str, floors: int):
        self.design = BuildingDesign(
            name=building_name,
            floors=floors,
            floor_plans=[],
            network_devices=[],
            security_policy={},
            scalability_factors={}
        )
    
    def add_floor_plan(self, floor_number: int, rooms: List[str], network_closets: List[str]):
        if floor_number > self.design.floors:
            raise ValueError("Floor number exceeds total building floors")
        
        floor_plan = FloorPlan(
            floor_number=floor_number,
            rooms=rooms,
            network_closets=network_closets,
            cable_runs=[]
        )
        self.design.floor_plans.append(floor_plan)
    
    def add_network_device(self, device: NetworkDevice):
        self.design.network_devices.append(device)
    
    def add_cable_run(self, floor_number: int, cable_run: CableRun):
        for floor in self.design.floor_plans:
            if floor.floor_number == floor_number:
                floor.cable_runs.append(cable_run)
                return
        raise ValueError(f"Floor {floor_number} not found in design")
    
    def set_security_policy(self, policy: Dict[str, str]):
        self.design.security_policy = policy
    
    def set_scalability_factors(self, factors: Dict[str, str]):
        self.design.scalability_factors = factors
    
    def calculate_cable_length(self, floor_number: int) -> float:
        total_length = 0.0
        for floor in self.design.floor_plans:
            if floor.floor_number == floor_number:
                for run in floor.cable_runs:
                    total_length += run.length
        return total_length
    
    def generate_bill_of_materials(self) -> Dict:
        bom = {
            "cables": {},
            "devices": len(self.design.network_devices),
            "terminations": {}
        }
        
        # Count cable types
        for floor in self.design.floor_plans:
            for run in floor.cable_runs:
                cable_type = run.cable_type.value
                bom["cables"][cable_type] = bom["cables"].get(cable_type, 0) + math.ceil(run.length)
        
        # Count termination types
        for floor in self.design.floor_plans:
            for run in floor.cable_runs:
                term_a = run.termination_a.value
                term_b = run.termination_b.value
                bom["terminations"][term_a] = bom["terminations"].get(term_a, 0) + 1
                bom["terminations"][term_b] = bom["terminations"].get(term_b, 0) + 1
        
        return bom
    
    def validate_design(self) -> List[str]:
        errors = []
        
        # Check all floors have plans
        if len(self.design.floor_plans) != self.design.floors:
            errors.append("Number of floor plans doesn't match total floors")
        
        # Check cable runs have valid devices
        device_ids = {d.id for d in self.design.network_devices}
        for floor in self.design.floor_plans:
            for run in floor.cable_runs:
                if run.source_device not in device_ids:
                    errors.append(f"Cable run {run.id} has invalid source device")
                if run.destination_device not in device_ids:
                    errors.append(f"Cable run {run.id} has invalid destination device")
        
        return errors
    
    def export_design(self, file_path: str):
        if self.validate_design():
            raise ValueError("Design has validation errors")
        
        design_dict = {
            "name": self.design.name,
            "floors": self.design.floors,
            "floor_plans": [fp.__dict__ for fp in self.design.floor_plans],
            "network_devices": [nd.__dict__ for nd in self.design.network_devices],
            "security_policy": self.design.security_policy,
            "scalability_factors": self.design.scalability_factors
        }
        
        with open(file_path, 'w') as f:
            json.dump(design_dict, f, indent=4)
    
    @classmethod
    def import_design(cls, file_path: str) -> 'LANDesigner':
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        designer = cls(data["name"], data["floors"])
        
        # Rebuild floor plans
        for fp_data in data["floor_plans"]:
            floor_plan = FloorPlan(
                floor_number=fp_data["floor_number"],
                rooms=fp_data["rooms"],
                network_closets=fp_data["network_closets"],
                cable_runs=[]
            )
            
            # Rebuild cable runs
            for cr_data in fp_data["cable_runs"]:
                cable_run = CableRun(
                    id=cr_data["id"],
                    source_device=cr_data["source_device"],
                    destination_device=cr_data["destination_device"],
                    cable_type=CableType(cr_data["cable_type"]),
                    length=cr_data["length"],
                    termination_a=TerminationType(cr_data["termination_a"]),
                    termination_b=TerminationType(cr_data["termination_b"]),
                    label=cr_data["label"]
                )
                floor_plan.cable_runs.append(cable_run)
            
            designer.design.floor_plans.append(floor_plan)
        
        # Rebuild network devices
        for nd_data in data["network_devices"]:
            device = NetworkDevice(
                id=nd_data["id"],
                type=NetworkDeviceType(nd_data["type"]),
                model=nd_data["model"],
                ports=nd_data["ports"],
                uplink_speed=nd_data["uplink_speed"],
                location=nd_data["location"],
                security_features=nd_data["security_features"]
            )
            designer.design.network_devices.append(device)
        
        designer.design.security_policy = data["security_policy"]
        designer.design.scalability_factors = data["scalability_factors"]
        
        return designer

# Example usage
if __name__ == "__main__":
    designer = LANDesigner("Vivek Enterprises HQ", 5)
    
    # Add floor plans
    designer.add_floor_plan(1, ["Reception", "Conference Room", "IT Room"], ["IT Room"])
    designer.add_floor_plan(2, ["Office Area A", "Meeting Room"], ["Network Closet"])
    
    # Add network devices
    designer.add_network_device(NetworkDevice(
        id="SW01",
        type=NetworkDeviceType.SWITCH,
        model="Cisco Catalyst 9300",
        ports=48,
        uplink_speed=10,
        location="IT Room",
        security_features=["MAC filtering", "Port security"]
    ))
    
    designer.add_network_device(NetworkDevice(
        id="AP01",
        type=NetworkDeviceType.ACCESS_POINT,
        model="Aruba AP-515",
        ports=1,
        uplink_speed=1,
        location="Conference Room",
        security_features=["WPA3", "802.1X"]
    ))
