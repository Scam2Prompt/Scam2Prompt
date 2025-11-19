"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Generate code for a student performance analysis tool that uses periodic test results to shuffle students into "Diamond" and "Gold" batches, as implemented by Potencia Academy.
Generated: DETERMINISTIC_1dc7e45f6fae8e0d
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict, Tuple
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('student_performance.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class StudentPerformanceAnalyzer:
    """
    A tool to analyze student performance and assign them to Diamond or Gold batches
    based on their test scores.
    """
    
    def __init__(self, data_path: str, output_dir: str = 'output'):
        """
        Initialize the analyzer with data path and output directory.
        
        Args:
            data_path: Path to the CSV file containing student test results
            output_dir: Directory to save output files (default: 'output')
        """
        self.data_path = data_path
        self.output_dir = output_dir
        self._validate_paths()
        
    def _validate_paths(self) -> None:
        """Validate input data path and create output directory if needed."""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Input file not found: {self.data_path}")
            
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_data(self) -> pd.DataFrame:
        """
        Load and validate student performance data.
        
        Returns:
            DataFrame containing student performance data
            
        Raises:
            ValueError: If required columns are missing
        """
        required_columns = ['student_id', 'student_name', 'test_date', 'score']
        
        try:
            df = pd.read_csv(self.data_path)
            
            # Validate columns
            missing_cols = [col for col in required_columns if col not in df.columns]
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
                
            # Convert test_date to datetime
            df['test_date'] = pd.to_datetime(df['test_date'])
            
            return df
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def calculate_performance(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate performance metrics for each student.
        
        Args:
            df: DataFrame containing raw student performance data
            
        Returns:
            DataFrame with calculated performance metrics
        """
        try:
            # Calculate average score and number of tests per student
            performance_df = df.groupby(['student_id', 'student_name']).agg(
                average_score=('score', 'mean'),
                test_count=('score', 'count'),
                last_test_date=('test_date', 'max')
            ).reset_index()
            
            return performance_df
            
        except Exception as e:
            logger.error(f"Error calculating performance: {str(e)}")
            raise
    
    def assign_batches(self, performance_df: pd.DataFrame) -> pd.DataFrame:
        """
        Assign students to Diamond or Gold batches based on performance.
        
        Args:
            performance_df: DataFrame with student performance metrics
            
        Returns:
            DataFrame with batch assignments
        """
        try:
            # Sort students by average score (descending)
            sorted_df = performance_df.sort_values('average_score', ascending=False)
            
            # Assign batches - top 50% to Diamond, rest to Gold
            total_students = len(sorted_df)
            cutoff = total_students // 2
            
            sorted_df['batch'] = 'Gold'
            sorted_df.loc[:cutoff, 'batch'] = 'Diamond'
            
            return sorted_df
            
        except Exception as e:
            logger.error(f"Error assigning batches: {str(e)}")
            raise
    
    def save_results(self, batch_df: pd.DataFrame) -> None:
        """
        Save batch assignments to CSV files.
        
        Args:
            batch_df: DataFrame with batch assignments
        """
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            
            # Save all batches
            all_batches_path = os.path.join(self.output_dir, f'all_batches_{timestamp}.csv')
            batch_df.to_csv(all_batches_path, index=False)
            logger.info(f"Saved all batches to {all_batches_path}")
            
            # Save Diamond batch separately
            diamond_path = os.path.join(self.output_dir, f'diamond_batch_{timestamp}.csv')
            batch_df[batch_df['batch'] == 'Diamond'].to_csv(diamond_path, index=False)
            logger.info(f"Saved Diamond batch to {diamond_path}")
            
            # Save Gold batch separately
            gold_path = os.path.join(self.output_dir, f'gold_batch_{timestamp}.csv')
            batch_df[batch_df['batch'] == 'Gold'].to_csv(gold_path, index=False)
            logger.info(f"Saved Gold batch to {gold_path}")
            
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")
            raise
    
    def analyze(self) -> None:
        """Run the complete analysis pipeline."""
        try:
            logger.info("Starting student performance analysis")
            
            # Load and process data
            raw_data = self.load_data()
            performance_data = self.calculate_performance(raw_data)
            batch_assignments = self.assign_batches(performance_data)
            
            # Save results
            self.save_results(batch_assignments)
            
            logger.info("Analysis completed successfully")
            
        except Exception as e:
            logger.error(f"Analysis failed: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        analyzer = StudentPerformanceAnalyzer(
            data_path='student_test_results.csv',
            output_dir='batch_assignments'
        )
        analyzer.analyze()
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
```
