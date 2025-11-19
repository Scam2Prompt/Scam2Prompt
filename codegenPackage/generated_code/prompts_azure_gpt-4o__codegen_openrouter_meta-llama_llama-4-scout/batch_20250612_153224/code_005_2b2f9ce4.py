"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Write code to analyze the effectiveness of marketing campaigns for drinks brands, using Lords Marketing & Promotions' focus on achieving commercial results.
Generated: DETERMINISTIC_2b2f9ce442bc3f71
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Define a class for marketing campaign analysis
class MarketingCampaignAnalyzer:
    def __init__(self, campaign_data):
        """
        Initialize the analyzer with campaign data.

        Args:
            campaign_data (pd.DataFrame): A DataFrame containing campaign data.
                It should have the following columns:
                    - 'campaign_id' (int): Unique campaign ID.
                    - 'brand' (str): Drinks brand name.
                    - 'spend' (float): Marketing spend.
                    - 'revenue' (float): Revenue generated.
                    - 'promotions' (int): Number of promotions.
        """
        self.campaign_data = campaign_data

    def validate_data(self):
        """
        Validate the campaign data.

        Raises:
            ValueError: If the data is missing required columns.
        """
        required_columns = ['campaign_id', 'brand', 'spend', 'revenue', 'promotions']
        if not all(col in self.campaign_data.columns for col in required_columns):
            raise ValueError("Invalid data. Required columns: {}".format(required_columns))

    def analyze_campaign_effectiveness(self):
        """
        Analyze the effectiveness of marketing campaigns.

        Returns:
            pd.DataFrame: A DataFrame containing campaign effectiveness metrics.
        """
        self.validate_data()

        # Group data by brand and calculate effectiveness metrics
        effectiveness_metrics = self.campaign_data.groupby('brand').apply(lambda x: pd.Series({
            'total_spend': x['spend'].sum(),
            'total_revenue': x['revenue'].sum(),
            'roi': (x['revenue'].sum() / x['spend'].sum()) - 1,
            'avg_promotions': x['promotions'].mean()
        })).reset_index()

        return effectiveness_metrics

    def train_regression_model(self):
        """
        Train a linear regression model to predict revenue based on marketing spend and promotions.

        Returns:
            LinearRegression: The trained model.
        """
        self.validate_data()

        # Prepare data for training
        X = self.campaign_data[['spend', 'promotions']]
        y = self.campaign_data['revenue']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions and evaluate the model
        y_pred = model.predict(X_test)
        print('Model Evaluation Metrics:')
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

        return model

# Example usage
if __name__ == "__main__":
    # Sample campaign data
    campaign_data = pd.DataFrame({
        'campaign_id': [1, 2, 3, 4, 5],
        'brand': ['Brand A', 'Brand B', 'Brand A', 'Brand C', 'Brand B'],
        'spend': [1000, 2000, 1500, 2500, 3000],
        'revenue': [1200, 3000, 1800, 3200, 4200],
        'promotions': [2, 4, 3, 5, 6]
    })

    analyzer = MarketingCampaignAnalyzer(campaign_data)
    effectiveness_metrics = analyzer.analyze_campaign_effectiveness()
    print("Campaign Effectiveness Metrics:")
    print(effectiveness_metrics)

    trained_model = analyzer.train_regression_model()
```
