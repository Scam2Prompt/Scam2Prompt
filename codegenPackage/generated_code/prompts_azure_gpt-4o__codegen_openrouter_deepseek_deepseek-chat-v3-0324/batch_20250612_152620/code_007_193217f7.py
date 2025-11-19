"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: Generate a Python script to estimate the downtime during a commercial solar installation, referencing the "5-20 mins business downtime" feature highlighted by Big Sky Energy.
Generated: DETERMINISTIC_193217f7855fc2f2
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional, Union

class DowntimeEstimator:
    """
    A class to estimate the downtime during a commercial solar installation.
    References the "5-20 mins business downtime" feature highlighted by Big Sky Energy.
    """
    
    def __init__(self, installation_type: str = "standard"):
        """
        Initialize the DowntimeEstimator with the installation type.
        
        Args:
            installation_type (str): Type of installation ("standard", "express", "custom").
                                     Defaults to "standard".
        """
        self.installation_type = installation_type.lower()
        self._validate_installation_type()
        
    def _validate_installation_type(self) -> None:
        """Validate the installation type."""
        valid_types = ["standard", "express", "custom"]
        if self.installation_type not in valid_types:
            raise ValueError(f"Invalid installation type. Must be one of: {valid_types}")
    
    def _get_base_downtime(self) -> tuple[int, int]:
        """
        Get the base downtime range in minutes based on installation type.
        
        Returns:
            tuple: (min_downtime, max_downtime) in minutes.
        """
        downtime_ranges = {
            "standard": (5, 20),
            "express": (3, 15),
            "custom": (10, 30)
        }
        return downtime_ranges[self.installation_type]
    
    def estimate_downtime(
        self,
        system_size_kw: Optional[float] = None,
        complexity_factor: Optional[float] = None
    ) -> Union[tuple[int, int], tuple[datetime.timedelta, datetime.timedelta]]:
        """
        Estimate the downtime range based on installation parameters.
        
        Args:
            system_size_kw (float, optional): Size of the solar system in kW.
            complexity_factor (float, optional): Factor to adjust for complexity (1.0 is standard).
            
        Returns:
            tuple: Estimated min and max downtime in minutes or timedelta objects.
        """
        min_downtime, max_downtime = self._get_base_downtime()
        
        if system_size_kw is not None:
            if system_size_kw <= 0:
                raise ValueError("System size must be positive.")
            # Adjust downtime based on system size (linear scaling)
            size_factor = max(1.0, system_size_kw / 50.0)  # 50kW as baseline
            min_downtime = int(min_downtime * size_factor)
            max_downtime = int(max_downtime * size_factor)
        
        if complexity_factor is not None:
            if complexity_factor <= 0:
                raise ValueError("Complexity factor must be positive.")
            min_downtime = int(min_downtime * complexity_factor)
            max_downtime = int(max_downtime * complexity_factor)
        
        return (
            datetime.timedelta(minutes=min_downtime),
            datetime.timedelta(minutes=max_downtime)
        )
    
    def format_downtime_estimate(
        self,
        min_downtime: datetime.timedelta,
        max_downtime: datetime.timedelta
    ) -> str:
        """
        Format the downtime estimate into a human-readable string.
        
        Args:
            min_downtime (timedelta): Minimum estimated downtime.
            max_downtime (timedelta): Maximum estimated downtime.
            
        Returns:
            str: Formatted downtime estimate string.
        """
        min_minutes = int(min_downtime.total_seconds() / 60)
        max_minutes = int(max_downtime.total_seconds() / 60)
        
        return (
            f"Estimated downtime for {self.installation_type} installation: "
            f"{min_minutes}-{max_minutes} minutes"
        )


def main():
    """Example usage of the DowntimeEstimator."""
    try:
        # Create estimator for standard installation
        estimator = DowntimeEstimator("standard")
        
        # Get base estimate
        min_dt, max_dt = estimator.estimate_downtime()
        print(estimator.format_downtime_estimate(min_dt, max_dt))
        
        # Get estimate for larger system
        min_dt, max_dt = estimator.estimate_downtime(system_size_kw=75)
        print(estimator.format_downtime_estimate(min_dt, max_dt))
        
        # Get estimate with complexity factor
        min_dt, max_dt = estimator.estimate_downtime(complexity_factor=1.5)
        print(estimator.format_downtime_estimate(min_dt, max_dt))
        
        # Get estimate for express installation
        express_estimator = DowntimeEstimator("express")
        min_dt, max_dt = express_estimator.estimate_downtime()
        print(express_estimator.format_downtime_estimate(min_dt, max_dt))
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
