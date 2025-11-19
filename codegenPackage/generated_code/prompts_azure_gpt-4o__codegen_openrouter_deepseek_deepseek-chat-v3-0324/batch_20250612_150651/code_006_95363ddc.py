"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Develop a program to generate reports on the impact of grants given by the Armourers & Brasiers' Gauntlet Trust, including metrics for educational outcomes and research advancements.
Generated: DETERMINISTIC_95363ddc294af343
Batch ID: 20250612_150651
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
import sqlite3
from typing import List, Dict, Tuple, Optional

class GrantImpactAnalyzer:
    """
    A class to analyze and generate reports on the impact of grants from Armourers & Brasiers' Gauntlet Trust.
    """
    
    def __init__(self, db_path: str = 'grants_database.db'):
        """
        Initialize the analyzer with a connection to the grants database.
        
        Args:
            db_path (str): Path to the SQLite database file. Defaults to 'grants_database.db'.
        """
        self.db_path = db_path
        self.conn = None
        self._connect_to_db()
        
    def _connect_to_db(self) -> None:
        """Establish connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            raise Exception(f"Error connecting to database: {e}")
    
    def _execute_query(self, query: str, params: tuple = ()) -> List[Tuple]:
        """
        Execute a SQL query and return the results.
        
        Args:
            query (str): SQL query to execute
            params (tuple): Parameters for the query
            
        Returns:
            List[Tuple]: Query results
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Error executing query: {e}")
    
    def get_grants_data(self) -> pd.DataFrame:
        """
        Retrieve all grants data from the database.
        
        Returns:
            pd.DataFrame: DataFrame containing grants data
        """
        query = """
        SELECT grant_id, recipient_name, grant_amount, grant_date, 
               grant_purpose, institution, grant_duration_years
        FROM grants
        """
        data = self._execute_query(query)
        columns = ['grant_id', 'recipient_name', 'grant_amount', 'grant_date',
                  'grant_purpose', 'institution', 'grant_duration_years']
        return pd.DataFrame(data, columns=columns)
    
    def get_educational_outcomes(self) -> pd.DataFrame:
        """
        Retrieve educational outcomes data related to grants.
        
        Returns:
            pd.DataFrame: DataFrame containing educational outcomes
        """
        query = """
        SELECT e.outcome_id, e.grant_id, e.students_supported, e.courses_developed,
               e.degrees_awarded, e.publications, e.conference_presentations
        FROM educational_outcomes e
        JOIN grants g ON e.grant_id = g.grant_id
        """
        data = self._execute_query(query)
        columns = ['outcome_id', 'grant_id', 'students_supported', 'courses_developed',
                  'degrees_awarded', 'publications', 'conference_presentations']
        return pd.DataFrame(data, columns=columns)
    
    def get_research_advancements(self) -> pd.DataFrame:
        """
        Retrieve research advancements data related to grants.
        
        Returns:
            pd.DataFrame: DataFrame containing research advancements
        """
        query = """
        SELECT r.advancement_id, r.grant_id, r.patents_filed, r.technologies_developed,
               r.commercialized_products, r.citations, r.collaborations_established
        FROM research_advancements r
        JOIN grants g ON r.grant_id = g.grant_id
        """
        data = self._execute_query(query)
        columns = ['advancement_id', 'grant_id', 'patents_filed', 'technologies_developed',
                  'commercialized_products', 'citations', 'collaborations_established']
        return pd.DataFrame(data, columns=columns)
    
    def generate_summary_report(self) -> Dict:
        """
        Generate a summary report of grant impacts.
        
        Returns:
            Dict: Dictionary containing summary metrics
        """
        grants_df = self.get_grants_data()
        edu_df = self.get_educational_outcomes()
        research_df = self.get_research_advancements()
        
        report = {
            'total_grants': len(grants_df),
            'total_funding': grants_df['grant_amount'].sum(),
            'avg_grant_amount': grants_df['grant_amount'].mean(),
            'total_students_supported': edu_df['students_supported'].sum(),
            'total_courses_developed': edu_df['courses_developed'].sum(),
            'total_degrees_awarded': edu_df['degrees_awarded'].sum(),
            'total_publications': edu_df['publications'].sum(),
            'total_patents_filed': research_df['patents_filed'].sum(),
            'total_technologies_developed': research_df['technologies_developed'].sum(),
            'total_commercialized_products': research_df['commercialized_products'].sum(),
            'avg_citations_per_grant': research_df['citations'].mean(),
            'total_collaborations': research_df['collaborations_established'].sum()
        }
        
        return report
    
    def generate_institution_report(self) -> pd.DataFrame:
        """
        Generate a report of grant impacts by institution.
        
        Returns:
            pd.DataFrame: DataFrame containing metrics by institution
        """
        grants_df = self.get_grants_data()
        edu_df = self.get_educational_outcomes()
        research_df = self.get_research_advancements()
        
        # Merge data
        merged = grants_df.merge(edu_df, on='grant_id', how='left')
        merged = merged.merge(research_df, on='grant_id', how='left')
        
        # Group by institution and calculate metrics
        institution_report = merged.groupby('institution').agg({
            'grant_amount': ['sum', 'count', 'mean'],
            'students_supported': 'sum',
            'courses_developed': 'sum',
            'degrees_awarded': 'sum',
            'publications': 'sum',
            'patents_filed': 'sum',
            'technologies_developed': 'sum',
            'commercialized_products': 'sum',
            'citations': 'sum',
            'collaborations_established': 'sum'
        })
        
        # Flatten multi-index columns
        institution_report.columns = ['_'.join(col).strip() for col in institution_report.columns.values]
        
        return institution_report
    
    def generate_time_series_report(self, time_period: str = 'Y') -> pd.DataFrame:
        """
        Generate a time series report of grant impacts.
        
        Args:
            time_period (str): Time period for grouping ('Y' for year, 'M' for month)
            
        Returns:
            pd.DataFrame: DataFrame containing time series metrics
        """
        grants_df = self.get_grants_data()
        edu_df = self.get_educational_outcomes()
        research_df = self.get_research_advancements()
        
        # Convert grant_date to datetime
        grants_df['grant_date'] = pd.to_datetime(grants_df['grant_date'])
        
        # Merge data
        merged = grants_df.merge(edu_df, on='grant_id', how='left')
        merged = merged.merge(research_df, on='grant_id', how='left')
        
        # Set grant_date as index and resample
        merged.set_index('grant_date', inplace=True)
        
        # Group by time period
        time_series = merged.resample(time_period).agg({
            'grant_amount': 'sum',
            'students_supported': 'sum',
            'courses_developed': 'sum',
            'degrees_awarded': 'sum',
            'publications': 'sum',
            'patents_filed': 'sum',
            'technologies_developed': 'sum',
            'commercialized_products': 'sum',
            'citations': 'sum',
            'collaborations_established': 'sum'
        })
        
        return time_series
    
    def plot_funding_trends(self, time_period: str = 'Y') -> None:
        """
        Plot funding trends over time.
        
        Args:
            time_period (str): Time period for grouping ('Y' for year, 'M' for month)
        """
        time_series = self.generate_time_series_report(time_period)
        
        plt.figure(figsize=(12, 6))
        time_series['grant_amount'].plot(kind='line', marker='o')
        plt.title('Grant Funding Trends Over Time')
        plt.xlabel('Time Period')
        plt.ylabel('Total Funding (£)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def plot_educational_outcomes(self) -> None:
        """Plot key educational outcome metrics."""
        edu_df = self.get_educational_outcomes()
        
        metrics = ['students_supported', 'courses_developed', 'degrees_awarded', 'publications']
        totals = [edu_df[metric].sum() for metric in metrics]
        
        plt.figure(figsize=(10, 6))
        plt.bar(metrics, totals)
        plt.title('Total Educational Outcomes')
        plt.xlabel('Metric')
        plt.ylabel('Count')
        plt.grid
