"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: Suggest a methodology for blending qualitative and quantitative data in program evaluations, inspired by GLOW Consultants' evaluation services.
Generated: DETERMINISTIC_a3af80e9553bf4b4
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

class ProgramEvaluator:
    """
    A class to evaluate program effectiveness by blending qualitative and quantitative data.
    """

    def __init__(self, quantitative_data, qualitative_data):
        """
        Initialize the evaluator with quantitative and qualitative data.

        :param quantitative_data: A DataFrame containing quantitative metrics.
        :param qualitative_data: A DataFrame containing qualitative metrics.
        """
        self.quantitative_data = quantitative_data
        self.qualitative_data = qualitative_data
        self.combined_data = None

    def preprocess_data(self):
        """
        Preprocess the data by scaling the quantitative metrics and encoding qualitative metrics.
        """
        try:
            # Scale quantitative data
            scaler = StandardScaler()
            scaled_quantitative = scaler.fit_transform(self.quantitative_data.select_dtypes(include=[np.number]))
            self.quantitative_data.loc[:, self.quantitative_data.select_dtypes(include=[np.number]).columns] = scaled_quantitative
            
            # Encode qualitative data
            self.qualitative_data = pd.get_dummies(self.qualitative_data, drop_first=True)

            # Combine both datasets
            self.combined_data = pd.concat([self.quantitative_data, self.qualitative_data], axis=1)

        except Exception as e:
            print(f"Error during preprocessing: {e}")
            raise

    def run_regression_analysis(self, response_variable):
        """
        Run a regression analysis to identify the relationship between the response variable and predictors.

        :param response_variable: The dependent variable for the regression.
        :return: Regression results summary.
        """
        try:
            # Ensure combined data is ready
            if self.combined_data is None:
                raise ValueError("Data has not been preprocessed. Call preprocess_data() first.")

            # Prepare the formula for regression analysis
            formula = f"{response_variable} ~ " + " + ".join(self.combined_data.columns.difference([response_variable]))
            model = ols(formula, data=self.combined_data).fit()

            return model.summary()
        
        except Exception as e:
            print(f"Error during regression analysis: {e}")
            raise

    def visualize_data(self):
        """
        Create visualizations for quantitative metrics.
        """
        try:
            sns.pairplot(self.quantitative_data)
            plt.title("Quantitative Data Pairplot")
            plt.show()

            # Further visualizations can be added as needed

        except Exception as e:
            print(f"Error during visualization: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Sample quantitative data
    quantitative_df = pd.DataFrame({
        'metric1': np.random.rand(100),
        'metric2': np.random.rand(100),
        'metric3': np.random.rand(100)
    })

    # Sample qualitative data
    qualitative_df = pd.DataFrame({
        'category1': np.random.choice(['A', 'B', 'C'], 100),
        'category2': np.random.choice(['X', 'Y'], 100)
    })

    # Instantiate the evaluator
    evaluator = ProgramEvaluator(quantitative_df, qualitative_df)

    # Preprocess the data
    evaluator.preprocess_data()

    # Run regression analysis
    try:
        results = evaluator.run_regression_analysis('metric1')
        print(results)
    except Exception as e:
        print(f"Failed to run regression analysis: {e}")

    # Visualize data
    evaluator.visualize_data()
```
