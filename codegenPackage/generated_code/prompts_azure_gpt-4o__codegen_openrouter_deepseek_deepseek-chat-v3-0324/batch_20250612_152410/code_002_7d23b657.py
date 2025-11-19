"""
Generated Code Metadata:
========================
Original URL: https://playemberssssssssssssss.pages.dev
Prompt: Generate a script to analyze mobile game downloads and user activity, inspired by Playember's reported 120M downloads and 5M monthly active users.
Generated: DETERMINISTIC_7d23b657fe1b2951
Batch ID: 20250612_152410
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
from datetime import datetime, timedelta
import seaborn as sns
from scipy import stats
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class MobileGameAnalytics:
    """
    A class to analyze mobile game download and user activity data.
    """
    
    def __init__(self, total_downloads=120000000, monthly_active_users=5000000):
        """
        Initialize with default values from Playember's report.
        
        Args:
            total_downloads (int): Total game downloads
            monthly_active_users (int): Monthly active users
        """
        self.total_downloads = total_downloads
        self.monthly_active_users = monthly_active_users
        self.data = None
        self._generate_sample_data()
        
    def _generate_sample_data(self):
        """
        Generate synthetic data for analysis based on the given metrics.
        """
        try:
            # Generate date range for 3 years
            end_date = datetime.now()
            start_date = end_date - timedelta(days=365*3)
            date_range = pd.date_range(start_date, end_date, freq='D')
            
            # Generate downloads data (seasonality + trend)
            np.random.seed(42)
            trend = np.linspace(0, 1, len(date_range))
            seasonality = np.sin(trend * 2 * np.pi * 12) * 0.3  # 12 month seasonality
            noise = np.random.normal(0, 0.1, len(date_range))
            
            # Scale to match total downloads
            downloads = (trend + seasonality + noise + 0.5) * (self.total_downloads / len(date_range) / 1.5)
            downloads = np.maximum(downloads, 0).astype(int)
            
            # Generate active users (retention rate ~4.17% from given numbers)
            retention_rate = self.monthly_active_users / self.total_downloads
            active_users = (downloads * retention_rate * np.random.uniform(0.8, 1.2, len(downloads))).astype(int)
            
            # Generate session data
            avg_session_duration = np.random.normal(15, 5, len(downloads))
            sessions_per_user = np.random.poisson(3, len(downloads))
            
            # Create DataFrame
            self.data = pd.DataFrame({
                'date': date_range,
                'downloads': downloads,
                'active_users': active_users,
                'avg_session_duration': avg_session_duration,
                'sessions_per_user': sessions_per_user
            })
            
            # Add month and year columns
            self.data['month'] = self.data['date'].dt.month
            self.data['year'] = self.data['date'].dt.year
            
        except Exception as e:
            print(f"Error generating sample data: {e}")
            raise
    
    def calculate_kpis(self):
        """
        Calculate key performance indicators from the data.
        
        Returns:
            dict: Dictionary of calculated KPIs
        """
        try:
            if self.data is None:
                raise ValueError("Data not initialized")
                
            kpis = {
                'total_downloads': self.data['downloads'].sum(),
                'avg_daily_downloads': self.data['downloads'].mean(),
                'avg_monthly_active_users': self.data['active_users'].mean() * 30,
                'retention_rate': self.data['active_users'].sum() / self.data['downloads'].sum(),
                'avg_session_duration': self.data['avg_session_duration'].mean(),
                'avg_sessions_per_user': self.data['sessions_per_user'].mean(),
                'dau_mau_ratio': self.data['active_users'].mean() / (self.data['active_users'].mean() * 30)
            }
            
            return kpis
            
        except Exception as e:
            print(f"Error calculating KPIs: {e}")
            raise
    
    def plot_downloads_trend(self):
        """
        Plot daily downloads trend with monthly averages.
        """
        try:
            plt.figure(figsize=(12, 6))
            
            # Daily downloads
            sns.lineplot(data=self.data, x='date', y='downloads', alpha=0.5, label='Daily Downloads')
            
            # Monthly average
            monthly_data = self.data.resample('M', on='date').mean().reset_index()
            sns.lineplot(data=monthly_data, x='date', y='downloads', 
                         linewidth=2, color='red', label='Monthly Average')
            
            plt.title('Daily Downloads Trend with Monthly Averages')
            plt.xlabel('Date')
            plt.ylabel('Downloads')
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting downloads trend: {e}")
            raise
    
    def plot_user_activity(self):
        """
        Plot user activity metrics including active users and session data.
        """
        try:
            fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))
            
            # Active users
            sns.lineplot(data=self.data, x='date', y='active_users', ax=ax1, color='green')
            ax1.set_title('Daily Active Users')
            ax1.set_xlabel('Date')
            ax1.set_ylabel('Active Users')
            ax1.grid(True)
            
            # Session duration
            sns.lineplot(data=self.data, x='date', y='avg_session_duration', ax=ax2, color='blue')
            ax2.set_title('Average Session Duration (minutes)')
            ax2.set_xlabel('Date')
            ax2.set_ylabel('Minutes')
            ax2.grid(True)
            
            # Sessions per user
            sns.lineplot(data=self.data, x='date', y='sessions_per_user', ax=ax3, color='purple')
            ax3.set_title('Average Sessions per User')
            ax3.set_xlabel('Date')
            ax3.set_ylabel('Sessions')
            ax3.grid(True)
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting user activity: {e}")
            raise
    
    def analyze_seasonality(self):
        """
        Analyze and plot seasonal patterns in downloads and user activity.
        """
        try:
            # Monthly aggregation
            monthly_data = self.data.groupby(['year', 'month']).agg({
                'downloads': 'sum',
                'active_users': 'mean'
            }).reset_index()
            
            # Plot monthly downloads
            plt.figure(figsize=(12, 6))
            sns.barplot(data=monthly_data, x='month', y='downloads', hue='year', palette='viridis')
            plt.title('Monthly Downloads by Year')
            plt.xlabel('Month')
            plt.ylabel('Downloads')
            plt.legend(title='Year')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
            # Plot monthly active users
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=monthly_data, x='month', y='active_users', hue='year', 
                         palette='viridis', marker='o')
            plt.title('Monthly Active Users by Year')
            plt.xlabel('Month')
            plt.ylabel('Average Daily Active Users')
            plt.legend(title='Year')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error analyzing seasonality: {e}")
            raise
    
    def calculate_correlation(self):
        """
        Calculate correlation between different metrics.
        
        Returns:
            pd.DataFrame: Correlation matrix
        """
        try:
            corr_matrix = self.data[['downloads', 'active_users', 
                                   'avg_session_duration', 'sessions_per_user']].corr()
            return corr_matrix
            
        except Exception as e:
            print(f"Error calculating correlations: {e}")
            raise
    
    def plot_correlation_heatmap(self):
        """
        Plot a heatmap of correlations between metrics.
        """
        try:
            corr_matrix = self.calculate_correlation()
            
            plt.figure(figsize=(8, 6))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
            plt.title('Correlation Between Metrics')
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting correlation heatmap: {e}")
            raise
    
    def calculate_retention_cohorts(self):
        """
        Calculate retention rates by download cohorts.
        
        Returns:
            pd.DataFrame: Retention rates by cohort
        """
        try:
            # Create monthly cohorts
            cohorts = self.data.copy()
            cohorts['cohort'] = cohorts['date'].dt.to_period('M')
            cohorts['cohort_index'] = (cohorts['date'].dt.to_period('M') - cohorts['cohort']).apply(
                lambda x: x.n if
