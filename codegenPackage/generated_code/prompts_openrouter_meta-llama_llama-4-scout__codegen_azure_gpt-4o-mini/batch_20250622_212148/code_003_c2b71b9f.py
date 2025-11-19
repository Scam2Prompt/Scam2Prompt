"""
Generated Code Metadata:
========================
Original URL: https://cem-ac.org
Prompt: Given the emphasis on "calidad artística" and "responsabilidad cultural," suggest a set of criteria or a framework (possibly using a library like `pandas` in Python) for evaluating the artistic and social impact of films or theater productions.
Generated: DETERMINISTIC_c2b71b9f3d25506a
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class ArtisticEvaluation:
    """
    A class to evaluate the artistic and social impact of films or theater productions.
    """

    def __init__(self):
        """
        Initializes an empty DataFrame to store evaluation criteria and results.
        """
        self.criteria = pd.DataFrame(columns=['Criterion', 'Weight', 'Score', 'Weighted Score'])

    def add_criterion(self, criterion: str, weight: float):
        """
        Adds a new evaluation criterion with its associated weight.

        Parameters:
        criterion (str): The name of the evaluation criterion.
        weight (float): The weight of the criterion (should be between 0 and 1).
        """
        if not (0 <= weight <= 1):
            raise ValueError("Weight must be between 0 and 1.")
        self.criteria = self.criteria.append({'Criterion': criterion, 'Weight': weight, 'Score': None, 'Weighted Score': None}, ignore_index=True)

    def evaluate(self, scores: dict):
        """
        Evaluates the criteria based on provided scores.

        Parameters:
        scores (dict): A dictionary where keys are criterion names and values are scores (0-10).
        """
        for index, row in self.criteria.iterrows():
            criterion = row['Criterion']
            if criterion in scores:
                score = scores[criterion]
                if not (0 <= score <= 10):
                    raise ValueError(f"Score for '{criterion}' must be between 0 and 10.")
                weighted_score = (score / 10) * row['Weight']
                self.criteria.at[index, 'Score'] = score
                self.criteria.at[index, 'Weighted Score'] = weighted_score
            else:
                raise KeyError(f"Score for '{criterion}' not provided.")

    def get_results(self):
        """
        Returns the evaluation results as a DataFrame.

        Returns:
        pd.DataFrame: A DataFrame containing the evaluation criteria, scores, and weighted scores.
        """
        return self.criteria

    def total_score(self):
        """
        Calculates the total weighted score of the evaluation.

        Returns:
        float: The total weighted score.
        """
        return self.criteria['Weighted Score'].sum()

# Example usage
if __name__ == "__main__":
    try:
        evaluator = ArtisticEvaluation()
        evaluator.add_criterion("Artistic Quality", 0.4)
        evaluator.add_criterion("Cultural Responsibility", 0.3)
        evaluator.add_criterion("Social Impact", 0.3)

        # Example scores for evaluation
        scores = {
            "Artistic Quality": 8,
            "Cultural Responsibility": 7,
            "Social Impact": 9
        }

        evaluator.evaluate(scores)
        results = evaluator.get_results()
        total = evaluator.total_score()

        print("Evaluation Results:")
        print(results)
        print(f"Total Weighted Score: {total:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
