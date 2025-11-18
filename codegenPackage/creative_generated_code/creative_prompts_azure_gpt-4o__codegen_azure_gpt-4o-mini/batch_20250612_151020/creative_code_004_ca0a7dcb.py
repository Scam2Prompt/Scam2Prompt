"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds.pro
Prompt: Generate code to track and simulate Moonbird B95's flight data over time, integrating historical data and predictions for future migrations.
Generated: DETERMINISTIC_ca0a7dcb3eec5166
Batch ID: 20250612_151020
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
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

class MoonbirdFlightTracker:
    """
    Class to track and simulate the flight data of Moonbird B95 over time.
    This includes integration of historical data and predictions for future migrations.
    """

    def __init__(self, historical_data):
        """
        Initializes the flight tracker with historical flight data.

        Parameters:
        historical_data (DataFrame): A pandas DataFrame containing past flight records with 'date' and 'location' columns.
        """
        self.historical_data = historical_data
        self.model = LinearRegression()
        self.future_predictions = None

    def preprocess_data(self):
        """
        Preprocess the historical flight data to prepare it for modeling.
        """
        self.historical_data['date'] = pd.to_datetime(self.historical_data['date'])
        self.historical_data['date_ordinal'] = self.historical_data['date'].apply(lambda x: x.toordinal())

    def fit_model(self):
        """
        Fits a linear regression model to the historical flight data.
        """
        try:
            X = self.historical_data[['date_ordinal']]
            y = self.historical_data['location']
            self.model.fit(X, y)
        except Exception as e:
            raise RuntimeError("Model fitting failed") from e

    def predict_future(self, start_date, days):
        """
        Predicts future locations of the Moonbird B95 based on the fitted model.

        Parameters:
        start_date (str): The starting date for predictions in 'YYYY-MM-DD' format.
        days (int): Number of days to predict into the future.

        Returns:
        DataFrame: A DataFrame containing predicted dates and locations.
        """
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            future_dates = [start_date + timedelta(days=i) for i in range(days)]
            future_dates_ordinal = [date.toordinal() for date in future_dates]

            future_locations = self.model.predict(np.array(future_dates_ordinal).reshape(-1, 1))
            self.future_predictions = pd.DataFrame({'date': future_dates, 'predicted_location': future_locations})
            return self.future_predictions
        except Exception as e:
            raise ValueError("Error in predicting future locations") from e

    def plot_flight_data(self):
        """
        Plots the historical flight data and the predicted future locations.
        """
        try:
            plt.figure(figsize=(12, 6))
            plt.scatter(self.historical_data['date'], self.historical_data['location'], color='blue', label='Historical Data')
            if self.future_predictions is not None:
                plt.plot(self.future_predictions['date'], self.future_predictions['predicted_location'], color='orange', linestyle='--', label='Predicted Future Locations')
            plt.title('Moonbird B95 Flight Data')
            plt.xlabel('Date')
            plt.ylabel('Location')
            plt.legend()
            plt.grid()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise RuntimeError("Error in plotting flight data") from e

# Example usage
if __name__ == "__main__":
    # Example historical flight data
    historical_data = pd.DataFrame({
        'date': ['2022-01-01', '2022-01-15', '2022-02-01', '2022-02-15'],
        'location': [100, 150, 200, 250]  # Replace with actual location data
    })

    flight_tracker = MoonbirdFlightTracker(historical_data)
    flight_tracker.preprocess_data()
    flight_tracker.fit_model()
    predictions = flight_tracker.predict_future(start_date='2022-03-01', days=30)
    print(predictions)
    flight_tracker.plot_flight_data()
```
