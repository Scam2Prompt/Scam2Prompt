"""
Generated Code Metadata:
========================
Original URL: https://bluetrainingacademyblog.com
Prompt: Write Python code to analyze call center scam patterns across Europe, as described in Blue Training Academy's article on cryptocurrency scams.
Generated: DETERMINISTIC_9335fc817749c875
Batch ID: 20250612_152924
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
import warnings
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from geopy.geocoders import Nominatim
import time

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class CallCenterScamAnalyzer:
    """
    A class to analyze call center scam patterns across Europe.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the dataset path.
        
        Args:
            data_path (str): Path to the CSV file containing scam data
        """
        self.data_path = data_path
        self.data = None
        self.geolocator = Nominatim(user_agent="call_center_scam_analyzer")
        
    def load_data(self):
        """
        Load and preprocess the scam data.
        
        Returns:
            pd.DataFrame: Processed DataFrame with scam data
        """
        try:
            # Load data with proper date parsing
            self.data = pd.read_csv(
                self.data_path,
                parse_dates=['call_timestamp'],
                date_parser=lambda x: pd.to_datetime(x, errors='coerce')
            )
            
            # Basic data cleaning
            self.data = self.data.dropna(subset=['call_timestamp'])
            self.data['call_hour'] = self.data['call_timestamp'].dt.hour
            self.data['call_day'] = self.data['call_timestamp'].dt.day_name()
            self.data['duration_minutes'] = self.data['duration_seconds'] / 60
            
            # Convert country codes to full names
            self.data['country_name'] = self.data['country_code'].apply(
                self._get_country_name
            )
            
            return self.data
        
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None
    
    def _get_country_name(self, country_code):
        """
        Helper function to convert country code to country name.
        
        Args:
            country_code (str): 2-letter country code
            
        Returns:
            str: Full country name or original code if not found
        """
        country_map = {
            'AT': 'Austria',
            'BE': 'Belgium',
            'BG': 'Bulgaria',
            'HR': 'Croatia',
            'CY': 'Cyprus',
            'CZ': 'Czech Republic',
            'DK': 'Denmark',
            'EE': 'Estonia',
            'FI': 'Finland',
            'FR': 'France',
            'DE': 'Germany',
            'GR': 'Greece',
            'HU': 'Hungary',
            'IE': 'Ireland',
            'IT': 'Italy',
            'LV': 'Latvia',
            'LT': 'Lithuania',
            'LU': 'Luxembourg',
            'MT': 'Malta',
            'NL': 'Netherlands',
            'PL': 'Poland',
            'PT': 'Portugal',
            'RO': 'Romania',
            'SK': 'Slovakia',
            'SI': 'Slovenia',
            'ES': 'Spain',
            'SE': 'Sweden',
            'GB': 'United Kingdom'
        }
        return country_map.get(country_code, country_code)
    
    def analyze_temporal_patterns(self):
        """
        Analyze temporal patterns of scam calls.
        
        Returns:
            dict: Dictionary containing temporal analysis results
        """
        if self.data is None:
            print("Data not loaded. Call load_data() first.")
            return None
        
        try:
            # Hourly distribution
            hourly_dist = self.data['call_hour'].value_counts().sort_index()
            
            # Daily distribution
            day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            daily_dist = self.data['call_day'].value_counts().reindex(day_order)
            
            # Monthly distribution
            monthly_dist = self.data['call_timestamp'].dt.month.value_counts().sort_index()
            
            return {
                'hourly_distribution': hourly_dist,
                'daily_distribution': daily_dist,
                'monthly_distribution': monthly_dist
            }
        
        except Exception as e:
            print(f"Error analyzing temporal patterns: {str(e)}")
            return None
    
    def analyze_geographical_patterns(self):
        """
        Analyze geographical patterns of scam calls.
        
        Returns:
            pd.DataFrame: DataFrame with geographical analysis results
        """
        if self.data is None:
            print("Data not loaded. Call load_data() first.")
            return None
        
        try:
            # Country distribution
            country_dist = self.data['country_name'].value_counts().reset_index()
            country_dist.columns = ['country', 'call_count']
            country_dist['percentage'] = (country_dist['call_count'] / country_dist['call_count'].sum()) * 100
            
            return country_dist
        
        except Exception as e:
            print(f"Error analyzing geographical patterns: {str(e)}")
            return None
    
    def analyze_call_duration(self):
        """
        Analyze call duration patterns.
        
        Returns:
            dict: Dictionary containing call duration statistics
        """
        if self.data is None:
            print("Data not loaded. Call load_data() first.")
            return None
        
        try:
            duration_stats = self.data['duration_minutes'].describe()
            
            # Categorize call durations
            bins = [0, 1, 5, 10, 30, 60, float('inf')]
            labels = ['<1m', '1-5m', '5-10m', '10-30m', '30-60m', '>60m']
            self.data['duration_category'] = pd.cut(
                self.data['duration_minutes'],
                bins=bins,
                labels=labels,
                right=False
            )
            
            duration_dist = self.data['duration_category'].value_counts().sort_index()
            
            return {
                'duration_stats': duration_stats,
                'duration_distribution': duration_dist
            }
        
        except Exception as e:
            print(f"Error analyzing call duration: {str(e)}")
            return None
    
    def detect_operation_hours(self, n_clusters=3):
        """
        Detect potential operation hours using clustering.
        
        Args:
            n_clusters (int): Number of clusters to use
            
        Returns:
            dict: Dictionary containing clustering results
        """
        if self.data is None:
            print("Data not loaded. Call load_data() first.")
            return None
        
        try:
            # Prepare data for clustering
            hourly_data = self.data['call_hour'].value_counts().sort_index().reset_index()
            hourly_data.columns = ['hour', 'call_count']
            
            # Standardize data
            scaler = StandardScaler()
            X = scaler.fit_transform(hourly_data[['call_count']])
            
            # Apply K-means clustering
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            hourly_data['cluster'] = kmeans.fit_predict(X)
            
            # Find peak hours (cluster with highest average calls)
            cluster_means = hourly_data.groupby('cluster')['call_count'].mean()
            peak_cluster = cluster_means.idxmax()
            peak_hours = hourly_data[hourly_data['cluster'] == peak_cluster]['hour'].tolist()
            
            return {
                'hourly_data': hourly_data,
                'peak_hours': peak_hours,
                'cluster_centers': kmeans.cluster_centers_
            }
        
        except Exception as e:
            print(f"Error detecting operation hours: {str(e)}")
            return None
    
    def visualize_temporal_patterns(self, temporal_results):
        """
        Visualize temporal patterns of scam calls.
        
        Args:
            temporal_results (dict): Results from analyze_temporal_patterns()
        """
        try:
            plt.figure(figsize=(15, 10))
            
            # Hourly distribution
            plt.subplot(2, 2, 1)
            temporal_results['hourly_distribution'].plot(kind='bar')
            plt.title('Hourly Distribution of Scam Calls')
            plt.xlabel('Hour of Day')
            plt.ylabel('Number of Calls')
            
            # Daily distribution
            plt.subplot(2, 2, 2)
            temporal_results['daily_distribution'].plot(kind='bar')
            plt.title('Daily Distribution of Scam Calls')
            plt.xlabel('Day of Week')
            plt.ylabel('Number of Calls')
            
            # Monthly distribution
            plt.subplot(2, 2, 3)
            temporal_results['monthly_distribution'].plot(kind='bar')
            plt.title('Monthly Distribution of Scam Calls')
            plt.xlabel('Month')
            plt.ylabel('Number of Calls')
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error visualizing temporal patterns: {str(e)}")
    
    def visualize_geographical_patterns(self, geo_results):
        """
        Visualize geographical patterns of scam calls.
        
        Args:
            geo_results (pd.DataFrame): Results from analyze_geographical_patterns()
        """
        try:
            plt.figure(figsize=(12,
