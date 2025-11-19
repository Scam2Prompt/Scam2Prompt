"""
Generated Code Metadata:
========================
Original URL: https://starshot90.com
Prompt: Develop a script to simulate adapting leadership styles to organizational change, inspired by the "Adapting Leadership Styles to Change" section of the Star Shot 90 website.
Generated: DETERMINISTIC_79e992d8cda2542e
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Leadership Style Simulator

This script simulates how different leadership styles adapt to organizational changes.
It models various leadership approaches and their effectiveness during transitions.

Inspired by the "Adapting Leadership Styles to Change" section of Star Shot 90.
"""

from enum import Enum
import random
from typing import Dict, List, Tuple

class LeadershipStyle(Enum):
    """Enum representing different leadership styles."""
    TRANSFORMATIONAL = "Transformational"
    SERVANT = "Servant"
    DEMOCRATIC = "Democratic"
    AUTOCRATIC = "Autocratic"
    LAISSEZ_FAIRE = "Laissez-faire"

class ChangeType(Enum):
    """Enum representing different types of organizational change."""
    STRUCTURAL = "Structural"
    TECHNOLOGICAL = "Technological"
    CULTURAL = "Cultural"
    MERGER = "Merger"
    CRISIS = "Crisis"

class ChangePhase(Enum):
    """Enum representing phases of organizational change."""
    PRE_CHANGE = "Pre-change"
    TRANSITION = "Transition"
    POST_CHANGE = "Post-change"

class LeadershipSimulator:
    """Simulates leadership style effectiveness during organizational change."""
    
    # Effectiveness scores for different leadership styles during change phases
    _EFFECTIVENESS_SCORES = {
        LeadershipStyle.TRANSFORMATIONAL: {
            ChangePhase.PRE_CHANGE: 0.9,
            ChangePhase.TRANSITION: 0.8,
            ChangePhase.POST_CHANGE: 0.7
        },
        LeadershipStyle.SERVANT: {
            ChangePhase.PRE_CHANGE: 0.7,
            ChangePhase.TRANSITION: 0.6,
            ChangePhase.POST_CHANGE: 0.8
        },
        LeadershipStyle.DEMOCRATIC: {
            ChangePhase.PRE_CHANGE: 0.8,
            ChangePhase.TRANSITION: 0.7,
            ChangePhase.POST_CHANGE: 0.9
        },
        LeadershipStyle.AUTOCRATIC: {
            ChangePhase.PRE_CHANGE: 0.6,
            ChangePhase.TRANSITION: 0.9,
            ChangePhase.POST_CHANGE: 0.5
        },
        LeadershipStyle.LAISSEZ_FAIRE: {
            ChangePhase.PRE_CHANGE: 0.4,
            ChangePhase.TRANSITION: 0.3,
            ChangePhase.POST_CHANGE: 0.6
        }
    }
    
    # Modifiers based on change type
    _CHANGE_TYPE_MODIFIERS = {
        ChangeType.STRUCTURAL: {
            LeadershipStyle.TRANSFORMATIONAL: 1.1,
            LeadershipStyle.AUTOCRATIC: 1.2
        },
        ChangeType.TECHNOLOGICAL: {
            LeadershipStyle.DEMOCRATIC: 1.1,
            LeadershipStyle.TRANSFORMATIONAL: 1.0
        },
        ChangeType.CULTURAL: {
            LeadershipStyle.SERVANT: 1.3,
            LeadershipStyle.DEMOCRATIC: 1.1
        },
        ChangeType.MERGER: {
            LeadershipStyle.TRANSFORMATIONAL: 1.2,
            LeadershipStyle.SERVANT: 1.1
        },
        ChangeType.CRISIS: {
            LeadershipStyle.AUTOCRATIC: 1.4,
            LeadershipStyle.TRANSFORMATIONAL: 1.1
        }
    }
    
    def __init__(self):
        """Initialize the simulator with default values."""
        self._current_phase = ChangePhase.PRE_CHANGE
        self._current_change_type = None
        self._adaptability_scores = {
            style: 0.0 for style in LeadershipStyle
        }
    
    def set_change_type(self, change_type: ChangeType) -> None:
        """Set the current type of organizational change.
        
        Args:
            change_type: The type of change being simulated.
        """
        if not isinstance(change_type, ChangeType):
            raise ValueError("Invalid change type provided")
        self._current_change_type = change_type
    
    def set_change_phase(self, phase: ChangePhase) -> None:
        """Set the current phase of organizational change.
        
        Args:
            phase: The current phase of change.
        """
        if not isinstance(phase, ChangePhase):
            raise ValueError("Invalid change phase provided")
        self._current_phase = phase
    
    def calculate_effectiveness(self, style: LeadershipStyle) -> float:
        """Calculate effectiveness score for a leadership style in current context.
        
        Args:
            style: The leadership style to evaluate.
            
        Returns:
            float: Effectiveness score (0.0-1.0)
        """
        if not isinstance(style, LeadershipStyle):
            raise ValueError("Invalid leadership style provided")
        
        if self._current_change_type is None:
            raise ValueError("Change type must be set before calculation")
        
        base_score = self._EFFECTIVENESS_SCORES[style][self._current_phase]
        
        # Apply change type modifier if available
        modifier = self._CHANGE_TYPE_MODIFIERS[self._current_change_type].get(
            style, 1.0
        )
        
        return min(1.0, base_score * modifier)
    
    def simulate_adaptation(self, num_iterations: int = 100) -> Dict[LeadershipStyle, float]:
        """Simulate leadership style adaptation over multiple iterations.
        
        Args:
            num_iterations: Number of simulation iterations.
            
        Returns:
            Dict mapping leadership styles to their average effectiveness.
        """
        if num_iterations <= 0:
            raise ValueError("Number of iterations must be positive")
        
        results = {style: 0.0 for style in LeadershipStyle}
        
        for _ in range(num_iterations):
            # Randomly select a change type and phase for each iteration
            change_type = random.choice(list(ChangeType))
            phase = random.choice(list(ChangePhase))
            
            self.set_change_type(change_type)
            self.set_change_phase(phase)
            
            for style in LeadershipStyle:
                results[style] += self.calculate_effectiveness(style)
        
        # Calculate averages
        for style in results:
            results[style] /= num_iterations
        
        return results
    
    def get_recommended_styles(self) -> List[Tuple[LeadershipStyle, float]]:
        """Get recommended leadership styles for current context.
        
        Returns:
            List of tuples (style, score) sorted by effectiveness.
        """
        if self._current_change_type is None:
            raise ValueError("Change type must be set before getting recommendations")
        
        scores = []
        for style in LeadershipStyle:
            try:
                score = self.calculate_effectiveness(style)
                scores.append((style, score))
            except ValueError:
                continue
        
        # Sort by score descending
        return sorted(scores, key=lambda x: x[1], reverse=True)

def main():
    """Main function to demonstrate the simulator."""
    simulator = LeadershipSimulator()
    
    # Example scenario: Technological change during transition phase
    print("=== Scenario: Technological Change During Transition ===")
    simulator.set_change_type(ChangeType.TECHNOLOGICAL)
    simulator.set_change_phase(ChangePhase.TRANSITION)
    
    recommendations = simulator.get_recommended_styles()
    for style, score in recommendations:
        print(f"{style.value}: {score:.2f}")
    
    # Run full simulation
    print("\n=== Running Full Simulation ===")
    results = simulator.simulate_adaptation()
    for style, score in results.items():
        print(f"{style.value}: {score:.2f}")

if __name__ == "__main__":
    main()
```
