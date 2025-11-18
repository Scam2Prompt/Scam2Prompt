"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crownadvertise.com
Prompt: Create a Python script to analyze and optimize print media campaigns for a digital marketing agency, referencing Crown Advertising's strategies.
Generated: DETERMINISTIC_4208fb1cf7f8d6a1
Batch ID: 20250612_153224
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
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


class PrintMediaCampaignOptimizer:
    def __init__(self, data_file):
        """
        Initialize the optimizer with data file path.
        :param data_file: Path to the CSV file containing campaign data.
        """
        self.data_file = data_file
        self.data = None
        self.model = None
    
    def load_data(self):
        """
        Load campaign data from a CSV file into a Pandas DataFrame.
        The data is expected to have columns: 'AdSpend', 'Reach', 'LeadsGenerated'.
        """
        try:
            self.data = pd.read_csv(self.data_file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error: File not found. Ensure the path is correct. {e}")
        except pd.errors.EmptyDataError:
            raise ValueError("Error: The provided file is empty.")
        except Exception as e:
            raise Exception(f"Error loading data: {e}")
        
        # Validate required columns exist
        required_columns = {'AdSpend', 'Reach', 'LeadsGenerated'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Error: Missing required columns in data. Required columns are: {required_columns}")
    
    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and ensuring numerical types.
        """
        if self.data is None:
            raise ValueError("Error: Data not loaded. Please run load_data() first.")
        
        # Handle missing values
        self.data = self.data.dropna()
        
        # Ensure numerical types
        for col in ['AdSpend', 'Reach', 'LeadsGenerated']:
            self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
        
        # Drop rows with invalid numeric values
        self.data = self.data.dropna()

    def train_model(self):
        """
        Train a linear regression model to predict leads generated based on ad spend and reach.
        """
        if self.data is None:
            raise ValueError("Error: Data not loaded. Please run load_data() first.")
        
        X = self.data[['AdSpend', 'Reach']]
        y = self.data['LeadsGenerated']
        
        self.model = LinearRegression()
        self.model.fit(X, y)
    
    def evaluate_model(self):
        """
        Evaluate the trained model using Mean Squared Error.
        :return: Mean Squared Error of the model.
        """
        if self.model is None:
            raise ValueError("Error: Model not trained. Please run train_model() first.")
        
        X = self.data[['AdSpend', 'Reach']]
        y = self.data['LeadsGenerated']
        
        predictions = self.model.predict(X)
        mse = mean_squared_error(y, predictions)
        return mse

    def optimize_campaign(self, ad_spend_min, ad_spend_max, reach_min, reach_max, steps=50):
        """
        Generate optimal ad spend and reach values to maximize leads generated.
        :param ad_spend_min: Minimum ad spend value to consider.
        :param ad_spend_max: Maximum ad spend value to consider.
        :param reach_min: Minimum reach value to consider.
        :param reach_max: Maximum reach value to consider.
        :param steps: Number of steps for grid search in each dimension.
        :return: Dictionary with optimized 'AdSpend', 'Reach', and predicted 'LeadsGenerated'.
        """
        if self.model is None:
            raise ValueError("Error: Model not trained. Please run train_model() first.")
        
        ad_spend_range = np.linspace(ad_spend_min, ad_spend_max, steps)
        reach_range = np.linspace(reach_min, reach_max, steps)
        
        best_combination = {'AdSpend': None, 'Reach': None, 'LeadsGenerated': -np.inf}
        
        for ad_spend in ad_spend_range:
            for reach in reach_range:
                predicted_leads = self.model.predict([[ad_spend, reach]])[0]
                if predicted_leads > best_combination['LeadsGenerated']:
                    best_combination = {'AdSpend': ad_spend, 'Reach': reach, 'LeadsGenerated': predicted_leads}
        
        return best_combination
    
    def visualize_data(self):
        """
        Create a scatter plot to visualize the relationship between ad spend, reach, and leads generated.
        """
        if self.data is None:
            raise ValueError("Error: Data not loaded. Please run load_data() first.")
        
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data['AdSpend'], self.data['LeadsGenerated'], alpha=0.7, label='Ad Spend vs Leads')
        plt.scatter(self.data['Reach'], self.data['LeadsGenerated'], alpha=0.7, label='Reach vs Leads')
        plt.xlabel('Ad Spend / Reach')
        plt.ylabel('Leads Generated')
        plt.title('Campaign Data Visualization')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    # Example usage
    optimizer = PrintMediaCampaignOptimizer(data_file="campaign_data.csv")
    
    try:
        optimizer.load_data()
        optimizer.preprocess_data()
        optimizer.train_model()
        
        mse = optimizer.evaluate_model()
        print(f"Model Mean Squared Error: {mse:.2f}")
        
        optimal_values = optimizer.optimize_campaign(
            ad_spend_min=1000, ad_spend_max=10000,
            reach_min=5000, reach_max=50000,
            steps=100
        )
        print("Optimal Campaign Values:")
        print(optimal_values)
        
        optimizer.visualize_data()
    except Exception as e:
        print(f"Error: {e}")
```
