"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Generate code to analyze clinical trial data for hereditary angioedema (HAE) treatment, incorporating insights from the CSL Seqirus team's presentation at #EAACI2024.
Generated: DETERMINISTIC_b2688c78240380df
Batch ID: 20250612_154653
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
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class HAETrialAnalyzer:
    """
    A class to analyze clinical trial data for Hereditary Angioedema (HAE) treatment.
    Incorporates insights from CSL Seqirus team's presentation at EAACI 2024.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with clinical trial data.
        
        Args:
            data_path (str): Path to the clinical trial data file (CSV format)
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            print("Data loaded and validated successfully.")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise
    
    def _validate_data(self):
        """
        Validate the loaded clinical trial data for required columns and data quality.
        """
        required_columns = {
            'patient_id', 'age', 'gender', 'treatment_group', 
            'baseline_attack_rate', 'post_treatment_attack_rate',
            'adverse_events', 'treatment_duration', 'biomarker_level'
        }
        
        missing_cols = required_columns - set(self.data.columns)
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
        if self.data.isnull().sum().sum() > 0:
            print("Warning: Data contains missing values that may need imputation.")
    
    def preprocess_data(self):
        """
        Preprocess the clinical trial data for analysis.
        """
        # Convert categorical variables
        self.data['gender'] = self.data['gender'].map({'Male': 0, 'Female': 1})
        self.data['treatment_group'] = self.data['treatment_group'].astype('category').cat.codes
        
        # Calculate attack rate reduction
        self.data['attack_rate_reduction'] = (
            self.data['baseline_attack_rate'] - self.data['post_treatment_attack_rate']
        )
        
        # Handle missing values
        self.data.fillna({
            'biomarker_level': self.data['biomarker_level'].median(),
            'adverse_events': 0
        }, inplace=True)
        
        # Standardize numerical features
        scaler = StandardScaler()
        numerical_cols = ['age', 'baseline_attack_rate', 'biomarker_level', 'treatment_duration']
        self.data[numerical_cols] = scaler.fit_transform(self.data[numerical_cols])
    
    def analyze_treatment_effectiveness(self):
        """
        Analyze the effectiveness of different treatment groups.
        """
        # Group by treatment and calculate metrics
        results = self.data.groupby('treatment_group').agg({
            'attack_rate_reduction': ['mean', 'std', 'count'],
            'adverse_events': 'mean'
        })
        
        # Perform statistical testing
        groups = self.data['treatment_group'].unique()
        if len(groups) == 2:
            group1 = self.data[self.data['treatment_group'] == groups[0]]['attack_rate_reduction']
            group2 = self.data[self.data['treatment_group'] == groups[1]]['attack_rate_reduction']
            t_stat, p_value = stats.ttest_ind(group1, group2)
            results['p_value'] = p_value
        
        return results
    
    def visualize_results(self):
        """
        Generate visualizations for the clinical trial results.
        """
        plt.figure(figsize=(15, 10))
        
        # Attack rate reduction by treatment
        plt.subplot(2, 2, 1)
        sns.boxplot(x='treatment_group', y='attack_rate_reduction', data=self.data)
        plt.title('Attack Rate Reduction by Treatment Group')
        
        # Adverse events by treatment
        plt.subplot(2, 2, 2)
        sns.barplot(x='treatment_group', y='adverse_events', data=self.data)
        plt.title('Adverse Events by Treatment Group')
        
        # Biomarker correlation
        plt.subplot(2, 2, 3)
        sns.scatterplot(x='biomarker_level', y='attack_rate_reduction', hue='treatment_group', data=self.data)
        plt.title('Biomarker Level vs. Attack Rate Reduction')
        
        # Age distribution
        plt.subplot(2, 2, 4)
        sns.histplot(x='age', hue='treatment_group', data=self.data, kde=True, multiple='stack')
        plt.title('Age Distribution by Treatment Group')
        
        plt.tight_layout()
        plt.show()
    
    def predict_treatment_response(self):
        """
        Build a predictive model for treatment response.
        """
        # Prepare features and target
        X = self.data[['age', 'gender', 'baseline_attack_rate', 'biomarker_level']]
        y = (self.data['attack_rate_reduction'] > self.data['attack_rate_reduction'].median()).astype(int)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = model.predict(X_test)
        print("Treatment Response Prediction Model Performance:")
        print(classification_report(y_test, y_pred))
        print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x='importance', y='feature', data=feature_importance)
        plt.title('Feature Importance for Treatment Response Prediction')
        plt.show()
        
        return model
    
    def generate_report(self, output_path):
        """
        Generate a comprehensive report of the analysis.
        
        Args:
            output_path (str): Path to save the report
        """
        try:
            with open(output_path, 'w') as f:
                f.write("Hereditary Angioedema (HAE) Clinical Trial Analysis Report\n")
                f.write("="*80 + "\n\n")
                
                # Basic statistics
                f.write("1. Dataset Overview:\n")
                f.write(f"- Number of patients: {len(self.data)}\n")
                f.write(f"- Treatment groups: {self.data['treatment_group'].nunique()}\n")
                f.write(f"- Average age: {self.data['age'].mean():.1f} years\n\n")
                
                # Treatment effectiveness
                f.write("2. Treatment Effectiveness Analysis:\n")
                effectiveness = self.analyze_treatment_effectiveness()
                f.write(effectiveness.to_string())
                f.write("\n\n")
                
                # Predictive model
                f.write("3. Treatment Response Prediction:\n")
                model = self.predict_treatment_response()
                f.write("Model trained and evaluated successfully.\n")
                
            print(f"Report generated successfully at: {output_path}")
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with clinical trial data
        analyzer = HAETrialAnalyzer('hae_clinical_trial_data.csv')
        
        # Preprocess data
        analyzer.preprocess_data()
        
        # Generate visualizations
        analyzer.visualize_results()
        
        # Generate comprehensive report
        analyzer.generate_report('hae_trial_analysis_report.txt')
        
    except Exception as e:
        print(f"Analysis failed: {str(e)}")
```
