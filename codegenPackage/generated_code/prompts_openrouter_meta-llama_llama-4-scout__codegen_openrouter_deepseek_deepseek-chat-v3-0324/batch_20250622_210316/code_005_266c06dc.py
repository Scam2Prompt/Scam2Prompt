"""
Generated Code Metadata:
========================
Original URL: https://publichealth-care.com
Prompt: Create a data analysis project to evaluate the impact of mental health counselors on medication prescriptions, using data from a specific health center.
Generated: DETERMINISTIC_266c06dcefa14560
Batch ID: 20250622_210316
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
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import statsmodels.api as sm
import warnings

# Configuration
warnings.filterwarnings('ignore')
plt.style.use('ggplot')
pd.set_option('display.max_columns', None)

class MentalHealthAnalysis:
    """
    A class to analyze the impact of mental health counselors on medication prescriptions.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the dataset path.
        
        Args:
            data_path (str): Path to the CSV file containing the data
        """
        self.data_path = data_path
        self.df = None
        self.scaler = StandardScaler()
        
    def load_data(self):
        """
        Load and preprocess the dataset.
        """
        try:
            # Load the dataset
            self.df = pd.read_csv(self.data_path)
            
            # Basic data cleaning
            self.df.dropna(inplace=True)
            self.df.reset_index(drop=True, inplace=True)
            
            # Convert categorical variables
            categorical_cols = ['gender', 'counselor_available', 'prescription_given']
            for col in categorical_cols:
                if col in self.df.columns:
                    self.df[col] = self.df[col].astype('category')
            
            print("Data loaded successfully. Shape:", self.df.shape)
            return True
        
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False
    
    def exploratory_analysis(self):
        """
        Perform exploratory data analysis and generate visualizations.
        """
        if self.df is None:
            print("Data not loaded. Please load data first.")
            return
        
        try:
            # Basic statistics
            print("\nBasic Statistics:")
            print(self.df.describe(include='all'))
            
            # Prescription rate by counselor availability
            plt.figure(figsize=(10, 6))
            sns.barplot(x='counselor_available', y='prescription_given', 
                        data=self.df, estimator=np.mean)
            plt.title('Prescription Rate by Counselor Availability')
            plt.ylabel('Prescription Rate')
            plt.xlabel('Counselor Available')
            plt.show()
            
            # Age distribution by prescription status
            plt.figure(figsize=(10, 6))
            sns.boxplot(x='prescription_given', y='age', data=self.df)
            plt.title('Age Distribution by Prescription Status')
            plt.ylabel('Age')
            plt.xlabel('Prescription Given')
            plt.show()
            
            # Correlation matrix
            numeric_df = self.df.select_dtypes(include=[np.number])
            if not numeric_df.empty:
                plt.figure(figsize=(10, 8))
                sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
                plt.title('Correlation Matrix')
                plt.show()
            
        except Exception as e:
            print(f"Error during exploratory analysis: {str(e)}")
    
    def statistical_test(self):
        """
        Perform statistical tests to evaluate the impact.
        """
        if self.df is None:
            print("Data not loaded. Please load data first.")
            return
        
        try:
            # Chi-square test for counselor availability and prescription
            if 'counselor_available' in self.df.columns and 'prescription_given' in self.df.columns:
                contingency_table = pd.crosstab(
                    self.df['counselor_available'], 
                    self.df['prescription_given']
                )
                chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
                print(f"\nChi-square Test Results:")
                print(f"Chi2 Statistic: {chi2:.4f}")
                print(f"P-value: {p:.4f}")
                print("Expected Frequencies:\n", expected)
            
            # T-test for age difference between prescription groups
            if 'age' in self.df.columns and 'prescription_given' in self.df.columns:
                group1 = self.df[self.df['prescription_given'] == 1]['age']
                group0 = self.df[self.df['prescription_given'] == 0]['age']
                t_stat, p_val = stats.ttest_ind(group1, group0)
                print(f"\nT-test Results (Age vs Prescription):")
                print(f"T-statistic: {t_stat:.4f}")
                print(f"P-value: {p_val:.4f}")
                
        except Exception as e:
            print(f"Error during statistical tests: {str(e)}")
    
    def build_model(self):
        """
        Build a predictive model to evaluate counselor impact.
        """
        if self.df is None:
            print("Data not loaded. Please load data first.")
            return
        
        try:
            # Prepare data
            X = self.df.drop('prescription_given', axis=1)
            X = pd.get_dummies(X, drop_first=True)
            y = self.df['prescription_given']
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.3, random_state=42
            )
            
            # Scale numeric features
            numeric_cols = X_train.select_dtypes(include=[np.number]).columns
            X_train[numeric_cols] = self.scaler.fit_transform(X_train[numeric_cols])
            X_test[numeric_cols] = self.scaler.transform(X_test[numeric_cols])
            
            # Logistic Regression
            model = LogisticRegression(max_iter=1000)
            model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = model.predict(X_test)
            y_prob = model.predict_proba(X_test)[:, 1]
            
            print("\nModel Evaluation:")
            print(classification_report(y_test, y_pred))
            print("\nConfusion Matrix:")
            print(confusion_matrix(y_test, y_pred))
            print(f"\nROC AUC Score: {roc_auc_score(y_test, y_prob):.4f}")
            
            # Feature importance
            print("\nFeature Importance (Odds Ratios):")
            odds_ratios = pd.DataFrame(
                np.exp(model.coef_[0]), 
                index=X.columns, 
                columns=['Odds Ratio']
            ).sort_values('Odds Ratio', ascending=False)
            print(odds_ratios)
            
            return model
            
        except Exception as e:
            print(f"Error during model building: {str(e)}")
            return None
    
    def run_analysis(self):
        """
        Run the complete analysis pipeline.
        """
        if not self.load_data():
            return
        
        self.exploratory_analysis()
        self.statistical_test()
        self.build_model()

# Example usage
if __name__ == "__main__":
    analyzer = MentalHealthAnalysis("mental_health_data.csv")
    analyzer.run_analysis()
```
