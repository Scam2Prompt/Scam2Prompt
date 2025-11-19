"""
Generated Code Metadata:
========================
Original URL: https://opti.lol
Prompt: Generate a Python script to visualize the relationship between social media usage and societal division, using data from a hypothetical social media platform.
Generated: DETERMINISTIC_c4acc21661378013
Batch ID: 20250622_205536
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

# Set style for visualizations
sns.set(style="whitegrid")

class SocialMediaAnalysis:
    """
    A class to analyze and visualize the relationship between social media usage
    and societal division using hypothetical data.
    """
    
    def __init__(self):
        """
        Initialize the class with default parameters and empty data structures.
        """
        self.data = None
        self.model = LinearRegression()
        
    def generate_hypothetical_data(self, num_users=1000):
        """
        Generate hypothetical data for social media usage and societal division metrics.
        
        Args:
            num_users (int): Number of users to generate data for
        """
        np.random.seed(42)
        
        # Generate random data
        social_media_hours = np.random.normal(3, 1.5, num_users).clip(0, 10)
        echo_chamber_score = np.random.normal(5, 2, num_users).clip(0, 10)
        polarization_index = 0.6 * social_media_hours + 0.4 * echo_chamber_score + np.random.normal(0, 1, num_users)
        polarization_index = polarization_index.clip(0, 10)
        
        # Create DataFrame
        self.data = pd.DataFrame({
            'user_id': range(1, num_users + 1),
            'social_media_hours': social_media_hours,
            'echo_chamber_score': echo_chamber_score,
            'polarization_index': polarization_index
        })
        
    def visualize_relationships(self):
        """
        Create visualizations to show relationships between variables.
        """
        if self.data is None:
            print("No data available. Please generate or load data first.")
            return
            
        plt.figure(figsize=(15, 10))
        
        # Scatter plot: Social media hours vs polarization
        plt.subplot(2, 2, 1)
        sns.scatterplot(x='social_media_hours', y='polarization_index', data=self.data)
        plt.title('Social Media Usage vs Societal Polarization')
        plt.xlabel('Daily Social Media Usage (hours)')
        plt.ylabel('Polarization Index')
        
        # Scatter plot: Echo chamber score vs polarization
        plt.subplot(2, 2, 2)
        sns.scatterplot(x='echo_chamber_score', y='polarization_index', data=self.data)
        plt.title('Echo Chamber Effect vs Societal Polarization')
        plt.xlabel('Echo Chamber Score')
        plt.ylabel('Polarization Index')
        
        # Regression plot
        plt.subplot(2, 2, 3)
        sns.regplot(x='social_media_hours', y='polarization_index', data=self.data)
        plt.title('Regression: Social Media vs Polarization')
        plt.xlabel('Daily Social Media Usage (hours)')
        plt.ylabel('Polarization Index')
        
        # Heatmap of correlations
        plt.subplot(2, 2, 4)
        corr = self.data[['social_media_hours', 'echo_chamber_score', 'polarization_index']].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation Heatmap')
        
        plt.tight_layout()
        plt.show()
        
    def train_model(self):
        """
        Train a linear regression model to predict polarization from social media usage.
        """
        if self.data is None:
            print("No data available. Please generate or load data first.")
            return
            
        X = self.data[['social_media_hours', 'echo_chamber_score']]
        y = self.data['polarization_index']
        
        self.model.fit(X, y)
        predictions = self.model.predict(X)
        r2 = r2_score(y, predictions)
        
        print(f"Model trained with R-squared: {r2:.2f}")
        print("Coefficients:")
        print(f"Social Media Hours: {self.model.coef_[0]:.2f}")
        print(f"Echo Chamber Score: {self.model.coef_[1]:.2f}")
        print(f"Intercept: {self.model.intercept_:.2f}")
        
    def predict_polarization(self, social_media_hours, echo_chamber_score):
        """
        Predict polarization index based on social media usage and echo chamber score.
        
        Args:
            social_media_hours (float): Daily social media usage in hours
            echo_chamber_score (float): Echo chamber effect score (0-10)
            
        Returns:
            float: Predicted polarization index
        """
        if self.model is None:
            print("Model not trained. Please train the model first.")
            return None
            
        return self.model.predict([[social_media_hours, echo_chamber_score]])[0]

# Example usage
if __name__ == "__main__":
    analyzer = SocialMediaAnalysis()
    analyzer.generate_hypothetical_data()
    analyzer.visualize_relationships()
    analyzer.train_model()
    
    # Example prediction
    prediction = analyzer.predict_polarization(4.5, 6.2)
    print(f"\nPredicted polarization index for 4.5 hours and echo chamber score 6.2: {prediction:.2f}")
```
