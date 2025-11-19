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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class MarketingCampaignAnalyzer:
    """
    A class to analyze the effectiveness of marketing campaigns for drinks brands.
    Focuses on commercial results as per Lords Marketing & Promotions' approach.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            data_path (str): Path to the CSV file containing campaign data
        """
        self.data_path = data_path
        self.data = None
        self.model = None
        self.scaler = StandardScaler()
        
    def load_data(self):
        """
        Load and preprocess the marketing campaign data.
        
        Returns:
            DataFrame: Processed campaign data
        """
        try:
            # Load data with common marketing campaign metrics
            self.data = pd.read_csv(self.data_path)
            
            # Basic data validation
            if self.data.empty:
                raise ValueError("Empty dataset provided")
                
            # Convert date columns if present
            if 'start_date' in self.data.columns:
                self.data['start_date'] = pd.to_datetime(self.data['start_date'])
            if 'end_date' in self.data.columns:
                self.data['end_date'] = pd.to_datetime(self.data['end_date'])
                
            # Calculate campaign duration if dates are available
            if 'start_date' in self.data.columns and 'end_date' in self.data.columns:
                self.data['duration_days'] = (self.data['end_date'] - self.data['start_date']).dt.days
                
            return self.data
            
        except FileNotFoundError:
            print(f"Error: File not found at {self.data_path}")
            return None
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None
    
    def preprocess_data(self):
        """
        Preprocess the data for analysis by handling missing values,
        encoding categorical variables, and scaling numerical features.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        try:
            # Handle missing values
            self.data.fillna({
                'budget': self.data['budget'].median(),
                'reach': self.data['reach'].median(),
                'sales_increase': 0  # Assume no sales increase if missing
            }, inplace=True)
            
            # Encode categorical variables
            if 'campaign_type' in self.data.columns:
                self.data = pd.get_dummies(self.data, columns=['campaign_type'], drop_first=True)
                
            if 'brand' in self.data.columns:
                self.data = pd.get_dummies(self.data, columns=['brand'], drop_first=True)
                
            # Scale numerical features
            numerical_cols = ['budget', 'reach', 'duration_days'] if 'duration_days' in self.data.columns else ['budget', 'reach']
            self.data[numerical_cols] = self.scaler.fit_transform(self.data[numerical_cols])
            
        except Exception as e:
            print(f"Error during data preprocessing: {str(e)}")
    
    def analyze_campaigns(self, target_metric='sales_increase'):
        """
        Analyze campaign effectiveness using descriptive statistics and visualization.
        
        Args:
            target_metric (str): The metric to analyze (default: 'sales_increase')
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        try:
            # Basic statistics
            print("\n=== Campaign Effectiveness Summary ===")
            print(f"Average {target_metric}: {self.data[target_metric].mean():.2f}")
            print(f"Median {target_metric}: {self.data[target_metric].median():.2f}")
            print(f"Best campaign: {self.data[target_metric].max():.2f}")
            print(f"Worst campaign: {self.data[target_metric].min():.2f}")
            
            # Budget vs Effectiveness
            if 'budget' in self.data.columns:
                plt.figure(figsize=(10, 6))
                sns.scatterplot(x='budget', y=target_metric, data=self.data)
                plt.title('Budget vs Campaign Effectiveness')
                plt.xlabel('Scaled Budget')
                plt.ylabel(target_metric)
                plt.show()
                
            # Duration vs Effectiveness (if available)
            if 'duration_days' in self.data.columns:
                plt.figure(figsize=(10, 6))
                sns.scatterplot(x='duration_days', y=target_metric, data=self.data)
                plt.title('Duration vs Campaign Effectiveness')
                plt.xlabel('Scaled Duration (days)')
                plt.ylabel(target_metric)
                plt.show()
                
            # ROI calculation if cost and revenue data available
            if all(col in self.data.columns for col in ['cost', 'revenue']):
                self.data['roi'] = (self.data['revenue'] - self.data['cost']) / self.data['cost']
                print("\n=== ROI Analysis ===")
                print(f"Average ROI: {self.data['roi'].mean():.2%}")
                print(f"Median ROI: {self.data['roi'].median():.2%}")
                
                plt.figure(figsize=(10, 6))
                sns.histplot(self.data['roi'], bins=20)
                plt.title('Distribution of ROI')
                plt.xlabel('Return on Investment')
                plt.ylabel('Number of Campaigns')
                plt.show()
                
        except Exception as e:
            print(f"Error during campaign analysis: {str(e)}")
    
    def train_effectiveness_model(self, target_metric='sales_increase'):
        """
        Train a machine learning model to predict campaign effectiveness.
        
        Args:
            target_metric (str): The target variable to predict (default: 'sales_increase')
            
        Returns:
            tuple: (model, test_mae, test_r2) if successful, None otherwise
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return None
            
        try:
            # Prepare features and target
            X = self.data.drop(columns=[target_metric, 'start_date', 'end_date'], errors='ignore')
            y = self.data[target_metric]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Train model
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            print("\n=== Model Performance ===")
            print(f"Mean Absolute Error: {mae:.2f}")
            print(f"R-squared Score: {r2:.2f}")
            
            # Feature importance
            feature_importance = pd.DataFrame({
                'feature': X.columns,
                'importance': self.model.feature_importances_
            }).sort_values('importance', ascending=False)
            
            print("\n=== Feature Importance ===")
            print(feature_importance.head(10))
            
            return self.model, mae, r2
            
        except Exception as e:
            print(f"Error during model training: {str(e)}")
            return None
    
    def optimize_budget_allocation(self, total_budget, target_metric='sales_increase'):
        """
        Optimize budget allocation across campaigns to maximize target metric.
        
        Args:
            total_budget (float): Total available budget
            target_metric (str): Metric to optimize for (default: 'sales_increase')
            
        Returns:
            DataFrame: Recommended budget allocation
        """
        if self.model is None:
            print("No trained model available. Please train a model first.")
            return None
            
        try:
            # Create a grid of possible budget allocations
            n_campaigns = len(self.data)
            min_budget = self.data['budget'].min()
            max_budget = self.data['budget'].max()
            
            # Simple proportional allocation based on predicted effectiveness
            X = self.data.drop(columns=[target_metric, 'start_date', 'end_date'], errors='ignore')
            predictions = self.model.predict(X)
            
            # Normalize predictions to get allocation weights
            weights = predictions / predictions.sum()
            allocations = weights * total_budget
            
            # Create recommendation DataFrame
            recommendations = pd.DataFrame({
                'campaign_id': self.data['campaign_id'] if 'campaign_id' in self.data.columns else range(n_campaigns),
                'current_budget': self.data['budget'],
                'recommended_budget': allocations,
                'predicted_effectiveness': predictions
            })
            
            recommendations['budget_change'] = recommendations['recommended
