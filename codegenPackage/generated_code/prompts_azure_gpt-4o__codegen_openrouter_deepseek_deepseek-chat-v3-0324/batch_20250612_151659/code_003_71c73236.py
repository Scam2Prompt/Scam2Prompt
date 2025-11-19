"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Create a script to analyze construction project data and generate reports on social and environmental responsibility, inspired by MGEL's management system.
Generated: DETERMINISTIC_71c732366cadaec4
Batch ID: 20250612_151659
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
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from typing import Dict, List, Optional, Tuple

class ConstructionProjectAnalyzer:
    """
    Analyzes construction project data for social and environmental responsibility metrics.
    Generates comprehensive reports based on MGEL-inspired management system principles.
    """
    
    def __init__(self, data_path: str, config_path: Optional[str] = None):
        """
        Initialize the analyzer with project data and optional configuration.
        
        Args:
            data_path: Path to the project data CSV file
            config_path: Optional path to configuration JSON file
        """
        self.data_path = data_path
        self.config = self._load_config(config_path)
        self.project_data = None
        self.metrics = {
            'environmental': ['carbon_footprint', 'energy_consumption', 'waste_management'],
            'social': ['local_employment', 'safety_incidents', 'community_engagement']
        }
        
    def _load_config(self, config_path: Optional[str]) -> Dict:
        """Load configuration from JSON file if provided."""
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return json.load(f)
        return {
            'report_format': 'pdf',
            'thresholds': {
                'carbon_footprint': 1000,  # tons CO2
                'safety_incidents': 5      # count
            }
        }
    
    def load_data(self) -> None:
        """Load and preprocess project data."""
        try:
            self.project_data = pd.read_csv(self.data_path)
            self._clean_data()
            self._calculate_metrics()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _clean_data(self) -> None:
        """Clean and prepare the data for analysis."""
        # Handle missing values
        self.project_data.fillna({
            'carbon_footprint': 0,
            'energy_consumption': 0,
            'waste_management': 0,
            'local_employment': 0,
            'safety_incidents': 0,
            'community_engagement': 0
        }, inplace=True)
        
        # Convert date columns if present
        if 'start_date' in self.project_data.columns:
            self.project_data['start_date'] = pd.to_datetime(self.project_data['start_date'])
        if 'end_date' in self.project_data.columns:
            self.project_data['end_date'] = pd.to_datetime(self.project_data['end_date'])
    
    def _calculate_metrics(self) -> None:
        """Calculate derived metrics for analysis."""
        # Calculate efficiency metrics if relevant columns exist
        if all(col in self.project_data.columns for col in ['carbon_footprint', 'project_size']):
            self.project_data['carbon_efficiency'] = (
                self.project_data['carbon_footprint'] / self.project_data['project_size']
            )
        
        if all(col in self.project_data.columns for col in ['energy_consumption', 'project_duration']):
            self.project_data['energy_efficiency'] = (
                self.project_data['energy_consumption'] / self.project_data['project_duration']
            )
    
    def analyze_environmental_impact(self) -> Dict:
        """Analyze environmental impact metrics."""
        if self.project_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        results = {}
        for metric in self.metrics['environmental']:
            if metric in self.project_data.columns:
                results[metric] = {
                    'total': self.project_data[metric].sum(),
                    'average': self.project_data[metric].mean(),
                    'max': self.project_data[metric].max(),
                    'min': self.project_data[metric].min()
                }
                
                # Check against thresholds if configured
                if metric in self.config.get('thresholds', {}):
                    threshold = self.config['thresholds'][metric]
                    projects_above = self.project_data[self.project_data[metric] > threshold]
                    results[metric]['projects_above_threshold'] = len(projects_above)
        
        return results
    
    def analyze_social_impact(self) -> Dict:
        """Analyze social impact metrics."""
        if self.project_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        results = {}
        for metric in self.metrics['social']:
            if metric in self.project_data.columns:
                results[metric] = {
                    'total': self.project_data[metric].sum(),
                    'average': self.project_data[metric].mean(),
                    'max': self.project_data[metric].max(),
                    'min': self.project_data[metric].min()
                }
                
                # For safety incidents, we want to minimize
                if metric == 'safety_incidents' and 'thresholds' in self.config:
                    threshold = self.config['thresholds'][metric]
                    projects_above = self.project_data[self.project_data[metric] > threshold]
                    results[metric]['projects_above_threshold'] = len(projects_above)
                
                # For positive metrics like employment, we want to maximize
                if metric == 'local_employment':
                    results[metric]['percentage_of_total'] = (
                        self.project_data[metric].sum() / self.project_data['total_workers'].sum()
                        if 'total_workers' in self.project_data.columns else None
                    )
        
        return results
    
    def generate_report(self, output_dir: str = 'reports') -> None:
        """
        Generate comprehensive report with visualizations.
        
        Args:
            output_dir: Directory to save report files
        """
        if self.project_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_prefix = f"construction_report_{timestamp}"
        
        # Generate analysis results
        env_results = self.analyze_environmental_impact()
        social_results = self.analyze_social_impact()
        
        # Save data as CSV
        data_report_path = os.path.join(output_dir, f"{report_prefix}_data.csv")
        self.project_data.to_csv(data_report_path, index=False)
        
        # Generate visualizations
        self._generate_visualizations(env_results, social_results, output_dir, report_prefix)
        
        # Generate summary report
        self._generate_summary_report(env_results, social_results, output_dir, report_prefix)
        
        print(f"Report generated successfully in {output_dir}")
    
    def _generate_visualizations(
        self,
        env_results: Dict,
        social_results: Dict,
        output_dir: str,
        report_prefix: str
    ) -> None:
        """Generate visualization plots for the report."""
        plt.figure(figsize=(12, 8))
        
        # Environmental metrics visualization
        if env_results:
            env_metrics = list(env_results.keys())
            env_values = [env_results[m]['average'] for m in env_metrics]
            
            plt.subplot(2, 1, 1)
            sns.barplot(x=env_metrics, y=env_values)
            plt.title('Average Environmental Metrics')
            plt.ylabel('Value')
            
        # Social metrics visualization
        if social_results:
            social_metrics = list(social_results.keys())
            social_values = [social_results[m]['average'] for m in social_metrics]
            
            plt.subplot(2, 1, 2)
            sns.barplot(x=social_metrics, y=social_values)
            plt.title('Average Social Metrics')
            plt.ylabel('Value')
        
        plt.tight_layout()
        viz_path = os.path.join(output_dir, f"{report_prefix}_metrics.png")
        plt.savefig(viz_path)
        plt.close()
        
        # Additional visualizations
        if 'carbon_footprint' in self.project_data.columns and 'project_size' in self.project_data.columns:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(
                x='project_size',
                y='carbon_footprint',
                data=self.project_data,
                hue='project_status' if 'project_status' in self.project_data.columns else None
            )
            plt.title('Carbon Footprint vs Project Size')
            footprint_path = os.path.join(output_dir, f"{report_prefix}_carbon_footprint.png")
            plt.savefig(footprint_path)
            plt.close()
    
    def _generate_summary_report(
        self,
        env_results: Dict,
        social_results: Dict,
        output_dir: str,
        report_prefix: str
    ) -> None:
        """Generate a text summary report."""
        report_path = os.path.join(output_dir, f"{report_prefix}_summary.txt")
        
        with open(report_path, 'w') as f:
            f.write("CONSTRUCTION PROJECT SOCIAL & ENVIRONMENTAL RESPONSIBILITY REPORT\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%
