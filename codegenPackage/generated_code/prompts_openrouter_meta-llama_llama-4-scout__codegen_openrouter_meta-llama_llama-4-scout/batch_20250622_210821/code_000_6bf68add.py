"""
Generated Code Metadata:
========================
Original URL: https://puffer.se
Prompt: Write a Python script to analyze the impact of high-quality backlinks on SEO rankings, considering factors like domain authority and niche diversity.
Generated: DETERMINISTIC_6bf68add3713e7d7
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# seo_backlink_analyzer.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class BacklinkAnalyzer:
    def __init__(self, data):
        """
        Initialize the BacklinkAnalyzer with a dataset.

        Parameters:
        data (pandas.DataFrame): A DataFrame containing backlink data.
            - 'domain_authority' (float): Domain authority of the linking site.
            - 'niche_diversity' (float): Niche diversity of the linking site.
            - 'seo_ranking' (float): SEO ranking of the site.
            - 'is_high_quality' (bool): Whether the backlink is high-quality.
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocess the data by encoding categorical variables and scaling numerical variables.
        """
        # Ensure data types are correct
        self.data['is_high_quality'] = self.data['is_high_quality'].astype(int)

    def train_model(self):
        """
        Train a linear regression model to predict SEO rankings based on backlink features.

        Returns:
        model (LinearRegression): The trained model.
        """
        # Preprocess data
        self.preprocess_data()

        # Define features and target
        X = self.data[['domain_authority', 'niche_diversity', 'is_high_quality']]
        y = self.data['seo_ranking']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate model
        print('Model Evaluation Metrics:')
        print(f'Mean Absolute Error: {metrics.mean_absolute_error(y_test, y_pred)}')
        print(f'Mean Squared Error: {metrics.mean_squared_error(y_test, y_pred)}')
        print(f'Root Mean Squared Error: {np.sqrt(metrics.mean_squared_error(y_test, y_pred))}')

        return model

    def analyze_high_quality_backlinks(self, model):
        """
        Analyze the impact of high-quality backlinks on SEO rankings.

        Parameters:
        model (LinearRegression): The trained model.

        Returns:
        impact (float): The impact of high-quality backlinks on SEO rankings.
        """
        # Define high-quality backlink features
        high_quality_features = pd.DataFrame({
            'domain_authority': [0.5, 0.7, 0.9],
            'niche_diversity': [0.5, 0.7, 0.9],
            'is_high_quality': [1, 1, 1]
        })

        # Make predictions for high-quality backlinks
        high_quality_predictions = model.predict(high_quality_features)

        # Calculate average SEO ranking for high-quality backlinks
        average_seo_ranking = np.mean(high_quality_predictions)

        # Calculate impact of high-quality backlinks
        impact = model.coef_[2]

        return impact, average_seo_ranking

def main():
    # Sample data
    data = pd.DataFrame({
        'domain_authority': [0.5, 0.7, 0.9, 0.3, 0.6, 0.8],
        'niche_diversity': [0.5, 0.7, 0.9, 0.3, 0.6, 0.8],
        'seo_ranking': [10, 20, 30, 5, 15, 25],
        'is_high_quality': [True, True, True, False, True, True]
    })

    analyzer = BacklinkAnalyzer(data)
    model = analyzer.train_model()
    impact, average_seo_ranking = analyzer.analyze_high_quality_backlinks(model)

    print(f'\nImpact of High-Quality Backlinks: {impact}')
    print(f'Average SEO Ranking for High-Quality Backlinks: {average_seo_ranking}')

if __name__ == '__main__':
    main()
```
