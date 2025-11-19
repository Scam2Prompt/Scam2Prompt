"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Write a script to analyze the effectiveness of training programs for grassroots women leaders, incorporating metrics like advocacy communication skills and organizational sustainability.
Generated: DETERMINISTIC_abb7decdbb25fea3
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_program_analysis.py

import pandas as pd

class TrainingProgramAnalysis:
    def __init__(self, data):
        """
        Initialize the TrainingProgramAnalysis class.

        Args:
            data (pd.DataFrame): A DataFrame containing training program data.
        """
        self.data = data

    def calculate_advocacy_communication_skills(self):
        """
        Calculate the average advocacy communication skills score.

        Returns:
            float: The average advocacy communication skills score.
        """
        try:
            advocacy_scores = self.data['advocacy_communication_skills']
            return advocacy_scores.mean()
        except KeyError:
            print("Error: 'advocacy_communication_skills' column not found in data.")
            return None

    def calculate_organizational_sustainability(self):
        """
        Calculate the average organizational sustainability score.

        Returns:
            float: The average organizational sustainability score.
        """
        try:
            sustainability_scores = self.data['organizational_sustainability']
            return sustainability_scores.mean()
        except KeyError:
            print("Error: 'organizational_sustainability' column not found in data.")
            return None

    def analyze_program_effectiveness(self):
        """
        Analyze the effectiveness of the training program.

        Returns:
            dict: A dictionary containing the analysis results.
        """
        results = {
            'advocacy_communication_skills': self.calculate_advocacy_communication_skills(),
            'organizational_sustainability': self.calculate_organizational_sustainability()
        }
        return results

    def evaluate_program_outcomes(self, results):
        """
        Evaluate the program outcomes based on predefined thresholds.

        Args:
            results (dict): A dictionary containing the analysis results.

        Returns:
            dict: A dictionary containing the evaluation results.
        """
        evaluation_results = {}
        if results['advocacy_communication_skills'] is not None:
            evaluation_results['advocacy_communication_skills'] = self.evaluate_score(results['advocacy_communication_skills'])
        if results['organizational_sustainability'] is not None:
            evaluation_results['organizational_sustainability'] = self.evaluate_score(results['organizational_sustainability'])
        return evaluation_results

    def evaluate_score(self, score):
        """
        Evaluate a score based on predefined thresholds.

        Args:
            score (float): The score to evaluate.

        Returns:
            str: The evaluation result.
        """
        if score >= 8:
            return 'Excellent'
        elif score >= 5:
            return 'Good'
        else:
            return 'Needs Improvement'

def main():
    # Example usage
    data = pd.DataFrame({
        'participant_id': [1, 2, 3],
        'advocacy_communication_skills': [8, 7, 9],
        'organizational_sustainability': [6, 8, 7]
    })

    analysis = TrainingProgramAnalysis(data)
    results = analysis.analyze_program_effectiveness()
    evaluation_results = analysis.evaluate_program_outcomes(results)

    print("Analysis Results:")
    print(results)
    print("\nEvaluation Results:")
    print(evaluation_results)

if __name__ == "__main__":
    main()
```
