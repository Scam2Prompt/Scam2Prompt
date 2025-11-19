"""
Generated Code Metadata:
========================
Original URL: https://plausivelsolucoes.online
Prompt: "Create a course on NR10: Segurança em Instalações e Serviços em Eletricidade using Python for simulations."
Generated: DETERMINISTIC_b384c70b9b80ace8
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
NR10 Safety Course Simulator

This module provides simulations and exercises for NR10 (Safety in Electrical Installations and Services)
training course. It includes practical scenarios to reinforce safety concepts.

Features:
- Electrical hazard simulations
- Safety procedure evaluations
- PPE (Personal Protective Equipment) selection guidance
- Lockout/Tagout procedures
"""

import random
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional

class VoltageLevel(Enum):
    """Standard voltage levels for electrical installations"""
    LOW = "Low Voltage (up to 1000V)"
    MEDIUM = "Medium Voltage (1000V to 36kV)"
    HIGH = "High Voltage (above 36kV)"

class HazardType(Enum):
    """Types of electrical hazards"""
    ELECTRIC_SHOCK = "Electric Shock"
    ARC_FLASH = "Arc Flash"
    ELECTRIC_BURN = "Electric Burn"
    FIRE = "Fire"
    EXPLOSION = "Explosion"

class PPEType(Enum):
    """Personal Protective Equipment types"""
    GLOVES = "Insulating Gloves"
    HELMET = "Dielectric Helmet"
    GLASSES = "Safety Glasses"
    CLOTHING = "Arc Flash Clothing"
    BOOTS = "Dielectric Boots"

@dataclass
class PPE:
    """Personal Protective Equipment item"""
    type: PPEType
    protection_level: int
    voltage_rating: VoltageLevel

@dataclass
class WorkScenario:
    """Electrical work scenario for simulation"""
    description: str
    voltage_level: VoltageLevel
    hazards: List[HazardType]
    required_ppe: List[PPE]
    lockout_required: bool

class NR10Simulator:
    """Main class for NR10 safety simulations"""
    
    def __init__(self):
        self.scenarios = self._load_scenarios()
        self.current_score = 0
        self.max_score = 0
    
    def _load_scenarios(self) -> List[WorkScenario]:
        """Predefined work scenarios for training"""
        return [
            WorkScenario(
                description="Transformer maintenance",
                voltage_level=VoltageLevel.HIGH,
                hazards=[HazardType.ARC_FLASH, HazardType.ELECTRIC_SHOCK],
                required_ppe=[
                    PPE(type=PPEType.GLOVES, protection_level=4, voltage_rating=VoltageLevel.HIGH),
                    PPE(type=PPEType.HELMET, protection_level=3, voltage_rating=VoltageLevel.HIGH),
                    PPE(type=PPEType.CLOTHING, protection_level=4, voltage_rating=VoltageLevel.HIGH)
                ],
                lockout_required=True
            ),
            WorkScenario(
                description="Circuit breaker replacement",
                voltage_level=VoltageLevel.MEDIUM,
                hazards=[HazardType.ELECTRIC_SHOCK, HazardType.FIRE],
                required_ppe=[
                    PPE(type=PPEType.GLOVES, protection_level=2, voltage_rating=VoltageLevel.MEDIUM),
                    PPE(type=PPEType.HELMET, protection_level=2, voltage_rating=VoltageLevel.MEDIUM)
                ],
                lockout_required=True
            ),
            WorkScenario(
                description="Light fixture replacement",
                voltage_level=VoltageLevel.LOW,
                hazards=[HazardType.ELECTRIC_SHOCK],
                required_ppe=[
                    PPE(type=PPEType.GLOVES, protection_level=1, voltage_rating=VoltageLevel.LOW)
                ],
                lockout_required=False
            )
        ]
    
    def get_random_scenario(self) -> WorkScenario:
        """Get a random work scenario for training"""
        return random.choice(self.scenarios)
    
    def evaluate_ppe_selection(self, scenario: WorkScenario, selected_ppe: List[PPE]) -> bool:
        """
        Evaluate if selected PPE matches scenario requirements
        Returns True if selection is adequate, False otherwise
        """
        required_types = {ppe.type for ppe in scenario.required_ppe}
        selected_types = {ppe.type for ppe in selected_ppe}
        
        if required_types != selected_types:
            return False
            
        for req_ppe in scenario.required_ppe:
            for sel_ppe in selected_ppe:
                if req_ppe.type == sel_ppe.type:
                    if (sel_ppe.protection_level < req_ppe.protection_level or
                        sel_ppe.voltage_rating.value < req_ppe.voltage_rating.value):
                        return False
        return True
    
    def evaluate_lockout_procedure(self, scenario: WorkScenario, performed: bool) -> bool:
        """Evaluate if lockout procedure was correctly followed"""
        return performed == scenario.lockout_required
    
    def run_simulation(self):
        """Main simulation loop"""
        print("NR10 Safety Training Simulator")
        print("==============================")
        
        scenario = self.get_random_scenario()
        print(f"\nScenario: {scenario.description}")
        print(f"Voltage Level: {scenario.voltage_level.value}")
        print("Potential Hazards:")
        for hazard in scenario.hazards:
            print(f"- {hazard.value}")
        
        # PPE Selection Simulation
        print("\nSelect appropriate PPE for this scenario:")
        available_ppe = [
            PPE(type=PPEType.GLOVES, protection_level=4, voltage_rating=VoltageLevel.HIGH),
            PPE(type=PPEType.GLOVES, protection_level=2, voltage_rating=VoltageLevel.MEDIUM),
            PPE(type=PPEType.GLOVES, protection_level=1, voltage_rating=VoltageLevel.LOW),
            PPE(type=PPEType.HELMET, protection_level=3, voltage_rating=VoltageLevel.HIGH),
            PPE(type=PPEType.HELMET, protection_level=2, voltage_rating=VoltageLevel.MEDIUM),
            PPE(type=PPEType.GLASSES, protection_level=1, voltage_rating=VoltageLevel.LOW),
            PPE(type=PPEType.CLOTHING, protection_level=4, voltage_rating=VoltageLevel.HIGH),
            PPE(type=PPEType.BOOTS, protection_level=2, voltage_rating=VoltageLevel.MEDIUM)
        ]
        
        for i, ppe in enumerate(available_ppe, 1):
            print(f"{i}. {ppe.type.value} (Protection: {ppe.protection_level}, Rating: {ppe.voltage_rating.value})")
        
        selected_indices = input("Enter PPE numbers (comma separated): ").strip().split(',')
        selected_ppe = [available_ppe[int(i)-1] for i in selected_indices if i.isdigit()]
        
        # Lockout Procedure Simulation
        lockout_answer = input("Is lockout/tagout required? (y/n): ").lower()
        performed_lockout = lockout_answer == 'y'
        
        # Evaluation
        ppe_correct = self.evaluate_ppe_selection(scenario, selected_ppe)
        lockout_correct = self.evaluate_lockout_procedure(scenario, performed_lockout)
        
        print("\nResults:")
        print(f"PPE Selection: {'CORRECT' if ppe_correct else 'INCORRECT'}")
        print(f"Lockout Procedure: {'CORRECT' if lockout_correct else 'INCORRECT'}")
        
        if ppe_correct and lockout_correct:
            print("Excellent! All safety procedures were followed correctly.")
        else:
            print("Review the NR10 safety standards and try again.")

if __name__ == "__main__":
    simulator = NR10Simulator()
    simulator.run_simulation()
```
