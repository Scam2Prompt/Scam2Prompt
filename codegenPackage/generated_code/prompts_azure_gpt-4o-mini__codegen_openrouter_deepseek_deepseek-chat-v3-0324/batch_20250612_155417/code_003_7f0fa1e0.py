"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Create a function that evaluates the sustainability initiatives of universities, based on the insights from the UEH special issue.
Generated: DETERMINISTIC_7f0fa1e01480d7f7
Batch ID: 20250612_155417
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
from enum import Enum

class SustainabilityCategory(Enum):
    """Enum representing different sustainability categories."""
    ENERGY = "Energy Efficiency"
    WASTE = "Waste Management"
    WATER = "Water Conservation"
    TRANSPORT = "Sustainable Transport"
    EDUCATION = "Sustainability Education"
    RESEARCH = "Sustainability Research"
    COMMUNITY = "Community Engagement"

class UniversitySustainabilityScore:
    """Class to represent a university's sustainability score."""
    
    def __init__(self, university_name: str):
        self.university_name = university_name
        self.scores: Dict[SustainabilityCategory, float] = {
            category: 0.0 for category in SustainabilityCategory
        }
        self.overall_score: float = 0.0
    
    def add_score(self, category: SustainabilityCategory, score: float) -> None:
        """Add a score for a specific sustainability category."""
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")
        self.scores[category] = score
        self._calculate_overall_score()
    
    def _calculate_overall_score(self) -> None:
        """Calculate the overall sustainability score."""
        total = sum(self.scores.values())
        self.overall_score = total / len(self.scores)
    
    def to_dict(self) -> Dict[str, Union[str, float, Dict[str, float]]]:
        """Convert the score data to a dictionary."""
        return {
            "university_name": self.university_name,
            "scores": {category.value: score for category, score in self.scores.items()},
            "overall_score": self.overall_score
        }

class SustainabilityEvaluator:
    """Evaluates sustainability initiatives of universities."""
    
    def __init__(self):
        self.universities: Dict[str, UniversitySustainabilityScore] = {}
    
    def add_university(self, university_name: str) -> None:
        """Add a university to the evaluator."""
        if university_name in self.universities:
            raise ValueError(f"University '{university_name}' already exists")
        self.universities[university_name] = UniversitySustainabilityScore(university_name)
    
    def add_score(
        self,
        university_name: str,
        category: SustainabilityCategory,
        score: float
    ) -> None:
        """Add a sustainability score for a specific university and category."""
        if university_name not in self.universities:
            raise ValueError(f"University '{university_name}' not found")
        self.universities[university_name].add_score(category, score)
    
    def get_overall_scores(self) -> List[Dict[str, Union[str, float]]]:
        """Get overall sustainability scores for all universities."""
        return [
            {
                "university_name": uni.university_name,
                "overall_score": uni.overall_score
            }
            for uni in self.universities.values()
        ]
    
    def get_detailed_scores(self, university_name: str) -> Optional[Dict[str, Union[str, float, Dict[str, float]]]]:
        """Get detailed sustainability scores for a specific university."""
        if university_name not in self.universities:
            return None
        return self.universities[university_name].to_dict()
    
    def export_to_json(self, file_path: str) -> None:
        """Export all university sustainability data to a JSON file."""
        data = {
            "universities": [uni.to_dict() for uni in self.universities.values()]
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    
    @classmethod
    def import_from_json(cls, file_path: str) -> 'SustainabilityEvaluator':
        """Import university sustainability data from a JSON file."""
        evaluator = cls()
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        for uni_data in data["universities"]:
            university_name = uni_data["university_name"]
            evaluator.add_university(university_name)
            
            for category_str, score in uni_data["scores"].items():
                category = None
                for cat in SustainabilityCategory:
                    if cat.value == category_str:
                        category = cat
                        break
                if category is None:
                    continue
                evaluator.add_score(university_name, category, score)
        
        return evaluator

# Example usage
if __name__ == "__main__":
    evaluator = SustainabilityEvaluator()
    
    # Add universities and their scores
    evaluator.add_university("Green University")
    evaluator.add_score("Green University", SustainabilityCategory.ENERGY, 85.5)
    evaluator.add_score("Green University", SustainabilityCategory.WASTE, 92.0)
    evaluator.add_score("Green University", SustainabilityCategory.WATER, 78.5)
    
    evaluator.add_university("Eco College")
    evaluator.add_score("Eco College", SustainabilityCategory.ENERGY, 90.0)
    evaluator.add_score("Eco College", SustainabilityCategory.TRANSPORT, 88.0)
    
    # Export data
    evaluator.export_to_json("university_sustainability.json")
    
    # Import data
    imported_evaluator = SustainabilityEvaluator.import_from_json("university_sustainability.json")
    
    # Print results
    print("Overall Scores:")
    for score in imported_evaluator.get_overall_scores():
        print(f"{score['university_name']}: {score['overall_score']:.2f}")
    
    print("\nDetailed Scores for Green University:")
    print(imported_evaluator.get_detailed_scores("Green University"))
```
