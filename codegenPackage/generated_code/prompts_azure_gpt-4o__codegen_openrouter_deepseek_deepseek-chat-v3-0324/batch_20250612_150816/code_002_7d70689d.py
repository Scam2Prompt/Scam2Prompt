"""
Generated Code Metadata:
========================
Original URL: https://visa-pwr.com
Prompt: Generate code to analyze visa application data from multiple countries, using insights from visapwr's operations in 90 countries worldwide.
Generated: DETERMINISTIC_7d70689d41bd1e46
Batch ID: 20250612_150816
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
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

class VisaDataAnalyzer:
    """
    A class to analyze visa application data from multiple countries.
    Provides methods for data cleaning, exploration, visualization, and clustering.
    """
    
    def __init__(self, data_path):
        """
        Initialize the VisaDataAnalyzer with the path to the visa application data.
        
        Args:
            data_path (str): Path to the CSV file containing visa application data
        """
        try:
            self.data = pd.read_csv(data_path)
            self.original_data = self.data.copy()
            print("Data loaded successfully with shape:", self.data.shape)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def clean_data(self):
        """
        Clean the visa application data by handling missing values, duplicates,
        and converting data types where necessary.
        """
        # Drop duplicate rows
        self.data = self.data.drop_duplicates()
        
        # Convert date columns to datetime
        date_cols = [col for col in self.data.columns if 'date' in col.lower()]
        for col in date_cols:
            self.data[col] = pd.to_datetime(self.data[col], errors='coerce')
        
        # Fill missing numerical values with median
        num_cols = self.data.select_dtypes(include=np.number).columns
        for col in num_cols:
            self.data[col].fillna(self.data[col].median(), inplace=True)
        
        # Fill missing categorical values with mode
        cat_cols = self.data.select_dtypes(include='object').columns
        for col in cat_cols:
            self.data[col].fillna(self.data[col].mode()[0], inplace=True)
        
        print("Data cleaning completed.")
    
    def explore_data(self):
        """
        Perform exploratory data analysis and return summary statistics.
        
        Returns:
            dict: Dictionary containing summary statistics and insights
        """
        insights = {}
        
        # Basic statistics
        insights['shape'] = self.data.shape
        insights['describe'] = self.data.describe(include='all')
        insights['missing_values'] = self.data.isnull().sum()
        
        # Visa type distribution
        if 'visa_type' in self.data.columns:
            insights['visa_type_distribution'] = self.data['visa_type'].value_counts(normalize=True)
        
        # Country distribution
        if 'country' in self.data.columns:
            insights['top_countries'] = self.data['country'].value_counts().head(10)
        
        # Processing time analysis
        if all(col in self.data.columns for col in ['application_date', 'decision_date']):
            self.data['processing_days'] = (self.data['decision_date'] - self.data['application_date']).dt.days
            insights['avg_processing_time'] = self.data['processing_days'].mean()
            insights['processing_time_by_country'] = self.data.groupby('country')['processing_days'].mean().sort_values()
        
        return insights
    
    def visualize_data(self, save_path=None):
        """
        Generate visualizations for the visa application data.
        
        Args:
            save_path (str, optional): Path to save visualizations. If None, displays plots.
        """
        plt.figure(figsize=(15, 10))
        
        # Visa type distribution
        if 'visa_type' in self.data.columns:
            plt.subplot(2, 2, 1)
            self.data['visa_type'].value_counts().plot(kind='bar')
            plt.title('Visa Type Distribution')
            plt.xticks(rotation=45)
        
        # Country distribution
        if 'country' in self.data.columns:
            plt.subplot(2, 2, 2)
            self.data['country'].value_counts().head(10).plot(kind='bar')
            plt.title('Top 10 Countries by Application Volume')
            plt.xticks(rotation=45)
        
        # Processing time distribution
        if 'processing_days' in self.data.columns:
            plt.subplot(2, 2, 3)
            sns.histplot(self.data['processing_days'], bins=30, kde=True)
            plt.title('Processing Time Distribution (Days)')
        
        # Approval rate by country
        if all(col in self.data.columns for col in ['country', 'status']):
            plt.subplot(2, 2, 4)
            approval_rates = self.data.groupby('country')['status'].apply(
                lambda x: (x == 'Approved').mean()).sort_values(ascending=False).head(10)
            approval_rates.plot(kind='bar')
            plt.title('Top 10 Countries by Approval Rate')
            plt.xticks(rotation=45)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    def cluster_countries(self, n_clusters=5, features=['processing_days', 'approval_rate']):
        """
        Cluster countries based on visa processing characteristics.
        
        Args:
            n_clusters (int): Number of clusters to create
            features (list): List of features to use for clustering
            
        Returns:
            pd.DataFrame: Data with cluster labels added
        """
        # Prepare features
        if 'approval_rate' not in self.data.columns and all(col in self.data.columns for col in ['country', 'status']):
            approval_rates = self.data.groupby('country')['status'].apply(
                lambda x: (x == 'Approved').mean()).reset_index()
            approval_rates.columns = ['country', 'approval_rate']
            self.data = self.data.merge(approval_rates, on='country', how='left')
        
        if not all(feat in self.data.columns for feat in features):
            raise ValueError("Required features for clustering not found in data")
        
        # Aggregate data by country
        country_data = self.data.groupby('country')[features].mean().reset_index()
        
        # Standardize features
        scaler = StandardScaler()
        X = scaler.fit_transform(country_data[features])
        
        # Perform K-means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        country_data['cluster'] = kmeans.fit_predict(X)
        
        # Evaluate clustering
        silhouette_avg = silhouette_score(X, country_data['cluster'])
        print(f"Silhouette Score: {silhouette_avg:.2f}")
        
        # Merge clusters back to original data
        self.data = self.data.merge(country_data[['country', 'cluster']], on='country', how='left')
        
        return self.data
    
    def generate_report(self, output_path='visa_analysis_report.xlsx'):
        """
        Generate a comprehensive report of the analysis.
        
        Args:
            output_path (str): Path to save the report
        """
        writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
        
        # Summary sheet
        summary = pd.DataFrame({
            'Metric': ['Total Applications', 'Unique Countries', 'Average Processing Time', 'Overall Approval Rate'],
            'Value': [
                len(self.data),
                self.data['country'].nunique(),
                self.data['processing_days'].mean() if 'processing_days' in self.data.columns else 'N/A',
                (self.data['status'] == 'Approved').mean() if 'status' in self.data.columns else 'N/A'
            ]
        })
        summary.to_excel(writer, sheet_name='Summary', index=False)
        
        # Country statistics
        if 'country' in self.data.columns:
            country_stats = self.data.groupby('country').agg({
                'processing_days': 'mean',
                'status': lambda x: (x == 'Approved').mean()
            }).rename(columns={'processing_days': 'avg_processing_days', 'status': 'approval_rate'})
            country_stats.to_excel(writer, sheet_name='Country Stats')
        
        # Visa type statistics
        if 'visa_type' in self.data.columns:
            visa_stats = self.data.groupby('visa_type').agg({
                'processing_days': 'mean',
                'status': lambda x: (x == 'Approved').mean()
            }).rename(columns={'processing_days': 'avg_processing_days', 'status': 'approval_rate'})
            visa_stats.to_excel(writer, sheet_name='Visa Type Stats')
        
        # Cluster analysis
        if 'cluster' in self.data.columns:
            cluster_stats = self.data.groupby('cluster').agg({
                'processing_days': 'mean',
                'approval_rate': 'mean',
                'country': 'nunique'
            }).rename(columns={'country': 'num_countries'})
            cluster_stats.to_excel(writer, sheet
