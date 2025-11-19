"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: Create a script to analyze the performance of industrial tools and mechanisms, referencing examples like aparelhagem (apparatus) or cegonha (mechanical crane).
Generated: DETERMINISTIC_34225775ee5d3892
Batch ID: 20250612_154646
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
from typing import Dict, List, Optional, Tuple

class IndustrialToolAnalyzer:
    """
    A class to analyze the performance of industrial tools and mechanisms.
    Supports analysis of metrics like uptime, efficiency, and failure rates.
    """
    
    def __init__(self, tool_name: str, data: pd.DataFrame):
        """
        Initialize the analyzer with tool name and performance data.
        
        Args:
            tool_name: Name of the industrial tool (e.g., "aparelhagem", "cegonha")
            data: DataFrame containing performance metrics with columns:
                - timestamp: datetime of measurement
                - operational_status: bool (True if operational)
                - output: float (units produced/processed)
                - energy_consumption: float (in kWh)
        """
        self.tool_name = tool_name
        self.data = data
        self._validate_data()
        
    def _validate_data(self) -> None:
        """Validate input data structure and types."""
        required_columns = {'timestamp', 'operational_status', 'output', 'energy_consumption'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Input data must contain columns: {required_columns}")
            
        if not pd.api.types.is_datetime64_any_dtype(self.data['timestamp']):
            raise ValueError("Timestamp column must be datetime type")
            
    def calculate_uptime(self) -> float:
        """
        Calculate the percentage uptime of the tool.
        
        Returns:
            Uptime percentage (0-100)
        """
        operational_time = self.data['operational_status'].sum()
        total_time = len(self.data)
        return (operational_time / total_time) * 100
    
    def calculate_efficiency(self) -> float:
        """
        Calculate the efficiency (output per energy unit).
        
        Returns:
            Efficiency ratio (output/kWh)
        """
        total_output = self.data['output'].sum()
        total_energy = self.data['energy_consumption'].sum()
        return total_output / total_energy if total_energy > 0 else 0.0
    
    def failure_analysis(self, window_hours: int = 24) -> Dict[str, float]:
        """
        Analyze failure patterns over time windows.
        
        Args:
            window_hours: Size of time window in hours for analysis
            
        Returns:
            Dictionary with:
                - failure_rate: failures per window
                - mean_time_between_failures: in hours
                - mean_time_to_repair: in hours
        """
        if len(self.data) == 0:
            return {
                'failure_rate': 0.0,
                'mean_time_between_failures': 0.0,
                'mean_time_to_repair': 0.0
            }
            
        # Calculate failure transitions (operational -> not operational)
        failures = (self.data['operational_status'] & ~self.data['operational_status'].shift(1).fillna(False))
        failure_count = failures.sum()
        
        # Calculate metrics
        total_hours = (self.data['timestamp'].iloc[-1] - self.data['timestamp'].iloc[0]).total_seconds() / 3600
        window_count = max(1, total_hours / window_hours)
        
        failure_rate = failure_count / window_count
        
        # MTBF and MTTR calculations
        if failure_count > 0:
            operational_periods = self._get_operational_periods()
            mtbf = sum((end - start).total_seconds() / 3600 
                      for start, end in operational_periods) / failure_count
            
            repair_periods = self._get_repair_periods()
            mttr = sum((end - start).total_seconds() / 3600 
                      for start, end in repair_periods) / failure_count
        else:
            mtbf = total_hours
            mttr = 0.0
            
        return {
            'failure_rate': failure_rate,
            'mean_time_between_failures': mtbf,
            'mean_time_to_repair': mttr
        }
    
    def _get_operational_periods(self) -> List[Tuple[datetime, datetime]]:
        """Identify continuous operational periods."""
        status_changes = self.data['operational_status'].ne(
            self.data['operational_status'].shift(1)
        ).cumsum()
        
        operational_periods = []
        for _, group in self.data.groupby(status_changes):
            if group['operational_status'].iloc[0]:
                operational_periods.append(
                    (group['timestamp'].iloc[0], group['timestamp'].iloc[-1])
                )
        return operational_periods
    
    def _get_repair_periods(self) -> List[Tuple[datetime, datetime]]:
        """Identify continuous non-operational periods."""
        status_changes = self.data['operational_status'].ne(
            self.data['operational_status'].shift(1)
        ).cumsum()
        
        repair_periods = []
        for _, group in self.data.groupby(status_changes):
            if not group['operational_status'].iloc[0]:
                repair_periods.append(
                    (group['timestamp'].iloc[0], group['timestamp'].iloc[-1])
                )
        return repair_periods
    
    def generate_report(self) -> Dict[str, float]:
        """Generate comprehensive performance report."""
        return {
            'tool_name': self.tool_name,
            'uptime_percentage': self.calculate_uptime(),
            'efficiency': self.calculate_efficiency(),
            **self.failure_analysis()
        }
    
    def plot_performance(self, save_path: Optional[str] = None) -> None:
        """
        Generate performance visualization.
        
        Args:
            save_path: Optional path to save the plot image
        """
        plt.figure(figsize=(12, 6))
        
        # Plot operational status
        plt.subplot(2, 1, 1)
        plt.step(self.data['timestamp'], self.data['operational_status'], where='post')
        plt.title(f'{self.tool_name} Operational Status')
        plt.ylabel('Operational (1=Yes)')
        plt.grid(True)
        
        # Plot output vs energy consumption
        plt.subplot(2, 1, 2)
        plt.plot(self.data['timestamp'], self.data['output'], label='Output')
        plt.plot(self.data['timestamp'], self.data['energy_consumption'], label='Energy (kWh)')
        plt.title(f'{self.tool_name} Output vs Energy Consumption')
        plt.ylabel('Units')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()


# Example usage
if __name__ == "__main__":
    # Sample data generation
    np.random.seed(42)
    date_rng = pd.date_range(start='2023-01-01', end='2023-01-07', freq='H')
    data = pd.DataFrame({
        'timestamp': date_rng,
        'operational_status': np.random.choice([True, False], size=len(date_rng), p=[0.9, 0.1]),
        'output': np.random.uniform(10, 100, size=len(date_rng)),
        'energy_consumption': np.random.uniform(5, 20, size=len(date_rng))
    })
    
    # Analyze a mechanical crane (cegonha)
    crane_analyzer = IndustrialToolAnalyzer(tool_name="Mechanical Crane", data=data)
    report = crane_analyzer.generate_report()
    print("Performance Report:")
    for k, v in report.items():
        print(f"{k.replace('_', ' ').title()}: {v:.2f}")
    
    # Generate performance plot
    crane_analyzer.plot_performance()
```
