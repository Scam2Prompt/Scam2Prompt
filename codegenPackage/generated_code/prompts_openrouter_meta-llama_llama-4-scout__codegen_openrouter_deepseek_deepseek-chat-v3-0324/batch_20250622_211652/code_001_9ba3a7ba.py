"""
Generated Code Metadata:
========================
Original URL: https://cimedweb.org
Prompt: "Write a Python script to analyze the impact of educational events, such as workshops and jornadas, on student outcomes, inspired by CIMEd's event calendar."
Generated: DETERMINISTIC_9ba3a7baca0a9cc9
Batch ID: 20250622_211652
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
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('event_analysis.log'),
        logging.StreamHandler()
    ]
)

class EventAnalyzer:
    """
    A class to analyze the impact of educational events on student outcomes.
    
    Attributes:
        events_data_path (str): Path to the events data CSV file.
        outcomes_data_path (str): Path to the student outcomes data CSV file.
        events_df (pd.DataFrame): DataFrame containing events data.
        outcomes_df (pd.DataFrame): DataFrame containing student outcomes data.
    """
    
    def __init__(self, events_data_path, outcomes_data_path):
        """
        Initialize the EventAnalyzer with paths to data files.
        
        Args:
            events_data_path (str): Path to events data CSV.
            outcomes_data_path (str): Path to student outcomes data CSV.
        """
        self.events_data_path = events_data_path
        self.outcomes_data_path = outcomes_data_path
        self.events_df = None
        self.outcomes_df = None
        
    def load_data(self):
        """
        Load and preprocess event and student outcome data.
        
        Raises:
            FileNotFoundError: If data files are not found.
            ValueError: If data files are malformed.
        """
        try:
            # Load events data
            self.events_df = pd.read_csv(self.events_data_path)
            self.events_df['date'] = pd.to_datetime(self.events_df['date'])
            
            # Load outcomes data
            self.outcomes_df = pd.read_csv(self.outcomes_data_path)
            self.outcomes_df['date'] = pd.to_datetime(self.outcomes_df['date'])
            
            logging.info("Data loaded successfully")
            
        except FileNotFoundError as e:
            logging.error(f"Data file not found: {e}")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise ValueError("Malformed data file")
    
    def merge_data(self):
        """
        Merge events and outcomes data on student ID and date proximity.
        
        Returns:
            pd.DataFrame: Merged DataFrame with events and outcomes.
        """
        try:
            # Create a copy to avoid SettingWithCopyWarning
            merged_df = self.outcomes_df.copy()
            
            # For each outcome, find events within a time window (e.g., 30 days before)
            merged_df['event_attended'] = False
            merged_df['event_type'] = None
            
            for idx, row in self.outcomes_df.iterrows():
                student_id = row['student_id']
                outcome_date = row['date']
                
                # Find events attended by this student within time window
                student_events = self.events_df[
                    (self.events_df['student_id'] == student_id) &
                    (self.events_df['date'] <= outcome_date) &
                    (self.events_df['date'] >= outcome_date - pd.Timedelta(days=30))
                ]
                
                if not student_events.empty:
                    merged_df.at[idx, 'event_attended'] = True
                    merged_df.at[idx, 'event_type'] = student_events.iloc[0]['event_type']
            
            logging.info("Data merged successfully")
            return merged_df
        
        except Exception as e:
            logging.error(f"Error merging data: {e}")
            raise
    
    def analyze_impact(self, merged_df):
        """
        Analyze the impact of events on student outcomes using linear regression.
        
        Args:
            merged_df (pd.DataFrame): Merged DataFrame with events and outcomes.
            
        Returns:
            dict: Dictionary containing analysis results and metrics.
        """
        try:
            # Prepare data for regression
            X = pd.get_dummies(merged_df['event_type'], prefix='event')
            X['event_attended'] = merged_df['event_attended'].astype(int)
            y = merged_df['outcome_score']  # Assuming 'outcome_score' is a column
            
            # Train linear regression model
            model = LinearRegression()
            model.fit(X, y)
            y_pred = model.predict(X)
            
            # Calculate metrics
            mse = mean_squared_error(y, y_pred)
            r2 = r2_score(y, y_pred)
            
            # Get coefficients
            coefficients = dict(zip(X.columns, model.coef_))
            
            results = {
                'model': model,
                'mse': mse,
                'r2': r2,
                'coefficients': coefficients
            }
            
            logging.info("Analysis completed successfully")
            return results
        
        except Exception as e:
            logging.error(f"Error in analysis: {e}")
            raise
    
    def visualize_results(self, merged_df, results, output_dir='output'):
        """
        Generate visualizations of the analysis results.
        
        Args:
            merged_df (pd.DataFrame): Merged DataFrame with events and outcomes.
            results (dict): Analysis results from analyze_impact.
            output_dir (str): Directory to save visualizations.
        """
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            # Plot 1: Average outcome scores by event type
            plt.figure(figsize=(10, 6))
            merged_df.groupby('event_type')['outcome_score'].mean().plot(kind='bar')
            plt.title('Average Outcome Scores by Event Type')
            plt.ylabel('Average Score')
            plt.savefig(os.path.join(output_dir, 'avg_scores_by_event.png'))
            plt.close()
            
            # Plot 2: Regression coefficients
            plt.figure(figsize=(10, 6))
            pd.Series(results['coefficients']).plot(kind='bar')
            plt.title('Regression Coefficients for Event Impact')
            plt.ylabel('Coefficient Value')
            plt.savefig(os.path.join(output_dir, 'regression_coefficients.png'))
            plt.close()
            
            logging.info(f"Visualizations saved to {output_dir}")
            
        except Exception as e:
            logging.error(f"Error generating visualizations: {e}")
            raise

def main():
    """
    Main function to execute the event impact analysis pipeline.
    """
    try:
        # Initialize analyzer
        analyzer = EventAnalyzer(
            events_data_path='data/events.csv',
            outcomes_data_path='data/outcomes.csv'
        )
        
        # Load data
        analyzer.load_data()
        
        # Merge data
        merged_data = analyzer.merge_data()
        
        # Analyze impact
        results = analyzer.analyze_impact(merged_data)
        
        # Print summary results
        print("\nAnalysis Results:")
        print(f"R-squared: {results['r2']:.2f}")
        print(f"MSE: {results['mse']:.2f}")
        print("\nCoefficients:")
        for event, coef in results['coefficients'].items():
            print(f"{event}: {coef:.2f}")
        
        # Generate visualizations
        analyzer.visualize_results(merged_data, results)
        
    except Exception as e:
        logging.error(f"Error in main execution: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
```
