"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Write Python code to simulate the design of an automation system based on the engineering services described by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_4439e6cea81b5bea
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Automation System Simulation for Multiservicios Industriales 3L

This module simulates an industrial automation system with various services including:
- Process control
- Equipment monitoring
- Maintenance scheduling
- Energy optimization
"""

import random
import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('AutomationSystem')

class EquipmentStatus(Enum):
    """Status of industrial equipment"""
    OPERATIONAL = auto()
    MAINTENANCE = auto()
    FAILED = auto()
    IDLE = auto()

class ProcessType(Enum):
    """Types of industrial processes"""
    MANUFACTURING = auto()
    PACKAGING = auto()
    QUALITY_CONTROL = auto()
    MATERIAL_HANDLING = auto()

@dataclass
class Equipment:
    """Represents industrial equipment"""
    id: str
    name: str
    status: EquipmentStatus
    last_maintenance: datetime
    next_maintenance: datetime
    energy_consumption: float  # kWh
    
    def needs_maintenance(self) -> bool:
        """Check if equipment needs maintenance"""
        return datetime.now() >= self.next_maintenance
    
    def perform_maintenance(self):
        """Perform maintenance on equipment"""
        if self.status == EquipmentStatus.FAILED:
            logger.warning(f"Cannot perform maintenance on failed equipment {self.id}")
            return False
        
        logger.info(f"Performing maintenance on {self.id}")
        self.status = EquipmentStatus.MAINTENANCE
        time.sleep(1)  # Simulate maintenance time
        self.status = EquipmentStatus.OPERATIONAL
        self.last_maintenance = datetime.now()
        self.next_maintenance = self.last_maintenance + timedelta(days=30)
        return True

@dataclass
class Process:
    """Represents an industrial process"""
    id: str
    type: ProcessType
    equipment_used: List[Equipment]
    parameters: Dict[str, float]
    is_running: bool = False
    
    def start(self):
        """Start the process"""
        if self.is_running:
            logger.warning(f"Process {self.id} is already running")
            return False
        
        for equipment in self.equipment_used:
            if equipment.status != EquipmentStatus.OPERATIONAL:
                logger.error(f"Cannot start process {self.id}: Equipment {equipment.id} not operational")
                return False
        
        logger.info(f"Starting process {self.id}")
        self.is_running = True
        return True
    
    def stop(self):
        """Stop the process"""
        if not self.is_running:
            logger.warning(f"Process {self.id} is not running")
            return False
        
        logger.info(f"Stopping process {self.id}")
        self.is_running = False
        return True

class AutomationSystem:
    """Main automation system class"""
    
    def __init__(self):
        self.equipment: Dict[str, Equipment] = {}
        self.processes: Dict[str, Process] = {}
        self.energy_consumption: float = 0.0
        self.total_uptime: float = 0.0
    
    def add_equipment(self, equipment: Equipment):
        """Add equipment to the system"""
        if equipment.id in self.equipment:
            logger.warning(f"Equipment {equipment.id} already exists")
            return False
        
        self.equipment[equipment.id] = equipment
        logger.info(f"Added equipment {equipment.id}")
        return True
    
    def remove_equipment(self, equipment_id: str):
        """Remove equipment from the system"""
        if equipment_id not in self.equipment:
            logger.warning(f"Equipment {equipment_id} not found")
            return False
        
        # Check if equipment is used in any process
        for process in self.processes.values():
            if any(e.id == equipment_id for e in process.equipment_used):
                logger.error(f"Cannot remove equipment {equipment_id}: Used in process {process.id}")
                return False
        
        del self.equipment[equipment_id]
        logger.info(f"Removed equipment {equipment_id}")
        return True
    
    def add_process(self, process: Process):
        """Add process to the system"""
        if process.id in self.processes:
            logger.warning(f"Process {process.id} already exists")
            return False
        
        # Validate all equipment exists
        for equipment in process.equipment_used:
            if equipment.id not in self.equipment:
                logger.error(f"Cannot add process {process.id}: Equipment {equipment.id} not found")
                return False
        
        self.processes[process.id] = process
        logger.info(f"Added process {process.id}")
        return True
    
    def remove_process(self, process_id: str):
        """Remove process from the system"""
        if process_id not in self.processes:
            logger.warning(f"Process {process_id} not found")
            return False
        
        if self.processes[process_id].is_running:
            logger.error(f"Cannot remove process {process_id}: Process is running")
            return False
        
        del self.processes[process_id]
        logger.info(f"Removed process {process_id}")
        return True
    
    def run_simulation(self, duration: int = 60):
        """Run the automation system simulation"""
        logger.info(f"Starting simulation for {duration} seconds")
        start_time = time.time()
        
        try:
            while time.time() - start_time < duration:
                # Randomly start/stop processes
                for process in self.processes.values():
                    if random.random() < 0.1:  # 10% chance to toggle
                        if process.is_running:
                            process.stop()
                        else:
                            process.start()
                
                # Check for maintenance needs
                for equipment in self.equipment.values():
                    if equipment.needs_maintenance():
                        equipment.perform_maintenance()
                
                # Simulate random equipment failures
                if random.random() < 0.05:  # 5% chance of failure
                    equipment_id = random.choice(list(self.equipment.keys()))
                    equipment = self.equipment[equipment_id]
                    if equipment.status == EquipmentStatus.OPERATIONAL:
                        logger.warning(f"Equipment {equipment_id} has failed!")
                        equipment.status = EquipmentStatus.FAILED
                
                # Update metrics
                running_processes = sum(1 for p in self.processes.values() if p.is_running)
                self.total_uptime += running_processes / len(self.processes) if self.processes else 0
                
                current_energy = sum(
                    e.energy_consumption 
                    for e in self.equipment.values() 
                    if e.status == EquipmentStatus.OPERATIONAL
                )
                self.energy_consumption += current_energy
                
                time.sleep(1)  # Simulate 1 second of operation
            
            logger.info("Simulation completed successfully")
            return True
        
        except Exception as e:
            logger.error(f"Simulation error: {str(e)}")
            return False
    
    def generate_report(self):
        """Generate a system status report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "equipment_count": len(self.equipment),
            "operational_equipment": sum(
                1 for e in self.equipment.values() 
                if e.status == EquipmentStatus.OPERATIONAL
            ),
            "process_count": len(self.processes),
            "running_processes": sum(1 for p in self.processes.values() if p.is_running),
            "total_energy_consumption": round(self.energy_consumption, 2),
            "system_uptime": round(self.total_uptime * 100, 2),
            "maintenance_needed": [
                e.id for e in self.equipment.values() 
                if e.needs_maintenance()
            ]
        }
        return report

def create_sample_system():
    """Create a sample automation system with test data"""
    system = AutomationSystem()
    
    # Add equipment
    equipment_data = [
        ("EQ-001", "Conveyor Belt", 5.2),
        ("EQ-002", "Packaging Machine", 8.5),
        ("EQ-003", "Quality Scanner", 2.1),
        ("EQ-004", "Robotic Arm", 6.7),
    ]
    
    for eq_id, name, consumption in equipment_data:
        last_maintenance = datetime.now() - timedelta(days=random.randint(0, 29))
        next_maintenance = last_maintenance + timedelta(days=30)
        equipment = Equipment(
            id=eq_id,
            name=name,
            status=EquipmentStatus.OPERATIONAL,
            last_maintenance=last_maintenance,
            next_maintenance=next_maintenance,
            energy_consumption=consumption
        )
        system.add_equipment(equipment)
    
    # Add processes
    process_data = [
        ("PR-001", ProcessType.MANUFACTURING
