"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: "Write a Python code to analyze the impact of strategic planning on organizational performance, considering factors such as goal achievement and employee engagement, as discussed in Matter's consulting approach."
Generated: DETERMINISTIC_c1a13375a5de0c1e
Batch ID: 20250622_210650
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

class OrganizationalPerformanceAnalyzer:
    """
    A class to analyze the impact of strategic planning on organizational performance.
    Considers factors like goal achievement and employee engagement.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the analyzer with optional data path.
        
        Args:
            data_path (str, optional): Path to CSV file containing organizational data.
                                      If None, generates synthetic data.
        """
        self.data = None
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
        if data_path:
            self.load_data(data_path)
        else:
            self.generate_synthetic_data()
    
    def load_data(self, data_path):
        """
        Load organizational data from CSV file.
        
        Args:
            data_path (str): Path to CSV file.
        
        Raises:
            FileNotFoundError: If file doesn't exist.
            ValueError: If file is not a valid CSV or missing required columns.
        """
        try:
            self.data = pd.read_csv(data_path)
            required_columns = {'strategic_planning', 'goal_achievement', 'employee_engagement', 'performance'}
            if not required_columns.issubset(self.data.columns):
                raise ValueError("CSV file is missing required columns")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {data_path}")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def generate_synthetic_data(self, n_samples=500):
        """
        Generate synthetic organizational data for analysis.
        
        Args:
            n_samples (int): Number of samples to generate.
        """
        np.random.seed(42)
        
        # Generate strategic planning scores (1-5 scale)
        strategic_planning = np.random.randint(1, 6, size=n_samples)
        
        # Generate goal achievement (positively correlated with strategic planning)
        goal_achievement = strategic_planning * 0.6 + np.random.normal(0, 0.5, size=n_samples)
        goal_achievement = np.clip(goal_achievement, 1, 5)
        
        # Generate employee engagement (positively correlated with strategic planning)
        employee_engagement = strategic_planning * 0.4 + np.random.normal(0, 0.7, size=n_samples)
        employee_engagement = np.clip(employee_engagement, 1, 5)
        
        # Generate performance metric (dependent variable)
        performance = (strategic_planning * 0.5 + 
                      goal_achievement * 0.3 + 
                      employee_engagement * 0.2 + 
                      np.random.normal(0, 0.3, size=n_samples))
        performance = np.clip(performance, 1, 10)
        
        self.data = pd.DataFrame({
            'strategic_planning': strategic_planning,
            'goal_achievement': goal_achievement,
            'employee_engagement': employee_engagement,
            'performance': performance
        })
    
    def preprocess_data(self):
        """
        Preprocess data for analysis.
        """
        # Ensure no missing values
        if self.data.isnull().any().any():
            self.data = self.data.dropna()
        
        # Normalize performance metric to 0-1 scale
        self.data['performance_norm'] = (self.data['performance'] - self.data['performance'].min()) / \
                                       (self.data['performance'].max() - self.data['performance'].min())
    
    def train_model(self):
        """
        Train a linear regression model to analyze impact.
        """
        try:
            # Prepare features and target
            X = self.data[['strategic_planning', 'goal_achievement', 'employee_engagement']]
            y = self.data['performance_norm']
            
            # Split data
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Train model
            self.model = LinearRegression()
            self.model.fit(self.X_train, self.y_train)
            
            # Evaluate model
            y_pred = self.model.predict(self.X_test)
            mse = mean_squared_error(self.y_test, y_pred)
            r2 = r2_score(self.y_test, y_pred)
            
            print(f"Model trained successfully. MSE: {mse:.4f}, R2: {r2:.4f}")
            
        except Exception as e:
            raise RuntimeError(f"Error training model: {str(e)}")
    
    def analyze_impact(self):
        """
        Analyze the impact of strategic planning and other factors on performance.
        
        Returns:
            dict: Analysis results including coefficients and statistics.
        """
        if not self.model:
            raise RuntimeError("Model not trained. Call train_model() first.")
        
        try:
            # Get coefficients
            coefficients = {
                'strategic_planning': self.model.coef_[0],
                'goal_achievement': self.model.coef_[1],
                'employee_engagement': self.model.coef_[2],
                'intercept': self.model.intercept_
            }
            
            # OLS summary for statistical significance
            X = sm.add_constant(self.X_train)
            ols_model = sm.OLS(self.y_train, X).fit()
            
            return {
                'coefficients': coefficients,
                'ols_summary': ols_model.summary(),
                'feature_importance': self._get_feature_importance()
            }
            
        except Exception as e:
            raise RuntimeError(f"Error analyzing impact: {str(e)}")
    
    def _get_feature_importance(self):
        """
        Calculate relative feature importance.
        
        Returns:
            dict: Normalized feature importance scores.
        """
        importance = np.abs(self.model.coef_)
        importance = importance / importance.sum()
        return dict(zip(self.X_train.columns, importance))
    
    def visualize_results(self):
        """
        Generate visualizations of the analysis.
        """
        try:
            plt.figure(figsize=(15, 10))
            
            # Scatter plot: Strategic Planning vs Performance
            plt.subplot(2, 2, 1)
            sns.regplot(x='strategic_planning', y='performance_norm', data=self.data)
            plt.title('Strategic Planning vs Performance')
            
            # Scatter plot: Goal Achievement vs Performance
            plt.subplot(2, 2, 2)
            sns.regplot(x='goal_achievement', y='performance_norm', data=self.data)
            plt.title('Goal Achievement vs Performance')
            
            # Scatter plot: Employee Engagement vs Performance
            plt.subplot(2, 2, 3)
            sns.regplot(x='employee_engagement', y='performance_norm', data=self.data)
            plt.title('Employee Engagement vs Performance')
            
            # Feature importance bar plot
            plt.subplot(2, 2, 4)
            importance = self._get_feature_importance()
            sns.barplot(x=list(importance.values()), y=list(importance.keys()))
            plt.title('Feature Importance')
            plt.xlabel('Relative Importance')
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            raise RuntimeError(f"Error generating visualizations: {str(e)}")

# Example usage
if __name__ == "__main__":
    analyzer = OrganizationalPerformanceAnalyzer()
    analyzer.preprocess_data()
    analyzer.train_model()
    results = analyzer.analyze_impact()
    analyzer.visualize_results()
```
