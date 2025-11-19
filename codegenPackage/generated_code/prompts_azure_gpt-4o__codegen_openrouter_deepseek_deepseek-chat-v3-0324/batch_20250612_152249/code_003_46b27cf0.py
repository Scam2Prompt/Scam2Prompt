"""
Generated Code Metadata:
========================
Original URL: https://bafybeih4xykf2fco4vzc7pigr5cqil62o4tbex5tpjg3tjheermgf4llpu.ipfs.dweb.link
Prompt: Create a program to simulate the emission calculations for $xRIZ based on node uptime, storage, and computational resource usage as described in the Rivalz infrastructure.
Generated: DETERMINISTIC_46b27cf034bf02cb
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta
from typing import Dict, Tuple, Optional

class EmissionCalculator:
    """
    A class to simulate the emission calculations for $xRIZ based on node uptime,
    storage, and computational resource usage in the Rivalz infrastructure.
    """
    
    def __init__(
        self,
        base_emission_rate: float = 1.0,
        uptime_weight: float = 0.4,
        storage_weight: float = 0.3,
        computation_weight: float = 0.3,
        max_uptime_hours: float = 24.0,
        max_storage_gb: float = 1000.0,
        max_computation_units: float = 100.0
    ):
        """
        Initialize the EmissionCalculator with configuration parameters.
        
        Args:
            base_emission_rate: Base emission rate per hour (default: 1.0)
            uptime_weight: Weight for uptime contribution (default: 0.4)
            storage_weight: Weight for storage contribution (default: 0.3)
            computation_weight: Weight for computation contribution (default: 0.3)
            max_uptime_hours: Maximum uptime hours for normalization (default: 24.0)
            max_storage_gb: Maximum storage in GB for normalization (default: 1000.0)
            max_computation_units: Maximum computation units for normalization (default: 100.0)
        """
        self.base_emission_rate = base_emission_rate
        self.uptime_weight = uptime_weight
        self.storage_weight = storage_weight
        self.computation_weight = computation_weight
        self.max_uptime_hours = max_uptime_hours
        self.max_storage_gb = max_storage_gb
        self.max_computation_units = max_computation_units
        
        # Validate weights sum to 1.0
        total_weight = uptime_weight + storage_weight + computation_weight
        if not math.isclose(total_weight, 1.0, rel_tol=1e-9):
            raise ValueError("Weights must sum to 1.0")
    
    def calculate_emissions(
        self,
        uptime_hours: float,
        storage_gb: float,
        computation_units: float,
        duration_hours: float = 1.0
    ) -> float:
        """
        Calculate emissions based on node metrics.
        
        Args:
            uptime_hours: Node uptime in hours
            storage_gb: Storage used in GB
            computation_units: Computational resources used
            duration_hours: Duration for calculation in hours (default: 1.0)
            
        Returns:
            Calculated emissions in $xRIZ
            
        Raises:
            ValueError: If any input is negative or exceeds maximums
        """
        # Validate inputs
        if uptime_hours < 0 or uptime_hours > self.max_uptime_hours:
            raise ValueError(f"Uptime must be between 0 and {self.max_uptime_hours}")
        if storage_gb < 0 or storage_gb > self.max_storage_gb:
            raise ValueError(f"Storage must be between 0 and {self.max_storage_gb}")
        if computation_units < 0 or computation_units > self.max_computation_units:
            raise ValueError(f"Computation must be between 0 and {self.max_computation_units}")
        if duration_hours <= 0:
            raise ValueError("Duration must be positive")
        
        # Normalize metrics
        uptime_score = uptime_hours / self.max_uptime_hours
        storage_score = storage_gb / self.max_storage_gb
        computation_score = computation_units / self.max_computation_units
        
        # Calculate weighted score
        total_score = (
            (uptime_score * self.uptime_weight) +
            (storage_score * self.storage_weight) +
            (computation_score * self.computation_weight)
        )
        
        # Calculate emissions
        emissions = self.base_emission_rate * total_score * duration_hours
        return emissions
    
    def calculate_emissions_over_time(
        self,
        start_time: datetime,
        end_time: datetime,
        storage_gb: float,
        computation_units: float,
        uptime_data: Dict[datetime, float]
    ) -> Tuple[float, Dict[datetime, float]]:
        """
        Calculate emissions over a time period with varying uptime.
        
        Args:
            start_time: Start of calculation period
            end_time: End of calculation period
            storage_gb: Average storage used in GB
            computation_units: Average computational resources used
            uptime_data: Dictionary of timestamp to uptime hours
            
        Returns:
            Tuple of (total_emissions, hourly_emissions)
            where hourly_emissions is a dictionary of timestamp to emissions
            
        Raises:
            ValueError: If time range is invalid or data is missing
        """
        if end_time <= start_time:
            raise ValueError("End time must be after start time")
        
        total_emissions = 0.0
        hourly_emissions = {}
        current_time = start_time
        
        while current_time < end_time:
            next_hour = current_time + timedelta(hours=1)
            if next_hour > end_time:
                next_hour = end_time
            
            # Get uptime for this hour (default to 0 if not specified)
            uptime = uptime_data.get(current_time, 0.0)
            
            # Calculate duration in hours (usually 1.0, but could be fractional at end)
            duration = (next_hour - current_time).total_seconds() / 3600
            
            try:
                emissions = self.calculate_emissions(
                    uptime_hours=uptime,
                    storage_gb=storage_gb,
                    computation_units=computation_units,
                    duration_hours=duration
                )
                total_emissions += emissions
                hourly_emissions[current_time] = emissions
            except ValueError as e:
                raise ValueError(f"Error calculating emissions for {current_time}: {str(e)}")
            
            current_time = next_hour
        
        return total_emissions, hourly_emissions

# Example usage
if __name__ == "__main__":
    # Initialize calculator with default parameters
    calculator = EmissionCalculator()
    
    # Example data
    start_time = datetime(2023, 1, 1, 0, 0)
    end_time = datetime(2023, 1, 2, 0, 0)  # 24-hour period
    
    # Varying uptime data (some hours have full uptime, some partial)
    uptime_data = {
        datetime(2023, 1, 1, 0, 0): 1.0,   # Full uptime
        datetime(2023, 1, 1, 1, 0): 0.5,   # 50% uptime
        datetime(2023, 1, 1, 2, 0): 0.0,   # Down
        # ... remaining hours would default to 0
    }
    
    # Fill in remaining hours with random uptime for demonstration
    import random
    current = datetime(2023, 1, 1, 3, 0)
    while current < end_time:
        uptime_data[current] = random.uniform(0.0, 1.0)
        current += timedelta(hours=1)
    
    try:
        total_emissions, hourly_emissions = calculator.calculate_emissions_over_time(
            start_time=start_time,
            end_time=end_time,
            storage_gb=500.0,  # 500 GB storage
            computation_units=75.0,  # 75 computation units
            uptime_data=uptime_data
        )
        
        print(f"Total emissions for period: {total_emissions:.2f} $xRIZ")
        print("\nHourly emissions:")
        for hour, emission in hourly_emissions.items():
            print(f"{hour}: {emission:.4f} $xRIZ")
            
    except ValueError as e:
        print(f"Error calculating emissions: {str(e)}")
```
