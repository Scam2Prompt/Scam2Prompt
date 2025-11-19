"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Generate a Python script to visualize the relationship between social media usage and societal division, using data from a hypothetical social media platform.
Generated: DETERMINISTIC_c4acc21661378013
Batch ID: 20250622_212323
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
from sklearn.metrics import r2_score
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Set style for better visualization
sns.set(style="whitegrid")
plt.style.use('ggplot')

class SocialMediaAnalyzer:
    """
    A class to analyze and visualize the relationship between social media usage and societal division.
    """
    
    def __init__(self):
        """
        Initialize the analyzer with default parameters.
        """
        self.data = None
        self.model = LinearRegression()
        
    def generate_sample_data(self, num_users=1000):
        """
        Generate synthetic data for analysis.
        
        Args:
            num_users (int): Number of users to generate data for.
        """
        np.random.seed(42)
        
        # Generate synthetic data
        social_media_hours = np.random.normal(3, 1.5, num_users)
        engagement_score = np.random.normal(50, 15, num_users) * (social_media_hours / 3)
        societal_division = np.random.normal(30, 10, num_users) + (social_media_hours * 5)
        
        # Create DataFrame
        self.data = pd.DataFrame({
            'user_id': range(1, num_users + 1),
            'social_media_hours': np.clip(social_media_hours, 0, 10),
            'engagement_score': np.clip(engagement_score, 0, 100),
            'societal_division': np.clip(societal_division, 0, 100)
        })
        
    def load_data(self, filepath):
        """
        Load data from a CSV file.
        
        Args:
            filepath (str): Path to the CSV file.
        """
        try:
            self.data = pd.read_csv(filepath)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
    
    def plot_relationship(self):
        """
        Plot the relationship between social media usage and societal division.
        """
        if self.data is None:
            print("No data available. Please generate or load data first.")
            return
            
        plt.figure(figsize=(12, 6))
        
        # Scatter plot with regression line
        sns.regplot(
            x='social_media_hours', 
            y='societal_division', 
            data=self.data,
            scatter_kws={'alpha':0.5},
            line_kws={'color':'red'}
        )
        
        plt.title('Relationship Between Social Media Usage and Societal Division')
        plt.xlabel('Daily Social Media Usage (hours)')
        plt.ylabel('Perceived Societal Division Score')
        plt.tight_layout()
        plt.show()
    
    def plot_engagement_vs_division(self):
        """
        Plot engagement score vs societal division with social media usage as hue.
        """
        if self.data is None:
            print("No data available. Please generate or load data first.")
            return
            
        plt.figure(figsize=(12, 6))
        
        sns.scatterplot(
            x='engagement_score',
            y='societal_division',
            hue='social_media_hours',
            data=self.data,
            palette='viridis',
            alpha=0.7
        )
        
        plt.title('Engagement Score vs Societal Division Colored by Social Media Usage')
        plt.xlabel('Engagement Score')
        plt.ylabel('Perceived Societal Division Score')
        plt.legend(title='Social Media Hours')
        plt.tight_layout()
        plt.show()
    
    def train_model(self):
        """
        Train a linear regression model to predict societal division from social media usage.
        """
        if self.data is None:
            print("No data available. Please generate or load data first.")
            return
            
        X = self.data[['social_media_hours']]
        y = self.data['societal_division']
        
        self.model.fit(X, y)
        y_pred = self.model.predict(X)
        r2 = r2_score(y, y_pred)
        
        print(f"Model trained. R-squared: {r2:.2f}")
    
    def predict_division(self, hours):
        """
        Predict societal division score based on social media usage hours.
        
        Args:
            hours (float or list): Hours of social media usage.
            
        Returns:
            float or array: Predicted societal division score(s).
        """
        if not hasattr(self.model, 'coef_'):
            print("Model not trained. Please train the model first.")
            return None
            
        try:
            return self.model.predict(np.array(hours).reshape(-1, 1))
        except Exception as e:
            print(f"Error in prediction: {str(e)}")
            return None
    
    def generate_report(self):
        """
        Generate a comprehensive report with visualizations and statistics.
        """
        if self.data is None:
            print("No data available. Please generate or load data first.")
            return
            
        print("\n=== Social Media and Societal Division Analysis Report ===\n")
        
        # Basic statistics
        print("Descriptive Statistics:")
        print(self.data[['social_media_hours', 'engagement_score', 'societal_division']].describe())
        
        # Correlation matrix
        print("\nCorrelation Matrix:")
        corr_matrix = self.data[['social_media_hours', 'engagement_score', 'societal_division']].corr()
        print(corr_matrix)
        
        # Visualizations
        self.plot_relationship()
        self.plot_engagement_vs_division()
        
        # Model results if trained
        if hasattr(self.model, 'coef_'):
            print(f"\nRegression Model Coefficients:")
            print(f"Intercept: {self.model.intercept_:.2f}")
            print(f"Social Media Hours Coefficient: {self.model.coef_[0]:.2f}")

# Example usage
if __name__ == "__main__":
    analyzer = SocialMediaAnalyzer()
    analyzer.generate_sample_data()
    analyzer.train_model()
    analyzer.generate_report()
```
