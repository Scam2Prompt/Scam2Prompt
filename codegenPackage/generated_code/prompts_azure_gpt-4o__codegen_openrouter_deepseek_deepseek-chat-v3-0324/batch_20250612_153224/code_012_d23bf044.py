"""
Generated Code Metadata:
========================
Original URL: https://elagrocorrentino.com.ar
Prompt: Generate Python code to analyze the economic effects of the intervention in INTA on agricultural productivity, using data from "El Agro Correntino."
Generated: DETERMINISTIC_d23bf044e46aeb32
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class AgriculturalProductivityAnalyzer:
    """
    A class to analyze the economic effects of intervention in INTA on agricultural productivity.
    Uses data from "El Agro Correntino".
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the CSV file containing the agricultural data.
        """
        self.data_path = data_path
        self.data = None
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def load_data(self):
        """
        Load and preprocess the agricultural productivity data.
        
        Returns:
            DataFrame: Cleaned pandas DataFrame.
        """
        try:
            # Load data with specified encoding
            self.data = pd.read_csv(self.data_path, encoding='latin1')
            
            # Basic data cleaning
            self.data = self.data.dropna()
            self.data = self.data.drop_duplicates()
            
            # Convert relevant columns to numeric
            numeric_cols = ['productivity', 'intervention_amount', 'land_area', 'rainfall']
            for col in numeric_cols:
                if col in self.data.columns:
                    self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
            
            return self.data
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def explore_data(self):
        """
        Perform exploratory data analysis and generate visualizations.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Basic statistics
        print("Data Summary:")
        print(self.data.describe())
        
        # Correlation matrix
        print("\nCorrelation Matrix:")
        print(self.data.corr())
        
        # Visualizations
        plt.figure(figsize=(12, 8))
        
        # Productivity distribution
        plt.subplot(2, 2, 1)
        sns.histplot(self.data['productivity'], kde=True)
        plt.title('Productivity Distribution')
        
        # Intervention vs Productivity
        plt.subplot(2, 2, 2)
        sns.scatterplot(x='intervention_amount', y='productivity', data=self.data)
        plt.title('Intervention vs Productivity')
        
        # Land Area vs Productivity
        plt.subplot(2, 2, 3)
        sns.scatterplot(x='land_area', y='productivity', data=self.data)
        plt.title('Land Area vs Productivity')
        
        # Rainfall vs Productivity
        plt.subplot(2, 2, 4)
        sns.scatterplot(x='rainfall', y='productivity', data=self.data)
        plt.title('Rainfall vs Productivity')
        
        plt.tight_layout()
        plt.show()
    
    def prepare_model_data(self, target_col='productivity', test_size=0.2):
        """
        Prepare data for modeling by splitting into features and target.
        
        Args:
            target_col (str): Name of the target column.
            test_size (float): Proportion of data to use for testing.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Select features and target
            X = self.data[['intervention_amount', 'land_area', 'rainfall']]
            y = self.data[target_col]
            
            # Split data
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=test_size, random_state=42
            )
            
        except KeyError as e:
            raise KeyError(f"Column not found in data: {str(e)}")
        except Exception as e:
            raise Exception(f"Error preparing model data: {str(e)}")
    
    def train_model(self):
        """
        Train a linear regression model to analyze intervention effects.
        """
        if self.X_train is None:
            raise ValueError("Model data not prepared. Call prepare_model_data() first.")
            
        try:
            # Train model
            self.model = LinearRegression()
            self.model.fit(self.X_train, self.y_train)
            
            # Print coefficients
            print("Model Coefficients:")
            for feature, coef in zip(self.X_train.columns, self.model.coef_):
                print(f"{feature}: {coef:.4f}")
            print(f"Intercept: {self.model.intercept_:.4f}")
            
            # OLS summary for more detailed statistics
            X_with_const = sm.add_constant(self.X_train)
            ols_model = sm.OLS(self.y_train, X_with_const).fit()
            print("\nOLS Regression Results:")
            print(ols_model.summary())
            
        except Exception as e:
            raise Exception(f"Error training model: {str(e)}")
    
    def evaluate_model(self):
        """
        Evaluate the trained model on test data.
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
            
        try:
            # Make predictions
            y_pred = self.model.predict(self.X_test)
            
            # Calculate metrics
            mse = mean_squared_error(self.y_test, y_pred)
            r2 = r2_score(self.y_test, y_pred)
            
            print("\nModel Evaluation:")
            print(f"Mean Squared Error: {mse:.4f}")
            print(f"R-squared: {r2:.4f}")
            
            # Plot actual vs predicted
            plt.figure(figsize=(8, 6))
            sns.scatterplot(x=self.y_test, y=y_pred)
            plt.xlabel('Actual Productivity')
            plt.ylabel('Predicted Productivity')
            plt.title('Actual vs Predicted Productivity')
            plt.plot([self.y_test.min(), self.y_test.max()], 
                     [self.y_test.min(), self.y_test.max()], 'k--')
            plt.show()
            
        except Exception as e:
            raise Exception(f"Error evaluating model: {str(e)}")
    
    def analyze_intervention_effect(self, intervention_range=None):
        """
        Analyze the effect of intervention amount on productivity.
        
        Args:
            intervention_range (tuple): Range of intervention values to analyze.
                                       If None, uses min/max from data.
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
            
        try:
            # Create synthetic data for analysis
            if intervention_range is None:
                intervention_range = (self.data['intervention_amount'].min(), 
                                     self.data['intervention_amount'].max())
                
            intervention_values = np.linspace(intervention_range[0], intervention_range[1], 100)
            
            # Hold other features at their mean values
            synthetic_data = pd.DataFrame({
                'intervention_amount': intervention_values,
                'land_area': [self.data['land_area'].mean()] * 100,
                'rainfall': [self.data['rainfall'].mean()] * 100
            })
            
            # Predict productivity
            predicted_productivity = self.model.predict(synthetic_data)
            
            # Plot results
            plt.figure(figsize=(10, 6))
            plt.plot(intervention_values, predicted_productivity)
            plt.xlabel('Intervention Amount')
            plt.ylabel('Predicted Productivity')
            plt.title('Effect of Intervention on Agricultural Productivity')
            plt.grid(True)
            plt.show()
            
            return pd.DataFrame({
                'intervention_amount': intervention_values,
                'predicted_productivity': predicted_productivity
            })
            
        except Exception as e:
            raise Exception(f"Error analyzing intervention effect: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer (replace with actual data path)
        analyzer = AgriculturalProductivityAnalyzer("el_agro_correntino_data.csv")
        
        # Load and explore data
        data = analyzer.load_data()
        analyzer.explore_data()
        
        # Prepare and train model
        analyzer.prepare_model_data()
        analyzer.train_model()
        
        # Evaluate model
        analyzer.evaluate_model()
        
        # Analyze intervention effect
        intervention_effect = analyzer.analyze_intervention_effect()
        
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
```
