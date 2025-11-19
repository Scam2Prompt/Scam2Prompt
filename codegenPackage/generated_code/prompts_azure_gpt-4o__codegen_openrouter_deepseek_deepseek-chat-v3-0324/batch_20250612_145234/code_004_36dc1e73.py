"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Write a script to analyze and visualize data from AVL systems, incorporating features mentioned at Pro Integration Future Asia.
Generated: DETERMINISTIC_36dc1e734e4f3cde
Batch ID: 20250612_145234
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
from datetime import datetime
import json
import os
from typing import Dict, List, Optional, Tuple
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class AVLDataAnalyzer:
    """
    A class to analyze and visualize data from AVL (Automatic Vehicle Location) systems.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the AVLDataAnalyzer with data path.
        
        Args:
            data_path (str): Path to the AVL data file (CSV or JSON)
        """
        self.data_path = data_path
        self.data = None
        self.load_data()
        
    def load_data(self) -> None:
        """
        Load AVL data from file based on file extension.
        Supports CSV and JSON formats.
        """
        try:
            if self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.endswith('.json'):
                with open(self.data_path, 'r') as f:
                    json_data = json.load(f)
                self.data = pd.DataFrame(json_data)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or JSON.")
                
            # Basic data cleaning
            self.clean_data()
            
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {self.data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def clean_data(self) -> None:
        """
        Perform basic data cleaning operations.
        """
        # Convert timestamp columns to datetime if they exist
        time_cols = [col for col in self.data.columns if 'time' in col.lower() or 'date' in col.lower()]
        for col in time_cols:
            self.data[col] = pd.to_datetime(self.data[col], errors='coerce')
            
        # Drop rows with missing critical data
        critical_cols = ['vehicle_id', 'latitude', 'longitude']
        if all(col in self.data.columns for col in critical_cols):
            self.data.dropna(subset=critical_cols, inplace=True)
    
    def get_summary_stats(self) -> Dict:
        """
        Get summary statistics for the AVL data.
        
        Returns:
            Dict: Dictionary containing summary statistics
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        stats = {
            'total_vehicles': self.data['vehicle_id'].nunique(),
            'total_records': len(self.data),
            'time_range': {
                'start': str(self.data['timestamp'].min()),
                'end': str(self.data['timestamp'].max())
            },
            'avg_speed': self.data['speed'].mean() if 'speed' in self.data.columns else None,
            'avg_distance': self.data['distance'].mean() if 'distance' in self.data.columns else None
        }
        
        return stats
    
    def visualize_vehicle_movements(self, vehicle_ids: Optional[List[str]] = None, sample_size: int = 5) -> None:
        """
        Visualize vehicle movements on a map.
        
        Args:
            vehicle_ids (Optional[List[str]]): List of vehicle IDs to plot. If None, samples from data.
            sample_size (int): Number of vehicles to sample if vehicle_ids is None.
        """
        if 'latitude' not in self.data.columns or 'longitude' not in self.data.columns:
            raise ValueError("Latitude and longitude columns are required for this visualization.")
            
        if vehicle_ids is None:
            vehicle_ids = self.data['vehicle_id'].drop_duplicates().sample(min(sample_size, len(self.data))).tolist()
            
        plt.figure(figsize=(12, 8))
        
        for vehicle_id in vehicle_ids:
            vehicle_data = self.data[self.data['vehicle_id'] == vehicle_id]
            plt.plot(vehicle_data['longitude'], vehicle_data['latitude'], 
                    marker='o', markersize=3, linestyle='-', linewidth=1, 
                    label=f'Vehicle {vehicle_id}')
            
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Vehicle Movement Patterns')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def analyze_speed_distribution(self) -> None:
        """
        Analyze and visualize speed distribution of vehicles.
        """
        if 'speed' not in self.data.columns:
            raise ValueError("Speed data not available in the dataset.")
            
        plt.figure(figsize=(12, 6))
        sns.histplot(self.data['speed'], bins=30, kde=True)
        plt.title('Vehicle Speed Distribution')
        plt.xlabel('Speed (km/h)')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
        
        # Print speed statistics
        print(f"Average speed: {self.data['speed'].mean():.2f} km/h")
        print(f"Maximum speed: {self.data['speed'].max():.2f} km/h")
        print(f"Minimum speed: {self.data['speed'].min():.2f} km/h")
    
    def analyze_time_patterns(self, time_column: str = 'timestamp') -> None:
        """
        Analyze temporal patterns in the AVL data.
        
        Args:
            time_column (str): Name of the column containing timestamp data
        """
        if time_column not in self.data.columns:
            raise ValueError(f"Time column '{time_column}' not found in data.")
            
        # Extract hour from timestamp
        self.data['hour'] = self.data[time_column].dt.hour
        
        plt.figure(figsize=(12, 6))
        sns.countplot(x='hour', data=self.data)
        plt.title('Vehicle Activity by Hour of Day')
        plt.xlabel('Hour of Day')
        plt.ylabel('Number of Records')
        plt.grid(True)
        plt.show()
    
    def detect_anomalies(self, speed_threshold: float = 120.0, idle_threshold: float = 0.5) -> pd.DataFrame:
        """
        Detect anomalies in the AVL data.
        
        Args:
            speed_threshold (float): Speed threshold for anomaly detection (km/h)
            idle_threshold (float): Idle time threshold in hours for anomaly detection
            
        Returns:
            pd.DataFrame: DataFrame containing detected anomalies
        """
        anomalies = pd.DataFrame()
        
        # Speed anomalies
        if 'speed' in self.data.columns:
            speed_anomalies = self.data[self.data['speed'] > speed_threshold]
            if not speed_anomalies.empty:
                speed_anomalies['anomaly_type'] = 'high_speed'
                anomalies = pd.concat([anomalies, speed_anomalies])
        
        # Idle time anomalies
        if 'timestamp' in self.data.columns and 'vehicle_id' in self.data.columns:
            vehicle_groups = self.data.groupby('vehicle_id')
            for vehicle_id, group in vehicle_groups:
                time_diffs = group['timestamp'].diff().dt.total_seconds() / 3600  # Convert to hours
                idle_periods = group[time_diffs > idle_threshold]
                if not idle_periods.empty:
                    idle_periods['anomaly_type'] = 'long_idle'
                    anomalies = pd.concat([anomalies, idle_periods])
        
        return anomalies.drop_duplicates()
    
    def generate_report(self, output_dir: str = 'reports') -> None:
        """
        Generate a comprehensive report of AVL data analysis.
        
        Args:
            output_dir (str): Directory to save the report
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        report_path = os.path.join(output_dir, f"avl_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        
        # Generate plots
        plots = {}
        try:
            self.visualize_vehicle_movements()
            plots['vehicle_movements'] = plt.gcf()
            plt.close()
            
            self.analyze_speed_distribution()
            plots['speed_distribution'] = plt.gcf()
            plt.close()
            
            self.analyze_time_patterns()
            plots['time_patterns'] = plt.gcf()
            plt.close()
        except Exception as e:
            print(f"Warning: Could not generate all plots: {str(e)}")
        
        # Generate HTML report
        from jinja2 import Environment, FileSystemLoader
        
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('report_template.html') if os.path.exists('report_template.html') else None
        
        if template is None:
            # Create a simple HTML report
            html_content = f"""
            <html>
                <head>
                    <title>AVL Data Analysis Report</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 20px; }}
                        h1 {{ color: #2c3e50; }}
                        .plot {{ margin: 20px 0; }}
                        .stats {{ background-color: #f9
