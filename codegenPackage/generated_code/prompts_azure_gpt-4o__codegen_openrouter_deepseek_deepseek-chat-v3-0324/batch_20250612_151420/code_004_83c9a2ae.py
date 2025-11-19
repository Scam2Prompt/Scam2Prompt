"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: Write code to analyze sports physiotherapy data, focusing on injury types and rehabilitation progress, inspired by Ayushman College's role as a physiotherapy service provider for sports events like the Commonwealth Games.
Generated: DETERMINISTIC_83c9a2ae50ea172b
Batch ID: 20250612_151420
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
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class SportsPhysioAnalyzer:
    """
    A class to analyze sports physiotherapy data including injury types and rehabilitation progress.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the path to the data file.
        
        Args:
            data_path (str): Path to the CSV file containing physiotherapy data
        """
        self.data_path = data_path
        self.data = None
        self.encoder = LabelEncoder()
        
    def load_data(self):
        """
        Load and preprocess the physiotherapy data.
        
        Returns:
            pd.DataFrame: Cleaned and preprocessed data
        """
        try:
            # Load data
            self.data = pd.read_csv(self.data_path)
            
            # Basic data cleaning
            self.data.dropna(inplace=True)
            self.data.drop_duplicates(inplace=True)
            
            # Convert categorical columns to numerical
            categorical_cols = self.data.select_dtypes(include=['object']).columns
            for col in categorical_cols:
                self.data[col] = self.encoder.fit_transform(self.data[col])
                
            return self.data
        
        except FileNotFoundError:
            print(f"Error: File not found at {self.data_path}")
            return None
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None
    
    def analyze_injury_types(self):
        """
        Analyze and visualize the distribution of injury types.
        """
        if self.data is None:
            print("Data not loaded. Please call load_data() first.")
            return
        
        plt.figure(figsize=(10, 6))
        sns.countplot(x='injury_type', data=self.data)
        plt.title('Distribution of Injury Types')
        plt.xlabel('Injury Type')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.show()
        
    def analyze_rehab_progress(self):
        """
        Analyze and visualize rehabilitation progress metrics.
        """
        if self.data is None:
            print("Data not loaded. Please call load_data() first.")
            return
        
        plt.figure(figsize=(12, 6))
        
        # Plot rehabilitation duration by injury type
        plt.subplot(1, 2, 1)
        sns.boxplot(x='injury_type', y='rehab_duration_days', data=self.data)
        plt.title('Rehabilitation Duration by Injury Type')
        plt.xlabel('Injury Type')
        plt.ylabel('Duration (days)')
        plt.xticks(rotation=45)
        
        # Plot recovery rate
        plt.subplot(1, 2, 2)
        sns.histplot(self.data['recovery_rate'], bins=20, kde=True)
        plt.title('Distribution of Recovery Rates')
        plt.xlabel('Recovery Rate (%)')
        plt.ylabel('Count')
        
        plt.tight_layout()
        plt.show()
    
    def predict_recovery_outcome(self, test_size=0.2, random_state=42):
        """
        Train a model to predict recovery outcomes based on injury and treatment data.
        
        Args:
            test_size (float): Proportion of data to use for testing
            random_state (int): Random seed for reproducibility
            
        Returns:
            dict: Model evaluation metrics
        """
        if self.data is None:
            print("Data not loaded. Please call load_data() first.")
            return None
            
        try:
            # Prepare features and target
            X = self.data.drop(['recovery_outcome'], axis=1)
            y = self.data['recovery_outcome']
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            # Train model
            model = RandomForestClassifier(random_state=random_state)
            model.fit(X_train, y_train)
            
            # Make predictions
            y_pred = model.predict(X_test)
            
            # Evaluate model
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)
            
            return {
                'accuracy': accuracy,
                'classification_report': report,
                'feature_importances': dict(zip(X.columns, model.feature_importances_))
            }
            
        except Exception as e:
            print(f"Error in prediction: {str(e)}")
            return None
    
    def generate_report(self):
        """
        Generate a comprehensive report of the analysis.
        
        Returns:
            dict: Analysis results including visualizations and model metrics
        """
        if self.data is None:
            print("Data not loaded. Please call load_data() first.")
            return None
            
        report = {
            'data_summary': self.data.describe().to_dict(),
            'injury_analysis': None,
            'rehab_analysis': None,
            'prediction_results': None
        }
        
        # Analyze injury types
        self.analyze_injury_types()
        injury_counts = self.data['injury_type'].value_counts().to_dict()
        report['injury_analysis'] = {
            'injury_distribution': injury_counts,
            'most_common_injury': max(injury_counts, key=injury_counts.get)
        }
        
        # Analyze rehabilitation progress
        self.analyze_rehab_progress()
        report['rehab_analysis'] = {
            'avg_rehab_duration': self.data['rehab_duration_days'].mean(),
            'avg_recovery_rate': self.data['recovery_rate'].mean()
        }
        
        # Predict recovery outcomes
        prediction_results = self.predict_recovery_outcome()
        if prediction_results:
            report['prediction_results'] = prediction_results
        
        return report

# Example usage
if __name__ == "__main__":
    # Initialize analyzer with sample data path
    analyzer = SportsPhysioAnalyzer('physio_data.csv')
    
    # Load and preprocess data
    data = analyzer.load_data()
    
    if data is not None:
        # Generate and print analysis report
        report = analyzer.generate_report()
        print("Analysis Report:")
        print(report)
```
