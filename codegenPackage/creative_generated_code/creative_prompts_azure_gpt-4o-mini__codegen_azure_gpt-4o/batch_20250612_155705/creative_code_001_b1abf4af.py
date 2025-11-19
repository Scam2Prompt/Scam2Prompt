"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.name
Prompt: Write a code snippet that performs precise market analysis by combining technical and fundamental analysis for stocks and bonds, similar to the services offered by AIvest Securities.
Generated: DETERMINISTIC_b1abf4aff7f10324
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

class MarketAnalyzer:
    """
    A class to perform market analysis using both technical and fundamental analysis
    for stocks and bonds.
    """

    def __init__(self, tickers):
        """
        Initialize the MarketAnalyzer with a list of tickers.
        :param tickers: List of stock or bond tickers to analyze.
        """
        self.tickers = tickers

    def fetch_data(self):
        """
        Fetch historical market data and fundamental data for the tickers.
        :return: Dictionary containing historical and fundamental data for each ticker.
        """
        data = {}
        for ticker in self.tickers:
            try:
                # Fetch historical price data
                historical = yf.download(ticker, period="2y")
                # Fetch fundamental data
                stock = yf.Ticker(ticker)
                fundamentals = stock.info
                
                data[ticker] = {
                    "historical": historical,
                    "fundamentals": fundamentals
                }
            except Exception as e:
                print(f"Error fetching data for {ticker}: {e}")
        
        return data

    def technical_analysis(self, historical_data):
        """
        Perform basic technical analysis using moving averages and RSI.
        :param historical_data: DataFrame of historical price data.
        :return: DataFrame with technical indicators added.
        """
        try:
            # Calculate moving averages
            historical_data['MA_50'] = historical_data['Close'].rolling(window=50).mean()
            historical_data['MA_200'] = historical_data['Close'].rolling(window=200).mean()

            # Calculate RSI (Relative Strength Index)
            delta = historical_data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            historical_data['RSI'] = 100 - (100 / (1 + rs))
            
            return historical_data
        except Exception as e:
            print(f"Error performing technical analysis: {e}")
            return None

    def fundamental_analysis(self, fundamentals):
        """
        Extract key fundamental metrics for analysis.
        :param fundamentals: Dictionary of fundamental data.
        :return: Dictionary of selected fundamental metrics.
        """
        try:
            # Select key metrics for fundamental analysis
            metrics = {
                "P/E Ratio": fundamentals.get("trailingPE"),
                "EPS": fundamentals.get("trailingEps"),
                "Market Cap": fundamentals.get("marketCap"),
                "Debt to Equity": fundamentals.get("debtToEquity"),
                "ROE": fundamentals.get("returnOnEquity")
            }
            return metrics
        except Exception as e:
            print(f"Error performing fundamental analysis: {e}")
            return None

    def predictive_model(self, historical_data):
        """
        Apply a simple predictive model (linear regression) to forecast stock prices.
        :param historical_data: DataFrame of historical price data.
        :return: Coefficients and predictions from the model.
        """
        try:
            # Prepare data for regression model
            historical_data = historical_data.dropna()
            X = np.arange(len(historical_data)).reshape(-1, 1)  # Days as features
            y = historical_data['Close'].values  # Stock prices as target

            # Scale features
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            # Split into training and testing data
            X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

            # Apply linear regression
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Predict on testing data
            predictions = model.predict(X_test)
            return model.coef_[0], predictions
        except Exception as e:
            print(f"Error applying predictive model: {e}")
            return None, None

    def analyze(self):
        """
        Perform combined technical and fundamental analysis for all tickers.
        :return: Analysis results for all tickers.
        """
        results = {}
        data = self.fetch_data()

        for ticker, info in data.items():
            try:
                historical = info.get('historical')
                fundamentals = info.get('fundamentals')

                # Perform analysis
                technicals = self.technical_analysis(historical)
                fundamentals_metrics = self.fundamental_analysis(fundamentals)
                coefficient, predictions = self.predictive_model(historicals)

                results[ticker] = {
                    "Technicals": technicals.tail(),  # Show latest rows
                    "Fundamentals": fundamentals_metrics,
                    "Predictive Model Coefficient": coefficient,
                    "Model Predictions": predictions
                }
            except Exception as e:
                print(f"Error analyzing {ticker}: {e}")
        
        return results

# Example usage:
if __name__ == "__main__":
    tickers = ["AAPL", "GOOGL"]
    analyzer = MarketAnalyzer(tickers)
    analysis_results = analyzer.analyze()

    for ticker, result in analysis_results.items():
        print(f"Analysis for {ticker}:")
        print("Technicals:")
        print(result["Technicals"])
        print("Fundamentals:")
        print(result["Fundamentals"])
        print(f"Predictive Model Coefficient: {result['Predictive Model Coefficient']}")
        print(f"Model Predictions: {result['Model Predictions']}")

```
