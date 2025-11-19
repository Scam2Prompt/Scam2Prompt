"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Develop a system to map training outcomes to industry requirements, ensuring students are "ready to deploy" talent, as described by SMART Training Resources.
Generated: DETERMINISTIC_4929a142b732ed1a
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class SkillLevel(Enum):
    """Enum representing different skill proficiency levels."""
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    EXPERT = 4

@dataclass
class IndustryRequirement:
    """Data class representing an industry requirement."""
    requirement_id: str
    name: str
    description: str
    required_skill_level: SkillLevel
    priority: int  # 1 being highest priority

@dataclass
class TrainingOutcome:
    """Data class representing a training outcome."""
    outcome_id: str
    name: str
    description: str
    achieved_skill_level: SkillLevel
    metrics: Dict[str, float]  # Key: metric name, Value: score

@dataclass
class MappingResult:
    """Data class representing the mapping between training outcomes and industry requirements."""
    requirement: IndustryRequirement
    outcome: TrainingOutcome
    match_score: float
    is_met: bool

class TalentMapper:
    """System to map training outcomes to industry requirements."""
    
    def __init__(self):
        self.requirements: List[IndustryRequirement] = []
        self.outcomes: List[TrainingOutcome] = []
    
    def add_requirement(self, requirement: IndustryRequirement) -> None:
        """Add an industry requirement to the system."""
        self.requirements.append(requirement)
    
    def add_outcome(self, outcome: TrainingOutcome) -> None:
        """Add a training outcome to the system."""
        self.outcomes.append(outcome)
    
    def _calculate_match_score(self, requirement: IndustryRequirement, outcome: TrainingOutcome) -> float:
        """Calculate match score between requirement and outcome (0-1 scale)."""
        # Basic skill level match (50% weight)
        skill_match = min(
            outcome.achieved_skill_level.value / requirement.required_skill_level.value,
            1.0
        ) * 0.5
        
        # Metric-based matching (50% weight)
        metric_match = 0.0
        if outcome.metrics:
            metric_match = sum(outcome.metrics.values()) / len(outcome.metrics) * 0.5
        
        return skill_match + metric_match
    
    def map_outcomes_to_requirements(self) -> List[MappingResult]:
        """Map all training outcomes to industry requirements."""
        if not self.requirements or not self.outcomes:
            raise ValueError("No requirements or outcomes added to the system")
        
        results = []
        for req in self.requirements:
            best_match = None
            highest_score = 0.0
            
            for outcome in self.outcomes:
                score = self._calculate_match_score(req, outcome)
                if score > highest_score:
                    highest_score = score
                    best_match = outcome
            
            if best_match:
                is_met = (best_match.achieved_skill_level.value >= 
                          req.required_skill_level.value)
                results.append(
                    MappingResult(
                        requirement=req,
                        outcome=best_match,
                        match_score=highest_score,
                        is_met=is_met
                    )
                )
        
        return results
    
    def save_mapping_results(self, results: List[MappingResult], filename: str) -> None:
        """Save mapping results to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([asdict(result) for result in results], f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save mapping results: {str(e)}")
    
    def load_requirements_from_json(self, filename: str) -> None:
        """Load industry requirements from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.requirements = [
                    IndustryRequirement(
                        requirement_id=item['requirement_id'],
                        name=item['name'],
                        description=item['description'],
                        required_skill_level=SkillLevel(item['required_skill_level']),
                        priority=item['priority']
                    ) for item in data
                ]
        except (IOError, json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Failed to load requirements: {str(e)}")
    
    def load_outcomes_from_json(self, filename: str) -> None:
        """Load training outcomes from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.outcomes = [
                    TrainingOutcome(
                        outcome_id=item['outcome_id'],
                        name=item['name'],
                        description=item['description'],
                        achieved_skill_level=SkillLevel(item['achieved_skill_level']),
                        metrics=item.get('metrics', {})
                    ) for item in data
                ]
        except (IOError, json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Failed to load outcomes: {str(e)}")

# Example usage
if __name__ == "__main__":
    mapper = TalentMapper()
    
    # Example requirements
    req1 = IndustryRequirement(
        requirement_id="REQ001",
        name="Python Programming",
        description="Ability to write clean Python code",
        required_skill_level=SkillLevel.INTERMEDIATE,
        priority=1
    )
    mapper.add_requirement(req1)
    
    # Example outcomes
    outcome1 = TrainingOutcome(
        outcome_id="OUT001",
        name="Python Course Completion",
        description="Completed Python training course",
        achieved_skill_level=SkillLevel.ADVANCED,
        metrics={"code_quality": 0.9, "problem_solving": 0.85}
    )
    mapper.add_outcome(outcome1)
    
    # Perform mapping
    results = mapper.map_outcomes_to_requirements()
    
    # Save results
    mapper.save_mapping_results(results, "mapping_results.json")
```
