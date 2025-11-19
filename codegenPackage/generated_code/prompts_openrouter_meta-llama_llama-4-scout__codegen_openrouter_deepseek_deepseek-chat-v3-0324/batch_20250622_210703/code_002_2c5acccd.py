"""
Generated Code Metadata:
========================
Original URL: https://punnami.in
Prompt: Create a Python program to analyze the impact of credit life insurance on rural communities, using data from CreditAccess Life Insurance as a case study.
Generated: DETERMINISTIC_2c5acccd3cd5898d
Batch ID: 20250622_210703
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

class CreditLifeInsuranceAnalyzer:
    """
    A class to analyze the impact of credit life insurance on rural communities.
    Uses CreditAccess Life Insurance as a case study.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the CSV file containing the insurance data
        """
        try:
            self.data = pd.read_csv(data_path)
            self._clean_data()
            print("Data loaded and cleaned successfully.")
        except FileNotFoundError:
            print(f"Error: File not found at {data_path}")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
    
    def _clean_data(self):
        """
        Clean and preprocess the data.
        """
        # Handle missing values
        self.data = self.data.dropna()
        
        # Convert categorical variables to numeric if needed
        if 'region_type' in self.data.columns:
            self.data['is_rural'] = self.data['region_type'].apply(
                lambda x: 1 if x.lower() == 'rural' else 0
            )
        
        # Ensure numeric columns are properly typed
        numeric_cols = ['premium_amount', 'claim_amount', 'household_income', 'loan_amount']
        for col in numeric_cols:
            if col in self.data.columns:
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
        
        # Drop any remaining NA values after conversion
        self.data = self.data.dropna()
    
    def descriptive_statistics(self):
        """
        Generate descriptive statistics for the dataset.
        
        Returns:
            DataFrame: Summary statistics
        """
        try:
            return self.data.describe(include='all')
        except Exception as e:
            print(f"Error generating statistics: {str(e)}")
            return None
    
    def plot_premium_distribution(self):
        """
        Plot the distribution of premium amounts.
        """
        try:
            plt.figure(figsize=(10, 6))
            sns.histplot(self.data['premium_amount'], kde=True)
            plt.title('Distribution of Premium Amounts')
            plt.xlabel('Premium Amount')
            plt.ylabel('Frequency')
            plt.show()
        except Exception as e:
            print(f"Error plotting premium distribution: {str(e)}")
    
    def plot_rural_vs_urban(self):
        """
        Compare insurance metrics between rural and urban areas.
        """
        try:
            if 'is_rural' not in self.data.columns:
                print("Warning: Rural/urban data not available")
                return
            
            plt.figure(figsize=(12, 6))
            
            # Premium comparison
            plt.subplot(1, 2, 1)
            sns.boxplot(x='is_rural', y='premium_amount', data=self.data)
            plt.title('Premium Amount by Region Type')
            plt.xlabel('Region Type (0=Urban, 1=Rural)')
            plt.ylabel('Premium Amount')
            
            # Claim comparison
            plt.subplot(1, 2, 2)
            sns.boxplot(x='is_rural', y='claim_amount', data=self.data)
            plt.title('Claim Amount by Region Type')
            plt.xlabel('Region Type (0=Urban, 1=Rural)')
            plt.ylabel('Claim Amount')
            
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting rural vs urban comparison: {str(e)}")
    
    def analyze_impact(self, outcome_var='household_income'):
        """
        Analyze the impact of credit life insurance on rural communities.
        
        Args:
            outcome_var (str): The outcome variable to analyze (default: household_income)
        
        Returns:
            dict: Regression results and metrics
        """
        try:
            if outcome_var not in self.data.columns:
                print(f"Error: {outcome_var} not found in data")
                return None
            
            # Prepare data
            rural_data = self.data[self.data['is_rural'] == 1]
            X = rural_data[['premium_amount', 'loan_amount']]
            y = rural_data[outcome_var]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Train model
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            # Make predictions
            y_pred = model.predict(X_test)
            
            # Calculate metrics
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            # OLS summary for more detailed statistics
            X_with_const = sm.add_constant(X_train)
            ols_model = sm.OLS(y_train, X_with_const)
            ols_results = ols_model.fit()
            
            return {
                'coefficients': model.coef_,
                'intercept': model.intercept_,
                'mse': mse,
                'r2': r2,
                'ols_summary': ols_results.summary()
            }
        except Exception as e:
            print(f"Error in impact analysis: {str(e)}")
            return None
    
    def generate_report(self, output_file='credit_life_impact_report.txt'):
        """
        Generate a comprehensive report of the analysis.
        
        Args:
            output_file (str): Path to save the report
        """
        try:
            with open(output_file, 'w') as f:
                f.write("Credit Life Insurance Impact Analysis Report\n")
                f.write("============================================\n\n")
                
                # Descriptive statistics
                f.write("Descriptive Statistics:\n")
                f.write(str(self.descriptive_statistics()) + "\n\n")
                
                # Impact analysis
                f.write("Impact Analysis on Rural Communities:\n")
                results = self.analyze_impact()
                if results:
                    f.write(f"Coefficients: {results['coefficients']}\n")
                    f.write(f"Intercept: {results['intercept']}\n")
                    f.write(f"Mean Squared Error: {results['mse']}\n")
                    f.write(f"R-squared: {results['r2']}\n\n")
                    f.write("Detailed OLS Results:\n")
                    f.write(str(results['ols_summary']))
                
            print(f"Report generated successfully at {output_file}")
        except Exception as e:
            print(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    analyzer = CreditLifeInsuranceAnalyzer('credit_life_insurance_data.csv')
    
    # Generate descriptive statistics
    print(analyzer.descriptive_statistics())
    
    # Visualize data
    analyzer.plot_premium_distribution()
    analyzer.plot_rural_vs_urban()
    
    # Analyze impact
    impact_results = analyzer.analyze_impact()
    if impact_results:
        print("\nImpact Analysis Results:")
        print(f"R-squared: {impact_results['r2']}")
        print(f"Coefficients: {impact_results['coefficients']}")
    
    # Generate full report
    analyzer.generate_report()
```
