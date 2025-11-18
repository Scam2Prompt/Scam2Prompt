"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nansenportfolio.app
Prompt: Write Python code to simulate a systematic value investing strategy using rigorous quantitative analysis and AI modeling techniques, as described by Grade World Investment Limited.
Generated: DETERMINISTIC_8637d127055ccd97
Batch ID: 20250612_151605
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
import yfinance as yf

class ValueInvestingStrategy:
    """
    Class to simulate a systematic value investing strategy using AI modeling techniques.
    """
    def __init__(self):
        self.model = RandomForestClassifier(random_state=42)
        self.scaler = StandardScaler()

    def fetch_data(self, ticker_list, start_date, end_date):
        """
        Fetches historical financial data for the given list of stock tickers.
        :param ticker_list: List of stock ticker symbols.
        :param start_date: Start date for historical data.
        :param end_date: End date for historical data.
        :return: DataFrame containing historical data for all tickers.
        """
        try:
            data = {}
            for ticker in ticker_list:
                data[ticker] = yf.download(ticker, start=start_date, end=end_date)
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def preprocess_data(self, data_dict):
        """
        Preprocess financial data for model training.
        :param data_dict: Dictionary containing stock data for multiple tickers.
        :return: Processed DataFrame ready for model training.
        """
        try:
            features = []
            labels = []
            for ticker, df in data_dict.items():
                df['Returns'] = df['Adj Close'].pct_change()
                df['Label'] = np.where(df['Returns'].shift(-1) > 0, 1, 0)  # 1 if next day return > 0, else 0
                df.dropna(inplace=True)

                # Append features & labels for modeling
                for _, row in df.iterrows():
                    features.append([
                        row['Open'], row['High'], row['Low'], row['Close'], row['Volume']
                    ])
                    labels.append(row['Label'])

            # Scale features and return as numpy arrays
            features = self.scaler.fit_transform(features)
            return np.array(features), np.array(labels)
        except Exception as e:
            print(f"Error preprocessing data: {e}")
            return None, None

    def train_model(self, features, labels):
        """
        Trains a Random Forest model on the provided features and labels.
        :param features: Numpy array of feature data.
        :param labels: Numpy array of label data.
        """
        try:
            X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
            self.model.fit(X_train, y_train)
            predictions = self.model.predict(X_test)

            print("Model Training Complete")
            print("Accuracy Score:", accuracy_score(y_test, predictions))
            print("Classification Report:")
            print(classification_report(y_test, predictions))
        except Exception as e:
            print(f"Error training model: {e}")

    def predict(self, features):
        """
        Makes predictions using the trained model.
        :param features: Numpy array of feature data for prediction.
        :return: Numpy array of predictions.
        """
        try:
            return self.model.predict(features)
        except Exception as e:
            print(f"Error during prediction: {e}")
            return None


# Main Function
if __name__ == "__main__":
    try:
        # Define ticker list and date range
        ticker_list = ["AAPL", "MSFT", "GOOG", "AMZN"]
        start_date = "2022-01-01"
        end_date = "2023-01-01"

        # Instantiate the ValueInvestingStrategy class
        strategy = ValueInvestingStrategy()

        # Fetch and preprocess the data
        data_dict = strategy.fetch_data(ticker_list, start_date, end_date)
        if data_dict:
            features, labels = strategy.preprocess_data(data_dict)
            if features is not None and labels is not None:
                # Train and evaluate the model
                strategy.train_model(features, labels)
    except Exception as main_error:
        print(f"An error occurred in the main function: {main_error}")
```
