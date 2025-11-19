"""
Generated Code Metadata:
========================
Original URL: https://abilityfordisabilityfund.com
Prompt: Develop a Python script that analyzes donation trends and provides insights for a disability fund organization.
Generated: DETERMINISTIC_49d9f8b9336dae92
Batch ID: 20250622_205926
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
from datetime import datetime
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class DonationAnalyzer:
    """
    A class to analyze donation trends and provide insights for a disability fund organization.
    """
    
    def __init__(self, data_path):
        """
        Initialize the DonationAnalyzer with data from the specified path.
        
        Args:
            data_path (str): Path to the donation data file (CSV format expected)
        """
        try:
            self.df = pd.read_csv(data_path)
            self._validate_data()
            self._preprocess_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {data_path}")
        except Exception as e:
            raise Exception(f"Error initializing DonationAnalyzer: {str(e)}")
    
    def _validate_data(self):
        """
        Validate the input data has required columns.
        """
        required_columns = {'donation_amount', 'donation_date', 'donor_id', 'campaign'}
        if not required_columns.issubset(self.df.columns):
            missing = required_columns - set(self.df.columns)
            raise ValueError(f"Missing required columns: {missing}")
    
    def _preprocess_data(self):
        """
        Preprocess the data by cleaning and transforming columns.
        """
        # Convert donation_date to datetime
        self.df['donation_date'] = pd.to_datetime(self.df['donation_date'])
        
        # Extract year and month from donation_date
        self.df['year'] = self.df['donation_date'].dt.year
        self.df['month'] = self.df['donation_date'].dt.month
        
        # Create a year-month column for easier grouping
        self.df['year_month'] = self.df['donation_date'].dt.to_period('M')
        
        # Remove any negative donations (if they exist)
        self.df = self.df[self.df['donation_amount'] > 0]
    
    def get_summary_statistics(self):
        """
        Get summary statistics for donations.
        
        Returns:
            dict: Dictionary containing various summary statistics
        """
        stats = {
            'total_donations': self.df['donation_amount'].sum(),
            'average_donation': self.df['donation_amount'].mean(),
            'median_donation': self.df['donation_amount'].median(),
            'num_donations': len(self.df),
            'num_unique_donors': self.df['donor_id'].nunique(),
            'num_campaigns': self.df['campaign'].nunique(),
            'first_donation_date': self.df['donation_date'].min(),
            'last_donation_date': self.df['donation_date'].max()
        }
        return stats
    
    def plot_donation_trends(self, period='monthly'):
        """
        Plot donation trends over time.
        
        Args:
            period (str): Time period to group by ('monthly' or 'yearly')
        """
        plt.figure(figsize=(12, 6))
        
        if period == 'monthly':
            grouped = self.df.groupby('year_month')['donation_amount'].sum()
            title = 'Monthly Donation Trends'
            xlabel = 'Month'
        elif period == 'yearly':
            grouped = self.df.groupby('year')['donation_amount'].sum()
            title = 'Yearly Donation Trends'
            xlabel = 'Year'
        else:
            raise ValueError("Period must be either 'monthly' or 'yearly'")
        
        grouped.plot(kind='line', marker='o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel('Total Donations ($)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def plot_donation_distribution(self):
        """
        Plot the distribution of donation amounts.
        """
        plt.figure(figsize=(12, 6))
        sns.histplot(self.df['donation_amount'], bins=30, kde=True)
        plt.title('Distribution of Donation Amounts')
        plt.xlabel('Donation Amount ($)')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def plot_top_campaigns(self, top_n=10):
        """
        Plot the top campaigns by total donations.
        
        Args:
            top_n (int): Number of top campaigns to display
        """
        campaign_totals = self.df.groupby('campaign')['donation_amount'].sum().sort_values(ascending=False)
        
        plt.figure(figsize=(12, 6))
        campaign_totals.head(top_n).plot(kind='bar')
        plt.title(f'Top {top_n} Campaigns by Total Donations')
        plt.xlabel('Campaign')
        plt.ylabel('Total Donations ($)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    
    def plot_donor_segmentation(self):
        """
        Plot donor segmentation by donation frequency and amount.
        """
        donor_stats = self.df.groupby('donor_id').agg(
            total_donated=('donation_amount', 'sum'),
            donation_count=('donor_id', 'count')
        ).reset_index()
        
        plt.figure(figsize=(12, 6))
        sns.scatterplot(
            data=donor_stats,
            x='donation_count',
            y='total_donated',
            alpha=0.6
        )
        plt.title('Donor Segmentation by Frequency and Amount')
        plt.xlabel('Number of Donations')
        plt.ylabel('Total Donated ($)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def predict_future_donations(self, forecast_months=6):
        """
        Predict future donations using linear regression.
        
        Args:
            forecast_months (int): Number of months to forecast ahead
            
        Returns:
            tuple: (predicted_values, model_score)
        """
        # Prepare time series data
        monthly_data = self.df.groupby('year_month')['donation_amount'].sum().reset_index()
        monthly_data['time_index'] = range(len(monthly_data))
        
        # Split data into features and target
        X = monthly_data[['time_index']]
        y = monthly_data['donation_amount']
        
        # Split into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train the model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate model performance
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        # Forecast future months
        last_index = monthly_data['time_index'].max()
        future_indices = np.array(range(last_index + 1, last_index + forecast_months + 1)).reshape(-1, 1)
        future_predictions = model.predict(future_indices)
        
        # Plot historical and predicted values
        plt.figure(figsize=(12, 6))
        plt.plot(monthly_data['year_month'].astype(str), monthly_data['donation_amount'], label='Historical')
        
        # Create future dates for plotting
        last_date = monthly_data['year_month'].max()
        future_dates = pd.period_range(
            start=last_date + 1,
            periods=forecast_months,
            freq='M'
        )
        
        plt.plot(future_dates.astype(str), future_predictions, 'r--', label='Forecast')
        plt.title('Donation Trend Forecast')
        plt.xlabel('Time')
        plt.ylabel('Donation Amount ($)')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
        return future_predictions, r2
    
    def generate_report(self, output_file='donation_report.txt'):
        """
        Generate a comprehensive report of donation insights.
        
        Args:
            output_file (str): Path to save the report
        """
        stats = self.get_summary_statistics()
        
        with open(output_file, 'w') as f:
            f.write("=== Disability Fund Donation Analysis Report ===\n\n")
            f.write(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("Summary Statistics:\n")
            f.write(f"- Total donations received: ${stats['total_donations']:,.2f}\n")
            f.write(f"- Number of donations: {stats['num_donations']:,}\n")
            f.write(f"- Average
