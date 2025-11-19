"""
Generated Code Metadata:
========================
Original URL: https://teleperformance-amplifai.com
Prompt: Write code to visualize employee engagement trends using AI, referencing AmplifAI's features.
Generated: DETERMINISTIC_b9c56256ade83ae6
Batch ID: 20250612_151504
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
from sklearn.preprocessing import PolynomialFeatures
from datetime import datetime
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class EmployeeEngagementVisualizer:
    """
    A class to visualize employee engagement trends with AI-powered insights.
    Inspired by AmplifAI's engagement analytics features.
    """
    
    def __init__(self, data_path):
        """
        Initialize the visualizer with employee engagement data.
        
        Args:
            data_path (str): Path to the CSV file containing engagement data
        """
        self.data = pd.read_csv(data_path)
        self._preprocess_data()
        
    def _preprocess_data(self):
        """Preprocess the engagement data for analysis."""
        # Convert date column to datetime
        self.data['date'] = pd.to_datetime(self.data['date'])
        
        # Calculate engagement score if not present
        if 'engagement_score' not in self.data.columns:
            self.data['engagement_score'] = (
                self.data[['participation_rate', 'satisfaction_score', 'productivity_score']]
                .mean(axis=1)
                .round(2)
            )
        
        # Sort by date
        self.data = self.data.sort_values('date')
        
    def plot_trend_over_time(self):
        """
        Plot engagement trends over time with AI-powered trend line.
        Similar to AmplifAI's time-series analytics.
        """
        plt.figure(figsize=(12, 6))
        
        # Actual engagement data
        sns.lineplot(
            x='date', 
            y='engagement_score', 
            data=self.data, 
            label='Actual Engagement',
            marker='o'
        )
        
        # AI-powered trend prediction
        self._add_ai_trend_line()
        
        plt.title('Employee Engagement Trends with AI-Powered Projection')
        plt.xlabel('Date')
        plt.ylabel('Engagement Score')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
    def _add_ai_trend_line(self):
        """Add AI-powered polynomial trend line to the plot."""
        # Prepare data for regression
        X = np.array(range(len(self.data))).reshape(-1, 1)
        y = self.data['engagement_score'].values
        
        # Create polynomial features
        poly = PolynomialFeatures(degree=2)
        X_poly = poly.fit_transform(X)
        
        # Train model
        model = LinearRegression()
        model.fit(X_poly, y)
        
        # Predict trend
        trend = model.predict(X_poly)
        
        # Plot trend line
        plt.plot(
            self.data['date'], 
            trend, 
            '--', 
            color='red', 
            label='AI Trend Projection'
        )
        
    def plot_engagement_distribution(self):
        """
        Plot distribution of engagement scores across employees.
        Similar to AmplifAI's engagement segmentation.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(
            self.data['engagement_score'], 
            bins=10, 
            kde=True,
            color='skyblue'
        )
        
        plt.title('Distribution of Employee Engagement Scores')
        plt.xlabel('Engagement Score')
        plt.ylabel('Number of Employees')
        plt.axvline(
            self.data['engagement_score'].mean(), 
            color='red', 
            linestyle='--', 
            label=f'Mean: {self.data["engagement_score"].mean():.2f}'
        )
        plt.legend()
        plt.tight_layout()
        plt.show()
        
    def plot_driver_analysis(self):
        """
        Plot impact of different drivers on engagement.
        Similar to AmplifAI's driver analysis.
        """
        if not all(col in self.data.columns for col in ['training_hours', 'manager_support', 'recognition']):
            print("Warning: Driver columns not found in data")
            return
            
        plt.figure(figsize=(10, 6))
        
        drivers = ['training_hours', 'manager_support', 'recognition']
        correlations = [self.data['engagement_score'].corr(self.data[driver]) for driver in drivers]
        
        sns.barplot(
            x=drivers,
            y=correlations,
            palette='viridis'
        )
        
        plt.title('Impact of Different Drivers on Engagement')
        plt.xlabel('Engagement Driver')
        plt.ylabel('Correlation with Engagement Score')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    def generate_insights_report(self):
        """
        Generate AI-powered insights about engagement trends.
        Similar to AmplifAI's automated insights.
        """
        insights = []
        
        # Trend analysis
        latest_score = self.data['engagement_score'].iloc[-1]
        earliest_score = self.data['engagement_score'].iloc[0]
        trend_direction = "increased" if latest_score > earliest_score else "decreased"
        trend_percentage = abs((latest_score - earliest_score) / earliest_score * 100)
        
        insights.append(
            f"Engagement has {trend_direction} by {trend_percentage:.1f}% over the period."
        )
        
        # Driver analysis
        if all(col in self.data.columns for col in ['training_hours', 'manager_support', 'recognition']):
            strongest_driver = max(
                ['training_hours', 'manager_support', 'recognition'],
                key=lambda x: abs(self.data['engagement_score'].corr(self.data[x]))
            )
            insights.append(
                f"The strongest engagement driver is {strongest_driver.replace('_', ' ')}."
            )
        
        # Segmentation insight
        low_engagement = (self.data['engagement_score'] < 5).mean() * 100
        if low_engagement > 20:
            insights.append(
                f"Warning: {low_engagement:.1f}% of employees have low engagement (<5)."
            )
        
        print("\nAI-Generated Engagement Insights:\n" + "-"*40)
        for i, insight in enumerate(insights, 1):
            print(f"{i}. {insight}")

# Example usage
if __name__ == "__main__":
    # Sample data (in a real scenario, this would be loaded from a file)
    sample_data = {
        'date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
        'participation_rate': [75, 78, 82, 80, 85],
        'satisfaction_score': [7.2, 7.5, 7.8, 7.6, 8.0],
        'productivity_score': [6.8, 7.0, 7.2, 7.1, 7.5],
        'training_hours': [5, 6, 7, 6, 8],
        'manager_support': [7.5, 7.7, 8.0, 7.8, 8.2],
        'recognition': [6.0, 6.5, 7.0, 6.8, 7.5]
    }
    
    # Create DataFrame and save to CSV for demo
    df = pd.DataFrame(sample_data)
    df.to_csv('employee_engagement_sample.csv', index=False)
    
    # Initialize visualizer and generate plots
    visualizer = EmployeeEngagementVisualizer('employee_engagement_sample.csv')
    visualizer.plot_trend_over_time()
    visualizer.plot_engagement_distribution()
    visualizer.plot_driver_analysis()
    visualizer.generate_insights_report()
```
