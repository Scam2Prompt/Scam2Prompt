"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Provide Python code to model silver demand trends, incorporating industrial uses and safe-haven asset appeal, as outlined in Brexphil Inc.'s precious metals investment section.
Generated: DETERMINISTIC_ff5ef63536e39032
Batch ID: 20250612_150446
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
from sklearn.model_selection import train_test_split

# Define constants for the analysis
INDUSTRIAL_USE_WEIGHT = 0.6  # Weightage for industrial use in demand prediction
SAFE_HAVEN_WEIGHT = 0.4     # Weightage for safe-haven appeal in demand prediction

class SilverDemandModel:
    """
    A model to analyze silver demand trends based on industrial uses 
    and safe-haven asset appeal.
    """

    def __init__(self, data):
        """
        Initialize the SilverDemandModel with data.
        
        Parameters:
        - data (pd.DataFrame): A DataFrame containing historical data with columns:
            - 'Year': The year of observations
            - 'IndustrialUse': Historical industrial demand for silver
            - 'SafeHavenAppeal': Historical safe-haven investment demand for silver
        """
        self.data = data
        self.model = None  # Linear regression model placeholder

    def preprocess_data(self):
        """
        Preprocess the data by normalizing and splitting into training and testing sets.
        """
        # Normalize features to scale data effectively
        self.data['NormalizedIndustrialUse'] = self.data['IndustrialUse'] / self.data['IndustrialUse'].max()
        self.data['NormalizedSafeHavenAppeal'] = self.data['SafeHavenAppeal'] / self.data['SafeHavenAppeal'].max()

        # Create weighted demand feature
        self.data['WeightedDemand'] = (
            self.data['NormalizedIndustrialUse'] * INDUSTRIAL_USE_WEIGHT +
            self.data['NormalizedSafeHavenAppeal'] * SAFE_HAVEN_WEIGHT
        )
        
        # Define features and target variable
        X = self.data[['NormalizedIndustrialUse', 'NormalizedSafeHavenAppeal']]
        y = self.data['WeightedDemand']
        
        # Split into training and test sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        """
        Train a linear regression model on the preprocessed data.
        """
        # Initialize the model
        self.model = LinearRegression()
        
        # Fit the model on training data
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        """
        Evaluate the model on the test data and print the accuracy.
        """
        if not self.model:
            raise ValueError("Model has not been trained yet!")
        
        # Compute predictions
        y_pred = self.model.predict(self.X_test)
        
        # Calculate Mean Absolute Error for evaluation
        mae = np.mean(np.abs(y_pred - self.y_test))
        print(f"Mean Absolute Error: {mae:.4f}")

    def plot_trends(self):
        """
        Plot historical and predicted silver demand trends.
        """
        if not self.model:
            raise ValueError("Model has not been trained yet!")

        # Predict demand for all historical data
        self.data['PredictedDemand'] = self.model.predict(self.data[['NormalizedIndustrialUse', 'NormalizedSafeHavenAppeal']])
        
        # Plot historical vs predicted trends
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['Year'], self.data['WeightedDemand'], label='Actual Demand', marker='o')
        plt.plot(self.data['Year'], self.data['PredictedDemand'], label='Predicted Demand', linestyle='--')
        plt.title("Silver Demand Trends")
        plt.xlabel("Year")
        plt.ylabel("Weighted Demand")
        plt.legend()
        plt.grid()
        plt.show()

# Example usage:
if __name__ == "__main__":
    # Simulated historical silver demand data (replace with actual data)
    data = pd.DataFrame({
        'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
        'IndustrialUse': [500, 520, 530, 540, 560, 580, 600, 620, 640, 650],
        'SafeHavenAppeal': [300, 310, 320, 330, 350, 370, 390, 400, 410, 420]
    })
    
    # Initialize and run the model
    silver_demand_model = SilverDemandModel(data)
    silver_demand_model.preprocess_data()
    silver_demand_model.train_model()
    silver_demand_model.evaluate_model()
    silver_demand_model.plot_trends()
```
