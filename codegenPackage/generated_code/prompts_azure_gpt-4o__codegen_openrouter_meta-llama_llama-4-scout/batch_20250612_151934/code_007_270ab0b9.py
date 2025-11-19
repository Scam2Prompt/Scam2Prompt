"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: Create a Python script to analyze the effectiveness of Certified Financial Analyst Training (CFAT) programs, incorporating metrics for learner progress and outcomes.
Generated: DETERMINISTIC_270ab0b9a1c1dcd6
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cfat_analysis.py

import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class CFATAnalyzer:
    """
    Analyzes the effectiveness of Certified Financial Analyst Training (CFAT) programs.
    """

    def __init__(self, data):
        """
        Initializes the CFATAnalyzer with learner data.

        Args:
            data (pd.DataFrame): A DataFrame containing learner data.
        """
        self.data = data

    def calculate_progress_metrics(self):
        """
        Calculates learner progress metrics.

        Returns:
            dict: A dictionary containing progress metrics (e.g., completion rate, average score).
        """
        # Calculate completion rate
        completed_learners = self.data[self.data['completed'] == True].shape[0]
        total_learners = self.data.shape[0]
        completion_rate = (completed_learners / total_learners) * 100

        # Calculate average score
        average_score = self.data['score'].mean()

        return {
            'completion_rate': completion_rate,
            'average_score': average_score
        }

    def analyze_outcomes(self):
        """
        Analyzes learner outcomes using linear regression.

        Returns:
            dict: A dictionary containing outcome metrics (e.g., coefficients, R-squared value).
        """
        # Prepare data for linear regression
        X = self.data[['hours_studied', 'prior_experience']]
        y = self.data['score']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate model performance
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = mse ** 0.5
        r2 = metrics.r2_score(y_test, y_pred)

        return {
            'coefficients': model.coef_,
            'intercept': model.intercept_,
            'mae': mae,
            'mse': mse,
            'rmse': rmse,
            'r2': r2
        }

def main():
    try:
        # Load sample data
        data = pd.DataFrame({
            'learner_id': [1, 2, 3, 4, 5],
            'hours_studied': [10, 20, 15, 30, 25],
            'prior_experience': [1, 2, 3, 4, 5],
            'completed': [True, False, True, True, False],
            'score': [80, 70, 90, 85, 75]
        })

        analyzer = CFATAnalyzer(data)

        # Calculate progress metrics
        progress_metrics = analyzer.calculate_progress_metrics()
        print("Progress Metrics:")
        print(f"Completion Rate: {progress_metrics['completion_rate']:.2f}%")
        print(f"Average Score: {progress_metrics['average_score']:.2f}")

        # Analyze outcomes
        outcome_metrics = analyzer.analyze_outcomes()
        print("\nOutcome Metrics:")
        print(f"Coefficients: {outcome_metrics['coefficients']}")
        print(f"Intercept: {outcome_metrics['intercept']:.2f}")
        print(f"MAE: {outcome_metrics['mae']:.2f}")
        print(f"MSE: {outcome_metrics['mse']:.2f}")
        print(f"RMSE: {outcome_metrics['rmse']:.2f}")
        print(f"R-squared: {outcome_metrics['r2']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
