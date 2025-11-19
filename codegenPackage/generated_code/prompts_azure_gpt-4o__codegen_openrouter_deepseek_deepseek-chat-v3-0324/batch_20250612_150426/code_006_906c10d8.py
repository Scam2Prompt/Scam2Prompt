"""
Generated Code Metadata:
========================
Original URL: https://finveracapitals.com
Prompt: Generate Python code to forecast market trends using historical data, similar to the analysis and forecasting mentioned on Finvera Capitals' website.
Generated: DETERMINISTIC_906c10d8a1261638
Batch ID: 20250612_150426
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
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
warnings.filterwarnings('ignore')

class MarketTrendForecaster:
    """
    A class for forecasting market trends using historical data.
    Supports both machine learning (Random Forest) and time series (ARIMA/SARIMAX) approaches.
    """
    
    def __init__(self, data_path=None, df=None):
        """
        Initialize the forecaster with either a file path or DataFrame.
        
        Args:
            data_path (str, optional): Path to CSV file containing historical data
            df (pd.DataFrame, optional): DataFrame containing historical data
        """
        if data_path:
            self.data = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')
        elif df is not None:
            self.data = df
        else:
            raise ValueError("Either data_path or df must be provided")
            
        self.scaler = MinMaxScaler()
        self.model = None
        self.model_type = None
        
    def preprocess_data(self, target_column, feature_columns=None, test_size=0.2):
        """
        Preprocess data for machine learning models.
        
        Args:
            target_column (str): Name of the target column to predict
            feature_columns (list, optional): List of feature columns. If None, uses all except target.
            test_size (float): Proportion of data to use for testing (0-1)
            
        Returns:
            tuple: (X_train, X_test, y_train, y_test)
        """
        if feature_columns is None:
            feature_columns = [col for col in self.data.columns if col != target_column]
            
        # Handle missing values
        self.data = self.data.dropna()
        
        # Scale features
        features = self.data[feature_columns]
        target = self.data[target_column]
        
        scaled_features = self.scaler.fit_transform(features)
        
        # Split into train/test
        X_train, X_test, y_train, y_test = train_test_split(
            scaled_features, target, test_size=test_size, shuffle=False
        )
        
        return X_train, X_test, y_train, y_test
    
    def train_random_forest(self, target_column, feature_columns=None, n_estimators=100, test_size=0.2):
        """
        Train a Random Forest model for market trend forecasting.
        
        Args:
            target_column (str): Name of the target column to predict
            feature_columns (list, optional): List of feature columns
            n_estimators (int): Number of trees in the forest
            test_size (float): Proportion of data to use for testing (0-1)
        """
        self.model_type = 'random_forest'
        
        X_train, X_test, y_train, y_test = self.preprocess_data(
            target_column, feature_columns, test_size
        )
        
        self.model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        mae = mean_absolute_error(y_test, predictions)
        
        print(f"Random Forest Model Evaluation:")
        print(f"Mean Squared Error: {mse:.4f}")
        print(f"Mean Absolute Error: {mae:.4f}")
        
    def train_arima(self, target_column, order=(1,1,1)):
        """
        Train an ARIMA model for time series forecasting.
        
        Args:
            target_column (str): Name of the target column to predict
            order (tuple): (p,d,q) order of the ARIMA model
        """
        self.model_type = 'arima'
        self.target_column = target_column
        
        # Fit ARIMA model
        self.model = ARIMA(self.data[target_column], order=order)
        self.model = self.model.fit()
        
        print(self.model.summary())
        
    def train_sarimax(self, target_column, order=(1,1,1), seasonal_order=(1,1,1,12)):
        """
        Train a SARIMAX model for time series forecasting with seasonality.
        
        Args:
            target_column (str): Name of the target column to predict
            order (tuple): (p,d,q) order of the model
            seasonal_order (tuple): (P,D,Q,s) seasonal order of the model
        """
        self.model_type = 'sarimax'
        self.target_column = target_column
        
        # Fit SARIMAX model
        self.model = SARIMAX(
            self.data[target_column],
            order=order,
            seasonal_order=seasonal_order,
            enforce_stationarity=False,
            enforce_invertibility=False
        )
        self.model = self.model.fit(disp=False)
        
        print(self.model.summary())
        
    def forecast(self, steps=5):
        """
        Generate forecasts using the trained model.
        
        Args:
            steps (int): Number of periods to forecast ahead
            
        Returns:
            pd.Series: Forecasted values with dates as index
        """
        if self.model is None:
            raise ValueError("No model has been trained. Call train_* method first.")
            
        if self.model_type in ['arima', 'sarimax']:
            # Time series forecasting
            forecast = self.model.get_forecast(steps=steps)
            forecast_values = forecast.predicted_mean
            conf_int = forecast.conf_int()
            
            # Create date index for future periods
            last_date = self.data.index[-1]
            freq = pd.infer_freq(self.data.index)
            future_dates = pd.date_range(
                start=last_date,
                periods=steps + 1,
                freq=freq
            )[1:]
            
            forecast_df = pd.DataFrame({
                'Forecast': forecast_values,
                'Lower CI': conf_int.iloc[:, 0],
                'Upper CI': conf_int.iloc[:, 1]
            }, index=future_dates)
            
            return forecast_df
            
        elif self.model_type == 'random_forest':
            # For ML models, we can't forecast into the future without features
            raise NotImplementedError(
                "For Random Forest, use predict() with new feature data instead of forecast()"
            )
            
    def plot_forecast(self, steps=5):
        """
        Plot historical data and forecast.
        
        Args:
            steps (int): Number of periods to forecast ahead
        """
        if self.model_type not in ['arima', 'sarimax']:
            raise ValueError("Plotting only supported for ARIMA/SARIMAX models")
            
        forecast_df = self.forecast(steps=steps)
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data[self.target_column], label='Historical')
        plt.plot(forecast_df.index, forecast_df['Forecast'], label='Forecast', color='red')
        plt.fill_between(
            forecast_df.index,
            forecast_df['Lower CI'],
            forecast_df['Upper CI'],
            color='pink',
            alpha=0.3
        )
        plt.title(f'Market Trend Forecast - {self.target_column}')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def predict(self, new_data):
        """
        Make predictions using the trained model on new feature data.
        
        Args:
            new_data (pd.DataFrame): New data with same features as training data
            
        Returns:
            np.array: Predicted values
        """
        if self.model_type != 'random_forest':
            raise ValueError("predict() is only for Random Forest models. Use forecast() for time series models.")
            
        if not isinstance(new_data, pd.DataFrame):
            raise ValueError("new_data must be a pandas DataFrame")
            
        # Scale features using the same scaler as training
        scaled_features = self.scaler.transform(new_data)
        return self.model.predict(scaled_features)

# Example usage
if __name__ == "__main__":
    # Example with synthetic data
    dates = pd.date_range(start='2020-01-01', periods=100, freq='M')
    values = np.cumsum(np.random.normal(0, 1, size=100)) + 100
    volumes = np.random.randint(100, 1000, size=100)
    
    data = pd.DataFrame({
        'Date': dates,
        'Price': values,
        'Volume': volumes
    }).set_index('Date')
    
    # Initialize forecaster
    forecaster = MarketTrendForecaster(df=data)
    
    # Time series approach
    print("\nTraining ARIMA model...")
    forecaster.train_arima(target_column='Price', order=(1,1,1))
    forecast = forecaster.forecast(steps=12)
    print("\nARIMA Forecast:")
    print(forecast)
    forecaster
