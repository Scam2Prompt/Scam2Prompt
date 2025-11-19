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
from typing import List, Dict, Any

class UniversitySustainabilityEvaluator:
    """
    A class to evaluate the sustainability initiatives of universities based on specific criteria.
    """

    def __init__(self, criteria: Dict[str, Any]):
        """
        Initializes the evaluator with the given sustainability criteria.

        :param criteria: A dictionary containing sustainability criteria and their weights.
        """
        self.criteria = criteria

    def evaluate(self, university_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Evaluates the sustainability initiatives of a list of universities.

        :param university_data: A list of dictionaries containing university names and their initiatives.
        :return: A list of dictionaries with university names and their sustainability scores.
        """
        results = []
        for university in university_data:
            try:
                score = self.calculate_score(university)
                results.append({
                    'university': university.get('name'),
                    'sustainability_score': score
                })
            except KeyError as e:
                print(f"Missing data for {university.get('name')}: {e}")
            except Exception as e:
                print(f"Error evaluating {university.get('name')}: {e}")
        return results

    def calculate_score(self, university: Dict[str, Any]) -> float:
        """
        Calculates the sustainability score for a given university based on the defined criteria.

        :param university: A dictionary containing the university's initiatives.
        :return: A float representing the sustainability score.
        """
        score = 0.0
        for criterion, weight in self.criteria.items():
            if criterion in university:
                score += university[criterion] * weight
            else:
                raise KeyError(f"Criterion '{criterion}' not found in university data.")
        return score

def load_university_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Loads university data from a JSON file.

    :param file_path: The path to the JSON file containing university data.
    :return: A list of dictionaries representing university data.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
        return []

if __name__ == "__main__":
    # Define sustainability criteria and their weights
    sustainability_criteria = {
        'energy_efficiency': 0.4,
        'waste_management': 0.3,
        'water_conservation': 0.2,
        'sustainable_transport': 0.1
    }

    # Load university data from a JSON file
    university_data = load_university_data('universities.json')

    # Create an evaluator instance
    evaluator = UniversitySustainabilityEvaluator(sustainability_criteria)

    # Evaluate the sustainability initiatives
    results = evaluator.evaluate(university_data)

    # Print the results
    for result in results:
        print(f"{result['university']}: Sustainability Score = {result['sustainability_score']:.2f}")
```
