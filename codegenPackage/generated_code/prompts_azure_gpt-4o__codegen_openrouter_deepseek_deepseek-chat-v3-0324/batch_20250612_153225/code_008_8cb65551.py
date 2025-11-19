"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Write code to calculate the cost-effectiveness of periodic maintenance for generators, using insights from Birlik Jeneratör's "Periyodik Bakım" service.
Generated: DETERMINISTIC_8cb65551f1f9cfad
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Generator Maintenance Cost-Effectiveness Calculator

This script calculates the cost-effectiveness of periodic maintenance for generators
based on input parameters such as maintenance cost, downtime cost, failure rate, etc.
"""

import math
from typing import Optional, Tuple

class GeneratorMaintenanceCalculator:
    """
    A class to calculate the cost-effectiveness of periodic generator maintenance.
    
    Attributes:
        maintenance_cost (float): Cost of periodic maintenance (in currency units)
        downtime_cost_per_hour (float): Cost of generator downtime per hour
        avg_maintenance_duration_hours (float): Average duration of maintenance in hours
        avg_failure_duration_hours (float): Average duration of failure repair in hours
        failure_rate_without_maintenance (float): Annual failure rate without maintenance (0-1)
        failure_rate_with_maintenance (float): Annual failure rate with maintenance (0-1)
        generator_value (float): Value of the generator (in currency units)
        useful_life_years (int): Expected useful life of generator in years
    """
    
    def __init__(
        self,
        maintenance_cost: float,
        downtime_cost_per_hour: float,
        avg_maintenance_duration_hours: float,
        avg_failure_duration_hours: float,
        failure_rate_without_maintenance: float,
        failure_rate_with_maintenance: float,
        generator_value: Optional[float] = None,
        useful_life_years: Optional[int] = None
    ):
        """
        Initialize the calculator with maintenance parameters.
        
        Args:
            maintenance_cost: Cost of periodic maintenance
            downtime_cost_per_hour: Cost of downtime per hour
            avg_maintenance_duration_hours: Average maintenance duration in hours
            avg_failure_duration_hours: Average failure repair duration in hours
            failure_rate_without_maintenance: Annual failure rate without maintenance
            failure_rate_with_maintenance: Annual failure rate with maintenance
            generator_value: Optional value of the generator
            useful_life_years: Optional useful life of generator in years
        """
        self.maintenance_cost = maintenance_cost
        self.downtime_cost_per_hour = downtime_cost_per_hour
        self.avg_maintenance_duration_hours = avg_maintenance_duration_hours
        self.avg_failure_duration_hours = avg_failure_duration_hours
        self.failure_rate_without_maintenance = failure_rate_without_maintenance
        self.failure_rate_with_maintenance = failure_rate_with_maintenance
        self.generator_value = generator_value
        self.useful_life_years = useful_life_years
        
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate that all inputs are within reasonable ranges."""
        if any(val < 0 for val in [
            self.maintenance_cost,
            self.downtime_cost_per_hour,
            self.avg_maintenance_duration_hours,
            self.avg_failure_duration_hours
        ]):
            raise ValueError("Cost and duration values cannot be negative")
        
        if not (0 <= self.failure_rate_without_maintenance <= 1):
            raise ValueError("Failure rate without maintenance must be between 0 and 1")
            
        if not (0 <= self.failure_rate_with_maintenance <= 1):
            raise ValueError("Failure rate with maintenance must be between 0 and 1")
            
        if self.failure_rate_with_maintenance > self.failure_rate_without_maintenance:
            raise ValueError("Maintenance should reduce failure rate")
            
        if self.generator_value is not None and self.generator_value < 0:
            raise ValueError("Generator value cannot be negative")
            
        if self.useful_life_years is not None and self.useful_life_years <= 0:
            raise ValueError("Useful life must be positive")
    
    def calculate_annual_costs(self, maintenance_frequency_per_year: int) -> Tuple[float, float]:
        """
        Calculate annual costs with and without maintenance.
        
        Args:
            maintenance_frequency_per_year: Number of maintenance operations per year
            
        Returns:
            Tuple of (annual_cost_with_maintenance, annual_cost_without_maintenance)
        """
        if maintenance_frequency_per_year <= 0:
            raise ValueError("Maintenance frequency must be positive")
        
        # Calculate maintenance costs
        maintenance_downtime_cost = (
            self.downtime_cost_per_hour * 
            self.avg_maintenance_duration_hours * 
            maintenance_frequency_per_year
        )
        total_maintenance_cost = (
            self.maintenance_cost * maintenance_frequency_per_year + 
            maintenance_downtime_cost
        )
        
        # Calculate failure costs with maintenance
        failure_cost_with_maintenance = (
            self.failure_rate_with_maintenance * 
            self.avg_failure_duration_hours * 
            self.downtime_cost_per_hour
        )
        
        # Calculate failure costs without maintenance
        failure_cost_without_maintenance = (
            self.failure_rate_without_maintenance * 
            self.avg_failure_duration_hours * 
            self.downtime_cost_per_hour
        )
        
        # Total annual costs
        annual_cost_with_maintenance = total_maintenance_cost + failure_cost_with_maintenance
        annual_cost_without_maintenance = failure_cost_without_maintenance
        
        return (annual_cost_with_maintenance, annual_cost_without_maintenance)
    
    def calculate_cost_effectiveness(
        self, 
        maintenance_frequency_per_year: int,
        discount_rate: float = 0.05
    ) -> Tuple[float, float, float]:
        """
        Calculate the cost-effectiveness of maintenance over the generator's life.
        
        Args:
            maintenance_frequency_per_year: Number of maintenance operations per year
            discount_rate: Annual discount rate for present value calculations
            
        Returns:
            Tuple of (npv_with_maintenance, npv_without_maintenance, cost_difference)
        """
        if self.useful_life_years is None:
            raise ValueError("Useful life must be specified for NPV calculation")
            
        if not (0 <= discount_rate <= 1):
            raise ValueError("Discount rate must be between 0 and 1")
        
        annual_with, annual_without = self.calculate_annual_costs(maintenance_frequency_per_year)
        
        # Calculate Net Present Value for both scenarios
        npv_with = 0
        npv_without = 0
        
        for year in range(1, self.useful_life_years + 1):
            discount_factor = 1 / ((1 + discount_rate) ** year)
            npv_with += annual_with * discount_factor
            npv_without += annual_without * discount_factor
        
        # Add generator value (if provided) as a one-time cost at year 0
        if self.generator_value is not None:
            npv_with += self.generator_value
            npv_without += self.generator_value
        
        cost_difference = npv_without - npv_with
        
        return (npv_with, npv_without, cost_difference)
    
    def find_optimal_maintenance_frequency(
        self,
        max_frequency: int = 12,
        discount_rate: float = 0.05
    ) -> Tuple[int, float]:
        """
        Find the maintenance frequency that maximizes cost savings.
        
        Args:
            max_frequency: Maximum frequency to consider (per year)
            discount_rate: Annual discount rate for present value calculations
            
        Returns:
            Tuple of (optimal_frequency, max_savings)
        """
        if max_frequency <= 0:
            raise ValueError("Maximum frequency must be positive")
            
        optimal_frequency = 0
        max_savings = -float('inf')
        
        for freq in range(1, max_frequency + 1):
            try:
                _, _, savings = self.calculate_cost_effectiveness(freq, discount_rate)
                if savings > max_savings:
                    max_savings = savings
                    optimal_frequency = freq
            except ValueError:
                continue
                
        return (optimal_frequency, max_savings)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator with example values
        calculator = GeneratorMaintenanceCalculator(
            maintenance_cost=5000,
            downtime_cost_per_hour=1000,
            avg_maintenance_duration_hours=8,
            avg_failure_duration_hours=24,
            failure_rate_without_maintenance=0.5,
            failure_rate_with_maintenance=0.1,
            generator_value=100000,
            useful_life_years=10
        )
        
        # Calculate annual costs for quarterly maintenance
        annual_with, annual_without = calculator.calculate_annual_costs(4)
        print(f"Annual cost with maintenance: ${annual_with:,.2f}")
        print(f"Annual cost without maintenance: ${annual_without:,.2f}")
        
        # Calculate NPV and cost difference
        npv_with, npv_without, diff = calculator.calculate_cost_effectiveness(4)
        print(f"\n10-year NPV with maintenance: ${npv_with:,.2f}")
        print(f"10-year NPV without maintenance: ${npv_without:,.2f}")
        print(f"Cost savings from maintenance: ${diff:,.2f}")
        
        # Find optimal
