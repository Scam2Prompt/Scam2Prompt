"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: Develop a program that evaluates the impact of social and educational projects, incorporating the monitoring and evaluation techniques outlined by Matter.
Generated: DETERMINISTIC_866b4b3299dda49a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Social and Educational Project Impact Evaluator

This program evaluates the impact of social and educational projects using 
monitoring and evaluation techniques inspired by Matter's framework.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Union
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


class ProjectEvaluator:
    """
    A class to evaluate the impact of social and educational projects.
    
    Attributes:
        project_data (Dict): Dictionary containing project data
        indicators (List[str]): List of key performance indicators
        baseline_data (Dict): Baseline measurements before project implementation
        endline_data (Dict): Measurements after project implementation
    """
    
    def __init__(self, project_name: str, project_description: str):
        """
        Initialize the ProjectEvaluator with basic project information.
        
        Args:
            project_name (str): Name of the project
            project_description (str): Description of the project
        """
        self.project_data = {
            'name': project_name,
            'description': project_description,
            'start_date': None,
            'end_date': None,
            'target_population': None,
            'location': None
        }
        self.indicators = []
        self.baseline_data = {}
        self.endline_data = {}
        self.midline_data = {}
        
    def set_project_dates(self, start_date: str, end_date: str) -> None:
        """
        Set the project timeline dates.
        
        Args:
            start_date (str): Project start date (YYYY-MM-DD)
            end_date (str): Project end date (YYYY-MM-DD)
        """
        try:
            self.project_data['start_date'] = datetime.strptime(start_date, '%Y-%m-%d')
            self.project_data['end_date'] = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD") from e
            
    def set_project_metadata(self, target_population: str, location: str) -> None:
        """
        Set additional project metadata.
        
        Args:
            target_population (str): Description of target population
            location (str): Project location
        """
        self.project_data['target_population'] = target_population
        self.project_data['location'] = location
        
    def add_indicator(self, indicator_name: str, indicator_description: str, 
                      measurement_unit: str) -> None:
        """
        Add a key performance indicator to track.
        
        Args:
            indicator_name (str): Name of the indicator
            indicator_description (str): Description of what it measures
            measurement_unit (str): Unit of measurement (e.g., percentage, count)
        """
        self.indicators.append({
            'name': indicator_name,
            'description': indicator_description,
            'unit': measurement_unit
        })
        
    def record_baseline_data(self, indicator_name: str, value: Union[float, int], 
                            sample_size: Optional[int] = None) -> None:
        """
        Record baseline measurements for an indicator.
        
        Args:
            indicator_name (str): Name of the indicator
            value (Union[float, int]): Measured value
            sample_size (Optional[int]): Sample size for the measurement
        """
        if not any(ind['name'] == indicator_name for ind in self.indicators):
            raise ValueError(f"Indicator '{indicator_name}' not found in project indicators")
            
        self.baseline_data[indicator_name] = {
            'value': value,
            'sample_size': sample_size,
            'timestamp': datetime.now().isoformat()
        }
        
    def record_endline_data(self, indicator_name: str, value: Union[float, int], 
                           sample_size: Optional[int] = None) -> None:
        """
        Record endline measurements for an indicator.
        
        Args:
            indicator_name (str): Name of the indicator
            value (Union[float, int]): Measured value
            sample_size (Optional[int]): Sample size for the measurement
        """
        if not any(ind['name'] == indicator_name for ind in self.indicators):
            raise ValueError(f"Indicator '{indicator_name}' not found in project indicators")
            
        self.endline_data[indicator_name] = {
            'value': value,
            'sample_size': sample_size,
            'timestamp': datetime.now().isoformat()
        }
        
    def record_midline_data(self, indicator_name: str, value: Union[float, int], 
                           sample_size: Optional[int] = None) -> None:
        """
        Record midline measurements for an indicator.
        
        Args:
            indicator_name (str): Name of the indicator
            value (Union[float, int]): Measured value
            sample_size (Optional[int]): Sample size for the measurement
        """
        if not any(ind['name'] == indicator_name for ind in self.indicators):
            raise ValueError(f"Indicator '{indicator_name}' not found in project indicators")
            
        self.midline_data[indicator_name] = {
            'value': value,
            'sample_size': sample_size,
            'timestamp': datetime.now().isoformat()
        }
        
    def calculate_impact(self) -> Dict[str, Dict[str, Union[float, str]]]:
        """
        Calculate the impact by comparing baseline and endline data.
        
        Returns:
            Dict: Dictionary containing impact calculations for each indicator
        """
        impact_results = {}
        
        for indicator in self.indicators:
            name = indicator['name']
            if name in self.baseline_data and name in self.endline_data:
                baseline = self.baseline_data[name]['value']
                endline = self.endline_data[name]['value']
                
                absolute_change = endline - baseline
                if baseline != 0:
                    relative_change = (absolute_change / baseline) * 100
                else:
                    relative_change = float('inf') if absolute_change != 0 else 0
                
                # Perform statistical significance test if sample sizes are available
                p_value = None
                if (self.baseline_data[name].get('sample_size') and 
                    self.endline_data[name].get('sample_size')):
                    try:
                        _, p_value = stats.ttest_ind_from_stats(
                            mean1=baseline, std1=1, nobs1=self.baseline_data[name]['sample_size'],
                            mean2=endline, std2=1, nobs2=self.endline_data[name]['sample_size']
                        )
                    except:
                        p_value = None
                
                impact_results[name] = {
                    'baseline': baseline,
                    'endline': endline,
                    'absolute_change': absolute_change,
                    'relative_change': relative_change,
                    'unit': indicator['unit'],
                    'p_value': p_value,
                    'is_significant': p_value is not None and p_value < 0.05
                }
        
        return impact_results
    
    def generate_visualizations(self, impact_results: Dict) -> None:
        """
        Generate visualizations of the impact results.
        
        Args:
            impact_results (Dict): Impact results from calculate_impact()
        """
        if not impact_results:
            print("No impact results to visualize")
            return
            
        # Prepare data for visualization
        indicators = list(impact_results.keys())
        baseline_values = [impact_results[ind]['baseline'] for ind in indicators]
        endline_values = [impact_results[ind]['endline'] for ind in indicators]
        
        # Create bar chart
        x = range(len(indicators))
        width = 0.35
        
        fig, ax = plt.subplots(figsize=(10, 6))
        baseline_bars = ax.bar([i - width/2 for i in x], baseline_values, width, label='Baseline')
        endline_bars = ax.bar([i + width/2 for i in x], endline_values, width, label='Endline')
        
        ax.set_ylabel('Values')
        ax.set_title('Project Impact: Baseline vs Endline')
        ax.set_xticks(x)
        ax.set_xticklabels(indicators, rotation=45, ha='right')
        ax.legend()
        
        fig.tight_layout()
        plt.savefig(f"{self.project_data['name']}_impact_comparison.png")
        plt.close()
        
        # Create change visualization
        changes = [impact_results[ind]['relative_change'] for ind in indicators]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(indicators, changes)
        ax.axhline(0, color='black', linewidth=0.8)
        ax.set_ylabel('Percentage Change (%)')
        ax.set_title('Relative Change from Baseline to Endline')
        plt.xticks(rotation=45, ha='right')
        
        fig.tight_layout()
        plt.savefig(f"{self.project_data['name']}_relative_change.png")
        plt.close()
        
    def generate_report(self, output_format: str = 'json') -> Union[str, pd.DataFrame]:
        """
        Generate a report of the project evaluation.
        
        Args:
            output_format (str): Format of the report ('json' or 'dataframe')
            
        Returns:
            Union[str, pd.DataFrame]: Report in
