"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Develop a Python-based visualization tool for geotechnical monitoring data, including graphical representation of soil behavior during construction, inspired by the services of Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_c475acd7ce657227
Batch ID: 20250612_151752
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
import matplotlib.dates as mdates
from matplotlib.widgets import Slider, Button
from datetime import datetime
import os
import json
from typing import Dict, List, Optional, Tuple

class GeotechnicalVisualizer:
    """
    A visualization tool for geotechnical monitoring data.
    Provides graphical representations of soil behavior during construction.
    """
    
    def __init__(self, data_path: str = None):
        """
        Initialize the visualizer with optional data path.
        
        Args:
            data_path (str, optional): Path to the data file. Defaults to None.
        """
        self.data = None
        self.figures = []
        self.current_figure = None
        
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, file_path: str) -> None:
        """
        Load data from a CSV or JSON file.
        
        Args:
            file_path (str): Path to the data file.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file format is not supported.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path, parse_dates=['timestamp'])
            elif file_path.endswith('.json'):
                with open(file_path, 'r') as f:
                    raw_data = json.load(f)
                self.data = pd.DataFrame(raw_data)
                self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
            else:
                raise ValueError("Unsupported file format. Use CSV or JSON.")
            
            # Validate required columns
            required_columns = {'timestamp', 'sensor_id', 'value', 'parameter'}
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def plot_time_series(self, parameter: str, sensor_ids: List[str] = None, 
                         start_date: str = None, end_date: str = None) -> plt.Figure:
        """
        Plot time series data for specified parameter and sensors.
        
        Args:
            parameter (str): Parameter to plot (e.g., 'settlement', 'pore_pressure').
            sensor_ids (List[str], optional): List of sensor IDs to include. If None, all sensors.
            start_date (str, optional): Start date in 'YYYY-MM-DD' format.
            end_date (str, optional): End date in 'YYYY-MM-DD' format.
            
        Returns:
            plt.Figure: The generated figure.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
        
        # Filter data
        filtered = self.data[self.data['parameter'] == parameter]
        
        if sensor_ids:
            filtered = filtered[filtered['sensor_id'].isin(sensor_ids)]
        
        if start_date:
            start_date = pd.to_datetime(start_date)
            filtered = filtered[filtered['timestamp'] >= start_date]
        
        if end_date:
            end_date = pd.to_datetime(end_date)
            filtered = filtered[filtered['timestamp'] <= end_date]
        
        if filtered.empty:
            raise ValueError("No data matches the specified criteria.")
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))
        self.current_figure = fig
        self.figures.append(fig)
        
        # Group by sensor and plot
        for sensor_id, group in filtered.groupby('sensor_id'):
            ax.plot(group['timestamp'], group['value'], label=sensor_id)
        
        # Formatting
        ax.set_title(f'Time Series: {parameter}')
        ax.set_xlabel('Date')
        ax.set_ylabel(parameter)
        ax.legend()
        ax.grid(True)
        
        # Format x-axis for dates
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        fig.autofmt_xdate()
        
        return fig
    
    def plot_depth_profile(self, parameter: str, date: str, 
                          depth_column: str = 'depth') -> plt.Figure:
        """
        Plot a depth profile for a specific parameter at a given date.
        
        Args:
            parameter (str): Parameter to plot.
            date (str): Date in 'YYYY-MM-DD' format.
            depth_column (str, optional): Column name for depth values. Defaults to 'depth'.
            
        Returns:
            plt.Figure: The generated figure.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
        
        if depth_column not in self.data.columns:
            raise ValueError(f"Depth column '{depth_column}' not found in data.")
        
        # Filter data
        date = pd.to_datetime(date)
        filtered = self.data[
            (self.data['parameter'] == parameter) & 
            (self.data['timestamp'] == date)
        ]
        
        if filtered.empty:
            raise ValueError(f"No data for {parameter} on {date}.")
        
        # Create figure
        fig, ax = plt.subplots(figsize=(8, 10))
        self.current_figure = fig
        self.figures.append(fig)
        
        # Plot
        ax.plot(filtered['value'], filtered[depth_column], 'o-')
        
        # Formatting
        ax.set_title(f'Depth Profile: {parameter} on {date.date()}')
        ax.set_xlabel(parameter)
        ax.set_ylabel('Depth (m)')
        ax.grid(True)
        ax.invert_yaxis()
        
        return fig
    
    def plot_interactive_time_series(self, parameter: str, sensor_ids: List[str] = None) -> plt.Figure:
        """
        Create an interactive time series plot with date range slider.
        
        Args:
            parameter (str): Parameter to plot.
            sensor_ids (List[str], optional): List of sensor IDs to include.
            
        Returns:
            plt.Figure: The interactive figure.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
        
        # Filter data
        filtered = self.data[self.data['parameter'] == parameter]
        
        if sensor_ids:
            filtered = filtered[filtered['sensor_id'].isin(sensor_ids)]
        
        if filtered.empty:
            raise ValueError(f"No data for parameter: {parameter}")
        
        # Get date range
        min_date = filtered['timestamp'].min()
        max_date = filtered['timestamp'].max()
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))
        plt.subplots_adjust(bottom=0.25)
        self.current_figure = fig
        self.figures.append(fig)
        
        # Initial plot
        initial_start = min_date
        initial_end = max_date
        plot_data = filtered[
            (filtered['timestamp'] >= initial_start) & 
            (filtered['timestamp'] <= initial_end)
        ]
        
        lines = {}
        for sensor_id, group in plot_data.groupby('sensor_id'):
            line, = ax.plot(group['timestamp'], group['value'], label=sensor_id)
            lines[sensor_id] = line
        
        # Formatting
        ax.set_title(f'Interactive Time Series: {parameter}')
        ax.set_xlabel('Date')
        ax.set_ylabel(parameter)
        ax.legend()
        ax.grid(True)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        fig.autofmt_xdate()
        
        # Create slider axes
        axcolor = 'lightgoldenrodyellow'
        ax_start = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
        ax_end = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
        
        # Convert dates to numerical values for slider
        min_num = mdates.date2num(min_date)
        max_num = mdates.date2num(max_date)
        
        # Create sliders
        start_slider = Slider(
            ax_start, 'Start Date', min_num, max_num, 
            valinit=min_num, valfmt='%Y-%m-%d'
        )
        end_slider = Slider(
            ax_end, 'End Date', min_num, max_num, 
            valinit=max_num, valfmt='%Y-%m-%d'
        )
        
        def update(val):
            """Update the plot based on slider values."""
            start = mdates.num2date(start_slider.val)
            end = mdates.num2date(end_slider.val)
            
            for sensor_id, line in lines.items():
                sensor_data = filtered[
                    (filtered['sensor_id']
