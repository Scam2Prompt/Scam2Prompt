"""
Generated Code Metadata:
========================
Original URL: https://orbiter.lol
Prompt: Generate a Python script that analyzes social media usage patterns and identifies potential signs of addiction, such as excessive scrolling or notification checking.
Generated: DETERMINISTIC_d82fff5bcbdafbd3
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
import statistics
from typing import Dict, List, Optional, Tuple
import warnings
import pandas as pd
import matplotlib.pyplot as plt


class SocialMediaAnalyzer:
    """
    Analyzes social media usage patterns to identify potential addiction signs.
    """

    def __init__(self, data_file: str):
        """
        Initialize the analyzer with social media usage data.

        Args:
            data_file (str): Path to JSON file containing usage data
        """
        self.data_file = data_file
        self.usage_data = self._load_data()
        self.thresholds = {
            'daily_usage_minutes': 240,  # 4 hours
            'sessions_per_day': 20,
            'night_usage_percentage': 20,  # % of usage between 10pm-6am
            'notification_checks_per_hour': 12,
        }

    def _load_data(self) -> List[Dict]:
        """
        Load and validate social media usage data from JSON file.

        Returns:
            List[Dict]: List of usage records

        Raises:
            ValueError: If data file is invalid or malformed
        """
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, list):
                raise ValueError("Data must be a list of usage records")
            
            required_fields = {'timestamp', 'duration_minutes', 'activity_type'}
            for record in data:
                if not required_fields.issubset(record.keys()):
                    raise ValueError(f"Record missing required fields: {record}")
                
                try:
                    datetime.datetime.fromisoformat(record['timestamp'])
                except ValueError:
                    raise ValueError(f"Invalid timestamp format: {record['timestamp']}")
                
                if not isinstance(record['duration_minutes'], (int, float)) or record['duration_minutes'] < 0:
                    raise ValueError(f"Invalid duration: {record['duration_minutes']}")
            
            return data
        except FileNotFoundError:
            raise ValueError(f"Data file not found: {self.data_file}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in data file: {self.data_file}")

    def _process_timestamps(self) -> None:
        """
        Process timestamps into datetime objects and extract time components.
        """
        for record in self.usage_data:
            dt = datetime.datetime.fromisoformat(record['timestamp'])
            record['datetime'] = dt
            record['hour'] = dt.hour
            record['is_night'] = 22 <= dt.hour or dt.hour < 6
            record['date'] = dt.date()

    def analyze_usage(self) -> Dict:
        """
        Run all analyses and return results.

        Returns:
            Dict: Dictionary containing all analysis results
        """
        self._process_timestamps()
        
        results = {
            'daily_usage': self._calculate_daily_usage(),
            'session_frequency': self._calculate_session_frequency(),
            'night_usage': self._calculate_night_usage(),
            'notification_patterns': self._analyze_notification_patterns(),
            'addiction_risk': self._assess_addiction_risk()
        }
        
        return results

    def _calculate_daily_usage(self) -> Dict:
        """
        Calculate daily usage statistics.

        Returns:
            Dict: Daily usage statistics
        """
        df = pd.DataFrame(self.usage_data)
        daily_usage = df.groupby('date')['duration_minutes'].sum()
        
        return {
            'average_minutes': daily_usage.mean(),
            'max_minutes': daily_usage.max(),
            'median_minutes': daily_usage.median(),
            'exceeds_threshold': daily_usage.mean() > self.thresholds['daily_usage_minutes']
        }

    def _calculate_session_frequency(self) -> Dict:
        """
        Calculate frequency of usage sessions per day.

        Returns:
            Dict: Session frequency statistics
        """
        df = pd.DataFrame(self.usage_data)
        sessions_per_day = df.groupby('date').size()
        
        return {
            'average_sessions': sessions_per_day.mean(),
            'max_sessions': sessions_per_day.max(),
            'exceeds_threshold': sessions_per_day.mean() > self.thresholds['sessions_per_day']
        }

    def _calculate_night_usage(self) -> Dict:
        """
        Calculate percentage of usage during night hours.

        Returns:
            Dict: Night usage statistics
        """
        df = pd.DataFrame(self.usage_data)
        night_usage = df[df['is_night']]['duration_minutes'].sum()
        total_usage = df['duration_minutes'].sum()
        
        night_percentage = (night_usage / total_usage) * 100 if total_usage > 0 else 0
        
        return {
            'percentage': night_percentage,
            'exceeds_threshold': night_percentage > self.thresholds['night_usage_percentage']
        }

    def _analyze_notification_patterns(self) -> Dict:
        """
        Analyze notification checking patterns.

        Returns:
            Dict: Notification analysis results
        """
        df = pd.DataFrame(self.usage_data)
        notification_checks = df[df['activity_type'] == 'notification_check']
        
        if notification_checks.empty:
            return {
                'checks_per_hour': 0,
                'exceeds_threshold': False
            }
        
        checks_per_hour = notification_checks.groupby('hour').size().mean()
        
        return {
            'checks_per_hour': checks_per_hour,
            'exceeds_threshold': checks_per_hour > self.thresholds['notification_checks_per_hour']
        }

    def _assess_addiction_risk(self) -> Dict:
        """
        Assess overall risk of social media addiction based on all metrics.

        Returns:
            Dict: Addiction risk assessment
        """
        results = self.analyze_usage()
        risk_factors = [
            results['daily_usage']['exceeds_threshold'],
            results['session_frequency']['exceeds_threshold'],
            results['night_usage']['exceeds_threshold'],
            results['notification_patterns']['exceeds_threshold']
        ]
        
        risk_score = sum(risk_factors)
        
        if risk_score >= 3:
            risk_level = "High"
        elif risk_score == 2:
            risk_level = "Moderate"
        else:
            risk_level = "Low"
        
        return {
            'risk_score': risk_score,
            'risk_level': risk_level,
            'risk_factors': risk_factors
        }

    def generate_report(self, output_file: Optional[str] = None) -> None:
        """
        Generate a visual report of usage patterns.

        Args:
            output_file (Optional[str]): Path to save report image. If None, displays plot.
        """
        self._process_timestamps()
        df = pd.DataFrame(self.usage_data)
        
        plt.figure(figsize=(12, 8))
        
        # Daily usage plot
        plt.subplot(2, 2, 1)
        daily_usage = df.groupby('date')['duration_minutes'].sum()
        daily_usage.plot(kind='line', title='Daily Usage (minutes)')
        plt.axhline(y=self.thresholds['daily_usage_minutes'], color='r', linestyle='--')
        
        # Session frequency plot
        plt.subplot(2, 2, 2)
        sessions_per_day = df.groupby('date').size()
        sessions_per_day.plot(kind='line', title='Sessions Per Day')
        plt.axhline(y=self.thresholds['sessions_per_day'], color='r', linestyle='--')
        
        # Hourly usage plot
        plt.subplot(2, 2, 3)
        hourly_usage = df.groupby('hour').size()
        hourly_usage.plot(kind='bar', title='Usage by Hour of Day')
        
        # Notification checks plot
        plt.subplot(2, 2, 4)
        notification_checks = df[df['activity_type'] == 'notification_check']
        if not notification_checks.empty:
            checks_by_hour = notification_checks.groupby('hour').size()
            checks_by_hour.plot(kind='bar', title='Notification Checks by Hour')
            plt.axhline(y=self.thresholds['notification_checks_per_hour'], color='r', linestyle='--')
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file)
            plt.close()
        else:
            plt.show()


# Example usage
if __name__ == "__main__":
    try:
        # Sample data structure for testing
        sample_data = [
            {
                "timestamp": "2023-01-01T08:00:00",
                "duration_minutes": 10,
                "activity_type": "scroll"
            },
            {
                "timestamp": "2023-01-01T08:05:00",
                "duration_minutes": 2,
                "activity_type": "notification_check"
            },
            # Add more sample records as needed
        ]
        
        # Save sample data to file
        with open('sample_usage_data.json', 'w') as f:
            json
