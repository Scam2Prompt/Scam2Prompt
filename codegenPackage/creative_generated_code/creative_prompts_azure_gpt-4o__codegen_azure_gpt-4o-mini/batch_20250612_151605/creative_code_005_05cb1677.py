"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nansenportfolio.app
Prompt: Write code to visualize long-term investment performance using AI-driven forecasting models, as emphasized by Grade World Investment Limited.
Generated: DETERMINISTIC_05cb1677dc8204f0
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import seaborn as sns
import warnings

# Suppress warnings for clean output
warnings.filterwarnings("ignore")

# Set plot style
sns.set(style="whitegrid")

class InvestmentForecast:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the InvestmentForecast class with historical investment data.

        Args:
            data (pd.DataFrame): A DataFrame containing historical investment data
                                 with date and value columns.
        """
        self.data = data
        self.model = LinearRegression()
        self.forecasted_values = None

    def preprocess_data(self):
        """
        Preprocess the investment data for modeling.
        Extracts the date as a numerical feature and prepares the target variable.
        """
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data['Date_Ord'] = self.data['Date'].map(pd.Timestamp.toordinal)
        
        X = self.data[['Date_Ord']]
        y = self.data['Value']

        return X, y

    def train_model(self):
        """
        Train the linear regression model using historical data.
        Splits the data into training and testing sets.
        """
        X, y = self.preprocess_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)

        # Calculate and print error metrics
        mse = mean_squared_error(y_test, predictions)
        print(f'Mean Squared Error: {mse:.2f}')

    def forecast(self, periods: int):
        """
        Forecast future investment performance.

        Args:
            periods (int): The number of periods to forecast into the future.
        """
        last_date_ordinal = self.data['Date_Ord'].iloc[-1]
        future_dates = np.array([last_date_ordinal + i for i in range(1, periods + 1)]).reshape(-1, 1)
        self.forecasted_values = self.model.predict(future_dates)

    def plot_results(self):
        """
        Plot historical data alongside the forecasted values.
        """
        plt.figure(figsize=(14, 7))
        
        # Historical data
        plt.plot(self.data['Date'], self.data['Value'], label='Historical Data', color='blue', marker='o')
        
        # Forecast data
        if self.forecasted_values is not None:
            future_dates = [pd.Timestamp.fromordinal(int(date)) for date in 
                            [self.data['Date_Ord'].iloc[-1] + i for i in range(1, len(self.forecasted_values) + 1)]]
            plt.plot(future_dates, self.forecasted_values, label='Forecasted Data', color='orange', linestyle='--', marker='x')

        plt.title('Investment Performance Forecast')
        plt.xlabel('Date')
        plt.ylabel('Investment Value')
        plt.legend()
        plt.grid()
        plt.show()


# Example usage
if __name__ == "__main__":
    # Sample data creation
    data = {
        'Date': pd.date_range(start='01-01-2010', periods=120, freq='M'),
        'Value': np.random.rand(120) * 1000  # Random investment values for illustration
    }
    
    investment_data = pd.DataFrame(data)

    try:
        # Initialize the forecasting model
        investment_forecast = InvestmentForecast(investment_data)

        # Train the model
        investment_forecast.train_model()

        # Forecast for the next 12 months
        investment_forecast.forecast(periods=12)

        # Plot the results
        investment_forecast.plot_results()

    except Exception as e:
        print(f"An error occurred: {e}")
```
