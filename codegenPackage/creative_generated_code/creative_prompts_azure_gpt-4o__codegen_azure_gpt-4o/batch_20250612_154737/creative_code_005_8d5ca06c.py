"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: Write a program to measure the success of a grants program using key results and indicators, as outlined in Gitcoin's Playbook.
Generated: DETERMINISTIC_8d5ca06cc5c600ba
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import statistics
from typing import List, Dict, Union

class GrantProgramEvaluator:
    """
    A class to evaluate the success of a grants program based on key results and indicators.
    """

    def __init__(self, key_results: List[Dict[str, Union[str, float]]]):
        """
        Initialize the evaluator with key results.

        :param key_results: A list of dictionaries containing key results and their values.
                            Example: [{'indicator': 'funds_distributed', 'value': 5000.0},
                                      {'indicator': 'projects_funded', 'value': 25}]
        """
        self.key_results = key_results

    def calculate_average(self) -> float:
        """
        Calculate the average value of all key result indicators.

        :return: The average value.
        """
        values = [kr['value'] for kr in self.key_results if 'value' in kr]
        if not values:
            raise ValueError("No valid values found in key results.")
        return statistics.mean(values)

    def calculate_maximum(self) -> float:
        """
        Calculate the maximum value across all key result indicators.

        :return: The maximum value.
        """
        values = [kr['value'] for kr in self.key_results if 'value' in kr]
        if not values:
            raise ValueError("No valid values found in key results.")
        return max(values)

    def calculate_minimum(self) -> float:
        """
        Calculate the minimum value across all key result indicators.

        :return: The minimum value.
        """
        values = [kr['value'] for kr in self.key_results if 'value' in kr]
        if not values:
            raise ValueError("No valid values found in key results.")
        return min(values)

    def get_indicator_summary(self) -> Dict[str, Union[float, int]]:
        """
        Generate a summary of indicators including their average, max, and min values.

        :return: A dictionary summarizing the indicators.
        """
        try:
            return {
                'average': self.calculate_average(),
                'maximum': self.calculate_maximum(),
                'minimum': self.calculate_minimum(),
                'total_indicators': len(self.key_results)
            }
        except ValueError as e:
            return {"error": str(e)}

    def export_results_to_json(self, filename: str) -> None:
        """
        Export the evaluation results to a JSON file.

        :param filename: The name of the file where results will be saved.
        :return: None
        """
        results = self.get_indicator_summary()
        try:
            with open(filename, 'w') as file:
                json.dump(results, file, indent=4)
            print(f"Results successfully exported to {filename}.")
        except IOError as e:
            print(f"Error saving results to file: {e}")

# Example Usage
if __name__ == "__main__":
    # Example key results based on Gitcoin's Playbook indicators
    key_results_data = [
        {'indicator': 'funds_distributed', 'value': 5000.0},
        {'indicator': 'projects_funded', 'value': 25},
        {'indicator': 'community_engagement', 'value': 85.0},
        {'indicator': 'innovation', 'value': 92.0}
    ]

    # Initialize the evaluator
    evaluator = GrantProgramEvaluator(key_results_data)

    # Print summary results
    print("Indicator Summary:", evaluator.get_indicator_summary())

    # Export results to JSON file
    evaluator.export_results_to_json("grant_program_results.json")
```
