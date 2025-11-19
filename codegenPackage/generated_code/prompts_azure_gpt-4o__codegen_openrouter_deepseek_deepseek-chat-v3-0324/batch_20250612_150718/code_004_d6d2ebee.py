"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Write a program to simulate the SOMAT entrance test scoring system, including sections like Verbal Ability, Quantitative Ability, and Case Analysis, as outlined on the SOMTU website.
Generated: DETERMINISTIC_d6d2ebeeab0f9d50
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Section:
    name: str
    max_score: int
    weight: float
    questions: List[Dict[str, str]]
    answers: Dict[int, str]

@dataclass
class TestResult:
    section_scores: Dict[str, float]
    weighted_scores: Dict[str, float]
    total_score: float

class SOMATScoringSystem:
    def __init__(self):
        self.sections: Dict[str, Section] = {}
        self.load_test_structure()
    
    def load_test_structure(self) -> None:
        """Load the test structure from a JSON file or default structure"""
        try:
            with open('somat_structure.json', 'r') as f:
                data = json.load(f)
                for section_data in data['sections']:
                    self.sections[section_data['name']] = Section(
                        name=section_data['name'],
                        max_score=section_data['max_score'],
                        weight=section_data['weight'],
                        questions=section_data['questions'],
                        answers=section_data['answers']
                    )
        except FileNotFoundError:
            # Default structure if file not found
            self.sections = {
                "Verbal Ability": Section(
                    name="Verbal Ability",
                    max_score=30,
                    weight=0.30,
                    questions=[
                        {"id": 1, "text": "Synonym of 'Eloquent'"},
                        {"id": 2, "text": "Antonym of 'Benevolent'"},
                        # ... more questions
                    ],
                    answers={1: "A", 2: "C", 3: "B", 4: "D", 5: "A"}
                ),
                "Quantitative Ability": Section(
                    name="Quantitative Ability",
                    max_score=30,
                    weight=0.35,
                    questions=[
                        {"id": 1, "text": "Solve for x: 2x + 5 = 15"},
                        {"id": 2, "text": "What is 15% of 200?"},
                        # ... more questions
                    ],
                    answers={1: "C", 2: "B", 3: "A", 4: "D", 5: "C"}
                ),
                "Case Analysis": Section(
                    name="Case Analysis",
                    max_score=40,
                    weight=0.35,
                    questions=[
                        {"id": 1, "text": "Analyze the business case and answer..."},
                        {"id": 2, "text": "What strategy would you recommend?"},
                        # ... more questions
                    ],
                    answers={1: "D", 2: "A", 3: "B", 4: "C", 5: "D"}
                )
            }
    
    def calculate_section_score(self, section_name: str, responses: Dict[int, str]) -> float:
        """Calculate raw score for a section based on responses"""
        if section_name not in self.sections:
            raise ValueError(f"Invalid section name: {section_name}")
        
        section = self.sections[section_name]
        correct = 0
        
        for q_id, answer in responses.items():
            if q_id in section.answers and answer == section.answers[q_id]:
                correct += 1
        
        return (correct / len(section.answers)) * section.max_score
    
    def calculate_total_score(self, all_responses: Dict[str, Dict[int, str]]) -> TestResult:
        """Calculate total score with weighted sections"""
        section_scores = {}
        weighted_scores = {}
        total_score = 0.0
        
        for section_name, responses in all_responses.items():
            raw_score = self.calculate_section_score(section_name, responses)
            section_scores[section_name] = raw_score
            weighted_score = raw_score * self.sections[section_name].weight
            weighted_scores[section_name] = weighted_score
            total_score += weighted_score
        
        return TestResult(
            section_scores=section_scores,
            weighted_scores=weighted_scores,
            total_score=total_score
        )
    
    def generate_report(self, result: TestResult) -> str:
        """Generate a printable report of the test results"""
        report = []
        report.append("SOMAT ENTRANCE TEST RESULTS")
        report.append("=" * 30)
        
        for section_name in result.section_scores:
            report.append(
                f"{section_name}: {result.section_scores[section_name]:.2f} "
                f"(Weighted: {result.weighted_scores[section_name]:.2f})"
            )
        
        report.append("-" * 30)
        report.append(f"TOTAL SCORE: {result.total_score:.2f}/100")
        report.append("=" * 30)
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    scoring_system = SOMATScoringSystem()
    
    # Sample responses (would normally come from user input)
    sample_responses = {
        "Verbal Ability": {1: "A", 2: "C", 3: "B", 4: "D", 5: "A"},
        "Quantitative Ability": {1: "C", 2: "B", 3: "A", 4: "D", 5: "C"},
        "Case Analysis": {1: "D", 2: "A", 3: "B", 4: "C", 5: "D"}
    }
    
    try:
        result = scoring_system.calculate_total_score(sample_responses)
        print(scoring_system.generate_report(result))
    except ValueError as e:
        print(f"Error calculating scores: {e}")
```
