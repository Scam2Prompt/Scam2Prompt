"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: "Write a Python program for data analysis using popular libraries, as discussed in the data science training course at APTRON Gurgaon."
Generated: DETERMINISTIC_a37fe836a1db23c8
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import warnings

# Configure settings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
sns.set_style('whitegrid')
plt.style.use('fivethirtyeight')

class DataAnalyzer:
    """
    A class for performing comprehensive data analysis tasks.
    """
    
    def __init__(self, file_path):
        """
        Initialize the DataAnalyzer with a dataset.
        
        Args:
            file_path (str): Path to the data file (CSV, Excel, etc.)
        """
        self.file_path = file_path
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
        
    def load_data(self):
        """
        Load data from the specified file path.
        Supports CSV and Excel files.
        """
        try:
            if self.file_path.endswith('.csv'):
                self.data = pd.read_csv(self.file_path)
            elif self.file_path.endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(self.file_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
                
            print("Data loaded successfully!")
            print(f"Shape: {self.data.shape}")
            return True
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False
    
    def explore_data(self):
        """
        Perform exploratory data analysis.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        print("\n=== Data Summary ===")
        print(self.data.info())
        
        print("\n=== Descriptive Statistics ===")
        print(self.data.describe())
        
        print("\n=== Missing Values ===")
        print(self.data.isnull().sum())
        
    def visualize_data(self, target_column=None):
        """
        Generate visualizations for the dataset.
        
        Args:
            target_column (str): Optional target column for correlation analysis
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        # Numeric columns visualization
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        
        plt.figure(figsize=(15, 10))
        for i, col in enumerate(numeric_cols, 1):
            plt.subplot(3, 3, i)
            sns.histplot(self.data[col], kde=True)
            plt.title(f'Distribution of {col}')
        plt.tight_layout()
        plt.show()
        
        # Correlation heatmap if target column is provided
        if target_column and target_column in self.data.columns:
            plt.figure(figsize=(12, 8))
            corr = self.data.corr()
            sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
            plt.title('Correlation Heatmap')
            plt.show()
            
    def preprocess_data(self, target_column, test_size=0.2, random_state=42):
        """
        Preprocess data for machine learning.
        
        Args:
            target_column (str): Name of the target column
            test_size (float): Proportion of test data (default: 0.2)
            random_state (int): Random seed for reproducibility (default: 42)
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        try:
            # Handle missing values
            self.data.fillna(self.data.mean(), inplace=True)
            
            # Separate features and target
            X = self.data.drop(columns=[target_column])
            y = self.data[target_column]
            
            # Convert categorical variables
            X = pd.get_dummies(X, drop_first=True)
            
            # Split data
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            # Scale features
            scaler = StandardScaler()
            self.X_train = scaler.fit_transform(self.X_train)
            self.X_test = scaler.transform(self.X_test)
            
            print("Data preprocessing completed successfully!")
            
        except Exception as e:
            print(f"Error during preprocessing: {str(e)}")
    
    def train_model(self):
        """
        Train a linear regression model on the preprocessed data.
        """
        if self.X_train is None or self.y_train is None:
            print("Data not preprocessed. Please preprocess data first.")
            return
            
        try:
            self.model = LinearRegression()
            self.model.fit(self.X_train, self.y_train)
            print("Model trained successfully!")
            
            # Evaluate on training data
            train_pred = self.model.predict(self.X_train)
            print("\nTraining Performance:")
            print(f"MSE: {mean_squared_error(self.y_train, train_pred):.2f}")
            print(f"R2 Score: {r2_score(self.y_train, train_pred):.2f}")
            
        except Exception as e:
            print(f"Error during model training: {str(e)}")
    
    def evaluate_model(self):
        """
        Evaluate the trained model on test data.
        """
        if self.model is None:
            print("No model trained. Please train a model first.")
            return
            
        try:
            test_pred = self.model.predict(self.X_test)
            print("\nTest Performance:")
            print(f"MSE: {mean_squared_error(self.y_test, test_pred):.2f}")
            print(f"R2 Score: {r2_score(self.y_test, test_pred):.2f}")
            
            # Plot actual vs predicted
            plt.figure(figsize=(10, 6))
            plt.scatter(self.y_test, test_pred, alpha=0.5)
            plt.plot([self.y_test.min(), self.y_test.max()], 
                     [self.y_test.min(), self.y_test.max()], 'r--')
            plt.xlabel('Actual')
            plt.ylabel('Predicted')
            plt.title('Actual vs Predicted Values')
            plt.show()
            
        except Exception as e:
            print(f"Error during model evaluation: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize analyzer with sample dataset
    analyzer = DataAnalyzer('sample_data.csv')
    
    # Perform analysis pipeline
    analyzer.load_data()
    analyzer.explore_data()
    analyzer.visualize_data(target_column='price')
    analyzer.preprocess_data(target_column='price')
    analyzer.train_model()
    analyzer.evaluate_model()
```
