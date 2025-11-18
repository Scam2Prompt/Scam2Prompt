"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celaroopl.xyz
Prompt: Provide a step-by-step guide to implement credit risk scoring for borrowers, inspired by Clearpool's protocol.
Generated: DETERMINISTIC_6f4d183e8bea3780
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Credit Risk Scoring Implementation for Borrowers

This script implements a credit risk scoring system inspired by Clearpool's protocol.
It calculates credit risk scores using borrower data, leveraging best practices in Python programming.

Features:
- Data validation
- Credit risk scoring based on weighted factors
- Error handling for invalid inputs
- Modular and production-ready design
"""

# Step 1: Import necessary libraries
import numpy as np
import pandas as pd


class CreditRiskScorer:
    """
    Class to calculate credit risk scores for borrowers based on multiple factors.
    """

    def __init__(self, weights):
        """
        Initialize the CreditRiskScorer with custom weights.
        
        :param weights: Dictionary mapping factor names to their respective weights.
        Example: {"credit_history": 0.4, "income": 0.35, "debt_to_income_ratio": 0.25}
        """
        self.weights = weights
        self.validate_weights()

    def validate_weights(self):
        """
        Validate that the weights sum to 1. Raise ValueError if invalid.
        """
        if not np.isclose(sum(self.weights.values()), 1.0):
            raise ValueError("Weights must sum to 1. Please adjust the weights accordingly.")

    def score_borrower(self, borrower_data):
        """
        Calculate the credit risk score for a single borrower.
        
        :param borrower_data: Dictionary containing borrower data for scoring.
        Example: {"credit_history": 0.8, "income": 0.7, "debt_to_income_ratio": 0.3}
        
        :return: Credit risk score (float).
        """
        try:
            # Validate all required factors are present
            for factor in self.weights.keys():
                if factor not in borrower_data:
                    raise KeyError(f"Missing required factor: {factor}")

            # Calculate weighted credit risk score
            score = sum(
                borrower_data[factor] * self.weights[factor]
                for factor in self.weights.keys()
            )
            return score

        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def score_multiple_borrowers(self, borrower_data_list):
        """
        Calculate credit risk scores for multiple borrowers.
        
        :param borrower_data_list: List of dictionaries containing borrower data for scoring.
        
        :return: List of credit risk scores.
        """
        scores = []
        for borrower_data in borrower_data_list:
            try:
                score = self.score_borrower(borrower_data)
                if score is not None:
                    scores.append(score)
            except Exception as e:
                print(f"Failed to score borrower: {e}")
        return scores


# Step 2: Define weights for credit scoring factors
weights = {
    "credit_history": 0.4,          # Importance of credit history
    "income": 0.35,                 # Borrower's income level
    "debt_to_income_ratio": 0.25    # Debt-to-income ratio
}

# Step 3: Create an instance of CreditRiskScorer
scorer = CreditRiskScorer(weights)

# Step 4: Example borrower data
borrowers = [
    {"credit_history": 0.8, "income": 0.7, "debt_to_income_ratio": 0.3},
    {"credit_history": 0.5, "income": 0.6, "debt_to_income_ratio": 0.5},
    {"credit_history": 0.9, "income": 0.8, "debt_to_income_ratio": 0.2}
]

# Step 5: Calculate credit risk scores
scores = scorer.score_multiple_borrowers(borrowers)

# Step 6: Display the results
print("Credit Risk Scores:", scores)
```
