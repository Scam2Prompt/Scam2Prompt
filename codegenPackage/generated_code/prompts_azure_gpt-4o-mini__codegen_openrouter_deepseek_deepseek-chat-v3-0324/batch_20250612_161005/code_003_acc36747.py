"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Explain how to measure the success of a grants program using key results and indicators as described in the Grants Program Canvas.
Generated: DETERMINISTIC_acc367479b5e65b6
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, field
from enum import Enum

class IndicatorType(Enum):
    """Enum representing different types of indicators."""
    QUANTITATIVE = "quantitative"
    QUALITATIVE = "qualitative"

@dataclass
class KeyResult:
    """Represents a key result in the Grants Program Canvas."""
    name: str
    description: str
    target_value: Union[int, float, str]
    current_value: Union[int, float, str] = 0
    indicator_type: IndicatorType = IndicatorType.QUANTITATIVE
    weight: float = 1.0  # Used for weighted scoring

    def progress(self) -> float:
        """Calculate progress towards the target as a percentage."""
        if isinstance(self.target_value, (int, float)) and isinstance(self.current_value, (int, float)):
            if self.target_value == 0:
                return 0.0
            return (self.current_value / self.target_value) * 100
        return 0.0  # Default for qualitative or non-numeric comparisons

@dataclass
class Objective:
    """Represents an objective with multiple key results."""
    name: str
    description: str
    key_results: List[KeyResult] = field(default_factory=list)

    def overall_progress(self) -> float:
        """Calculate weighted average progress across all key results."""
        if not self.key_results:
            return 0.0
        
        total_weight = sum(kr.weight for kr in self.key_results)
        if total_weight == 0:
            return 0.0
            
        weighted_sum = sum(kr.progress() * kr.weight for kr in self.key_results)
        return weighted_sum / total_weight

@dataclass
class GrantsProgram:
    """Represents a grants program with objectives and key results."""
    name: str
    objectives: List[Objective] = field(default_factory=list)

    def add_objective(self, objective: Objective) -> None:
        """Add an objective to the program."""
        self.objectives.append(objective)

    def program_success_score(self) -> float:
        """Calculate overall program success score as average of objective progress."""
        if not self.objectives:
            return 0.0
        return sum(obj.overall_progress() for obj in self.objectives) / len(self.objectives)

    def to_json(self) -> str:
        """Serialize the GrantsProgram to JSON."""
        return json.dumps({
            "name": self.name,
            "objectives": [
                {
                    "name": obj.name,
                    "description": obj.description,
                    "key_results": [
                        {
                            "name": kr.name,
                            "description": kr.description,
                            "target_value": kr.target_value,
                            "current_value": kr.current_value,
                            "indicator_type": kr.indicator_type.value,
                            "weight": kr.weight
                        }
                        for kr in obj.key_results
                    ]
                }
                for obj in self.objectives
            ]
        }, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'GrantsProgram':
        """Deserialize a GrantsProgram from JSON."""
        data = json.loads(json_str)
        program = cls(name=data["name"])
        
        for obj_data in data["objectives"]:
            objective = Objective(
                name=obj_data["name"],
                description=obj_data["description"]
            )
            
            for kr_data in obj_data["key_results"]:
                key_result = KeyResult(
                    name=kr_data["name"],
                    description=kr_data["description"],
                    target_value=kr_data["target_value"],
                    current_value=kr_data["current_value"],
                    indicator_type=IndicatorType(kr_data["indicator_type"]),
                    weight=kr_data["weight"]
                )
                objective.key_results.append(key_result)
            
            program.add_objective(objective)
        
        return program

# Example usage
if __name__ == "__main__":
    # Create a grants program
    program = GrantsProgram(name="Community Development Grants")

    # Add objectives and key results
    objective1 = Objective(
        name="Increase Community Engagement",
        description="Engage more community members in grant-funded projects"
    )
    objective1.key_results.extend([
        KeyResult(
            name="Number of participants",
            description="Total number of community members participating",
            target_value=500,
            current_value=320,
            indicator_type=IndicatorType.QUANTITATIVE,
            weight=0.6
        ),
        KeyResult(
            name="Participant satisfaction",
            description="Average satisfaction score from surveys (1-5 scale)",
            target_value=4.5,
            current_value=4.2,
            indicator_type=IndicatorType.QUANTITATIVE,
            weight=0.4
        )
    ])

    objective2 = Objective(
        name="Project Completion Rate",
        description="Ensure projects are completed successfully"
    )
    objective2.key_results.append(
        KeyResult(
            name="Completion percentage",
            description="Percentage of projects completed on time and within budget",
            target_value=90,  # 90%
            current_value=75,
            indicator_type=IndicatorType.QUANTITATIVE,
            weight=1.0
        )
    )

    program.add_objective(objective1)
    program.add_objective(objective2)

    # Calculate and display metrics
    print(f"Program: {program.name}")
    print(f"Overall Success Score: {program.program_success_score():.1f}%")
    
    for obj in program.objectives:
        print(f"\nObjective: {obj.name} - {obj.overall_progress():.1f}%")
        for kr in obj.key_results:
            print(f"  - {kr.name}: {kr.current_value}/{kr.target_value} ({kr.progress():.1f}%)")

    # Serialize to JSON
    json_data = program.to_json()
    print("\nJSON Representation:")
    print(json_data)

    # Deserialize from JSON
    loaded_program = GrantsProgram.from_json(json_data)
    assert loaded_program.name == program.name
```
