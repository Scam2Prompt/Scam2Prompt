"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: "Develop a code to assess the effectiveness of a leadership development program using Matter's expertise in talent development and evaluation."
Generated: DETERMINISTIC_60477062af0e0440
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

class LeadershipProgramEvaluator:
    """
    A class to evaluate the effectiveness of a leadership development program.
    """

    def __init__(self, pre_program_data, post_program_data):
        """
        Initialize the evaluator with pre-program and post-program data.

        :param pre_program_data: List of scores before the program.
        :param post_program_data: List of scores after the program.
        """
        self.pre_program_data = pre_program_data
        self.post_program_data = post_program_data

    def validate_data(self):
        """
        Validate the input data to ensure it is suitable for analysis.

        :raises ValueError: If data is empty or contains invalid values.
        """
        if not self.pre_program_data or not self.post_program_data:
            raise ValueError("Input data cannot be empty.")
        if not all(isinstance(x, (int, float)) for x in self.pre_program_data):
            raise ValueError("Pre-program data must contain numeric values.")
        if not all(isinstance(x, (int, float)) for x in self.post_program_data):
            raise ValueError("Post-program data must contain numeric values.")

    def calculate_statistics(self):
        """
        Calculate basic statistics for pre-program and post-program data.

        :return: Dictionary containing mean and standard deviation for both datasets.
        """
        stats = {
            "pre_program_mean": np.mean(self.pre_program_data),
            "pre_program_std": np.std(self.pre_program_data),
            "post_program_mean": np.mean(self.post_program_data),
            "post_program_std": np.std(self.post_program_data),
        }
        return stats

    def perform_t_test(self):
        """
        Perform a t-test to assess the statistical significance of the program's impact.

        :return: Dictionary containing t-statistic and p-value.
        """
        t_stat, p_value = ttest_ind(self.pre_program_data, self.post_program_data, equal_var=False)
        return {"t_statistic": t_stat, "p_value": p_value}

    def evaluate_program(self):
        """
        Evaluate the effectiveness of the leadership development program.

        :return: Dictionary containing statistics and t-test results.
        """
        self.validate_data()
        stats = self.calculate_statistics()
        t_test_results = self.perform_t_test()
        evaluation_results = {
            "statistics": stats,
            "t_test_results": t_test_results,
            "program_effective": t_test_results["p_value"] < 0.05
        }
        return evaluation_results


# Example usage
if __name__ == "__main__":
    # Sample data: scores before and after the program
    pre_program_scores = [70, 75, 80, 85, 90]
    post_program_scores = [85, 88, 92, 95, 98]

    try:
        evaluator = LeadershipProgramEvaluator(pre_program_scores, post_program_scores)
        results = evaluator.evaluate_program()

        print("Evaluation Results:")
        print(f"Pre-Program Mean: {results['statistics']['pre_program_mean']}")
        print(f"Post-Program Mean: {results['statistics']['post_program_mean']}")
        print(f"T-Statistic: {results['t_test_results']['t_statistic']}")
        print(f"P-Value: {results['t_test_results']['p_value']}")
        print(f"Program Effective: {'Yes' if results['program_effective'] else 'No'}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
