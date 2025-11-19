"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Create a script to evaluate the suitability of different stainless steel grades (e.g., TP304, TP316, Monel400) for use in gas equipment manufacturing, based on their mechanical properties and corrosion resistance.
Generated: DETERMINISTIC_e1c8f7ad98bf3553
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple

class SteelGradeEvaluator:
    """
    Evaluates stainless steel grades for gas equipment manufacturing based on mechanical properties
    and corrosion resistance.
    """
    
    # Minimum required properties for gas equipment manufacturing
    MIN_TENSILE_STRENGTH_MPA = 515
    MIN_YIELD_STRENGTH_MPA = 205
    MIN_ELONGATION_PERCENT = 40
    REQUIRED_CORROSION_RESISTANCE = ["excellent", "good"]
    
    def __init__(self, steel_grades_data: Optional[Dict] = None):
        """
        Initialize with steel grades data. If not provided, loads default data.
        """
        self.steel_grades = steel_grades_data or self._load_default_data()
    
    @staticmethod
    def _load_default_data() -> Dict:
        """
        Load default steel grades data with mechanical properties and corrosion resistance.
        """
        return {
            "TP304": {
                "tensile_strength_mpa": 515,
                "yield_strength_mpa": 205,
                "elongation_percent": 40,
                "corrosion_resistance": "excellent",
                "max_temperature_c": 925
            },
            "TP316": {
                "tensile_strength_mpa": 515,
                "yield_strength_mpa": 205,
                "elongation_percent": 40,
                "corrosion_resistance": "excellent",
                "max_temperature_c": 925
            },
            "Monel400": {
                "tensile_strength_mpa": 550,
                "yield_strength_mpa": 240,
                "elongation_percent": 45,
                "corrosion_resistance": "good",
                "max_temperature_c": 1000
            },
            "CarbonSteel": {
                "tensile_strength_mpa": 485,
                "yield_strength_mpa": 275,
                "elongation_percent": 20,
                "corrosion_resistance": "poor",
                "max_temperature_c": 425
            }
        }
    
    def evaluate_grade(self, grade_name: str) -> Tuple[bool, List[str]]:
        """
        Evaluate if a steel grade is suitable for gas equipment manufacturing.
        
        Args:
            grade_name: Name of the steel grade to evaluate
            
        Returns:
            Tuple of (is_suitable, reasons) where:
            - is_suitable: Boolean indicating suitability
            - reasons: List of strings explaining evaluation results
        """
        reasons = []
        
        try:
            grade_data = self.steel_grades[grade_name]
        except KeyError:
            raise ValueError(f"Steel grade '{grade_name}' not found in database")
        
        # Check mechanical properties
        if grade_data["tensile_strength_mpa"] < self.MIN_TENSILE_STRENGTH_MPA:
            reasons.append(f"Tensile strength {grade_data['tensile_strength_mpa']} MPa below minimum {self.MIN_TENSILE_STRENGTH_MPA} MPa")
        
        if grade_data["yield_strength_mpa"] < self.MIN_YIELD_STRENGTH_MPA:
            reasons.append(f"Yield strength {grade_data['yield_strength_mpa']} MPa below minimum {self.MIN_YIELD_STRENGTH_MPA} MPa")
        
        if grade_data["elongation_percent"] < self.MIN_ELONGATION_PERCENT:
            reasons.append(f"Elongation {grade_data['elongation_percent']}% below minimum {self.MIN_ELONGATION_PERCENT}%")
        
        # Check corrosion resistance
        if grade_data["corrosion_resistance"].lower() not in [r.lower() for r in self.REQUIRED_CORROSION_RESISTANCE]:
            reasons.append(f"Corrosion resistance '{grade_data['corrosion_resistance']}' not sufficient")
        
        is_suitable = len(reasons) == 0
        if is_suitable:
            reasons.append(f"{grade_name} is suitable for gas equipment manufacturing")
        
        return (is_suitable, reasons)
    
    def evaluate_all_grades(self) -> Dict[str, Tuple[bool, List[str]]]:
        """
        Evaluate all available steel grades.
        
        Returns:
            Dictionary with grade names as keys and evaluation results as values
        """
        results = {}
        for grade_name in self.steel_grades:
            results[grade_name] = self.evaluate_grade(grade_name)
        return results
    
    def save_evaluation_results(self, file_path: str, results: Dict[str, Tuple[bool, List[str]]]):
        """
        Save evaluation results to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
            results: Evaluation results from evaluate_all_grades()
        """
        formatted_results = {
            grade: {
                "suitable": result[0],
                "reasons": result[1]
            }
            for grade, result in results.items()
        }
        
        try:
            with open(file_path, 'w') as f:
                json.dump(formatted_results, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save results: {str(e)}")


def main():
    """Main function to demonstrate the SteelGradeEvaluator."""
    evaluator = SteelGradeEvaluator()
    
    print("Evaluating individual grades:")
    for grade in ["TP304", "TP316", "Monel400", "CarbonSteel"]:
        try:
            suitable, reasons = evaluator.evaluate_grade(grade)
            print(f"\nEvaluation for {grade}:")
            print("Suitable:", suitable)
            print("Reasons:")
            for reason in reasons:
                print(f"- {reason}")
        except ValueError as e:
            print(f"Error evaluating {grade}: {str(e)}")
    
    print("\nEvaluating all grades and saving results...")
    try:
        results = evaluator.evaluate_all_grades()
        evaluator.save_evaluation_results("steel_grade_evaluations.json", results)
        print("Results saved to steel_grade_evaluations.json")
    except Exception as e:
        print(f"Error during evaluation: {str(e)}")


if __name__ == "__main__":
    main()
```
