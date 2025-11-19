"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write code to simulate the impact of safety measures on the performance of construction operations, addressing issues of efficiency and worker conditions as discussed by AFCO.
Generated: DETERMINISTIC_5585dadf4adca15d
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto
import random
from datetime import datetime, timedelta

class SafetyMeasure(Enum):
    """Enum representing different safety measures that can be implemented."""
    PPE = auto()  # Personal Protective Equipment
    TRAINING = auto()  # Safety training programs
    SUPERVISION = auto()  # Increased supervision
    EQUIPMENT_UPGRADE = auto()  # Upgraded safety equipment
    WORK_REST_SCHEDULE = auto()  # Optimized work-rest schedules

@dataclass
class Worker:
    """Represents a construction worker with attributes affecting performance and safety."""
    id: int
    skill_level: float  # 0-1 scale
    fatigue: float = 0.0  # 0-1 scale
    safety_compliance: float = 0.8  # 0-1 scale, default 80% compliance

@dataclass
class ConstructionTask:
    """Represents a construction task with base performance metrics."""
    id: int
    name: str
    base_duration: float  # in hours
    base_risk: float  # 0-1 scale
    required_skill: float  # 0-1 scale

@dataclass
class SafetyImpact:
    """Represents the impact of a safety measure on various metrics."""
    measure: SafetyMeasure
    efficiency_impact: float  # -1 to 1 (-ve is reduction, +ve is improvement)
    risk_reduction: float  # 0-1 scale
    cost: float  # Implementation cost

class ConstructionSimulation:
    """Simulates the impact of safety measures on construction operations."""
    
    def __init__(self, workers: List[Worker], tasks: List[ConstructionTask], 
                 safety_impacts: Dict[SafetyMeasure, SafetyImpact]):
        self.workers = workers
        self.tasks = tasks
        self.safety_impacts = safety_impacts
        self.active_measures: List[SafetyMeasure] = []
        self.results = []
        
    def add_safety_measure(self, measure: SafetyMeasure) -> None:
        """Add a safety measure to the simulation."""
        if measure not in self.active_measures:
            self.active_measures.append(measure)
    
    def remove_safety_measure(self, measure: SafetyMeasure) -> None:
        """Remove a safety measure from the simulation."""
        if measure in self.active_measures:
            self.active_measures.remove(measure)
    
    def calculate_task_duration(self, task: ConstructionTask, worker: Worker) -> float:
        """Calculate the adjusted duration of a task considering safety measures and worker conditions."""
        duration = task.base_duration
        
        # Adjust for worker skill
        skill_factor = 1.0 + (task.required_skill - worker.skill_level)
        duration *= skill_factor
        
        # Adjust for fatigue
        fatigue_factor = 1.0 + worker.fatigue * 0.5
        duration *= fatigue_factor
        
        # Adjust for safety measures
        for measure in self.active_measures:
            impact = self.safety_impacts[measure]
            duration *= (1.0 - impact.efficiency_impact)
        
        return max(duration, task.base_duration * 0.5)  # Minimum 50% of base duration
    
    def calculate_task_risk(self, task: ConstructionTask, worker: Worker) -> float:
        """Calculate the adjusted risk of a task considering safety measures and worker conditions."""
        risk = task.base_risk
        
        # Adjust for worker compliance
        risk *= (1.0 - worker.safety_compliance)
        
        # Adjust for safety measures
        for measure in self.active_measures:
            impact = self.safety_impacts[measure]
            risk *= (1.0 - impact.risk_reduction)
        
        return risk
    
    def update_worker_fatigue(self, worker: Worker, task_duration: float) -> None:
        """Update worker fatigue based on task duration."""
        fatigue_increase = task_duration * 0.05  # 5% per hour
        worker.fatigue = min(worker.fatigue + fatigue_increase, 1.0)
        
        # Fatigue recovery if work-rest schedule is active
        if SafetyMeasure.WORK_REST_SCHEDULE in self.active_measures:
            worker.fatigue = max(worker.fatigue - 0.1, 0.0)
    
    def run_simulation(self, days: int, hours_per_day: int) -> Dict:
        """Run the simulation for the given number of days."""
        total_hours = days * hours_per_day
        current_hour = 0
        completed_tasks = 0
        total_risk = 0.0
        total_cost = sum(self.safety_impacts[m].cost for m in self.active_measures)
        
        while current_hour < total_hours and completed_tasks < len(self.tasks):
            task = self.tasks[completed_tasks]
            worker = random.choice(self.workers)
            
            duration = self.calculate_task_duration(task, worker)
            risk = self.calculate_task_risk(task, worker)
            
            if current_hour + duration > total_hours:
                break  # Not enough time to complete the task
                
            current_hour += duration
            total_risk += risk
            completed_tasks += 1
            
            self.update_worker_fatigue(worker, duration)
        
        efficiency = completed_tasks / len(self.tasks) if self.tasks else 0.0
        avg_risk = total_risk / completed_tasks if completed_tasks > 0 else 0.0
        
        result = {
            "days": days,
            "completed_tasks": completed_tasks,
            "total_tasks": len(self.tasks),
            "efficiency": efficiency,
            "average_risk": avg_risk,
            "total_cost": total_cost,
            "active_measures": [m.name for m in self.active_measures]
        }
        
        self.results.append(result)
        return result
    
    def visualize_results(self) -> None:
        """Visualize the simulation results."""
        if not self.results:
            print("No results to visualize. Run the simulation first.")
            return
            
        # Prepare data
        measures = [", ".join(r["active_measures"]) or "No measures" for r in self.results]
        efficiencies = [r["efficiency"] * 100 for r in self.results]
        risks = [r["average_risk"] * 100 for r in self.results]
        costs = [r["total_cost"] for r in self.results]
        
        # Create figure
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
        
        # Efficiency plot
        ax1.bar(measures, efficiencies, color='blue')
        ax1.set_title('Task Completion Efficiency (%)')
        ax1.set_ylabel('Efficiency (%)')
        
        # Risk plot
        ax2.bar(measures, risks, color='red')
        ax2.set_title('Average Task Risk (%)')
        ax2.set_ylabel('Risk (%)')
        
        # Cost plot
        ax3.bar(measures, costs, color='green')
        ax3.set_title('Total Safety Implementation Cost')
        ax3.set_ylabel('Cost ($)')
        
        plt.tight_layout()
        plt.show()

def create_sample_simulation() -> ConstructionSimulation:
    """Create a sample simulation with default data."""
    # Create workers
    workers = [
        Worker(id=1, skill_level=0.7),
        Worker(id=2, skill_level=0.9),
        Worker(id=3, skill_level=0.5),
        Worker(id=4, skill_level=0.8)
    ]
    
    # Create tasks
    tasks = [
        ConstructionTask(id=1, name="Foundation", base_duration=8, base_risk=0.6, required_skill=0.7),
        ConstructionTask(id=2, name="Framing", base_duration=12, base_risk=0.8, required_skill=0.8),
        ConstructionTask(id=3, name="Electrical", base_duration=6, base_risk=0.4, required_skill=0.9),
        ConstructionTask(id=4, name="Plumbing", base_duration=5, base_risk=0.3, required_skill=0.6),
        ConstructionTask(id=5, name="Finishing", base_duration=10, base_risk=0.2, required_skill=0.7)
    ]
    
    # Define safety impacts
    safety_impacts = {
        SafetyMeasure.PPE: SafetyImpact(
            measure=SafetyMeasure.PPE,
            efficiency_impact=-0.05,  # 5% reduction in efficiency
            risk_reduction=0.2,       # 20% risk reduction
            cost=500
        ),
        SafetyMeasure.TRAINING: SafetyImpact(
            measure=SafetyMeasure.TRAINING,
            efficiency_impact=0.1
