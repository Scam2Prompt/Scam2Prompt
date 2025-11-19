"""
Generated Code Metadata:
========================
Original URL: https://lalitarora.in
Prompt: Write code to analyze business growth metrics using actionable insights, following the growth hacking principles discussed by Dr. Lalit Arora.
Generated: DETERMINISTIC_a29b78a7ddf723b3
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
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

class GrowthAnalyzer:
    """
    A class to analyze business growth metrics and provide actionable insights
    based on growth hacking principles.
    """
    
    def __init__(self, data_path):
        """
        Initialize the GrowthAnalyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing business metrics
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            self._preprocess_data()
            print("Data loaded and preprocessed successfully.")
        except Exception as e:
            print(f"Error initializing GrowthAnalyzer: {str(e)}")
            raise
    
    def _validate_data(self):
        """Validate the input data for required columns and data quality."""
        required_columns = ['date', 'revenue', 'customers', 'acquisition_cost', 'retention_rate']
        missing_cols = [col for col in required_columns if col not in self.data.columns]
        
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
        if self.data.isnull().values.any():
            raise ValueError("Data contains missing values")
    
    def _preprocess_data(self):
        """Preprocess the data for analysis."""
        # Convert date to datetime
        self.data['date'] = pd.to_datetime(self.data['date'])
        
        # Calculate derived metrics
        self.data['customer_lifetime_value'] = self.data['revenue'] / self.data['customers']
        self.data['roi'] = (self.data['revenue'] - self.data['acquisition_cost']) / self.data['acquisition_cost']
        self.data['growth_rate'] = self.data['revenue'].pct_change() * 100
        
        # Sort by date
        self.data.sort_values('date', inplace=True)
    
    def plot_growth_trends(self):
        """Plot key growth metrics over time."""
        plt.figure(figsize=(15, 10))
        
        plt.subplot(2, 2, 1)
        sns.lineplot(x='date', y='revenue', data=self.data)
        plt.title('Revenue Growth')
        
        plt.subplot(2, 2, 2)
        sns.lineplot(x='date', y='customers', data=self.data)
        plt.title('Customer Growth')
        
        plt.subplot(2, 2, 3)
        sns.lineplot(x='date', y='growth_rate', data=self.data)
        plt.title('Growth Rate (%)')
        
        plt.subplot(2, 2, 4)
        sns.lineplot(x='date', y='roi', data=self.data)
        plt.title('Return on Investment')
        
        plt.tight_layout()
        plt.show()
    
    def calculate_correlation(self):
        """Calculate correlation between different growth metrics."""
        corr_matrix = self.data[['revenue', 'customers', 'acquisition_cost', 
                                'retention_rate', 'customer_lifetime_value', 'roi']].corr()
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Matrix of Growth Metrics')
        plt.show()
        
        return corr_matrix
    
    def analyze_growth_drivers(self):
        """
        Identify key drivers of growth using linear regression.
        Returns coefficients showing impact of each factor on revenue.
        """
        X = self.data[['customers', 'acquisition_cost', 'retention_rate']]
        y = self.data['revenue']
        
        model = LinearRegression()
        model.fit(X, y)
        
        coefficients = pd.DataFrame({
            'feature': X.columns,
            'coefficient': model.coef_,
            'abs_impact': np.abs(model.coef_)
        }).sort_values('abs_impact', ascending=False)
        
        r2 = r2_score(y, model.predict(X))
        print(f"Model R-squared: {r2:.2f}")
        
        return coefficients
    
    def calculate_aarrr_metrics(self):
        """
        Calculate metrics based on the AARRR (Pirate Metrics) framework:
        - Acquisition
        - Activation
        - Retention
        - Revenue
        - Referral
        """
        metrics = {
            'acquisition_rate': self.data['customers'].pct_change().mean() * 100,
            'activation_rate': 0.7,  # Placeholder - would normally come from user data
            'retention_rate': self.data['retention_rate'].mean(),
            'revenue_per_user': self.data['customer_lifetime_value'].mean(),
            'referral_rate': 0.15  # Placeholder - would normally come from referral data
        }
        
        return pd.DataFrame.from_dict(metrics, orient='index', columns=['value'])
    
    def generate_actionable_insights(self):
        """Generate actionable insights based on the analysis."""
        insights = []
        
        # Growth rate analysis
        avg_growth = self.data['growth_rate'].mean()
        if avg_growth < 5:
            insights.append("🚨 Warning: Low average growth rate (<5%). Focus on customer acquisition and retention.")
        else:
            insights.append(f"✅ Healthy average growth rate: {avg_growth:.1f}%")
        
        # ROI analysis
        avg_roi = self.data['roi'].mean()
        if avg_roi < 2:
            insights.append("🚨 Low ROI detected. Optimize acquisition costs or increase customer value.")
        else:
            insights.append(f"✅ Strong ROI: {avg_roi:.1f}x return on investment")
        
        # Retention analysis
        avg_retention = self.data['retention_rate'].mean()
        if avg_retention < 0.7:
            insights.append("🚨 Low retention rate. Implement retention strategies like loyalty programs.")
        else:
            insights.append(f"✅ Good retention rate: {avg_retention:.1%}")
        
        # Growth drivers
        drivers = self.analyze_growth_drivers()
        top_driver = drivers.iloc[0]['feature']
        insights.append(f"📈 Top growth driver: {top_driver.replace('_', ' ').title()}")
        
        return insights
    
    def forecast_growth(self, periods=6):
        """
        Forecast future growth using linear regression.
        
        Args:
            periods (int): Number of future periods to forecast
        """
        # Prepare data
        self.data['period'] = range(len(self.data))
        X = self.data[['period']]
        y = self.data['revenue']
        
        # Train model
        model = LinearRegression()
        model.fit(X, y)
        
        # Create future periods
        future_periods = range(len(self.data), len(self.data) + periods)
        future_X = pd.DataFrame({'period': future_periods})
        future_dates = pd.date_range(
            start=self.data['date'].iloc[-1],
            periods=periods + 1,
            freq='M'
        )[1:]
        
        # Predict
        forecast = model.predict(future_X)
        
        # Create results dataframe
        results = pd.DataFrame({
            'date': future_dates,
            'forecasted_revenue': forecast,
            'period': future_periods
        })
        
        # Plot results
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['date'], self.data['revenue'], label='Historical')
        plt.plot(results['date'], results['forecasted_revenue'], label='Forecast', linestyle='--')
        plt.title('Revenue Forecast')
        plt.xlabel('Date')
        plt.ylabel('Revenue')
        plt.legend()
        plt.grid(True)
        plt.show()
        
        return results

# Example usage
if __name__ == "__main__":
    try:
        analyzer = GrowthAnalyzer('business_metrics.csv')
        
        # Generate insights
        print("\nActionable Insights:")
        for insight in analyzer.generate_actionable_insights():
            print(f"- {insight}")
            
        # Show visualizations
        analyzer.plot_growth_trends()
        analyzer.calculate_correlation()
        
        # Forecast
        forecast = analyzer.forecast_growth()
        print("\nRevenue Forecast:")
        print(forecast[['date', 'forecasted_revenue']].to_string(index=False))
        
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
```
