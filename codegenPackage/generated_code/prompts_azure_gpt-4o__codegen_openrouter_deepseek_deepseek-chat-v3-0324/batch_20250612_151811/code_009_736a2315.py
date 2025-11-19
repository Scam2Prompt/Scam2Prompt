"""
Generated Code Metadata:
========================
Original URL: https://eximiousglobal.com
Prompt: Develop a program to track and optimize time-to-fill metrics for recruitment processes, leveraging the data-driven approach mentioned in Eximious Global's RPO services.
Generated: DETERMINISTIC_736a23159a58fe21
Batch ID: 20250612_151811
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
from datetime import datetime
from typing import List, Dict, Optional
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RecruitmentTimeTracker:
    """
    A class to track and optimize time-to-fill metrics for recruitment processes.
    """
    
    def __init__(self, data_path: Optional[str] = None):
        """
        Initialize the RecruitmentTimeTracker.
        
        Args:
            data_path (str, optional): Path to recruitment data CSV file. Defaults to None.
        """
        self.data = None
        self.model = None
        self.features = None
        self.target = None
        
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, data_path: str) -> None:
        """
        Load recruitment data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing recruitment data.
            
        Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the data format is invalid.
        """
        try:
            self.data = pd.read_csv(data_path)
            logger.info(f"Successfully loaded data from {data_path}")
            
            # Validate required columns
            required_columns = {
                'position_id', 'position_title', 'department', 
                'recruiter', 'application_date', 'offer_date', 
                'hire_date', 'candidate_source', 'interview_stages'
            }
            
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            # Calculate time-to-fill
            self._calculate_metrics()
            
        except FileNotFoundError as e:
            logger.error(f"Data file not found: {data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Invalid data format: {str(e)}")
    
    def _calculate_metrics(self) -> None:
        """
        Calculate time-to-fill and other relevant metrics.
        """
        # Convert date columns to datetime
        date_cols = ['application_date', 'offer_date', 'hire_date']
        for col in date_cols:
            self.data[col] = pd.to_datetime(self.data[col], errors='coerce')
        
        # Calculate time-to-fill (days from application to hire)
        self.data['time_to_fill'] = (self.data['hire_date'] - self.data['application_date']).dt.days
        
        # Calculate time-to-offer (days from application to offer)
        self.data['time_to_offer'] = (self.data['offer_date'] - self.data['application_date']).dt.days
        
        # Calculate offer-to-hire (days from offer to hire)
        self.data['offer_to_hire'] = (self.data['hire_date'] - self.data['offer_date']).dt.days
        
        logger.info("Calculated time-to-fill metrics")
    
    def get_summary_stats(self) -> Dict:
        """
        Get summary statistics for time-to-fill metrics.
        
        Returns:
            dict: Dictionary containing summary statistics.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        return {
            'mean_time_to_fill': self.data['time_to_fill'].mean(),
            'median_time_to_fill': self.data['time_to_fill'].median(),
            'min_time_to_fill': self.data['time_to_fill'].min(),
            'max_time_to_fill': self.data['time_to_fill'].max(),
            'std_time_to_fill': self.data['time_to_fill'].std(),
            'count': len(self.data)
        }
    
    def analyze_by_dimension(self, dimension: str) -> pd.DataFrame:
        """
        Analyze time-to-fill metrics by a specific dimension (e.g., department, recruiter).
        
        Args:
            dimension (str): Column name to group by.
            
        Returns:
            pd.DataFrame: Aggregated metrics by the specified dimension.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        if dimension not in self.data.columns:
            raise ValueError(f"Dimension '{dimension}' not found in data.")
            
        return self.data.groupby(dimension).agg({
            'time_to_fill': ['mean', 'median', 'count'],
            'time_to_offer': ['mean', 'median'],
            'offer_to_hire': ['mean', 'median']
        }).sort_values(('time_to_fill', 'mean'))
    
    def visualize_metrics(self, dimension: str, top_n: int = 10) -> None:
        """
        Visualize time-to-fill metrics by a specific dimension.
        
        Args:
            dimension (str): Column name to visualize by.
            top_n (int): Number of top items to display. Defaults to 10.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        analysis = self.analyze_by_dimension(dimension)
        analysis = analysis.head(top_n)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(
            x=analysis.index,
            y=analysis[('time_to_fill', 'mean')]
        )
        plt.title(f'Average Time-to-Fill by {dimension}')
        plt.xlabel(dimension)
        plt.ylabel('Days')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def prepare_model_data(self, features: List[str], target: str = 'time_to_fill') -> None:
        """
        Prepare data for predictive modeling.
        
        Args:
            features (List[str]): List of feature columns to use.
            target (str): Target column to predict. Defaults to 'time_to_fill'.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        # Check if features exist
        missing_features = set(features) - set(self.data.columns)
        if missing_features:
            raise ValueError(f"Features not found in data: {missing_features}")
            
        if target not in self.data.columns:
            raise ValueError(f"Target column '{target}' not found in data.")
            
        self.features = features
        self.target = target
        
        # Handle categorical features
        self._preprocess_data()
        
    def _preprocess_data(self) -> None:
        """
        Preprocess data for modeling (handle categoricals, missing values).
        """
        # One-hot encode categorical features
        categoricals = [f for f in self.features if self.data[f].dtype == 'object']
        if categoricals:
            self.data = pd.get_dummies(
                self.data,
                columns=categoricals,
                drop_first=True
            )
            # Update features list with encoded columns
            self.features = [
                col for col in self.data.columns 
                if col.startswith(tuple(self.features)) and col != self.target
            ]
        
        # Drop rows with missing target values
        self.data = self.data.dropna(subset=[self.target])
        
        # Fill remaining missing values with median for numeric columns
        for col in self.features:
            if pd.api.types.is_numeric_dtype(self.data[col]):
                self.data[col].fillna(self.data[col].median(), inplace=True)
    
    def train_model(self, test_size: float = 0.2, random_state: int = 42) -> Dict:
        """
        Train a linear regression model to predict time-to-fill.
        
        Args:
            test_size (float): Proportion of data to use for testing. Defaults to 0.2.
            random_state (int): Random seed for reproducibility. Defaults to 42.
            
        Returns:
            dict: Dictionary containing model performance metrics.
        """
        if not self.features or not self.target:
            raise ValueError("Features and target not set. Call prepare_model_data first.")
            
        X = self.data[self.features]
        y = self.data[self.target]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        
        logger.info(f"Model trained with MAE: {mae:.2f} days")
        
        return {
            'mae': mae,
            'coefficients': dict(zip(self.features, self.model.coef_)),
            'intercept': self.model.intercept_
        }
    
    def predict_time_to_fill(self, input_data:
