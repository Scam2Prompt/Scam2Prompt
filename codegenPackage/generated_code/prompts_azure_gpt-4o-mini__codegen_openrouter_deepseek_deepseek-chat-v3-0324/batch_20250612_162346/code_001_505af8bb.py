"""
Generated Code Metadata:
========================
Original URL: https://ng-mc.de
Prompt: Write a Python function that analyzes past management successes and failures to provide strategic recommendations, inspired by the principles outlined on ng-mc.de.
Generated: DETERMINISTIC_505af8bb5d6463fd
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from enum import Enum
import datetime

class OutcomeType(Enum):
    SUCCESS = "success"
    FAILURE = "failure"

class ManagementCase:
    """
    Represents a management case with its attributes and outcomes.
    """
    def __init__(
        self,
        title: str,
        description: str,
        outcome: OutcomeType,
        date: datetime.date,
        key_factors: List[str],
        lessons_learned: str
    ):
        self.title = title
        self.description = description
        self.outcome = outcome
        self.date = date
        self.key_factors = key_factors
        self.lessons_learned = lessons_learned

class ManagementAnalyzer:
    """
    Analyzes past management cases to provide strategic recommendations.
    """
    def __init__(self, cases: List[ManagementCase]):
        self.cases = cases

    def _filter_cases_by_outcome(self, outcome: OutcomeType) -> List[ManagementCase]:
        """Filter cases by their outcome type."""
        return [case for case in self.cases if case.outcome == outcome]

    def _get_common_factors(self, cases: List[ManagementCase]) -> Dict[str, int]:
        """Identify common factors among cases."""
        factor_counts = {}
        for case in cases:
            for factor in case.key_factors:
                factor_counts[factor] = factor_counts.get(factor, 0) + 1
        return factor_counts

    def _generate_recommendations(self, success_factors: Dict[str, int], failure_factors: Dict[str, int]) -> List[str]:
        """Generate strategic recommendations based on success and failure factors."""
        recommendations = []
        
        # Recommend leveraging top success factors
        top_success = sorted(success_factors.items(), key=lambda x: x[1], reverse=True)[:3]
        if top_success:
            recommendations.append(
                "Focus on these key success factors: " + 
                ", ".join([f"{factor} (appeared {count} times)" for factor, count in top_success])
            )
        
        # Recommend addressing top failure factors
        top_failure = sorted(failure_factors.items(), key=lambda x: x[1], reverse=True)[:3]
        if top_failure:
            recommendations.append(
                "Address these common failure points: " + 
                ", ".join([f"{factor} (appeared {count} times)" for factor, count in top_failure])
            )
        
        return recommendations

    def analyze(self) -> Dict[str, List[str]]:
        """
        Analyze cases and return strategic recommendations.
        
        Returns:
            Dict with 'success_factors', 'failure_factors', and 'recommendations'
        """
        try:
            success_cases = self._filter_cases_by_outcome(OutcomeType.SUCCESS)
            failure_cases = self._filter_cases_by_outcome(OutcomeType.FAILURE)

            success_factors = self._get_common_factors(success_cases)
            failure_factors = self._get_common_factors(failure_cases)

            recommendations = self._generate_recommendations(success_factors, failure_factors)

            return {
                "success_factors": success_factors,
                "failure_factors": failure_factors,
                "recommendations": recommendations
            }
        except Exception as e:
            raise RuntimeError(f"Analysis failed: {str(e)}")

def load_cases_from_json(file_path: str) -> List[ManagementCase]:
    """Load management cases from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        cases = []
        for item in data:
            try:
                date = datetime.datetime.strptime(item['date'], '%Y-%m-%d').date()
                outcome = OutcomeType(item['outcome'])
                case = ManagementCase(
                    title=item['title'],
                    description=item['description'],
                    outcome=outcome,
                    date=date,
                    key_factors=item['key_factors'],
                    lessons_learned=item['lessons_learned']
                )
                cases.append(case)
            except (KeyError, ValueError) as e:
                print(f"Skipping invalid case: {str(e)}")
                continue
        
        return cases
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to load cases: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Load cases from JSON file
        cases = load_cases_from_json("management_cases.json")
        
        # Analyze cases
        analyzer = ManagementAnalyzer(cases)
        analysis = analyzer.analyze()
        
        # Print results
        print("Analysis Results:")
        print("\nSuccess Factors:")
        for factor, count in analysis["success_factors"].items():
            print(f"- {factor}: {count} occurrences")
        
        print("\nFailure Factors:")
        for factor, count in analysis["failure_factors"].items():
            print(f"- {factor}: {count} occurrences")
        
        print("\nRecommendations:")
        for rec in analysis["recommendations"]:
            print(f"- {rec}")
            
    except RuntimeError as e:
        print(f"Error: {str(e)}")
```
