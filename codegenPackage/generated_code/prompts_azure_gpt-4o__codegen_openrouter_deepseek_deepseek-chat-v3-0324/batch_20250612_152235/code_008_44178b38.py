"""
Generated Code Metadata:
========================
Original URL: https://moonmouse.pages.dev
Prompt: Generate code to analyze Moon Mouse's partnerships data and visualize the impact of each partner on the token's projected growth.
Generated: DETERMINISTIC_44178b38c1f3de0e
Batch ID: 20250612_152235
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
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

class PartnershipAnalyzer:
    """
    A class to analyze and visualize the impact of partnerships on token growth.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with partnership data.
        
        Args:
            data_path (str): Path to the CSV file containing partnership data
        """
        self.data = pd.read_csv(data_path)
        self._preprocess_data()
        self.model = None
        
    def _preprocess_data(self):
        """
        Clean and preprocess the partnership data.
        """
        # Convert dates to datetime
        if 'partnership_date' in self.data.columns:
            self.data['partnership_date'] = pd.to_datetime(self.data['partnership_date'])
        
        # Fill missing values
        self.data.fillna({
            'partner_size': 0,
            'marketing_budget': 0,
            'projected_growth_impact': 0
        }, inplace=True)
        
        # Calculate days since partnership
        if 'partnership_date' in self.data.columns:
            latest_date = self.data['partnership_date'].max()
            self.data['days_since_partnership'] = (latest_date - self.data['partnership_date']).dt.days
        
    def train_growth_model(self):
        """
        Train a linear regression model to predict growth impact based on partnership features.
        """
        # Features and target
        features = ['partner_size', 'marketing_budget', 'days_since_partnership']
        X = self.data[features]
        y = self.data['projected_growth_impact']
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model trained with MSE: {mse:.2f}, R2: {r2:.2f}")
        
    def visualize_partnership_impact(self):
        """
        Create visualizations showing partnership impact on token growth.
        """
        plt.figure(figsize=(15, 10))
        
        # Partner size vs growth impact
        plt.subplot(2, 2, 1)
        sns.scatterplot(data=self.data, x='partner_size', y='projected_growth_impact', hue='partner_type')
        plt.title('Partner Size vs Growth Impact')
        plt.xlabel('Partner Size (log scale)')
        plt.ylabel('Projected Growth Impact (%)')
        plt.xscale('log')
        
        # Marketing budget vs growth impact
        plt.subplot(2, 2, 2)
        sns.scatterplot(data=self.data, x='marketing_budget', y='projected_growth_impact', hue='partner_type')
        plt.title('Marketing Budget vs Growth Impact')
        plt.xlabel('Marketing Budget (log scale)')
        plt.ylabel('Projected Growth Impact (%)')
        plt.xscale('log')
        
        # Time since partnership vs growth impact
        if 'days_since_partnership' in self.data.columns:
            plt.subplot(2, 2, 3)
            sns.lineplot(data=self.data, x='days_since_partnership', y='projected_growth_impact', 
                         hue='partner_type', ci=None)
            plt.title('Time Since Partnership vs Growth Impact')
            plt.xlabel('Days Since Partnership')
            plt.ylabel('Projected Growth Impact (%)')
        
        # Partner type distribution
        plt.subplot(2, 2, 4)
        partner_counts = self.data['partner_type'].value_counts()
        plt.pie(partner_counts, labels=partner_counts.index, autopct='%1.1f%%')
        plt.title('Partner Type Distribution')
        
        plt.tight_layout()
        plt.show()
        
    def predict_growth_impact(self, partner_size, marketing_budget, days_since_partnership):
        """
        Predict growth impact for a new partnership.
        
        Args:
            partner_size (float): Size of the partner organization
            marketing_budget (float): Marketing budget allocated
            days_since_partnership (int): Days since partnership began
            
        Returns:
            float: Predicted growth impact percentage
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_growth_model() first.")
            
        features = np.array([[partner_size, marketing_budget, days_since_partnership]])
        return self.model.predict(features)[0]

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with sample data
        analyzer = PartnershipAnalyzer('partnership_data.csv')
        
        # Train growth prediction model
        analyzer.train_growth_model()
        
        # Visualize partnership impacts
        analyzer.visualize_partnership_impact()
        
        # Example prediction
        prediction = analyzer.predict_growth_impact(
            partner_size=1000,
            marketing_budget=50000,
            days_since_partnership=30
        )
        print(f"Predicted growth impact: {prediction:.2f}%")
        
    except FileNotFoundError:
        print("Error: Partnership data file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
