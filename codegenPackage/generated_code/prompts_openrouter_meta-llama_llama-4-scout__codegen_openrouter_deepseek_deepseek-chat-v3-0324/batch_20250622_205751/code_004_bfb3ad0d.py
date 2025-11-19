"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: "Write a code snippet to calculate the production capacity of a textile mill with world-class machinery, similar to Ramji Acro's setup."
Generated: DETERMINISTIC_bfb3ad0d7a3e63f4
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TextileMillCapacityCalculator:
    """
    A class to calculate the production capacity of a textile mill with world-class machinery.
    Assumptions:
    - Machines operate 24/7 with 95% uptime
    - Standard fabric width of 60 inches
    - Production speed varies by machine type
    """
    
    def __init__(self, machine_count: int, machine_type: str):
        """
        Initialize the calculator with machine count and type.
        
        Args:
            machine_count: Number of machines in the mill
            machine_type: Type of machine ('weaving', 'knitting', 'spinning')
        """
        self.machine_count = machine_count
        self.machine_type = machine_type.lower()
        self.validate_inputs()
        
        # Machine speeds in meters per minute (industry standards)
        self.machine_speeds = {
            'weaving': 30,   # Modern rapier looms
            'knitting': 20,  # Circular knitting machines
            'spinning': 15   # Ring spinning frames
        }
        
        # Efficiency factors (95% uptime)
        self.uptime_factor = 0.95
        
    def validate_inputs(self):
        """Validate that inputs are within reasonable ranges."""
        if self.machine_count <= 0:
            raise ValueError("Machine count must be positive")
        if self.machine_type not in ['weaving', 'knitting', 'spinning']:
            raise ValueError("Invalid machine type. Must be 'weaving', 'knitting', or 'spinning'")
    
    def calculate_daily_capacity(self) -> float:
        """
        Calculate daily production capacity in meters.
        
        Returns:
            Daily production capacity in meters
        """
        try:
            speed = self.machine_speeds[self.machine_type]
            minutes_per_day = 24 * 60
            return (speed * minutes_per_day * self.machine_count * self.uptime_factor)
        except KeyError:
            raise ValueError("Invalid machine type configuration")
    
    def calculate_monthly_capacity(self, working_days: int = 30) -> float:
        """
        Calculate monthly production capacity.
        
        Args:
            working_days: Number of working days in month (default 30)
            
        Returns:
            Monthly production capacity in meters
        """
        if working_days <= 0 or working_days > 31:
            raise ValueError("Working days must be between 1 and 31")
            
        daily_capacity = self.calculate_daily_capacity()
        return daily_capacity * working_days
    
    def calculate_yearly_capacity(self) -> float:
        """
        Calculate yearly production capacity (365 days).
        
        Returns:
            Yearly production capacity in meters
        """
        daily_capacity = self.calculate_daily_capacity()
        return daily_capacity * 365


# Example usage
if __name__ == "__main__":
    try:
        # Create calculator for a mill with 50 weaving machines
        mill_calculator = TextileMillCapacityCalculator(
            machine_count=50,
            machine_type='weaving'
        )
        
        # Print capacity metrics
        print(f"Daily Capacity: {mill_calculator.calculate_daily_capacity():,.2f} meters")
        print(f"Monthly Capacity (30 days): {mill_calculator.calculate_monthly_capacity():,.2f} meters")
        print(f"Yearly Capacity: {mill_calculator.calculate_yearly_capacity():,.2f} meters")
        
    except ValueError as e:
        print(f"Error: {e}")
```
