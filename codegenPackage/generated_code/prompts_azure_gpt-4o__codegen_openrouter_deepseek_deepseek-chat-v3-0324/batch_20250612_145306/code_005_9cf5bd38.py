"""
Generated Code Metadata:
========================
Original URL: https://shift4strategy.com
Prompt: Write a script to model marketing and sales strategies for a CBD company, inspired by SHIFT4's success in transforming such businesses.
Generated: DETERMINISTIC_9cf5bd38fd598e5d
Batch ID: 20250612_145306
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class CBDSalesStrategyModel:
    """
    A class to model and analyze marketing and sales strategies for a CBD company.
    Inspired by SHIFT4's approach to transforming CBD businesses.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the model with optional data path.
        If no data is provided, generates synthetic data for demonstration.
        """
        if data_path:
            self.data = pd.read_csv(data_path)
        else:
            self.data = self._generate_synthetic_data()
        
        self.model = None
        self.features = None
        self.target = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
    
    def _generate_synthetic_data(self):
        """
        Generate synthetic sales data for demonstration purposes.
        """
        np.random.seed(42)
        num_days = 365
        start_date = datetime(2023, 1, 1)
        
        dates = [start_date + timedelta(days=i) for i in range(num_days)]
        days_of_week = [date.weekday() for date in dates]
        is_weekend = [1 if day >= 5 else 0 for day in days_of_week]
        
        data = pd.DataFrame({
            'date': dates,
            'day_of_week': days_of_week,
            'is_weekend': is_weekend,
            'google_ads_spend': np.random.normal(500, 100, num_days).clip(300, 700),
            'facebook_ads_spend': np.random.normal(400, 80, num_days).clip(200, 600),
            'email_campaigns': np.random.poisson(3, num_days),
            'influencer_marketing': np.random.binomial(1, 0.3, num_days),
            'discount_pct': np.random.uniform(0, 0.2, num_days),
            'competitor_price_index': np.random.normal(1.0, 0.1, num_days),
            'website_traffic': np.random.poisson(2000, num_days),
            'conversion_rate': np.random.beta(5, 100, num_days),
            'sales': None
        })
        
        # Simulate sales based on marketing inputs
        coefficients = {
            'google_ads_spend': 0.8,
            'facebook_ads_spend': 0.6,
            'email_campaigns': 50,
            'influencer_marketing': 200,
            'discount_pct': 1000,
            'competitor_price_index': -500,
            'website_traffic': 0.2,
            'conversion_rate': 3000,
            'is_weekend': 150
        }
        
        noise = np.random.normal(0, 200, num_days)
        data['sales'] = (
            data['google_ads_spend'] * coefficients['google_ads_spend'] +
            data['facebook_ads_spend'] * coefficients['facebook_ads_spend'] +
            data['email_campaigns'] * coefficients['email_campaigns'] +
            data['influencer_marketing'] * coefficients['influencer_marketing'] +
            data['discount_pct'] * coefficients['discount_pct'] +
            data['competitor_price_index'] * coefficients['competitor_price_index'] +
            data['website_traffic'] * coefficients['website_traffic'] +
            data['conversion_rate'] * coefficients['conversion_rate'] +
            data['is_weekend'] * coefficients['is_weekend'] +
            noise
        ).clip(0)
        
        return data
    
    def preprocess_data(self):
        """
        Prepare data for modeling by selecting features and target,
        and splitting into training and test sets.
        """
        self.features = [
            'google_ads_spend',
            'facebook_ads_spend',
            'email_campaigns',
            'influencer_marketing',
            'discount_pct',
            'competitor_price_index',
            'website_traffic',
            'conversion_rate',
            'is_weekend'
        ]
        
        self.target = 'sales'
        
        X = self.data[self.features]
        y = self.data[self.target]
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
    
    def train_model(self):
        """
        Train a linear regression model on the prepared data.
        """
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
    
    def evaluate_model(self):
        """
        Evaluate the trained model on test data and return metrics.
        """
        if not self.model:
            raise ValueError("Model has not been trained yet.")
        
        y_pred = self.model.predict(self.X_test)
        
        mse = mean_squared_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        
        return {
            'mse': mse,
            'rmse': np.sqrt(mse),
            'r2': r2
        }
    
    def plot_feature_importance(self):
        """
        Plot the feature importance based on model coefficients.
        """
        if not self.model:
            raise ValueError("Model has not been trained yet.")
        
        importance = pd.DataFrame({
            'feature': self.features,
            'coefficient': self.model.coef_
        }).sort_values('coefficient', ascending=False)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x='coefficient', y='feature', data=importance)
        plt.title('Feature Importance for CBD Sales')
        plt.xlabel('Coefficient Value')
        plt.ylabel('Feature')
        plt.tight_layout()
        plt.show()
    
    def optimize_marketing_mix(self, budget_constraint=1000):
        """
        Optimize marketing spend allocation given a budget constraint.
        Returns the optimal allocation for maximum sales.
        """
        if not self.model:
            raise ValueError("Model has not been trained yet.")
        
        from scipy.optimize import minimize
        
        # Get coefficients for marketing channels
        coef_dict = dict(zip(self.features, self.model.coef_))
        
        # Define objective function to maximize sales
        def objective(x):
            google, facebook, email, influencer = x
            return -(
                google * coef_dict['google_ads_spend'] +
                facebook * coef_dict['facebook_ads_spend'] +
                email * coef_dict['email_campaigns'] +
                influencer * coef_dict['influencer_marketing']
            )
        
        # Constraints
        constraints = (
            {'type': 'ineq', 'fun': lambda x: budget_constraint - sum(x)},  # Budget constraint
            {'type': 'ineq', 'fun': lambda x: x[0]},  # Google ads >= 0
            {'type': 'ineq', 'fun': lambda x: x[1]},  # Facebook ads >= 0
            {'type': 'ineq', 'fun': lambda x: x[2]},  # Email campaigns >= 0
            {'type': 'ineq', 'fun': lambda x: x[3]}   # Influencer marketing >= 0
        )
        
        # Initial guess (equal distribution)
        x0 = [budget_constraint/4] * 4
        
        # Optimize
        result = minimize(objective, x0, method='SLSQP', constraints=constraints)
        
        if not result.success:
            raise RuntimeError("Optimization failed to converge.")
        
        optimal_allocation = {
            'google_ads_spend': result.x[0],
            'facebook_ads_spend': result.x[1],
            'email_campaigns': result.x[2],
            'influencer_marketing': result.x[3]
        }
        
        return optimal_allocation
    
    def forecast_sales(self, future_days=30):
        """
        Forecast sales for future days based on current trends.
        """
        if not self.model:
            raise ValueError("Model has not been trained yet.")
        
        last_date = self.data['date'].max()
        future_dates = [last_date + timedelta(days=i) for i in range(1, future_days+1)]
        days_of_week = [date.weekday() for date in future_dates]
        is_weekend = [1 if day >= 5 else 0 for day in days_of_week]
        
        # Create future dataframe with average values for other features
        future_data = pd.DataFrame({
            'date': future_dates,
