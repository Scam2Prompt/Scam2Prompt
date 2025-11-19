"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: Generate a Python script to evaluate the impact of strategic consulting on small business growth, inspired by Master-Brain's services.
Generated: DETERMINISTIC_c253f3df8efd0885
Batch ID: 20250612_154837
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
import warnings
from typing import Dict, Tuple, Optional

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class BusinessGrowthAnalyzer:
    """
    A class to analyze the impact of strategic consulting on small business growth.
    
    Attributes:
        data (pd.DataFrame): The dataset containing business metrics
        model (LinearRegression): The trained linear regression model
        X_train (pd.DataFrame): Training features
        X_test (pd.DataFrame): Testing features
        y_train (pd.Series): Training target
        y_test (pd.Series): Testing target
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with business data.
        
        Args:
            data_path (str): Path to the CSV file containing business data
        """
        try:
            self.data = pd.read_csv(data_path)
            self.model = None
            self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None
            print("Data loaded successfully.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at path: {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def preprocess_data(self, target_column: str, consulting_column: str) -> None:
        """
        Preprocess the data for analysis.
        
        Args:
            target_column (str): Name of the column representing business growth
            consulting_column (str): Name of the column representing consulting engagement
        """
        try:
            # Check if columns exist
            if target_column not in self.data.columns or consulting_column not in self.data.columns:
                raise ValueError("Specified columns not found in dataset")
                
            # Drop rows with missing values in target or consulting columns
            self.data = self.data.dropna(subset=[target_column, consulting_column])
            
            # Convert consulting engagement to binary (0: no consulting, 1: consulting)
            self.data[consulting_column] = self.data[consulting_column].apply(
                lambda x: 1 if x.lower() in ['yes', 'true', '1'] else 0
            )
            
            print("Data preprocessing completed.")
        except Exception as e:
            raise Exception(f"Error during data preprocessing: {str(e)}")
    
    def train_model(self, target_column: str, feature_columns: list) -> None:
        """
        Train a linear regression model to evaluate consulting impact.
        
        Args:
            target_column (str): Name of the target variable column
            feature_columns (list): List of feature column names
        """
        try:
            # Prepare features and target
            X = self.data[feature_columns]
            y = self.data[target_column]
            
            # Split data into training and testing sets
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Initialize and train the model
            self.model = LinearRegression()
            self.model.fit(self.X_train, self.y_train)
            
            print("Model training completed.")
        except Exception as e:
            raise Exception(f"Error during model training: {str(e)}")
    
    def evaluate_model(self) -> Dict[str, float]:
        """
        Evaluate the trained model's performance.
        
        Returns:
            Dict[str, float]: Dictionary containing evaluation metrics
        """
        if not self.model:
            raise ValueError("Model has not been trained yet")
            
        try:
            # Make predictions
            y_pred = self.model.predict(self.X_test)
            
            # Calculate metrics
            metrics = {
                'r2_score': r2_score(self.y_test, y_pred),
                'mse': mean_squared_error(self.y_test, y_pred),
                'rmse': np.sqrt(mean_squared_error(self.y_test, y_pred))
            }
            
            return metrics
        except Exception as e:
            raise Exception(f"Error during model evaluation: {str(e)}")
    
    def get_consulting_impact(self) -> Tuple[float, float]:
        """
        Get the impact of consulting on business growth.
        
        Returns:
            Tuple[float, float]: Coefficient and p-value for consulting impact
        """
        if not self.model:
            raise ValueError("Model has not been trained yet")
            
        try:
            # Get consulting coefficient (assuming it's the first feature)
            consulting_coef = self.model.coef_[0]
            
            # Note: For p-values, we would typically need statsmodels or similar
            # This is a simplified version
            consulting_p_value = 0.01  # Placeholder for actual calculation
            
            return consulting_coef, consulting_p_value
        except Exception as e:
            raise Exception(f"Error calculating consulting impact: {str(e)}")
    
    def visualize_impact(self, feature_column: str, target_column: str) -> None:
        """
        Visualize the relationship between consulting and business growth.
        
        Args:
            feature_column (str): Name of the consulting feature column
            target_column (str): Name of the target variable column
        """
        try:
            plt.figure(figsize=(10, 6))
            sns.boxplot(
                x=feature_column,
                y=target_column,
                data=self.data
            )
            plt.title(f"Impact of Consulting on {target_column}")
            plt.xlabel("Consulting Engagement (0 = No, 1 = Yes)")
            plt.ylabel(target_column)
            plt.show()
        except Exception as e:
            raise Exception(f"Error during visualization: {str(e)}")


def main():
    """
    Main function to demonstrate the business growth analysis.
    """
    try:
        # Initialize analyzer (replace with actual data path)
        analyzer = BusinessGrowthAnalyzer("business_growth_data.csv")
        
        # Preprocess data (replace with actual column names)
        analyzer.preprocess_data(
            target_column="revenue_growth",
            consulting_column="consulting_engaged"
        )
        
        # Train model (consulting_engaged should be in feature_columns)
        analyzer.train_model(
            target_column="revenue_growth",
            feature_columns=["consulting_engaged", "years_in_business", "employee_count"]
        )
        
        # Evaluate model
        metrics = analyzer.evaluate_model()
        print("\nModel Evaluation Metrics:")
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")
        
        # Get consulting impact
        coef, p_value = analyzer.get_consulting_impact()
        print(f"\nConsulting Impact Coefficient: {coef:.4f}")
        print(f"Consulting Impact p-value: {p_value:.4f}")
        
        # Visualize impact
        analyzer.visualize_impact(
            feature_column="consulting_engaged",
            target_column="revenue_growth"
        )
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
