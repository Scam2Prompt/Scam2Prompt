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
from typing import List, Dict, Any

class TrainingOutcome:
    """
    A class to represent a training outcome.
    """
    def __init__(self, outcome_id: str, description: str, skills: List[str]):
        self.outcome_id = outcome_id
        self.description = description
        self.skills = skills

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the TrainingOutcome instance to a dictionary.
        """
        return {
            "outcome_id": self.outcome_id,
            "description": self.description,
            "skills": self.skills
        }

class IndustryRequirement:
    """
    A class to represent an industry requirement.
    """
    def __init__(self, requirement_id: str, description: str, required_skills: List[str]):
        self.requirement_id = requirement_id
        self.description = description
        self.required_skills = required_skills

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the IndustryRequirement instance to a dictionary.
        """
        return {
            "requirement_id": self.requirement_id,
            "description": self.description,
            "required_skills": self.required_skills
        }

class TrainingMappingSystem:
    """
    A class to map training outcomes to industry requirements.
    """
    def __init__(self):
        self.training_outcomes: List[TrainingOutcome] = []
        self.industry_requirements: List[IndustryRequirement] = []

    def add_training_outcome(self, outcome: TrainingOutcome):
        """
        Add a training outcome to the system.
        """
        self.training_outcomes.append(outcome)

    def add_industry_requirement(self, requirement: IndustryRequirement):
        """
        Add an industry requirement to the system.
        """
        self.industry_requirements.append(requirement)

    def map_outcomes_to_requirements(self) -> Dict[str, List[str]]:
        """
        Map training outcomes to industry requirements based on skills.
        Returns a dictionary where keys are outcome IDs and values are lists of matching requirement IDs.
        """
        mapping = {}
        for outcome in self.training_outcomes:
            mapping[outcome.outcome_id] = []
            for requirement in self.industry_requirements:
                if set(outcome.skills).intersection(set(requirement.required_skills)):
                    mapping[outcome.outcome_id].append(requirement.requirement_id)
        return mapping

    def save_to_file(self, filename: str):
        """
        Save the training outcomes and industry requirements to a JSON file.
        """
        try:
            data = {
                "training_outcomes": [outcome.to_dict() for outcome in self.training_outcomes],
                "industry_requirements": [requirement.to_dict() for requirement in self.industry_requirements]
            }
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str):
        """
        Load training outcomes and industry requirements from a JSON file.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.training_outcomes = [TrainingOutcome(**outcome) for outcome in data.get("training_outcomes", [])]
                self.industry_requirements = [IndustryRequirement(**requirement) for requirement in data.get("industry_requirements", [])]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    system = TrainingMappingSystem()

    # Adding training outcomes
    system.add_training_outcome(TrainingOutcome("TO1", "Web Development", ["HTML", "CSS", "JavaScript"]))
    system.add_training_outcome(TrainingOutcome("TO2", "Data Science", ["Python", "Machine Learning", "Statistics"]))

    # Adding industry requirements
    system.add_industry_requirement(IndustryRequirement("IR1", "Frontend Developer", ["HTML", "CSS", "JavaScript"]))
    system.add_industry_requirement(IndustryRequirement("IR2", "Data Analyst", ["Python", "Statistics"]))

    # Mapping outcomes to requirements
    mapping = system.map_outcomes_to_requirements()
    print("Mapping of training outcomes to industry requirements:")
    print(mapping)

    # Save to file
    system.save_to_file("training_mapping.json")

    # Load from file
    new_system = TrainingMappingSystem()
    new_system.load_from_file("training_mapping.json")
    print("Loaded training outcomes and requirements:")
    print(new_system.map_outcomes_to_requirements())
```
