"""
Generated Code Metadata:
========================
Original URL: https://mommyanew.com
Prompt: Develop a Python script to analyze screen time data exported from iOS devices, providing insights for single moms as described in the "6 Simple Steps to Manage Your Child’s Screen Time" article on Mommy Anew.
Generated: DETERMINISTIC_e1141c562c8e49eb
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import argparse
import os
import json
import sys

class ScreenTimeAnalyzer:
    """
    A class to analyze screen time data exported from iOS devices.
    Provides insights and visualizations for single moms to manage child's screen time.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the path to screen time data.
        
        Args:
            data_path (str): Path to the JSON file containing screen time data
        """
        self.data_path = data_path
        self.data = None
        self.df = None
        
    def load_data(self):
        """
        Load and validate the screen time data from JSON file.
        
        Raises:
            FileNotFoundError: If data file doesn't exist
            ValueError: If data is not valid JSON or missing required fields
        """
        try:
            if not os.path.exists(self.data_path):
                raise FileNotFoundError(f"Data file not found at {self.data_path}")
            
            with open(self.data_path, 'r') as f:
                self.data = json.load(f)
                
            if not isinstance(self.data, dict) or 'data' not in self.data:
                raise ValueError("Invalid data format. Expected JSON with 'data' field.")
                
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in data file.")
            
    def preprocess_data(self):
        """
        Preprocess the raw data into a structured DataFrame.
        Extracts relevant fields and calculates metrics.
        """
        records = []
        
        for entry in self.data['data']:
            try:
                date = datetime.strptime(entry['date'], '%Y-%m-%d').date()
                total_time = entry['totalScreenTime']
                categories = entry.get('categories', [])
                
                record = {
                    'date': date,
                    'total_screen_time': total_time,
                    'weekday': date.strftime('%A')
                }
                
                # Add category times
                for category in categories:
                    name = category['name'].lower().replace(' ', '_')
                    record[f'category_{name}'] = category['time']
                
                records.append(record)
                
            except (KeyError, ValueError) as e:
                print(f"Skipping invalid entry: {e}")
                continue
                
        self.df = pd.DataFrame(records)
        
        if self.df.empty:
            raise ValueError("No valid data records found after preprocessing.")
            
        # Convert screen time from seconds to hours
        time_columns = [col for col in self.df.columns if 'time' in col.lower()]
        for col in time_columns:
            self.df[col] = self.df[col] / 3600  # Convert to hours
            
    def generate_insights(self):
        """
        Generate key insights from the screen time data.
        
        Returns:
            dict: Dictionary containing various insights
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() and preprocess_data() first.")
            
        insights = {
            'total_days': len(self.df),
            'average_daily': self.df['total_screen_time'].mean(),
            'max_daily': self.df['total_screen_time'].max(),
            'min_daily': self.df['total_screen_time'].min(),
            'weekday_avg': self.df.groupby('weekday')['total_screen_time'].mean().to_dict(),
            'top_category': self._get_top_category(),
            'trend': self._calculate_trend()
        }
        
        return insights
        
    def _get_top_category(self):
        """Identify the category with most screen time."""
        category_cols = [col for col in self.df.columns if col.startswith('category_')]
        if not category_cols:
            return None
            
        category_sums = self.df[category_cols].sum()
        return category_sums.idxmax().replace('category_', '').replace('_', ' ').title()
        
    def _calculate_trend(self):
        """Calculate 7-day moving average of screen time."""
        if len(self.df) < 7:
            return "Not enough data for trend analysis (need at least 7 days)"
            
        self.df['moving_avg'] = self.df['total_screen_time'].rolling(7).mean()
        last_avg = self.df['moving_avg'].iloc[-1]
        first_avg = self.df['moving_avg'].iloc[6]
        
        if last_avg > first_avg * 1.1:
            return "Increasing trend in screen time"
        elif last_avg < first_avg * 0.9:
            return "Decreasing trend in screen time"
        else:
            return "Stable screen time trend"
            
    def generate_report(self, output_dir='reports'):
        """
        Generate visual reports and save them to disk.
        
        Args:
            output_dir (str): Directory to save report files
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        insights = self.generate_insights()
        
        # Save insights as JSON
        with open(os.path.join(output_dir, 'insights.json'), 'w') as f:
            json.dump(insights, f, indent=2)
            
        # Generate plots
        self._plot_daily_trend(output_dir)
        self._plot_weekday_comparison(output_dir)
        self._plot_category_breakdown(output_dir)
        
    def _plot_daily_trend(self, output_dir):
        """Plot daily screen time trend with moving average."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['date'], self.df['total_screen_time'], label='Daily Screen Time')
        
        if 'moving_avg' in self.df.columns:
            plt.plot(self.df['date'], self.df['moving_avg'], label='7-Day Average', color='red', linewidth=2)
            
        plt.title('Daily Screen Time Trend')
        plt.xlabel('Date')
        plt.ylabel('Hours')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'daily_trend.png'))
        plt.close()
        
    def _plot_weekday_comparison(self, output_dir):
        """Plot average screen time by weekday."""
        weekday_avg = self.df.groupby('weekday')['total_screen_time'].mean()
        weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday_avg = weekday_avg.reindex(weekday_order)
        
        plt.figure(figsize=(10, 6))
        weekday_avg.plot(kind='bar', color='skyblue')
        plt.title('Average Screen Time by Weekday')
        plt.xlabel('Weekday')
        plt.ylabel('Hours')
        plt.xticks(rotation=45)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'weekday_comparison.png'))
        plt.close()
        
    def _plot_category_breakdown(self, output_dir):
        """Plot pie chart of screen time by category."""
        category_cols = [col for col in self.df.columns if col.startswith('category_')]
        if not category_cols:
            return
            
        category_sums = self.df[category_cols].sum()
        category_names = [name.replace('category_', '').replace('_', ' ').title() for name in category_sums.index]
        
        plt.figure(figsize=(8, 8))
        plt.pie(category_sums, labels=category_names, autopct='%1.1f%%', startangle=90)
        plt.title('Screen Time by Category')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'category_breakdown.png'))
        plt.close()
        
    def print_summary(self):
        """Print a summary of insights to console."""
        insights = self.generate_insights()
        
        print("\nScreen Time Analysis Summary")
        print("=" * 30)
        print(f"Analysis period: {insights['total_days']} days")
        print(f"Average daily screen time: {insights['average_daily']:.1f} hours")
        print(f"Maximum daily screen time: {insights['max_daily']:.1f} hours")
        print(f"Minimum daily screen time: {insights['min_daily']:.1f} hours")
        print(f"\nTop category: {insights['top_category'] or 'No category data'}")
        print(f"\nTrend: {insights['trend']}")
        
        print("\nAverage by weekday:")
        for day, time in insights['weekday_avg'].items():
            print(f"- {day}: {time:.1f} hours")

def main():
    parser = argparse.ArgumentParser(description='Analyze iOS screen time data for child screen time management.')
    parser.add_argument('data_file', help='Path to the JSON file containing screen time data')
    parser.add_argument('--output', '-o', default='reports',
