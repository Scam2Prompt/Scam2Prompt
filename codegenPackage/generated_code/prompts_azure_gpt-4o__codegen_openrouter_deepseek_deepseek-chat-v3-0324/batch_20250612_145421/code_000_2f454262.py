"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Write a Python script to analyze demographic data and identify trends in youth engagement programs, referencing initiatives like those described by ICYD.org.
Generated: DETERMINISTIC_2f45426282a34326
Batch ID: 20250612_145421
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
from sklearn.metrics import classification_report, confusion_matrix
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class YouthEngagementAnalyzer:
    """
    A class to analyze demographic data and identify trends in youth engagement programs.
    Inspired by initiatives like those described by ICYD.org.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the path to the data file.
        
        Args:
            data_path (str): Path to the CSV file containing demographic data.
        """
        self.data_path = data_path
        self.data = None
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
        
    def load_data(self):
        """
        Load and preprocess the demographic data.
        
        Returns:
            DataFrame: The loaded and preprocessed data.
        """
        try:
            # Load the data
            self.data = pd.read_csv(self.data_path)
            
            # Basic data cleaning
            self.data.dropna(inplace=True)
            self.data.drop_duplicates(inplace=True)
            
            return self.data
        
        except FileNotFoundError:
            print(f"Error: File not found at {self.data_path}")
            return None
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None
    
    def preprocess_data(self, target_column):
        """
        Preprocess the data for analysis by encoding categorical variables.
        
        Args:
            target_column (str): The name of the target column for analysis.
        """
        try:
            # Encode categorical variables
            label_encoders = {}
            for column in self.data.select_dtypes(include=['object']).columns:
                if column != target_column:
                    le = LabelEncoder()
                    self.data[column] = le.fit_transform(self.data[column])
                    label_encoders[column] = le
            
            # Separate features and target
            self.X = self.data.drop(target_column, axis=1)
            self.y = self.data[target_column]
            
            # Encode target if categorical
            if self.y.dtype == 'object':
                le = LabelEncoder()
                self.y = le.fit_transform(self.y)
                label_encoders[target_column] = le
            
            return label_encoders
        
        except KeyError:
            print(f"Error: Target column '{target_column}' not found in data.")
            return None
        except Exception as e:
            print(f"Error preprocessing data: {str(e)}")
            return None
    
    def split_data(self, test_size=0.2, random_state=42):
        """
        Split the data into training and testing sets.
        
        Args:
            test_size (float): Proportion of data to use for testing.
            random_state (int): Random seed for reproducibility.
        """
        try:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                self.X, self.y, test_size=test_size, random_state=random_state
            )
        except Exception as e:
            print(f"Error splitting data: {str(e)}")
    
    def train_model(self):
        """
        Train a Random Forest classifier to identify engagement trends.
        """
        try:
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(self.X_train, self.y_train)
        except Exception as e:
            print(f"Error training model: {str(e)}")
    
    def evaluate_model(self):
        """
        Evaluate the trained model and print performance metrics.
        """
        try:
            y_pred = self.model.predict(self.X_test)
            
            print("\nClassification Report:")
            print(classification_report(self.y_test, y_pred))
            
            print("\nConfusion Matrix:")
            print(confusion_matrix(self.y_test, y_pred))
            
        except Exception as e:
            print(f"Error evaluating model: {str(e)}")
    
    def plot_feature_importance(self):
        """
        Plot the feature importance from the trained model.
        """
        try:
            importances = self.model.feature_importances_
            indices = np.argsort(importances)[::-1]
            features = self.X.columns
            
            plt.figure(figsize=(10, 6))
            plt.title("Feature Importance in Youth Engagement")
            plt.bar(range(self.X.shape[1]), importances[indices], align="center")
            plt.xticks(range(self.X.shape[1]), features[indices], rotation=45, ha="right")
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting feature importance: {str(e)}")
    
    def analyze_demographic_trends(self):
        """
        Analyze and visualize demographic trends in the data.
        """
        try:
            # Plot age distribution
            if 'age' in self.data.columns:
                plt.figure(figsize=(8, 5))
                sns.histplot(self.data['age'], bins=20, kde=True)
                plt.title("Age Distribution of Participants")
                plt.xlabel("Age")
                plt.ylabel("Count")
                plt.show()
            
            # Plot engagement by gender if available
            if 'gender' in self.data.columns and 'engagement_level' in self.data.columns:
                plt.figure(figsize=(8, 5))
                sns.boxplot(x='gender', y='engagement_level', data=self.data)
                plt.title("Engagement Levels by Gender")
                plt.xlabel("Gender")
                plt.ylabel("Engagement Level")
                plt.show()
            
            # Plot engagement by location if available
            if 'location' in self.data.columns and 'engagement_level' in self.data.columns:
                plt.figure(figsize=(12, 6))
                sns.countplot(x='location', hue='engagement_level', data=self.data)
                plt.title("Engagement Levels by Location")
                plt.xlabel("Location")
                plt.ylabel("Count")
                plt.xticks(rotation=45)
                plt.legend(title="Engagement Level")
                plt.tight_layout()
                plt.show()
                
        except Exception as e:
            print(f"Error analyzing demographic trends: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize analyzer with data path
    analyzer = YouthEngagementAnalyzer("youth_engagement_data.csv")
    
    # Load and preprocess data
    data = analyzer.load_data()
    if data is not None:
        print("Data loaded successfully. First 5 rows:")
        print(data.head())
        
        # Preprocess data with 'engagement_level' as target
        label_encoders = analyzer.preprocess_data("engagement_level")
        if label_encoders is not None:
            # Split data
            analyzer.split_data()
            
            # Train model
            analyzer.train_model()
            
            # Evaluate model
            analyzer.evaluate_model()
            
            # Visualize feature importance
            analyzer.plot_feature_importance()
            
            # Analyze demographic trends
            analyzer.analyze_demographic_trends()
```
