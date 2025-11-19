"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Generate a script to analyze industrial hygiene data for occupational exposure sampling and PPE assessments, referencing the services provided by iSi Environmental.
Generated: DETERMINISTIC_4642f99740d1d1da
Batch ID: 20250612_151811
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
from scipy import stats
import os
import json
from datetime import datetime

class IndustrialHygieneAnalyzer:
    """
    A class to analyze industrial hygiene data for occupational exposure sampling and PPE assessments.
    References services similar to those provided by iSi Environmental.
    """
    
    def __init__(self, data_source=None):
        """
        Initialize the analyzer with optional data source.
        
        Args:
            data_source (str or pd.DataFrame): Path to data file or DataFrame containing hygiene data
        """
        self.data = None
        self.exposure_limits = {}
        self._load_default_exposure_limits()
        
        if data_source is not None:
            self.load_data(data_source)
    
    def _load_default_exposure_limits(self):
        """Load default occupational exposure limits (OELs) from embedded JSON."""
        default_limits = {
            "noise": 85,  # dB, 8-hour TWA
            "dust": 5,    # mg/m3, 8-hour TWA
            "CO": 25,     # ppm, 8-hour TWA
            "H2S": 10,    # ppm, 8-hour TWA
            "benzene": 0.5,  # ppm, 8-hour TWA
        }
        self.exposure_limits = default_limits
    
    def load_exposure_limits(self, limits_file):
        """
        Load custom exposure limits from JSON file.
        
        Args:
            limits_file (str): Path to JSON file containing exposure limits
        """
        try:
            with open(limits_file, 'r') as f:
                custom_limits = json.load(f)
            self.exposure_limits.update(custom_limits)
        except FileNotFoundError:
            print(f"Warning: Exposure limits file {limits_file} not found. Using defaults.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {limits_file}. Using defaults.")
    
    def load_data(self, data_source):
        """
        Load industrial hygiene data from file or DataFrame.
        
        Args:
            data_source (str or pd.DataFrame): Path to CSV/Excel file or DataFrame
        """
        if isinstance(data_source, pd.DataFrame):
            self.data = data_source.copy()
        elif isinstance(data_source, str):
            try:
                if data_source.endswith('.csv'):
                    self.data = pd.read_csv(data_source)
                elif data_source.endswith(('.xls', '.xlsx')):
                    self.data = pd.read_excel(data_source)
                else:
                    raise ValueError("Unsupported file format. Use CSV or Excel.")
            except Exception as e:
                print(f"Error loading data: {str(e)}")
                raise
        else:
            raise TypeError("Data source must be a file path or DataFrame")
        
        self._validate_data()
    
    def _validate_data(self):
        """Validate the loaded data structure."""
        required_columns = ['sample_id', 'contaminant', 'concentration', 'units', 'duration']
        if not all(col in self.data.columns for col in required_columns):
            missing = [col for col in required_columns if col not in self.data.columns]
            raise ValueError(f"Missing required columns: {missing}")
        
        if 'date' in self.data.columns:
            try:
                self.data['date'] = pd.to_datetime(self.data['date'])
            except ValueError:
                print("Warning: Could not parse date column. Continuing without date processing.")
    
    def calculate_twa(self, group_cols=None):
        """
        Calculate Time-Weighted Averages (TWA) for exposure data.
        
        Args:
            group_cols (list, optional): Columns to group by when calculating TWAs
            
        Returns:
            pd.DataFrame: DataFrame with TWA calculations
        """
        if group_cols is None:
            group_cols = ['contaminant']
        
        if not all(col in self.data.columns for col in group_cols):
            raise ValueError("One or more group columns not found in data")
        
        # Calculate TWA: sum(concentration * duration) / sum(duration)
        twa_data = self.data.copy()
        twa_data['weighted_conc'] = twa_data['concentration'] * twa_data['duration']
        
        grouped = twa_data.groupby(group_cols)
        sum_weighted = grouped['weighted_conc'].sum()
        sum_duration = grouped['duration'].sum()
        
        twa_results = (sum_weighted / sum_duration).reset_index()
        twa_results.columns = group_cols + ['twa_concentration']
        
        # Add exposure limit comparison
        twa_results['exposure_limit'] = twa_results['contaminant'].map(self.exposure_limits)
        twa_results['percent_of_limit'] = (twa_results['twa_concentration'] / 
                                          twa_results['exposure_limit']) * 100
        
        return twa_results
    
    def assess_ppe_requirements(self, twa_results=None):
        """
        Assess PPE requirements based on exposure levels.
        
        Args:
            twa_results (pd.DataFrame, optional): Pre-calculated TWA results
            
        Returns:
            pd.DataFrame: PPE recommendations
        """
        if twa_results is None:
            twa_results = self.calculate_twa()
        
        ppe_assessment = twa_results.copy()
        
        def _get_ppe_recommendation(row):
            percent = row['percent_of_limit']
            contaminant = row['contaminant']
            
            if percent < 50:
                return "Basic PPE (gloves, safety glasses)"
            elif 50 <= percent < 100:
                return f"Enhanced PPE (respirator for {contaminant}, face shield)"
            else:
                return f"Critical PPE (supplied air for {contaminant}, full-body protection)"
        
        ppe_assessment['ppe_recommendation'] = ppe_assessment.apply(_get_ppe_recommendation, axis=1)
        return ppe_assessment
    
    def generate_exposure_report(self, output_file=None):
        """
        Generate a comprehensive exposure assessment report.
        
        Args:
            output_file (str, optional): Path to save report (PDF or HTML)
        """
        twa_results = self.calculate_twa()
        ppe_assessment = self.assess_ppe_requirements(twa_results)
        
        report_data = pd.merge(twa_results, ppe_assessment, how='left')
        
        if output_file:
            try:
                if output_file.endswith('.html'):
                    report_data.to_html(output_file, index=False)
                elif output_file.endswith('.csv'):
                    report_data.to_csv(output_file, index=False)
                else:
                    print("Unsupported output format. Returning DataFrame.")
                    return report_data
            except Exception as e:
                print(f"Error saving report: {str(e)}")
                return report_data
        else:
            return report_data
    
    def plot_exposure_distribution(self, contaminant=None, save_path=None):
        """
        Plot exposure distribution for a specific contaminant or all contaminants.
        
        Args:
            contaminant (str, optional): Specific contaminant to plot
            save_path (str, optional): Path to save the plot image
        """
        plot_data = self.data.copy()
        
        if contaminant:
            plot_data = plot_data[plot_data['contaminant'] == contaminant]
            if plot_data.empty:
                raise ValueError(f"No data found for contaminant: {contaminant}")
        
        plt.figure(figsize=(10, 6))
        
        for contam, group in plot_data.groupby('contaminant'):
            limit = self.exposure_limits.get(contam, None)
            
            plt.hist(group['concentration'], bins=20, alpha=0.5, label=contam)
            
            if limit:
                plt.axvline(limit, color='r', linestyle='--', 
                           label=f'{contam} Limit ({limit} {group["units"].iloc[0]})')
        
        plt.xlabel('Concentration')
        plt.ylabel('Frequency')
        plt.title('Exposure Distribution')
        plt.legend()
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    def calculate_statistics(self):
        """
        Calculate descriptive statistics for the exposure data.
        
        Returns:
            dict: Dictionary of statistical measures
        """
        stats_results = {}
        
        for contam, group in self.data.groupby('contaminant'):
            concentrations = group['concentration']
            stats_results[contam] = {
                'count': len(concentrations),
                'mean': np.mean(concentrations),
                'median': np.median(concentrations),
                'std_dev': np.std(concentrations),
                'min': np.min(concentrations),
                'max': np.max(concentrations),
                'exposure_limit': self.exposure_limits.get(contam, None),
                'percent_above_limit': (sum(concentrations > self.exposure_limits.get(contam, np.inf)) / 
                                       len(concentrations)) * 100
            }
