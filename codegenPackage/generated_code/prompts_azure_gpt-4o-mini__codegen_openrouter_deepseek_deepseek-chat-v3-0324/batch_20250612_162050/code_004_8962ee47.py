"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Write a program that models the effects of automation on creative processes, based on the ideas presented in "KI, Gewalt und Krieg."
Generated: DETERMINISTIC_8962ee4773ec40ef
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A program to model the effects of automation on creative processes, inspired by the ideas in "KI, Gewalt und Krieg."

This simulation explores how automation influences creativity, productivity, and originality in creative workflows.
"""

import random
from typing import List, Dict, Tuple
from enum import Enum, auto
import matplotlib.pyplot as plt
import numpy as np


class CreativeProcess(Enum):
    """Enum representing different stages of a creative process."""
    IDEA_GENERATION = auto()
    DEVELOPMENT = auto()
    REFINEMENT = auto()
    FINALIZATION = auto()


class AutomationLevel(Enum):
    """Enum representing different levels of automation."""
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    FULL = 4


class CreativeAgent:
    """Represents a creative agent (human or automated system)."""
    
    def __init__(self, is_automated: bool, creativity_factor: float):
        """
        Initialize a creative agent.
        
        Args:
            is_automated: Whether the agent is automated (True) or human (False)
            creativity_factor: A measure of the agent's creativity (0.0 to 1.0)
        """
        self.is_automated = is_automated
        self.creativity_factor = creativity_factor
        self.originality = random.uniform(0.5, 1.0) if not is_automated else random.uniform(0.1, 0.7)
        self.efficiency = random.uniform(0.7, 1.0) if is_automated else random.uniform(0.3, 0.8)
    
    def contribute(self, process: CreativeProcess) -> float:
        """
        Simulate contribution to a creative process stage.
        
        Args:
            process: The creative process stage
            
        Returns:
            A score representing the quality of contribution
        """
        if process == CreativeProcess.IDEA_GENERATION:
            return self.originality * self.creativity_factor
        elif process == CreativeProcess.DEVELOPMENT:
            return (self.originality * 0.3 + self.efficiency * 0.7) * self.creativity_factor
        else:
            return self.efficiency * self.creativity_factor


class CreativeWorkflow:
    """Models a creative workflow with different automation levels."""
    
    def __init__(self, team: List[CreativeAgent]):
        """Initialize with a team of creative agents."""
        self.team = team
        self.automation_level = self._calculate_automation_level()
    
    def _calculate_automation_level(self) -> AutomationLevel:
        """Calculate the overall automation level of the team."""
        automated_count = sum(1 for agent in self.team if agent.is_automated)
        ratio = automated_count / len(self.team)
        
        if ratio == 0:
            return AutomationLevel.NONE
        elif ratio < 0.25:
            return AutomationLevel.LOW
        elif ratio < 0.5:
            return AutomationLevel.MEDIUM
        elif ratio < 0.75:
            return AutomationLevel.HIGH
        else:
            return AutomationLevel.FULL
    
    def execute_process(self) -> Dict[CreativeProcess, float]:
        """
        Execute the creative process and return scores for each stage.
        
        Returns:
            Dictionary mapping process stages to quality scores
        """
        results = {}
        for process in CreativeProcess:
            contributions = [agent.contribute(process) for agent in self.team]
            results[process] = sum(contributions) / len(contributions)
        return results
    
    def evaluate_impact(self) -> Tuple[float, float, float]:
        """
        Evaluate the overall impact of automation on the creative process.
        
        Returns:
            Tuple of (originality_score, efficiency_score, overall_quality)
        """
        process_results = self.execute_process()
        originality = process_results[CreativeProcess.IDEA_GENERATION]
        efficiency = sum(process_results.values()) / len(process_results)
        overall = (originality * 0.4) + (efficiency * 0.6)
        return originality, efficiency, overall


def simulate_automation_impact(
    num_simulations: int = 100,
    team_size: int = 10,
    automation_ratios: List[float] = None
) -> Dict[AutomationLevel, Tuple[float, float, float]]:
    """
    Run multiple simulations to model automation's impact on creative processes.
    
    Args:
        num_simulations: Number of simulations per automation level
        team_size: Size of creative teams to simulate
        automation_ratios: List of automation ratios to test
        
    Returns:
        Dictionary mapping automation levels to average results
    """
    if automation_ratios is None:
        automation_ratios = [0, 0.25, 0.5, 0.75, 1.0]
    
    results = {level: [] for level in AutomationLevel}
    
    for ratio in automation_ratios:
        for _ in range(num_simulations):
            team = []
            automated_count = int(team_size * ratio)
            
            # Create automated agents
            for _ in range(automated_count):
                team.append(CreativeAgent(is_automated=True, creativity_factor=random.uniform(0.5, 0.9)))
            
            # Create human agents
            for _ in range(team_size - automated_count):
                team.append(CreativeAgent(is_automated=False, creativity_factor=random.uniform(0.7, 1.0)))
            
            workflow = CreativeWorkflow(team)
            originality, efficiency, overall = workflow.evaluate_impact()
            results[workflow.automation_level].append((originality, efficiency, overall))
    
    # Calculate averages
    averages = {}
    for level, values in results.items():
        if values:
            avg_originality = sum(v[0] for v in values) / len(values)
            avg_efficiency = sum(v[1] for v in values) / len(values)
            avg_overall = sum(v[2] for v in values) / len(values)
            averages[level] = (avg_originality, avg_efficiency, avg_overall)
    
    return averages


def plot_results(results: Dict[AutomationLevel, Tuple[float, float, float]]) -> None:
    """Visualize the simulation results."""
    levels = [level.name for level in results.keys()]
    originality = [values[0] for values in results.values()]
    efficiency = [values[1] for values in results.values()]
    overall = [values[2] for values in results.values()]
    
    x = np.arange(len(levels))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width, originality, width, label='Originality')
    rects2 = ax.bar(x, efficiency, width, label='Efficiency')
    rects3 = ax.bar(x + width, overall, width, label='Overall Quality')
    
    ax.set_ylabel('Scores')
    ax.set_title('Impact of Automation on Creative Processes')
    ax.set_xticks(x)
    ax.set_xticklabels(levels)
    ax.legend()
    
    fig.tight_layout()
    plt.show()


def main():
    """Run the simulation and display results."""
    print("Simulating the impact of automation on creative processes...")
    results = simulate_automation_impact()
    
    print("\nResults:")
    for level, (originality, efficiency, overall) in results.items():
        print(f"{level.name}:")
        print(f"  Originality: {originality:.2f}")
        print(f"  Efficiency: {efficiency:.2f}")
        print(f"  Overall Quality: {overall:.2f}")
        print()
    
    plot_results(results)


if __name__ == "__main__":
    main()
```
