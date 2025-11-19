"""
Generated Code Metadata:
========================
Original URL: https://foundationlabs.tech
Prompt: Write a program that models the transformational impact of computational knowledge on real-world systems, inspired by Foundation Labs' focus on shaping civilization's arc.
Generated: DETERMINISTIC_9b82f3bdd3d36779
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A simulation modeling the transformational impact of computational knowledge on real-world systems.
Inspired by Foundation Labs' focus on shaping civilization's arc.

This program models how computational knowledge propagates through and transforms various societal systems.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
from dataclasses import dataclass
import random
from enum import Enum, auto


class SystemType(Enum):
    """Types of societal systems that can be transformed."""
    ECONOMIC = auto()
    POLITICAL = auto()
    TECHNOLOGICAL = auto()
    CULTURAL = auto()
    ENVIRONMENTAL = auto()


@dataclass
class SystemState:
    """Represents the state of a societal system at a point in time."""
    stability: float  # 0.0 to 1.0
    complexity: float  # 0.0 to 1.0
    adaptability: float  # 0.0 to 1.0
    knowledge_integration: float  # 0.0 to 1.0


class SocietalSystem:
    """Models a societal system and its transformation through computational knowledge."""
    
    def __init__(self, system_type: SystemType, initial_state: SystemState):
        self.system_type = system_type
        self.state = initial_state
        self.history: List[SystemState] = [initial_state]
        
    def apply_knowledge_impact(self, knowledge_input: float) -> None:
        """
        Apply computational knowledge impact to the system.
        
        Args:
            knowledge_input: Amount of computational knowledge applied (0.0 to 1.0)
        """
        try:
            if not 0 <= knowledge_input <= 1:
                raise ValueError("Knowledge input must be between 0 and 1")
                
            # Calculate transformations
            new_stability = min(1.0, self.state.stability * (1 + 0.2 * knowledge_input))
            new_complexity = min(1.0, self.state.complexity * (1 + 0.3 * knowledge_input))
            new_adaptability = min(1.0, self.state.adaptability * (1 + 0.4 * knowledge_input))
            new_knowledge = min(1.0, self.state.knowledge_integration + knowledge_input * 0.5)
            
            # Create new state
            new_state = SystemState(
                stability=new_stability,
                complexity=new_complexity,
                adaptability=new_adaptability,
                knowledge_integration=new_knowledge
            )
            
            self.state = new_state
            self.history.append(new_state)
            
        except Exception as e:
            print(f"Error applying knowledge impact: {e}")
            raise

    def get_current_metrics(self) -> Dict[str, float]:
        """Return current system metrics as a dictionary."""
        return {
            'stability': self.state.stability,
            'complexity': self.state.complexity,
            'adaptability': self.state.adaptability,
            'knowledge_integration': self.state.knowledge_integration
        }


class CivilizationModel:
    """Models the civilization with multiple interacting systems."""
    
    def __init__(self):
        self.systems: Dict[SystemType, SocietalSystem] = {}
        self.time_step = 0
        
        # Initialize all system types with random initial states
        for system_type in SystemType:
            initial_state = SystemState(
                stability=random.uniform(0.3, 0.7),
                complexity=random.uniform(0.2, 0.6),
                adaptability=random.uniform(0.4, 0.8),
                knowledge_integration=0.0
            )
            self.systems[system_type] = SocietalSystem(system_type, initial_state)
    
    def advance_time_step(self, knowledge_distribution: Dict[SystemType, float]) -> None:
        """
        Advance the simulation by one time step, applying knowledge to systems.
        
        Args:
            knowledge_distribution: Dictionary mapping system types to knowledge input (0.0 to 1.0)
        """
        try:
            self.time_step += 1
            
            # Apply knowledge to each system
            for system_type, knowledge_input in knowledge_distribution.items():
                if system_type in self.systems:
                    self.systems[system_type].apply_knowledge_impact(knowledge_input)
                
            # Simulate cross-system interactions
            self._simulate_system_interactions()
            
        except Exception as e:
            print(f"Error advancing time step: {e}")
            raise
    
    def _simulate_system_interactions(self) -> None:
        """Simulate interactions between different societal systems."""
        # Economic system affects all others
        economic_impact = self.systems[SystemType.ECONOMIC].state.knowledge_integration * 0.1
        
        for system in self.systems.values():
            if system.system_type != SystemType.ECONOMIC:
                system.state.adaptability = min(1.0, system.state.adaptability + economic_impact)
    
    def get_system_metrics(self) -> Dict[SystemType, Dict[str, float]]:
        """Get current metrics for all systems."""
        return {system_type: system.get_current_metrics() 
                for system_type, system in self.systems.items()}
    
    def visualize_history(self, metric: str = 'knowledge_integration') -> None:
        """
        Visualize the historical progression of a metric across all systems.
        
        Args:
            metric: Which metric to visualize (stability, complexity, adaptability, knowledge_integration)
        """
        try:
            plt.figure(figsize=(10, 6))
            
            for system_type, system in self.systems.items():
                history = system.history
                values = [getattr(state, metric) for state in history]
                plt.plot(range(len(values)), values, label=system_type.name)
            
            plt.title(f"Evolution of {metric.replace('_', ' ').title()} Over Time")
            plt.xlabel("Time Step")
            plt.ylabel(metric.replace('_', ' ').title())
            plt.legend()
            plt.grid(True)
            plt.show()
            
        except Exception as e:
            print(f"Error visualizing history: {e}")
            raise


def run_simulation(time_steps: int = 20) -> None:
    """
    Run a complete simulation of knowledge impact on civilization.
    
    Args:
        time_steps: Number of time steps to simulate
    """
    try:
        model = CivilizationModel()
        
        for _ in range(time_steps):
            # Distribute knowledge randomly across systems
            knowledge_distribution = {
                system_type: random.uniform(0.1, 0.8) 
                for system_type in SystemType
            }
            model.advance_time_step(knowledge_distribution)
        
        # Print final metrics
        print("\nFinal System Metrics:")
        for system_type, metrics in model.get_system_metrics().items():
            print(f"\n{system_type.name}:")
            for metric, value in metrics.items():
                print(f"  {metric.replace('_', ' ').title()}: {value:.2f}")
        
        # Visualize knowledge integration progression
        model.visualize_history()
        
    except Exception as e:
        print(f"Error running simulation: {e}")
        raise


if __name__ == "__main__":
    run_simulation()
```
