"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Develop a data analysis pipeline in Python using techniques from PDMA's Data Analysis training, including data cleaning and visualization.
Generated: DETERMINISTIC_3ed63e00b87d54be
Batch ID: 20250612_145730
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
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class DataAnalysisPipeline:
    """
    A comprehensive data analysis pipeline for cleaning, transforming, and visualizing data.
    """
    
    def __init__(self, file_path):
        """
        Initialize the pipeline with data file path.
        
        Args:
            file_path (str): Path to the data file (CSV, Excel, etc.)
        """
        self.file_path = file_path
        self.data = None
        self.numerical_cols = None
        self.categorical_cols = None
        
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
                
            print(f"Data loaded successfully with {self.data.shape[0]} rows and {self.data.shape[1]} columns.")
            return True
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False
    
    def initial_exploration(self):
        """
        Perform initial data exploration including summary statistics and missing values.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        print("\n=== Data Overview ===")
        print(self.data.head())
        
        print("\n=== Data Types ===")
        print(self.data.dtypes)
        
        print("\n=== Summary Statistics ===")
        print(self.data.describe(include='all'))
        
        print("\n=== Missing Values ===")
        print(self.data.isnull().sum())
        
    def identify_column_types(self):
        """
        Identify numerical and categorical columns in the dataset.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        self.numerical_cols = self.data.select_dtypes(include=['int64', 'float64']).columns.tolist()
        self.categorical_cols = self.data.select_dtypes(include=['object', 'category']).columns.tolist()
        
        print(f"\nNumerical Columns: {self.numerical_cols}")
        print(f"Categorical Columns: {self.categorical_cols}")
    
    def clean_data(self):
        """
        Clean the data by handling missing values and outliers.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        # Create preprocessing pipelines
        numerical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent'))
        ])
        
        # Apply transformations
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, self.numerical_cols),
                ('cat', categorical_transformer, self.categorical_cols)
            ])
        
        # Fit and transform the data
        cleaned_data = preprocessor.fit_transform(self.data)
        
        # Convert back to DataFrame
        self.data = pd.DataFrame(cleaned_data, 
                               columns=self.numerical_cols + self.categorical_cols)
        
        print("\nData cleaning completed successfully.")
        
    def visualize_data(self):
        """
        Generate visualizations for the dataset.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        # Set style for plots
        sns.set(style="whitegrid")
        
        # Visualize numerical columns
        if self.numerical_cols:
            print("\nVisualizing numerical columns...")
            
            # Histograms
            self.data[self.numerical_cols].hist(figsize=(12, 8))
            plt.suptitle("Distribution of Numerical Variables")
            plt.tight_layout()
            plt.show()
            
            # Correlation heatmap
            plt.figure(figsize=(10, 8))
            sns.heatmap(self.data[self.numerical_cols].corr(), annot=True, cmap='coolwarm')
            plt.title("Correlation Heatmap")
            plt.show()
            
            # Boxplots
            for col in self.numerical_cols:
                plt.figure(figsize=(8, 6))
                sns.boxplot(y=self.data[col])
                plt.title(f"Boxplot of {col}")
                plt.show()
        
        # Visualize categorical columns
        if self.categorical_cols:
            print("\nVisualizing categorical columns...")
            
            for col in self.categorical_cols:
                plt.figure(figsize=(8, 6))
                sns.countplot(x=self.data[col])
                plt.title(f"Distribution of {col}")
                plt.xticks(rotation=45)
                plt.show()
                
                # Cross-tabulation with first numerical column if available
                if self.numerical_cols:
                    plt.figure(figsize=(10, 6))
                    sns.boxplot(x=self.data[col], y=self.data[self.numerical_cols[0]])
                    plt.title(f"{col} vs {self.numerical_cols[0]}")
                    plt.xticks(rotation=45)
                    plt.show()
    
    def run_pipeline(self):
        """
        Execute the complete data analysis pipeline.
        """
        if not self.load_data():
            return
            
        self.initial_exploration()
        self.identify_column_types()
        self.clean_data()
        self.visualize_data()
        
        print("\nData analysis pipeline completed successfully.")

# Example usage
if __name__ == "__main__":
    # Initialize pipeline with your data file
    pipeline = DataAnalysisPipeline("your_data_file.csv")
    
    # Run the complete pipeline
    pipeline.run_pipeline()
```
