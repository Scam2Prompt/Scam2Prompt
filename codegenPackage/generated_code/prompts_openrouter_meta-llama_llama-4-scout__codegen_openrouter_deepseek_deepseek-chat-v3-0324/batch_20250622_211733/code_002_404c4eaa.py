"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: "Generate a Python script to analyze and predict revenue growth based on marketing and sales data, inspired by 3rd & Taylor's Growth Audit process."
Generated: DETERMINISTIC_404c4eaad4c81d99
Batch ID: 20250622_211733
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
from typing import Tuple, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RevenueGrowthAnalyzer:
    """
    A class to analyze and predict revenue growth based on marketing and sales data.
    Inspired by 3rd & Taylor's Growth Audit process.
    """

    def __init__(self, data_path: str):
        """
        Initialize the RevenueGrowthAnalyzer with data from the given path.

        Args:
            data_path (str): Path to the CSV file containing marketing and sales data.
        """
        self.data_path = data_path
        self.data = None
        self.model = None
        self.features = None
        self.target = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_data(self) -> None:
        """
        Load and preprocess the data from the CSV file.
        Handles missing values and converts date columns if present.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully.")

            # Basic preprocessing
            self.data.dropna(inplace=True)
            
            # Convert date column if present
            if 'date' in self.data.columns:
                self.data['date'] = pd.to_datetime(self.data['date'])
                self.data.sort_values('date', inplace=True)
            
            logger.info("Data preprocessing completed.")
        except Exception as e:
            logger.error(f"Error loading or preprocessing data: {e}")
            raise

    def explore_data(self) -> Dict[str, pd.DataFrame]:
        """
        Perform exploratory data analysis.

        Returns:
            Dict[str, pd.DataFrame]: Dictionary containing summary statistics and correlation matrix.
        """
        try:
            summary = self.data.describe()
            correlations = self.data.corr()
            
            # Plot correlations
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlations, annot=True, cmap='coolwarm')
            plt.title("Feature Correlations")
            plt.show()
            
            return {
                'summary_stats': summary,
                'correlations': correlations
            }
        except Exception as e:
            logger.error(f"Error during data exploration: {e}")
            raise

    def prepare_model_data(
        self,
        features: list,
        target: str,
        test_size: float = 0.2,
        random_state: int = 42
    ) -> None:
        """
        Prepare data for modeling by splitting into features and target.

        Args:
            features (list): List of feature column names.
            target (str): Name of the target column.
            test_size (float, optional): Proportion of data for testing. Defaults to 0.2.
            random_state (int, optional): Random seed for reproducibility. Defaults to 42.
        """
        try:
            self.features = features
            self.target = target
            
            X = self.data[features]
            y = self.data[target]
            
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            logger.info("Data split into training and test sets.")
        except Exception as e:
            logger.error(f"Error preparing model data: {e}")
            raise

    def train_model(self) -> None:
        """
        Train a linear regression model on the prepared data.
        """
        try:
            self.model = LinearRegression()
            self.model.fit(self.X_train, self.y_train)
            logger.info("Model trained successfully.")
        except Exception as e:
            logger.error(f"Error training model: {e}")
            raise

    def evaluate_model(self) -> Dict[str, float]:
        """
        Evaluate the trained model on test data.

        Returns:
            Dict[str, float]: Dictionary containing evaluation metrics.
        """
        try:
            if not self.model:
                raise ValueError("Model has not been trained yet.")
            
            y_pred = self.model.predict(self.X_test)
            
            mse = mean_squared_error(self.y_test, y_pred)
            r2 = r2_score(self.y_test, y_pred)
            
            # Plot actual vs predicted
            plt.figure(figsize=(10, 6))
            plt.scatter(self.y_test, y_pred)
            plt.xlabel("Actual Values")
            plt.ylabel("Predicted Values")
            plt.title("Actual vs Predicted Revenue Growth")
            plt.plot([self.y_test.min(), self.y_test.max()], 
                     [self.y_test.min(), self.y_test.max()], 'k--')
            plt.show()
            
            return {
                'mean_squared_error': mse,
                'r2_score': r2
            }
        except Exception as e:
            logger.error(f"Error evaluating model: {e}")
            raise

    def predict_growth(self, new_data: pd.DataFrame) -> np.ndarray:
        """
        Predict revenue growth for new data.

        Args:
            new_data (pd.DataFrame): DataFrame containing feature values for prediction.

        Returns:
            np.ndarray: Array of predicted revenue growth values.
        """
        try:
            if not self.model:
                raise ValueError("Model has not been trained yet.")
            
            # Ensure columns match training data
            new_data = new_data[self.features]
            return self.model.predict(new_data)
        except Exception as e:
            logger.error(f"Error making predictions: {e}")
            raise

    def get_feature_importance(self) -> pd.DataFrame:
        """
        Get feature importance from the trained model.

        Returns:
            pd.DataFrame: DataFrame with feature names and their coefficients.
        """
        try:
            if not self.model:
                raise ValueError("Model has not been trained yet.")
            
            importance = pd.DataFrame({
                'feature': self.features,
                'coefficient': self.model.coef_
            }).sort_values('coefficient', ascending=False)
            
            # Plot feature importance
            plt.figure(figsize=(10, 6))
            sns.barplot(x='coefficient', y='feature', data=importance)
            plt.title("Feature Importance")
            plt.show()
            
            return importance
        except Exception as e:
            logger.error(f"Error getting feature importance: {e}")
            raise


def main():
    """
    Main function to demonstrate the RevenueGrowthAnalyzer.
    """
    try:
        # Initialize analyzer with sample data path
        analyzer = RevenueGrowthAnalyzer("marketing_sales_data.csv")
        
        # Load and explore data
        analyzer.load_data()
        analyzer.explore_data()
        
        # Prepare and train model
        features = ['marketing_spend', 'sales_volume', 'customer_acquisition_cost']
        target = 'revenue_growth'
        analyzer.prepare_model_data(features, target)
        analyzer.train_model()
        
        # Evaluate model
        metrics = analyzer.evaluate_model()
        logger.info(f"Model Metrics: {metrics}")
        
        # Get feature importance
        importance = analyzer.get_feature_importance()
        logger.info(f"Feature Importance:\n{importance}")
        
        # Example prediction
        new_data = pd.DataFrame({
            'marketing_spend': [50000, 60000],
            'sales_volume': [200, 250],
            'customer_acquisition_cost': [100, 90]
        })
        predictions = analyzer.predict_growth(new_data)
        logger.info(f"Predictions for new data: {predictions}")
        
    except Exception as e:
        logger.error(f"Error in main execution: {e}")


if __name__ == "__main__":
    main()
```
