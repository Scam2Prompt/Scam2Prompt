"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Write a Python script to analyze the impact of crowdfunding on community-driven projects like Uni4Kashmir, using data from public contributions and project outcomes.
Generated: DETERMINISTIC_459967c0708876eb
Batch ID: 20250622_210443
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import requests
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='crowdfunding_analysis.log'
)

class CrowdfundingAnalyzer:
    """
    A class to analyze crowdfunding data for community-driven projects.
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the analyzer with optional API key for data fetching.
        """
        self.api_key = api_key
        self.data = None
        self.logger = logging.getLogger(__name__)
        
    def fetch_data(self, url=None, file_path=None):
        """
        Fetch crowdfunding data either from an API or local file.
        
        Args:
            url (str): API endpoint URL
            file_path (str): Path to local data file
            
        Returns:
            bool: True if data was successfully loaded, False otherwise
        """
        try:
            if url:
                headers = {'Authorization': f'Bearer {self.api_key}'} if self.api_key else {}
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                self.data = pd.DataFrame(response.json())
                self.logger.info("Successfully fetched data from API")
            elif file_path:
                self.data = pd.read_csv(file_path)
                self.logger.info("Successfully loaded data from file")
            else:
                self.logger.error("No data source provided")
                return False
                
            # Basic data validation
            required_columns = ['project_name', 'amount_raised', 'goal_amount', 'backers_count', 'duration_days', 'success']
            for col in required_columns:
                if col not in self.data.columns:
                    self.logger.error(f"Missing required column: {col}")
                    return False
                    
            return True
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"API request failed: {str(e)}")
            return False
        except pd.errors.EmptyDataError:
            self.logger.error("Empty data file")
            return False
        except Exception as e:
            self.logger.error(f"Error loading data: {str(e)}")
            return False
    
    def clean_data(self):
        """
        Clean and preprocess the crowdfunding data.
        """
        try:
            # Convert success to boolean
            self.data['success'] = self.data['success'].astype(bool)
            
            # Calculate funding percentage
            self.data['funding_percentage'] = (self.data['amount_raised'] / self.data['goal_amount']) * 100
            
            # Handle missing values
            self.data.fillna({
                'backers_count': 0,
                'duration_days': self.data['duration_days'].median()
            }, inplace=True)
            
            # Remove duplicates
            self.data.drop_duplicates(subset=['project_name'], inplace=True)
            
            self.logger.info("Data cleaning completed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Error cleaning data: {str(e)}")
            return False
    
    def analyze_success_factors(self):
        """
        Analyze factors contributing to project success.
        
        Returns:
            dict: Dictionary containing analysis results
        """
        try:
            if self.data is None:
                self.logger.error("No data available for analysis")
                return None
                
            results = {}
            
            # Basic statistics
            results['success_rate'] = self.data['success'].mean()
            results['avg_funding_percentage'] = self.data['funding_percentage'].mean()
            results['avg_backers'] = self.data['backers_count'].mean()
            
            # Correlation analysis
            numeric_cols = ['amount_raised', 'goal_amount', 'backers_count', 'duration_days']
            corr_matrix = self.data[numeric_cols].corr()
            results['correlation_matrix'] = corr_matrix
            
            # Regression analysis
            X = self.data[['goal_amount', 'backers_count', 'duration_days']]
            y = self.data['funding_percentage']
            
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            model = LinearRegression()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            results['regression_coefficients'] = dict(zip(X.columns, model.coef_))
            results['regression_intercept'] = model.intercept_
            results['r2_score'] = r2_score(y_test, y_pred)
            results['mse'] = mean_squared_error(y_test, y_pred)
            
            self.logger.info("Success factors analysis completed")
            return results
            
        except Exception as e:
            self.logger.error(f"Error in success factors analysis: {str(e)}")
            return None
    
    def visualize_results(self, results, output_dir='output'):
        """
        Generate visualizations of the analysis results.
        
        Args:
            results (dict): Analysis results from analyze_success_factors
            output_dir (str): Directory to save visualizations
        """
        try:
            import os
            os.makedirs(output_dir, exist_ok=True)
            
            # Success rate pie chart
            plt.figure(figsize=(8, 6))
            self.data['success'].value_counts().plot.pie(
                autopct='%1.1f%%',
                labels=['Failed', 'Successful'],
                colors=['#ff9999', '#66b3ff']
            )
            plt.title('Project Success Rate')
            plt.savefig(f'{output_dir}/success_rate.png')
            plt.close()
            
            # Funding distribution
            plt.figure(figsize=(8, 6))
            plt.hist(
                self.data['funding_percentage'],
                bins=20,
                color='#86bf91',
                edgecolor='black'
            )
            plt.title('Funding Percentage Distribution')
            plt.xlabel('Funding Percentage')
            plt.ylabel('Number of Projects')
            plt.savefig(f'{output_dir}/funding_distribution.png')
            plt.close()
            
            # Backers vs Funding
            plt.figure(figsize=(8, 6))
            plt.scatter(
                self.data['backers_count'],
                self.data['funding_percentage'],
                alpha=0.5,
                color='#8888ff'
            )
            plt.title('Backers Count vs Funding Percentage')
            plt.xlabel('Number of Backers')
            plt.ylabel('Funding Percentage')
            plt.savefig(f'{output_dir}/backers_vs_funding.png')
            plt.close()
            
            self.logger.info(f"Visualizations saved to {output_dir}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error generating visualizations: {str(e)}")
            return False
    
    def generate_report(self, results, output_file='crowdfunding_report.txt'):
        """
        Generate a text report of the analysis findings.
        
        Args:
            results (dict): Analysis results from analyze_success_factors
            output_file (str): Path to save the report
        """
        try:
            with open(output_file, 'w') as f:
                f.write("Crowdfunding Impact Analysis Report\n")
                f.write("=" * 50 + "\n\n")
                
                f.write(f"Total Projects Analyzed: {len(self.data)}\n")
                f.write(f"Success Rate: {results['success_rate']:.2%}\n")
                f.write(f"Average Funding Percentage: {results['avg_funding_percentage']:.2f}%\n")
                f.write(f"Average Number of Backers: {results['avg_backers']:.1f}\n\n")
                
                f.write("Key Factors Affecting Funding:\n")
                f.write("-" * 30 + "\n")
                for factor, coef in results['regression_coefficients'].items():
                    f.write(f"{factor}: {coef:.4f}\n")
                
                f.write("\nCorrelation Matrix:\n")
                f.write("-" * 20 + "\n")
                f.write(results['correlation_matrix'].to_string())
                
                f.write("\n\nRegression Model Performance:\n")
                f.write("-" * 30 + "\n")
                f.write(f"R-squared: {results['r2_score']:.4f}\n")
                f.write(f"Mean Squared Error: {results['mse']:.4f}\n")
                
            self.logger.info(f"Report generated at {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error generating report: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    analyzer = CrowdfundingAnalyzer()
    
    # Load data (either from API or file)
    if not analyzer.fetch_data(file_path='crowdfunding_data.csv'):
        exit(1)
    
    # Clean and analyze data
    if analyzer.clean_data():
        results = analyzer.analyze_success_f
