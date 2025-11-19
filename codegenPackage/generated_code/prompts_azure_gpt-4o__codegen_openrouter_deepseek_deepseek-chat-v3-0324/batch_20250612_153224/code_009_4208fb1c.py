"""
Generated Code Metadata:
========================
Original URL: https://crownadvertise.com
Prompt: Create a Python script to analyze and optimize print media campaigns for a digital marketing agency, referencing Crown Advertising's strategies.
Generated: DETERMINISTIC_4208fb1cf7f8d6a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Print Media Campaign Analyzer and Optimizer
Inspired by Crown Advertising's strategies for digital marketing agencies.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import warnings
import logging
import json
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('campaign_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Suppress sklearn warnings
warnings.filterwarnings('ignore', category=UserWarning)

class PrintMediaAnalyzer:
    """
    A class to analyze and optimize print media campaigns.
    """
    
    def __init__(self, data_file=None):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            data_file (str): Path to CSV file containing campaign data
        """
        self.data = None
        self.model = None
        self.features = None
        self.target = None
        
        if data_file:
            self.load_data(data_file)
    
    def load_data(self, file_path):
        """
        Load campaign data from a CSV file.
        
        Args:
            file_path (str): Path to CSV file
        """
        try:
            self.data = pd.read_csv(file_path)
            logger.info(f"Successfully loaded data from {file_path}")
            self._preprocess_data()
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def _preprocess_data(self):
        """
        Preprocess the campaign data.
        """
        if self.data is None:
            raise ValueError("No data loaded for preprocessing")
            
        try:
            # Convert date columns to datetime
            if 'start_date' in self.data.columns:
                self.data['start_date'] = pd.to_datetime(self.data['start_date'])
            if 'end_date' in self.data.columns:
                self.data['end_date'] = pd.to_datetime(self.data['end_date'])
            
            # Calculate campaign duration in days
            if 'start_date' in self.data.columns and 'end_date' in self.data.columns:
                self.data['duration_days'] = (self.data['end_date'] - self.data['start_date']).dt.days
            
            # Fill missing values with median for numerical columns
            numeric_cols = self.data.select_dtypes(include=[np.number]).columns
            self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].median())
            
            logger.info("Data preprocessing completed successfully")
        except Exception as e:
            logger.error(f"Error during data preprocessing: {str(e)}")
            raise
    
    def set_features_target(self, features, target):
        """
        Set features and target variable for modeling.
        
        Args:
            features (list): List of feature column names
            target (str): Target column name
        """
        self.features = features
        self.target = target
    
    def train_model(self):
        """
        Train a linear regression model to predict campaign performance.
        """
        if self.data is None:
            raise ValueError("No data available for modeling")
        if not self.features or not self.target:
            raise ValueError("Features and target must be set before training")
            
        try:
            X = self.data[self.features]
            y = self.data[self.target]
            
            # Split data into training and test sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Train the model
            self.model = LinearRegression()
            self.model.fit(X_train, y_train)
            
            # Evaluate the model
            y_pred = self.model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            logger.info(f"Model trained successfully. MSE: {mse:.2f}, R2: {r2:.2f}")
            
            return {
                'mse': mse,
                'r2': r2,
                'coefficients': dict(zip(self.features, self.model.coef_))
            }
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise
    
    def predict_performance(self, campaign_data):
        """
        Predict performance for a new campaign.
        
        Args:
            campaign_data (dict): Dictionary containing feature values for prediction
            
        Returns:
            float: Predicted performance metric
        """
        if self.model is None:
            raise ValueError("Model has not been trained")
            
        try:
            # Convert input to DataFrame
            input_df = pd.DataFrame([campaign_data])
            
            # Ensure all features are present
            missing_features = set(self.features) - set(input_df.columns)
            if missing_features:
                raise ValueError(f"Missing features in input: {missing_features}")
                
            # Make prediction
            prediction = self.model.predict(input_df[self.features])
            return prediction[0]
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            raise
    
    def optimize_budget_allocation(self, total_budget, constraints=None):
        """
        Optimize budget allocation across different print media channels.
        
        Args:
            total_budget (float): Total available budget
            constraints (dict): Optional constraints for budget allocation
            
        Returns:
            dict: Optimized budget allocation
        """
        if self.model is None:
            raise ValueError("Model must be trained before optimization")
            
        try:
            # Simplified optimization approach (real implementation would use more sophisticated methods)
            coefficients = dict(zip(self.features, self.model.coef_))
            
            # Sort channels by their coefficient (impact on target)
            sorted_channels = sorted(
                coefficients.items(), 
                key=lambda x: abs(x[1]), 
                reverse=True
            )
            
            # Allocate budget proportionally to impact
            total_impact = sum(abs(coef) for _, coef in sorted_channels)
            allocation = {}
            
            for channel, coef in sorted_channels:
                allocation[channel] = (abs(coef) / total_impact) * total_budget
            
            # Apply constraints if provided
            if constraints:
                for channel, max_budget in constraints.items():
                    if channel in allocation and allocation[channel] > max_budget:
                        allocation[channel] = max_budget
                        # Redistribute remaining budget
                        remaining = allocation[channel] - max_budget
                        total_impact = sum(
                            abs(c) for ch, c in sorted_channels 
                            if ch != channel and ch not in constraints
                        )
                        
                        for ch, coef in sorted_channels:
                            if ch != channel and ch not in constraints:
                                allocation[ch] += (abs(coef) / total_impact) * remaining
            
            return allocation
        except Exception as e:
            logger.error(f"Error during budget optimization: {str(e)}")
            raise
    
    def generate_visual_report(self, output_dir='reports'):
        """
        Generate visual reports of campaign performance.
        
        Args:
            output_dir (str): Directory to save reports
        """
        if self.data is None:
            raise ValueError("No data available for reporting")
            
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            # Generate performance over time plot
            if 'start_date' in self.data.columns and self.target in self.data.columns:
                plt.figure(figsize=(12, 6))
                self.data.sort_values('start_date').plot(
                    x='start_date', 
                    y=self.target, 
                    kind='line',
                    title='Campaign Performance Over Time'
                )
                plt.savefig(os.path.join(output_dir, 'performance_over_time.png'))
                plt.close()
            
            # Generate channel performance comparison
            if self.features and self.target:
                correlations = self.data[self.features + [self.target]].corr()[self.target]
                correlations = correlations.drop(self.target)
                
                plt.figure(figsize=(10, 6))
                correlations.sort_values().plot(
                    kind='barh',
                    title='Channel Performance Correlation'
                )
                plt.savefig(os.path.join(output_dir, 'channel_correlation.png'))
                plt.close()
            
            logger.info(f"Visual reports generated in {output_dir}")
        except Exception as e:
            logger.error(f"Error generating visual reports: {str(e)}")
            raise
    
    def save_analysis_results(self, output_file='analysis_results.json'):
        """
        Save analysis results to a JSON file.
        
        Args:
            output_file (str): Path to output JSON file
        """
        if self.model is None:
            raise ValueError("No model available to save results")
            
        try:
            results = {
                'model_metrics': {
                    'features': self.features
