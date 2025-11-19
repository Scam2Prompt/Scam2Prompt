"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: How can I use data-driven decision-making in a patrol guard tour system as described on Buford Security Blog?
Generated: DETERMINISTIC_7507fd20a0e86b36
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PatrolTourSystem:
    """
    A data-driven patrol guard tour system that analyzes tour data
    to optimize security operations.
    """
    
    def __init__(self, data_source: str):
        """
        Initialize the patrol tour system with a data source.
        
        Args:
            data_source: Path to JSON file containing tour data
        """
        self.data_source = data_source
        self.tour_data = self._load_data()
        
    def _load_data(self) -> List[Dict]:
        """
        Load and validate tour data from JSON file.
        
        Returns:
            List of tour records as dictionaries
            
        Raises:
            FileNotFoundError: If data file doesn't exist
            json.JSONDecodeError: If data is not valid JSON
        """
        try:
            with open(self.data_source, 'r') as f:
                data = json.load(f)
                
            if not isinstance(data, list):
                raise ValueError("Data should be a list of tour records")
                
            return data
            
        except FileNotFoundError:
            logger.error(f"Data file not found: {self.data_source}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in data file: {self.data_source}")
            raise
    
    def analyze_tour_completion(self) -> pd.DataFrame:
        """
        Analyze tour completion rates and times.
        
        Returns:
            DataFrame with analysis results
        """
        df = pd.DataFrame(self.tour_data)
        
        # Convert timestamps to datetime objects
        df['start_time'] = pd.to_datetime(df['start_time'])
        df['end_time'] = pd.to_datetime(df['end_time'])
        
        # Calculate tour duration in minutes
        df['duration_min'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60
        
        # Calculate completion rate
        completion_stats = df.groupby('guard_id').agg({
            'completed': 'mean',
            'duration_min': ['mean', 'std']
        })
        
        completion_stats.columns = ['completion_rate', 'avg_duration', 'duration_std']
        
        return completion_stats.round(2)
    
    def identify_anomalies(self, threshold: float = 2.0) -> pd.DataFrame:
        """
        Identify anomalous tours based on duration.
        
        Args:
            threshold: Standard deviations from mean to consider anomalous
            
        Returns:
            DataFrame containing anomalous tours
        """
        df = pd.DataFrame(self.tour_data)
        df['duration'] = (pd.to_datetime(df['end_time']) - 
                          pd.to_datetime(df['start_time'])).dt.total_seconds() / 60
        
        # Calculate z-scores for durations
        mean_duration = df['duration'].mean()
        std_duration = df['duration'].std()
        df['z_score'] = (df['duration'] - mean_duration) / std_duration
        
        # Filter anomalies
        anomalies = df[abs(df['z_score']) > threshold]
        return anomalies.sort_values('z_score', ascending=False)
    
    def optimize_route_schedule(self) -> Dict:
        """
        Optimize patrol routes based on historical data.
        
        Returns:
            Dictionary with recommended schedule changes
        """
        df = pd.DataFrame(self.tour_data)
        
        # Analyze most frequent checkpoints
        checkpoint_counts = df['checkpoints'].explode().value_counts()
        top_checkpoints = checkpoint_counts.head(5).index.tolist()
        
        # Analyze time between checkpoints
        df['start_time'] = pd.to_datetime(df['start_time'])
        time_analysis = df.groupby('guard_id')['start_time'].diff().dt.total_seconds().mean() / 60
        
        return {
            'recommended_checkpoints': top_checkpoints,
            'avg_time_between_tours_min': round(time_analysis, 2),
            'suggestion': "Focus patrols on high-frequency checkpoints and adjust timing based on averages"
        }
    
    def generate_report(self, output_file: Optional[str] = None) -> str:
        """
        Generate a comprehensive report of tour analysis.
        
        Args:
            output_file: Optional path to save report as JSON
            
        Returns:
            JSON string containing report data
        """
        report = {
            'timestamp': datetime.now().isoformat(),
            'completion_analysis': self.analyze_tour_completion().to_dict(),
            'anomalies': self.identify_anomalies().to_dict(orient='records'),
            'optimization_recommendations': self.optimize_route_schedule()
        }
        
        report_json = json.dumps(report, indent=2)
        
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(report_json)
                logger.info(f"Report saved to {output_file}")
            except IOError as e:
                logger.error(f"Failed to save report: {e}")
                raise
        
        return report_json

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample data
        tour_system = PatrolTourSystem('tour_data.json')
        
        # Generate and print report
        report = tour_system.generate_report('patrol_report.json')
        print(report)
        
    except Exception as e:
        logger.error(f"Error in patrol tour system: {e}")
```
