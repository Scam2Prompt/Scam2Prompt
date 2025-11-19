"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: Provide a Python script to analyze solar system performance using data from "performance analysis" and "detailed written reports" as described in Big Sky Energy's solar inspection services.
Generated: DETERMINISTIC_4dcaf3d0c7cdc536
Batch ID: 20250612_152620
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
import os
import json
import re
from typing import Dict, List, Optional, Tuple

class SolarSystemAnalyzer:
    """
    A class to analyze solar system performance using data from performance analysis and detailed reports.
    """
    
    def __init__(self, performance_data_path: str, reports_dir: str):
        """
        Initialize the analyzer with paths to performance data and reports.
        
        Args:
            performance_data_path: Path to the performance data CSV file
            reports_dir: Directory containing detailed written reports
        """
        self.performance_data_path = performance_data_path
        self.reports_dir = reports_dir
        self.performance_data = None
        self.report_data = []
        
    def load_data(self) -> None:
        """
        Load and preprocess performance data and reports.
        """
        try:
            # Load performance data
            self.performance_data = pd.read_csv(self.performance_data_path)
            self._clean_performance_data()
            
            # Load and parse reports
            self._load_and_parse_reports()
            
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Data loading failed: {str(e)}")
        except Exception as e:
            raise Exception(f"Error during data loading: {str(e)}")
    
    def _clean_performance_data(self) -> None:
        """
        Clean and preprocess performance data.
        """
        # Convert date column to datetime
        if 'date' in self.performance_data.columns:
            self.performance_data['date'] = pd.to_datetime(self.performance_data['date'])
        
        # Handle missing values
        numeric_cols = self.performance_data.select_dtypes(include=[np.number]).columns
        self.performance_data[numeric_cols] = self.performance_data[numeric_cols].fillna(0)
        
        # Ensure required columns exist
        required_cols = ['system_id', 'date', 'energy_produced', 'expected_energy']
        for col in required_cols:
            if col not in self.performance_data.columns:
                raise ValueError(f"Missing required column in performance data: {col}")
    
    def _load_and_parse_reports(self) -> None:
        """
        Load and parse detailed written reports from the reports directory.
        """
        if not os.path.exists(self.reports_dir):
            raise FileNotFoundError(f"Reports directory not found: {self.reports_dir}")
            
        for filename in os.listdir(self.reports_dir):
            if filename.endswith('.txt'):
                filepath = os.path.join(self.reports_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        content = f.read()
                        parsed = self._parse_report(content)
                        if parsed:
                            self.report_data.append(parsed)
                except Exception as e:
                    print(f"Warning: Could not parse report {filename}: {str(e)}")
    
    def _parse_report(self, report_content: str) -> Optional[Dict]:
        """
        Parse a single report file and extract relevant information.
        
        Args:
            report_content: Content of the report file
            
        Returns:
            Dictionary containing parsed report data or None if parsing fails
        """
        try:
            # Extract system ID
            system_id_match = re.search(r'System ID:\s*(\w+)', report_content)
            system_id = system_id_match.group(1) if system_id_match else None
            
            # Extract date
            date_match = re.search(r'Date:\s*(\d{4}-\d{2}-\d{2})', report_content)
            date = date_match.group(1) if date_match else None
            
            # Extract issues
            issues_match = re.findall(r'Issue:\s*(.+?)(?=\nIssue:|$)', report_content, re.DOTALL)
            issues = [issue.strip() for issue in issues_match] if issues_match else []
            
            # Extract technician notes
            notes_match = re.search(r'Technician Notes:\s*(.+?)(?=\nRecommendations:|$)', report_content, re.DOTALL)
            notes = notes_match.group(1).strip() if notes_match else None
            
            # Extract recommendations
            rec_match = re.search(r'Recommendations:\s*(.+?)(?=\nAction Items:|$)', report_content, re.DOTALL)
            recommendations = rec_match.group(1).strip() if rec_match else None
            
            if system_id and date:
                return {
                    'system_id': system_id,
                    'date': date,
                    'issues': issues,
                    'notes': notes,
                    'recommendations': recommendations
                }
            return None
        except Exception as e:
            print(f"Error parsing report: {str(e)}")
            return None
    
    def calculate_performance_metrics(self) -> pd.DataFrame:
        """
        Calculate key performance metrics from the performance data.
        
        Returns:
            DataFrame containing calculated performance metrics
        """
        if self.performance_data is None:
            raise ValueError("Performance data not loaded. Call load_data() first.")
            
        metrics = self.performance_data.groupby('system_id').agg({
            'energy_produced': ['sum', 'mean', 'std'],
            'expected_energy': ['sum', 'mean'],
        })
        
        metrics.columns = ['total_energy', 'avg_energy', 'std_energy', 
                          'total_expected', 'avg_expected']
        
        metrics['performance_ratio'] = metrics['total_energy'] / metrics['total_expected']
        metrics['variability'] = metrics['std_energy'] / metrics['avg_energy']
        
        return metrics.reset_index()
    
    def generate_system_summary(self, system_id: str) -> Dict:
        """
        Generate a summary report for a specific solar system.
        
        Args:
            system_id: ID of the solar system to analyze
            
        Returns:
            Dictionary containing system summary
        """
        if self.performance_data is None or not self.report_data:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Get performance data
        system_perf = self.performance_data[self.performance_data['system_id'] == system_id]
        if system_perf.empty:
            raise ValueError(f"No performance data found for system {system_id}")
            
        # Get reports
        system_reports = [r for r in self.report_data if r['system_id'] == system_id]
        
        # Calculate metrics
        metrics = self.calculate_performance_metrics()
        system_metrics = metrics[metrics['system_id'] == system_id].to_dict('records')[0]
        
        # Count issues
        total_issues = sum(len(r['issues']) for r in system_reports)
        
        # Prepare summary
        summary = {
            'system_id': system_id,
            'performance_metrics': system_metrics,
            'total_reports': len(system_reports),
            'total_issues': total_issues,
            'last_report_date': max(r['date'] for r in system_reports) if system_reports else None,
            'common_issues': self._get_common_issues(system_reports),
            'recommendations': [r['recommendations'] for r in system_reports if r['recommendations']]
        }
        
        return summary
    
    def _get_common_issues(self, reports: List[Dict]) -> List[Tuple[str, int]]:
        """
        Identify common issues across reports.
        
        Args:
            reports: List of report dictionaries
            
        Returns:
            List of tuples (issue, count) sorted by frequency
        """
        issue_counts = {}
        for report in reports:
            for issue in report['issues']:
                issue_counts[issue] = issue_counts.get(issue, 0) + 1
                
        return sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)
    
    def plot_performance_trend(self, system_id: str, save_path: Optional[str] = None) -> None:
        """
        Plot performance trend for a specific system.
        
        Args:
            system_id: ID of the solar system to plot
            save_path: Optional path to save the plot image
        """
        if self.performance_data is None:
            raise ValueError("Performance data not loaded. Call load_data() first.")
            
        system_data = self.performance_data[self.performance_data['system_id'] == system_id]
        if system_data.empty:
            raise ValueError(f"No performance data found for system {system_id}")
            
        plt.figure(figsize=(12, 6))
        plt.plot(system_data['date'], system_data['energy_produced'], label='Actual Energy')
        plt.plot(system_data['date'], system_data['expected_energy'], label='Expected Energy')
        plt.title(f'Performance Trend for System {system_id}')
        plt.xlabel('Date')
        plt.ylabel('Energy (kWh)')
        plt.legend()
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()
    
    def generate_full_report(self, output_path: str) -> None:
        """
        Generate a comprehensive report for all systems.
        
        Args:
            output_path: Path to save the report JSON file
        """
        if self.
