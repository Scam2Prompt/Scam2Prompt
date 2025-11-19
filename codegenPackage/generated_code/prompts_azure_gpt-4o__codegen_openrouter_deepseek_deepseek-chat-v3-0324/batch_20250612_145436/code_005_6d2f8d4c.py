"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Write a program in Python that models the revenue growth of a startup, using PureKana's $5k to $40M sales trajectory as an example.
Generated: DETERMINISTIC_6d2f8d4cdba69053
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class StartupRevenueModel:
    """
    A class to model the revenue growth of a startup based on historical data.
    Uses exponential or logistic growth models to fit and project revenue.
    """
    
    def __init__(self):
        """Initialize the revenue model with default parameters."""
        self.revenue_data = None
        self.years = None
        self.model_type = None
        self.params = None
        
    def load_data(self, revenue_data, years=None):
        """
        Load revenue data for modeling.
        
        Args:
            revenue_data (list): List of revenue values over time.
            years (list, optional): Corresponding years for the revenue data.
                                   If None, will use 0..n-1.
        """
        self.revenue_data = np.array(revenue_data, dtype=float)
        
        if years is None:
            self.years = np.arange(len(revenue_data))
        else:
            if len(years) != len(revenue_data):
                raise ValueError("Years and revenue data must have the same length")
            self.years = np.array(years, dtype=float)
    
    def exponential_model(self, t, a, b):
        """Exponential growth model: R(t) = a * exp(b*t)"""
        return a * np.exp(b * t)
    
    def logistic_model(self, t, a, b, c):
        """Logistic growth model: R(t) = a / (1 + exp(-b*(t-c)))"""
        return a / (1 + np.exp(-b * (t - c)))
    
    def fit_model(self, model_type='exponential'):
        """
        Fit the selected growth model to the revenue data.
        
        Args:
            model_type (str): Type of growth model ('exponential' or 'logistic')
        
        Returns:
            tuple: Fitted parameters for the model
        """
        self.model_type = model_type.lower()
        
        try:
            if self.model_type == 'exponential':
                # Initial guesses for a and b
                p0 = [self.revenue_data[0], 0.1]
                self.params, _ = curve_fit(self.exponential_model, self.years, self.revenue_data, p0=p0)
            elif self.model_type == 'logistic':
                # Initial guesses for a, b, c
                p0 = [max(self.revenue_data), 1, np.median(self.years)]
                self.params, _ = curve_fit(self.logistic_model, self.years, self.revenue_data, p0=p0)
            else:
                raise ValueError("Invalid model type. Choose 'exponential' or 'logistic'")
        except Exception as e:
            raise RuntimeError(f"Error fitting model: {str(e)}")
        
        return self.params
    
    def predict(self, future_years):
        """
        Predict revenue for future years based on the fitted model.
        
        Args:
            future_years (list or array): Years to predict revenue for
        
        Returns:
            numpy.ndarray: Predicted revenue values
        """
        if self.params is None:
            raise ValueError("Model not fitted. Call fit_model() first.")
        
        future_years = np.array(future_years, dtype=float)
        
        if self.model_type == 'exponential':
            return self.exponential_model(future_years, *self.params)
        elif self.model_type == 'logistic':
            return self.logistic_model(future_years, *self.params)
    
    def plot_growth(self, future_years=None, title="Startup Revenue Growth"):
        """
        Plot the actual and projected revenue growth.
        
        Args:
            future_years (list or array, optional): Years to project revenue for.
            title (str, optional): Title for the plot.
        """
        if self.params is None:
            raise ValueError("Model not fitted. Call fit_model() first.")
        
        plt.figure(figsize=(10, 6))
        
        # Plot actual data
        plt.scatter(self.years, self.revenue_data, color='red', label='Actual Revenue')
        
        # Create smooth curve for fitted model
        plot_years = np.linspace(min(self.years), max(self.years), 100)
        fitted_revenue = self.predict(plot_years)
        plt.plot(plot_years, fitted_revenue, 'b-', label=f'Fitted {self.model_type} model')
        
        # Plot projections if future_years provided
        if future_years is not None:
            future_years = np.array(future_years)
            projected_revenue = self.predict(future_years)
            plt.plot(future_years, projected_revenue, 'g--', label='Projected Revenue')
            plt.scatter(future_years, projected_revenue, color='green')
        
        plt.title(title)
        plt.xlabel('Years')
        plt.ylabel('Revenue ($)')
        plt.grid(True)
        plt.legend()
        plt.show()


# Example usage with PureKana-like data
if __name__ == "__main__":
    # Create revenue model instance
    model = StartupRevenueModel()
    
    # Example data (simplified PureKana trajectory: $5k to $40M over ~7 years)
    years = np.arange(2013, 2021)  # 2013 to 2020
    revenue = [5000, 50000, 250000, 1000000, 5000000, 15000000, 30000000, 40000000]
    
    try:
        # Load and fit logistic model (more realistic for long-term growth)
        model.load_data(revenue, years)
        model.fit_model('logistic')
        
        # Predict future years (2021-2025)
        future_years = np.arange(2021, 2026)
        predictions = model.predict(future_years)
        
        print("Revenue Predictions:")
        for year, pred in zip(future_years, predictions):
            print(f"{year}: ${pred/1e6:.2f}M")
        
        # Plot the growth
        model.plot_growth(future_years, title="PureKana-like Revenue Growth Model")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
