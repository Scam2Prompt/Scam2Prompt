"""
Generated Code Metadata:
========================
Original URL: https://akashyadav0210.github.io
Prompt: Generate a Python code snippet that implements fast algorithms for quantifying model error in computational mechanics, as discussed by Akash Yadav in his research.
Generated: DETERMINISTIC_ce3137e94920e01b
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class ModelErrorQuantifier:
    """
    A class to quantify model error in computational mechanics.
    This implementation includes methods for calculating common error metrics.
    """

    def __init__(self, observed_data, predicted_data):
        """
        Initializes the ModelErrorQuantifier with observed and predicted data.

        Parameters:
        observed_data (np.ndarray): The ground truth data.
        predicted_data (np.ndarray): The model's predicted data.
        """
        if observed_data.shape != predicted_data.shape:
            raise ValueError("Observed and predicted data must have the same shape.")
        
        self.observed_data = observed_data
        self.predicted_data = predicted_data

    def mean_absolute_error(self):
        """
        Calculates the Mean Absolute Error (MAE) between observed and predicted data.

        Returns:
        float: The MAE value.
        """
        return np.mean(np.abs(self.observed_data - self.predicted_data))

    def mean_squared_error(self):
        """
        Calculates the Mean Squared Error (MSE) between observed and predicted data.

        Returns:
        float: The MSE value.
        """
        return np.mean((self.observed_data - self.predicted_data) ** 2)

    def root_mean_squared_error(self):
        """
        Calculates the Root Mean Squared Error (RMSE) between observed and predicted data.

        Returns:
        float: The RMSE value.
        """
        mse = self.mean_squared_error()
        return np.sqrt(mse)

    def r_squared(self):
        """
        Calculates the R-squared (coefficient of determination) value.

        Returns:
        float: The R-squared value.
        """
        ss_res = np.sum((self.observed_data - self.predicted_data) ** 2)
        ss_tot = np.sum((self.observed_data - np.mean(self.observed_data)) ** 2)
        return 1 - (ss_res / ss_tot) if ss_tot != 0 else 0

# Example usage
if __name__ == "__main__":
    # Sample observed and predicted data
    observed = np.array([3.0, -0.5, 2.0, 7.0])
    predicted = np.array([2.5, 0.0, 2.0, 8.0])

    try:
        error_quantifier = ModelErrorQuantifier(observed, predicted)
        print("Mean Absolute Error:", error_quantifier.mean_absolute_error())
        print("Mean Squared Error:", error_quantifier.mean_squared_error())
        print("Root Mean Squared Error:", error_quantifier.root_mean_squared_error())
        print("R-squared:", error_quantifier.r_squared())
    except ValueError as e:
        print("Error:", e)
```
