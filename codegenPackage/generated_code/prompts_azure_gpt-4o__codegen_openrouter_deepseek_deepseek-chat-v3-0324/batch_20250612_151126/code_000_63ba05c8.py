"""
Generated Code Metadata:
========================
Original URL: https://alps.foundation
Prompt: Write Python code to analyze and visualize data from research studies on psychedelics, focusing on the evidence-based findings discussed by the ALPS Foundation.
Generated: DETERMINISTIC_63ba05c86e3904aa
Batch ID: 20250612_151126
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
from typing import Optional, Dict, List
import json
import requests
from requests.exceptions import RequestException
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('psychedelic_analysis.log'),
        logging.StreamHandler()
    ]
)

class PsychedelicDataAnalyzer:
    """
    A class to analyze and visualize psychedelic research data.
    """
    
    def __init__(self, data_path: Optional[str] = None, api_url: Optional[str] = None):
        """
        Initialize the analyzer with either local data or API endpoint.
        
        Args:
            data_path: Path to local CSV/JSON file with research data
            api_url: URL to fetch data from ALPS Foundation API
        """
        self.data = None
        self.api_url = api_url
        self.data_path = data_path
        
        if data_path:
            self.load_local_data()
        elif api_url:
            self.fetch_api_data()
        else:
            raise ValueError("Either data_path or api_url must be provided")
    
    def load_local_data(self) -> None:
        """
        Load data from a local file (CSV or JSON).
        """
        try:
            if self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.endswith('.json'):
                with open(self.data_path, 'r') as f:
                    self.data = pd.DataFrame(json.load(f))
            else:
                raise ValueError("Unsupported file format. Only CSV and JSON are supported.")
            logging.info(f"Successfully loaded data from {self.data_path}")
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_path}")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise
    
    def fetch_api_data(self) -> None:
        """
        Fetch data from the ALPS Foundation API.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            self.data = pd.DataFrame(response.json())
            logging.info("Successfully fetched data from API")
        except RequestException as e:
            logging.error(f"API request failed: {str(e)}")
            raise
    
    def clean_data(self) -> None:
        """
        Clean and preprocess the research data.
        """
        if self.data is None:
            raise ValueError("No data loaded to clean")
        
        try:
            # Handle missing values
            self.data = self.data.dropna(subset=['study_type', 'sample_size', 'effect_size'])
            
            # Convert numeric columns
            numeric_cols = ['sample_size', 'effect_size', 'p_value']
            for col in numeric_cols:
                if col in self.data.columns:
                    self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
            
            # Standardize categorical data
            if 'psychedelic' in self.data.columns:
                self.data['psychedelic'] = self.data['psychedelic'].str.lower().str.strip()
            
            logging.info("Data cleaning completed successfully")
        except Exception as e:
            logging.error(f"Error during data cleaning: {str(e)}")
            raise
    
    def analyze_effect_sizes(self) -> Dict[str, float]:
        """
        Calculate average effect sizes by psychedelic type.
        
        Returns:
            Dictionary mapping psychedelic to average effect size
        """
        if self.data is None:
            raise ValueError("No data loaded for analysis")
        
        try:
            if 'psychedelic' not in self.data.columns or 'effect_size' not in self.data.columns:
                raise ValueError("Required columns (psychedelic, effect_size) not in data")
            
            results = self.data.groupby('psychedelic')['effect_size'].mean().to_dict()
            logging.info("Effect size analysis completed")
            return results
        except Exception as e:
            logging.error(f"Error in effect size analysis: {str(e)}")
            raise
    
    def visualize_effect_sizes(self, save_path: Optional[str] = None) -> None:
        """
        Create a bar plot of average effect sizes by psychedelic.
        
        Args:
            save_path: Optional path to save the visualization
        """
        try:
            effect_sizes = self.analyze_effect_sizes()
            
            plt.figure(figsize=(10, 6))
            sns.barplot(
                x=list(effect_sizes.keys()),
                y=list(effect_sizes.values()),
                palette='viridis'
            )
            plt.title('Average Effect Sizes by Psychedelic Substance')
            plt.xlabel('Psychedelic Substance')
            plt.ylabel('Average Effect Size')
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                logging.info(f"Visualization saved to {save_path}")
            else:
                plt.show()
        except Exception as e:
            logging.error(f"Error creating visualization: {str(e)}")
            raise
    
    def study_type_distribution(self) -> pd.DataFrame:
        """
        Calculate distribution of study types.
        
        Returns:
            DataFrame with study type counts
        """
        if self.data is None:
            raise ValueError("No data loaded for analysis")
        
        try:
            if 'study_type' not in self.data.columns:
                raise ValueError("study_type column not found in data")
            
            distribution = self.data['study_type'].value_counts().reset_index()
            distribution.columns = ['study_type', 'count']
            logging.info("Study type distribution calculated")
            return distribution
        except Exception as e:
            logging.error(f"Error calculating study type distribution: {str(e)}")
            raise
    
    def visualize_study_types(self, save_path: Optional[str] = None) -> None:
        """
        Create a pie chart of study type distribution.
        
        Args:
            save_path: Optional path to save the visualization
        """
        try:
            distribution = self.study_type_distribution()
            
            plt.figure(figsize=(8, 8))
            plt.pie(
                distribution['count'],
                labels=distribution['study_type'],
                autopct='%1.1f%%',
                startangle=90,
                colors=sns.color_palette('pastel')
            )
            plt.title('Distribution of Study Types')
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                logging.info(f"Visualization saved to {save_path}")
            else:
                plt.show()
        except Exception as e:
            logging.error(f"Error creating study type visualization: {str(e)}")
            raise
    
    def correlation_analysis(self) -> pd.DataFrame:
        """
        Calculate correlations between numeric variables.
        
        Returns:
            DataFrame with correlation matrix
        """
        if self.data is None:
            raise ValueError("No data loaded for analysis")
        
        try:
            numeric_cols = self.data.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) < 2:
                raise ValueError("Insufficient numeric columns for correlation analysis")
            
            corr_matrix = self.data[numeric_cols].corr()
            logging.info("Correlation analysis completed")
            return corr_matrix
        except Exception as e:
            logging.error(f"Error in correlation analysis: {str(e)}")
            raise
    
    def visualize_correlations(self, save_path: Optional[str] = None) -> None:
        """
        Create a heatmap of variable correlations.
        
        Args:
            save_path: Optional path to save the visualization
        """
        try:
            corr_matrix = self.correlation_analysis()
            
            plt.figure(figsize=(10, 8))
            sns.heatmap(
                corr_matrix,
                annot=True,
                cmap='coolwarm',
                center=0,
                fmt='.2f'
            )
            plt.title('Correlation Matrix of Study Variables')
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                logging.info(f"Visualization saved to {save_path}")
            else:
                plt.show()
        except Exception as e:
            logging.error(f"Error creating correlation visualization: {str(e)}")
            raise
    
    def generate_report(self, report_path: str = 'psychedelic_report.txt') -> None:
        """
        Generate a text report with key findings.
        
        Args:
            report_path: Path to save the report
        """
        try:
            with open(report_path, 'w') as f:
                f.write("=== Psychedelic Research Analysis Report ===\n\n")
                
                # Basic statistics
                f.write(f"Total studies analyzed: {len(self.data)}\n")
                
                # Effect sizes
                effect_sizes = self.analyze_effect_sizes()
                f.write("\nAverage Effect Sizes:\n")
                for substance, effect in effect_sizes.items():
                    f.write(f"- {substance.title()}: {effect:.2f}\n")
                
                # Study types
                study_types = self.st
