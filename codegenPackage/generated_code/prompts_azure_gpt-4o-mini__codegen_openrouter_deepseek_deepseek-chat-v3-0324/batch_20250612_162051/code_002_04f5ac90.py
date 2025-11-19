"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Create a Python script that analyzes the effectiveness of promotional campaigns, similar to the services offered by NMKT for small and medium enterprises.
Generated: DETERMINISTIC_04f5ac9017d42679
Batch ID: 20250612_162051
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
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('campaign_analysis.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class CampaignAnalyzer:
    """
    A class to analyze the effectiveness of promotional campaigns.
    """
    
    def __init__(self, data_path):
        """
        Initialize the CampaignAnalyzer with data from the given path.
        
        Args:
            data_path (str): Path to the CSV file containing campaign data.
        """
        self.data_path = data_path
        self.data = None
        self.campaigns = None
        self.models = {}
        
    def load_data(self):
        """
        Load and preprocess the campaign data.
        
        Raises:
            FileNotFoundError: If the data file is not found.
            ValueError: If the data is malformed or missing required columns.
        """
        try:
            # Load data
            self.data = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully")
            
            # Check required columns
            required_columns = ['campaign_id', 'start_date', 'end_date', 
                              'budget', 'revenue', 'customers_reached']
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError("Data is missing required columns")
                
            # Convert dates to datetime
            self.data['start_date'] = pd.to_datetime(self.data['start_date'])
            self.data['end_date'] = pd.to_datetime(self.data['end_date'])
            
            # Calculate campaign duration in days
            self.data['duration_days'] = (self.data['end_date'] - self.data['start_date']).dt.days
            
            # Calculate ROI
            self.data['roi'] = (self.data['revenue'] - self.data['budget']) / self.data['budget']
            
            # Calculate customer acquisition cost
            self.data['cac'] = self.data['budget'] / self.data['customers_reached']
            
            # Group by campaign
            self.campaigns = self.data.groupby('campaign_id').agg({
                'budget': 'sum',
                'revenue': 'sum',
                'customers_reached': 'sum',
                'duration_days': 'mean',
                'roi': 'mean',
                'cac': 'mean'
            })
            
            logger.info("Data preprocessing completed")
            
        except FileNotFoundError:
            logger.error(f"Data file not found at {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Data loading error: {str(e)}")
    
    def analyze_campaigns(self):
        """
        Analyze campaign effectiveness and generate key metrics.
        
        Returns:
            dict: Dictionary containing analysis results.
        """
        if self.campaigns is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            results = {
                'total_campaigns': len(self.campaigns),
                'average_roi': self.campaigns['roi'].mean(),
                'average_cac': self.campaigns['cac'].mean(),
                'total_revenue': self.campaigns['revenue'].sum(),
                'total_budget': self.campaigns['budget'].sum(),
                'most_effective_campaign': self.campaigns['roi'].idxmax(),
                'least_effective_campaign': self.campaigns['roi'].idxmin()
            }
            
            logger.info("Campaign analysis completed")
            return results
            
        except Exception as e:
            logger.error(f"Error analyzing campaigns: {str(e)}")
            raise
    
    def plot_campaign_performance(self, save_path=None):
        """
        Generate visualizations of campaign performance.
        
        Args:
            save_path (str, optional): Path to save the plot. If None, plot is displayed.
        """
        if self.campaigns is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            plt.figure(figsize=(12, 6))
            
            # ROI by campaign
            plt.subplot(1, 2, 1)
            self.campaigns['roi'].sort_values().plot(kind='barh')
            plt.title('ROI by Campaign')
            plt.xlabel('Return on Investment')
            
            # CAC by campaign
            plt.subplot(1, 2, 2)
            self.campaigns['cac'].sort_values().plot(kind='barh', color='orange')
            plt.title('Customer Acquisition Cost by Campaign')
            plt.xlabel('Cost per Customer')
            
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path)
                logger.info(f"Plot saved to {save_path}")
            else:
                plt.show()
                
        except Exception as e:
            logger.error(f"Error generating plots: {str(e)}")
            raise
    
    def build_regression_model(self, campaign_id):
        """
        Build a simple linear regression model to predict revenue based on budget.
        
        Args:
            campaign_id (str): ID of the campaign to model.
            
        Returns:
            dict: Model metrics including coefficients and performance.
        """
        try:
            campaign_data = self.data[self.data['campaign_id'] == campaign_id]
            
            if len(campaign_data) == 0:
                raise ValueError(f"No data found for campaign {campaign_id}")
                
            X = campaign_data[['budget']].values
            y = campaign_data['revenue'].values
            
            model = LinearRegression()
            model.fit(X, y)
            
            y_pred = model.predict(X)
            
            metrics = {
                'coefficient': model.coef_[0],
                'intercept': model.intercept_,
                'mse': mean_squared_error(y, y_pred),
                'r2': r2_score(y, y_pred)
            }
            
            self.models[campaign_id] = model
            logger.info(f"Regression model built for campaign {campaign_id}")
            return metrics
            
        except Exception as e:
            logger.error(f"Error building model for campaign {campaign_id}: {str(e)}")
            raise
    
    def predict_revenue(self, campaign_id, budget):
        """
        Predict revenue for a given budget using the campaign's regression model.
        
        Args:
            campaign_id (str): ID of the campaign.
            budget (float): Budget amount to predict revenue for.
            
        Returns:
            float: Predicted revenue.
        """
        try:
            if campaign_id not in self.models:
                self.build_regression_model(campaign_id)
                
            model = self.models[campaign_id]
            return model.predict([[budget]])[0]
            
        except Exception as e:
            logger.error(f"Error predicting revenue: {str(e)}")
            raise
    
    def generate_report(self, output_path):
        """
        Generate a comprehensive report of campaign analysis.
        
        Args:
            output_path (str): Path to save the report.
        """
        try:
            analysis = self.analyze_campaigns()
            
            with open(output_path, 'w') as f:
                f.write("Campaign Effectiveness Analysis Report\n")
                f.write("="*50 + "\n\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write("Summary Metrics:\n")
                f.write("-"*50 + "\n")
                f.write(f"Total Campaigns Analyzed: {analysis['total_campaigns']}\n")
                f.write(f"Average ROI: {analysis['average_roi']:.2f}\n")
                f.write(f"Average Customer Acquisition Cost: {analysis['average_cac']:.2f}\n")
                f.write(f"Total Revenue Generated: {analysis['total_revenue']:.2f}\n")
                f.write(f"Total Budget Spent: {analysis['total_budget']:.2f}\n\n")
                
                f.write("Top Performing Campaigns:\n")
                f.write("-"*50 + "\n")
                top_campaigns = self.campaigns.sort_values('roi', ascending=False).head(3)
                for idx, row in top_campaigns.iterrows():
                    f.write(f"Campaign {idx}: ROI={row['roi']:.2f}, Revenue={row['revenue']:.2f}, CAC={row['cac']:.2f}\n")
                
                f.write("\nRecommendations:\n")
                f.write("-"*50 + "\n")
                f.write("1. Allocate more budget to high-ROI campaigns\n")
                f.write("2. Investigate and optimize low-performing campaigns\n")
                f.write("3. Consider customer acquisition cost when planning future campaigns\n")
            
            logger.info(f"Report generated and saved to {output_path}")
            
        except Exception as e:
