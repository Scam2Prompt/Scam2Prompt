"""
Generated Code Metadata:
========================
Original URL: https://yo-channel.com
Prompt: "Write a Python script to track and analyze the effects ofファスティング on autonomic nervous system balance."
Generated: DETERMINISTIC_11c5b83e4a77f832
Batch ID: 20250622_211841
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
import json
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fasting_ans_analysis.log'),
        logging.StreamHandler()
    ]
)

class FastingANSAnalyzer:
    """
    A class to track and analyze the effects of fasting on autonomic nervous system (ANS) balance.
    Measures include Heart Rate Variability (HRV) metrics like RMSSD and LF/HF ratio.
    """
    
    def __init__(self, data_file='fasting_data.json'):
        """
        Initialize the analyzer with a data file.
        
        Args:
            data_file (str): Path to JSON file storing fasting and ANS data.
        """
        self.data_file = data_file
        self.data = self._load_data()
        
    def _load_data(self):
        """
        Load data from JSON file or initialize empty structure if file doesn't exist.
        
        Returns:
            dict: Dictionary containing fasting and ANS data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {
                'fasting_sessions': [],
                'ans_measurements': []
            }
        except Exception as e:
            logging.error(f"Error loading data file: {e}")
            return {
                'fasting_sessions': [],
                'ans_measurements': []
            }
    
    def _save_data(self):
        """
        Save current data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            logging.error(f"Error saving data file: {e}")
    
    def add_fasting_session(self, start_time, end_time, notes=None):
        """
        Add a new fasting session to the tracker.
        
        Args:
            start_time (str): ISO format datetime string for start time.
            end_time (str): ISO format datetime string for end time.
            notes (str, optional): Additional notes about the session.
        """
        try:
            session = {
                'start_time': start_time,
                'end_time': end_time,
                'duration_hours': self._calculate_duration(start_time, end_time),
                'notes': notes or ''
            }
            self.data['fasting_sessions'].append(session)
            self._save_data()
            logging.info("Fasting session added successfully.")
        except Exception as e:
            logging.error(f"Error adding fasting session: {e}")
    
    def add_ans_measurement(self, timestamp, rmssd, lf_hf_ratio, notes=None):
        """
        Add a new ANS measurement (HRV metrics).
        
        Args:
            timestamp (str): ISO format datetime string for measurement time.
            rmssd (float): RMSSD value in ms.
            lf_hf_ratio (float): LF/HF ratio.
            notes (str, optional): Additional notes about the measurement.
        """
        try:
            measurement = {
                'timestamp': timestamp,
                'rmssd': float(rmssd),
                'lf_hf_ratio': float(lf_hf_ratio),
                'notes': notes or ''
            }
            self.data['ans_measurements'].append(measurement)
            self._save_data()
            logging.info("ANS measurement added successfully.")
        except Exception as e:
            logging.error(f"Error adding ANS measurement: {e}")
    
    def _calculate_duration(self, start_time, end_time):
        """
        Calculate duration between two timestamps in hours.
        
        Args:
            start_time (str): ISO format datetime string.
            end_time (str): ISO format datetime string.
            
        Returns:
            float: Duration in hours.
        """
        try:
            start = datetime.fromisoformat(start_time)
            end = datetime.fromisoformat(end_time)
            return (end - start).total_seconds() / 3600
        except Exception as e:
            logging.error(f"Error calculating duration: {e}")
            return 0.0
    
    def get_fasting_period_measurements(self, days_before=1, days_after=1):
        """
        Get ANS measurements around fasting periods.
        
        Args:
            days_before (int): Days before fasting to include.
            days_after (int): Days after fasting to include.
            
        Returns:
            pd.DataFrame: DataFrame containing relevant measurements.
        """
        try:
            measurements_df = pd.DataFrame(self.data['ans_measurements'])
            sessions_df = pd.DataFrame(self.data['fasting_sessions'])
            
            if measurements_df.empty or sessions_df.empty:
                logging.warning("No measurements or fasting sessions available.")
                return pd.DataFrame()
            
            measurements_df['timestamp'] = pd.to_datetime(measurements_df['timestamp'])
            sessions_df['start_time'] = pd.to_datetime(sessions_df['start_time'])
            sessions_df['end_time'] = pd.to_datetime(sessions_df['end_time'])
            
            relevant_measurements = []
            
            for _, session in sessions_df.iterrows():
                start_window = session['start_time'] - pd.Timedelta(days=days_before)
                end_window = session['end_time'] + pd.Timedelta(days=days_after)
                
                mask = (measurements_df['timestamp'] >= start_window) & \
                       (measurements_df['timestamp'] <= end_window)
                
                session_measurements = measurements_df[mask].copy()
                session_measurements['session_id'] = session.name
                session_measurements['time_relative_to_fasting'] = \
                    (session_measurements['timestamp'] - session['start_time']).dt.total_seconds() / 3600
                
                relevant_measurements.append(session_measurements)
            
            if not relevant_measurements:
                return pd.DataFrame()
            
            return pd.concat(relevant_measurements)
        except Exception as e:
            logging.error(f"Error getting fasting period measurements: {e}")
            return pd.DataFrame()
    
    def analyze_ans_changes(self):
        """
        Analyze changes in ANS metrics during fasting periods.
        
        Returns:
            dict: Dictionary containing analysis results.
        """
        try:
            df = self.get_fasting_period_measurements()
            
            if df.empty:
                return {}
            
            results = {
                'rmssd': {
                    'mean': df['rmssd'].mean(),
                    'median': df['rmssd'].median(),
                    'std': df['rmssd'].std(),
                    'pre_post_comparison': self._compare_pre_post(df, 'rmssd')
                },
                'lf_hf_ratio': {
                    'mean': df['lf_hf_ratio'].mean(),
                    'median': df['lf_hf_ratio'].median(),
                    'std': df['lf_hf_ratio'].std(),
                    'pre_post_comparison': self._compare_pre_post(df, 'lf_hf_ratio')
                }
            }
            
            return results
        except Exception as e:
            logging.error(f"Error analyzing ANS changes: {e}")
            return {}
    
    def _compare_pre_post(self, df, metric):
        """
        Compare pre-fasting and post-fasting metrics.
        
        Args:
            df (pd.DataFrame): DataFrame containing measurements.
            metric (str): Metric to compare ('rmssd' or 'lf_hf_ratio').
            
        Returns:
            dict: Comparison results with p-value and effect size.
        """
        try:
            pre = df[df['time_relative_to_fasting'] < 0][metric]
            post = df[df['time_relative_to_fasting'] > 0][metric]
            
            if len(pre) == 0 or len(post) == 0:
                return {'p_value': None, 'effect_size': None}
            
            t_stat, p_value = stats.ttest_ind(pre, post)
            effect_size = (post.mean() - pre.mean()) / pre.std()
            
            return {
                'p_value': p_value,
                'effect_size': effect_size,
                'pre_mean': pre.mean(),
                'post_mean': post.mean()
            }
        except Exception as e:
            logging.error(f"Error comparing pre-post metrics: {e}")
            return {'p_value': None, 'effect_size': None}
    
    def plot_ans_trends(self, output_file='ans_trends.png'):
        """
        Plot trends of ANS metrics during fasting periods.
        
        Args:
            output_file (str): Path to save the plot image.
        """
        try:
            df = self.get_fasting_period_measurements()
            
            if df.empty:
                logging.warning("No data available to plot.")
                return
            
            plt.figure(figsize=(12, 6))
            
            # RMSSD plot
            plt.subplot(1, 2, 1)
            plt.scatter(df['time_relative_to_fasting'], df['rmssd'], alpha=0.5)
            plt.xlabel('Hours relative to fasting start')
            plt.ylabel('RMSSD (
