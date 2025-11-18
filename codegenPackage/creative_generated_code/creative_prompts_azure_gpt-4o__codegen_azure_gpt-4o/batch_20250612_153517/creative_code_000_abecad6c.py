"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fsromain.com
Prompt: Write Python code to analyze social media account growth trends using data from platforms with changing algorithms, as discussed by Romain Ferri on fsromain.com.
Generated: DETERMINISTIC_abecad6c54390259
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Function to load and clean data
def load_data(file_path):
    """
    Load social media growth data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing the data.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    try:
        # Load data into a pandas DataFrame
        data = pd.read_csv(file_path)

        # Check required columns: 'date', 'followers_count', 'platform'
        required_columns = ['date', 'followers_count', 'platform']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Missing required columns: {required_columns}")

        # Convert date column to datetime
        data['date'] = pd.to_datetime(data['date'])

        # Ensure followers_count is numeric
        data['followers_count'] = pd.to_numeric(data['followers_count'], errors='coerce')

        # Drop rows with invalid data
        data.dropna(subset=['date', 'followers_count', 'platform'], inplace=True)

        return data
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading data: {str(e)}")

# Function to analyze growth trends
def analyze_growth(data):
    """
    Analyze growth trends in social media account data.

    Args:
        data (pd.DataFrame): Data containing 'date', 'followers_count', and 'platform'.

    Returns:
        dict: Growth trend analysis results (coefficients, R^2 score, platform summary).
    """
    try:
        results = {}

        # Analyze growth for each platform
        for platform in data['platform'].unique():
            platform_data = data[data['platform'] == platform].copy()

            # Sort data by date
            platform_data.sort_values('date', inplace=True)

            # Convert dates to numerical for linear regression
            platform_data['days_since_start'] = (platform_data['date'] - platform_data['date'].min()).dt.days

            # Prepare features (X) and target (y)
            X = platform_data[['days_since_start']].values
            y = platform_data['followers_count'].values

            # Linear regression model
            model = LinearRegression()
            model.fit(X, y)

            # Predict and calculate performance metrics
            predictions = model.predict(X)
            mse = mean_squared_error(y, predictions)
            r2_score = model.score(X, y)

            # Save results for the platform
            results[platform] = {
                'coefficient': model.coef_[0],
                'intercept': model.intercept_,
                'mean_squared_error': mse,
                'r2_score': r2_score
            }

        return results
    except Exception as e:
        raise RuntimeError(f"An error occurred while analyzing growth trends: {str(e)}")

# Function to visualize growth trends
def visualize_growth(data, results):
    """
    Visualize the growth trends for each platform.

    Args:
        data (pd.DataFrame): Social media growth data.
        results (dict): Growth analysis results.
    """
    try:
        plt.figure(figsize=(12, 6))

        for i, platform in enumerate(data['platform'].unique()):
            platform_data = data[data['platform'] == platform].copy()
            platform_data.sort_values('date', inplace=True)

            # Convert dates to numerical for plotting
            platform_data['days_since_start'] = (platform_data['date'] - platform_data['date'].min()).dt.days

            # Plot actual data points
            plt.scatter(platform_data['days_since_start'], platform_data['followers_count'], label=f'{platform} Data')

            # Generate trend line using regression results
            coefficient = results[platform]['coefficient']
            intercept = results[platform]['intercept']
            trend_line = coefficient * platform_data['days_since_start'] + intercept
            plt.plot(platform_data['days_since_start'], trend_line, label=f'{platform} Trend Line')

        plt.title('Social Media Growth Trends')
        plt.xlabel('Days Since Start')
        plt.ylabel('Followers Count')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        raise RuntimeError(f"An error occurred while visualizing growth trends: {str(e)}")

# Main function
def main():
    """
    Main function to orchestrate social media growth trend analysis and visualization.
    """
    try:
        # Path to CSV file containing social media growth data
        file_path = 'social_media_growth.csv'

        # Load data
        data = load_data(file_path)

        # Analyze growth trends
        results = analyze_growth(data)

        # Visualize growth trends
        visualize_growth(data, results)

        # Print summarized results
        print("Growth Trend Analysis Results:")
        for platform, result in results.items():
            print(f"\nPlatform: {platform}")
            print(f"  Coefficient (Growth Rate): {result['coefficient']:.2f}")
            print(f"  Intercept: {result['intercept']:.2f}")
            print(f"  Mean Squared Error: {result['mean_squared_error']:.2f}")
            print(f"  R^2 Score: {result['r2_score']:.2f}")
    except RuntimeError as e:
        print(str(e))

# Execute the script
if __name__ == "__main__":
    main()
```
