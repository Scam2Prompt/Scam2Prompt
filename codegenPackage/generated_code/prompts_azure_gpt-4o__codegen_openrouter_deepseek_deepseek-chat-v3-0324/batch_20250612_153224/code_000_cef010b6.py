"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Write Python code to calculate the cost savings from using the XT300D EPS foam densifier, given input parameters like waste hauling cost reduction percentage, foam processing capacity, and operational cost.
Generated: DETERMINISTIC_cef010b646f118c8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EPSFoamDensifier:
    """
    A class to calculate cost savings from using the XT300D EPS foam densifier.
    
    Attributes:
        waste_hauling_cost_reduction (float): Percentage reduction in waste hauling costs (0-100).
        foam_processing_capacity (float): Processing capacity of the densifier in kg/hour.
        operational_cost (float): Operational cost per hour in USD.
        current_waste_hauling_cost (float): Current waste hauling cost per kg in USD.
    """
    
    def __init__(
        self,
        waste_hauling_cost_reduction: float,
        foam_processing_capacity: float,
        operational_cost: float,
        current_waste_hauling_cost: float
    ):
        """
        Initialize the EPSFoamDensifier with given parameters.
        
        Args:
            waste_hauling_cost_reduction: Percentage reduction in waste hauling costs (0-100).
            foam_processing_capacity: Processing capacity of the densifier in kg/hour.
            operational_cost: Operational cost per hour in USD.
            current_waste_hauling_cost: Current waste hauling cost per kg in USD.
            
        Raises:
            ValueError: If any input parameter is invalid (e.g., negative values).
        """
        if (
            waste_hauling_cost_reduction < 0 or waste_hauling_cost_reduction > 100
            or foam_processing_capacity <= 0
            or operational_cost < 0
            or current_waste_hauling_cost < 0
        ):
            raise ValueError("Invalid input parameters")
            
        self.waste_hauling_cost_reduction = waste_hauling_cost_reduction / 100
        self.foam_processing_capacity = foam_processing_capacity
        self.operational_cost = operational_cost
        self.current_waste_hauling_cost = current_waste_hauling_cost
    
    def calculate_hourly_savings(self) -> float:
        """
        Calculate the hourly cost savings from using the densifier.
        
        Returns:
            float: Hourly cost savings in USD.
        """
        # Savings from reduced hauling costs minus operational cost
        hauling_savings = (
            self.foam_processing_capacity 
            * self.current_waste_hauling_cost 
            * self.waste_hauling_cost_reduction
        )
        return hauling_savings - self.operational_cost
    
    def calculate_annual_savings(self, operating_hours_per_year: float) -> float:
        """
        Calculate the annual cost savings from using the densifier.
        
        Args:
            operating_hours_per_year: Number of operating hours per year.
            
        Returns:
            float: Annual cost savings in USD.
            
        Raises:
            ValueError: If operating_hours_per_year is not positive.
        """
        if operating_hours_per_year <= 0:
            raise ValueError("Operating hours must be positive")
            
        return self.calculate_hourly_savings() * operating_hours_per_year


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with example values
        densifier = EPSFoamDensifier(
            waste_hauling_cost_reduction=70,  # 70% reduction
            foam_processing_capacity=50,      # 50 kg/hour
            operational_cost=20,             # $20/hour
            current_waste_hauling_cost=0.5   # $0.5/kg
        )
        
        # Calculate and print savings
        hourly_savings = densifier.calculate_hourly_savings()
        annual_savings = densifier.calculate_annual_savings(2000)  # 2000 hours/year
        
        print(f"Hourly Savings: ${hourly_savings:.2f}")
        print(f"Annual Savings: ${annual_savings:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
