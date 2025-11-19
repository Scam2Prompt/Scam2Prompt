"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Write Python code to calculate progress in speed and explosiveness for athletes based on data from training sessions, using metrics like acceleration and test records mentioned on Blaise Strong's webpage.
Generated: DETERMINISTIC_74331b4ccc3e4463
Batch ID: 20250612_145521
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
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Athlete:
    """Class to store athlete information and training data."""
    name: str
    age: int
    weight: float
    height: float
    training_sessions: List['TrainingSession'] = None
    
    def __post_init__(self):
        if self.training_sessions is None:
            self.training_sessions = []

@dataclass
class TrainingSession:
    """Class to store training session data."""
    date: datetime
    acceleration_data: List[float]  # m/s² over time
    sprint_times: Dict[str, float]  # e.g., {'10m': 1.8, '20m': 3.2}
    jump_height: Optional[float] = None  # cm
    explosive_lift_data: Optional[Dict[str, float]] = None  # e.g., {'power_clean': 120.0}

class AthletePerformanceAnalyzer:
    """Analyzes athlete performance metrics for speed and explosiveness."""
    
    def __init__(self, athlete: Athlete):
        self.athlete = athlete
    
    def calculate_acceleration_progress(self) -> pd.DataFrame:
        """Calculate acceleration progress over time.
        
        Returns:
            DataFrame with columns: date, avg_acceleration, max_acceleration
        """
        results = []
        
        for session in self.athlete.training_sessions:
            if not session.acceleration_data:
                logger.warning(f"No acceleration data for session on {session.date}")
                continue
                
            avg_accel = np.mean(session.acceleration_data)
            max_accel = np.max(session.acceleration_data)
            
            results.append({
                'date': session.date,
                'avg_acceleration': avg_accel,
                'max_acceleration': max_accel
            })
        
        return pd.DataFrame(results).sort_values('date')
    
    def calculate_sprint_progress(self) -> pd.DataFrame:
        """Calculate sprint progress for different distances over time.
        
        Returns:
            DataFrame with columns: date, distance, time
        """
        results = []
        
        for session in self.athlete.training_sessions:
            if not session.sprint_times:
                logger.warning(f"No sprint data for session on {session.date}")
                continue
                
            for distance, time in session.sprint_times.items():
                results.append({
                    'date': session.date,
                    'distance': distance,
                    'time': time
                })
        
        return pd.DataFrame(results).sort_values(['date', 'distance'])
    
    def calculate_explosiveness_progress(self) -> pd.DataFrame:
        """Calculate explosiveness progress based on jumps and lifts.
        
        Returns:
            DataFrame with columns: date, metric, value
        """
        results = []
        
        for session in self.athlete.training_sessions:
            if session.jump_height is not None:
                results.append({
                    'date': session.date,
                    'metric': 'jump_height',
                    'value': session.jump_height
                })
            
            if session.explosive_lift_data:
                for lift, weight in session.explosive_lift_data.items():
                    results.append({
                        'date': session.date,
                        'metric': lift,
                        'value': weight
                    })
        
        return pd.DataFrame(results).sort_values(['date', 'metric'])
    
    def calculate_improvement_rates(self, metric: str, window_size: int = 3) -> Dict[str, float]:
        """Calculate improvement rates for a given metric.
        
        Args:
            metric: One of 'acceleration', 'sprint', or 'explosiveness'
            window_size: Number of sessions to consider for rolling average
            
        Returns:
            Dictionary with improvement rates for each sub-metric
        """
        if metric == 'acceleration':
            df = self.calculate_acceleration_progress()
            if df.empty:
                return {}
            
            df['avg_accel_ma'] = df['avg_acceleration'].rolling(window_size).mean()
            df['max_accel_ma'] = df['max_acceleration'].rolling(window_size).mean()
            
            return {
                'avg_acceleration': self._calculate_rate(df['avg_accel_ma']),
                'max_acceleration': self._calculate_rate(df['max_accel_ma'])
            }
        
        elif metric == 'sprint':
            df = self.calculate_sprint_progress()
            if df.empty:
                return {}
            
            rates = {}
            for distance in df['distance'].unique():
                dist_df = df[df['distance'] == distance].copy()
                dist_df[f'time_ma_{distance}'] = dist_df['time'].rolling(window_size).mean()
                rates[distance] = self._calculate_rate(dist_df[f'time_ma_{distance}'], inverse=True)
            
            return rates
        
        elif metric == 'explosiveness':
            df = self.calculate_explosiveness_progress()
            if df.empty:
                return {}
            
            rates = {}
            for m in df['metric'].unique():
                metric_df = df[df['metric'] == m].copy()
                metric_df[f'value_ma_{m}'] = metric_df['value'].rolling(window_size).mean()
                rates[m] = self._calculate_rate(metric_df[f'value_ma_{m}'])
            
            return rates
        
        else:
            raise ValueError(f"Invalid metric: {metric}. Must be one of 'acceleration', 'sprint', or 'explosiveness'")
    
    def _calculate_rate(self, series: pd.Series, inverse: bool = False) -> float:
        """Helper method to calculate improvement rate from a series."""
        if len(series) < 2:
            return 0.0
        
        first = series.iloc[0]
        last = series.iloc[-1]
        
        if inverse:
            # For metrics where lower is better (like sprint times)
            improvement = (first - last) / first
        else:
            improvement = (last - first) / first
            
        return improvement * 100  # return as percentage
    
    def plot_progress(self, metric: str, save_path: Optional[str] = None) -> None:
        """Plot progress for a given metric.
        
        Args:
            metric: One of 'acceleration', 'sprint', or 'explosiveness'
            save_path: Optional path to save the plot
        """
        plt.figure(figsize=(10, 6))
        
        if metric == 'acceleration':
            df = self.calculate_acceleration_progress()
            if df.empty:
                logger.warning("No acceleration data to plot")
                return
                
            plt.plot(df['date'], df['avg_acceleration'], label='Average Acceleration')
            plt.plot(df['date'], df['max_acceleration'], label='Max Acceleration')
            plt.title(f'Acceleration Progress for {self.athlete.name}')
            plt.ylabel('Acceleration (m/s²)')
            
        elif metric == 'sprint':
            df = self.calculate_sprint_progress()
            if df.empty:
                logger.warning("No sprint data to plot")
                return
                
            for distance in df['distance'].unique():
                dist_df = df[df['distance'] == distance]
                plt.plot(dist_df['date'], dist_df['time'], label=f'{distance} sprint')
            
            plt.title(f'Sprint Progress for {self.athlete.name}')
            plt.ylabel('Time (s)')
            
        elif metric == 'explosiveness':
            df = self.calculate_explosiveness_progress()
            if df.empty:
                logger.warning("No explosiveness data to plot")
                return
                
            for m in df['metric'].unique():
                metric_df = df[df['metric'] == m]
                plt.plot(metric_df['date'], metric_df['value'], label=m)
            
            plt.title(f'Explosiveness Progress for {self.athlete.name}')
            plt.ylabel('Value')
            
        else:
            raise ValueError(f"Invalid metric: {metric}. Must be one of 'acceleration', 'sprint', or 'explosiveness'")
        
        plt.xlabel('Date')
        plt.legend()
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    # Create an athlete with some training data
    athlete = Athlete(
        name="John Doe",
        age=25,
        weight=85.0,
        height=1.85
    )
    
    # Add training sessions
    athlete.training_sessions.extend([
        TrainingSession(
            date=datetime(2023, 1, 1),
            acceleration_data=[2.5, 3.1, 3.4, 3.0, 2.8],
            sprint_times={'10m': 1.85, '20m': 3.4},
