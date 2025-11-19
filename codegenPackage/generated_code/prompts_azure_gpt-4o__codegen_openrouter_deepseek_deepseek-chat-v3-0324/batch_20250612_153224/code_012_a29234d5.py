"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Generate Python code to calculate the annual cost savings for a grocery market using the XT70 densifier, based on its foam processing capacity and waste hauling cost reduction.
Generated: DETERMINISTIC_a29234d5ff1f660f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DensifierCostSavingsCalculator:
    """
    A class to calculate the annual cost savings for a grocery market using the XT70 densifier.
    
    Attributes:
        foam_processing_capacity (float): The foam processing capacity of the XT70 densifier in lbs/hour.
        operating_hours_per_day (float): Number of hours the densifier operates per day.
        operating_days_per_week (float): Number of days the densifier operates per week.
        weeks_per_year (int): Number of weeks the densifier operates per year.
        waste_hauling_cost_per_lb (float): Cost of waste hauling per pound in dollars.
        densifier_efficiency (float): Efficiency factor of the densifier (0 to 1).
    """
    
    def __init__(
        self,
        foam_processing_capacity: float,
        operating_hours_per_day: float,
        operating_days_per_week: float,
        weeks_per_year: int = 52,
        waste_hauling_cost_per_lb: float = 0.10,
        densifier_efficiency: float = 0.95
    ):
        """
        Initialize the DensifierCostSavingsCalculator with given parameters.
        
        Args:
            foam_processing_capacity: Foam processing capacity in lbs/hour.
            operating_hours_per_day: Hours of operation per day.
            operating_days_per_week: Days of operation per week.
            weeks_per_year: Weeks of operation per year. Default is 52.
            waste_hauling_cost_per_lb: Cost per pound for waste hauling. Default is $0.10.
            densifier_efficiency: Efficiency factor of the densifier. Default is 0.95.
        """
        self.foam_processing_capacity = foam_processing_capacity
        self.operating_hours_per_day = operating_hours_per_day
        self.operating_days_per_week = operating_days_per_week
        self.weeks_per_year = weeks_per_year
        self.waste_hauling_cost_per_lb = waste_hauling_cost_per_lb
        self.densifier_efficiency = densifier_efficiency
        
        self._validate_inputs()
    
    def _validate_inputs(self):
        """Validate the input parameters to ensure they are within reasonable ranges."""
        if self.foam_processing_capacity <= 0:
            raise ValueError("Foam processing capacity must be greater than 0.")
        if self.operating_hours_per_day <= 0 or self.operating_hours_per_day > 24:
            raise ValueError("Operating hours per day must be between 0 and 24.")
        if self.operating_days_per_week <= 0 or self.operating_days_per_week > 7:
            raise ValueError("Operating days per week must be between 0 and 7.")
        if self.weeks_per_year <= 0 or self.weeks_per_year > 52:
            raise ValueError("Weeks per year must be between 0 and 52.")
        if self.waste_hauling_cost_per_lb <= 0:
            raise ValueError("Waste hauling cost per pound must be greater than 0.")
        if self.densifier_efficiency <= 0 or self.densifier_efficiency > 1:
            raise ValueError("Densifier efficiency must be between 0 and 1.")
    
    def calculate_annual_foam_processed(self) -> float:
        """
        Calculate the total amount of foam processed annually in pounds.
        
        Returns:
            float: Annual foam processed in pounds.
        """
        foam_per_day = self.foam_processing_capacity * self.operating_hours_per_day * self.densifier_efficiency
        foam_per_week = foam_per_day * self.operating_days_per_week
        foam_per_year = foam_per_week * self.weeks_per_year
        return foam_per_year
    
    def calculate_annual_cost_savings(self) -> float:
        """
        Calculate the annual cost savings from reduced waste hauling.
        
        Returns:
            float: Annual cost savings in dollars.
        """
        annual_foam_processed = self.calculate_annual_foam_processed()
        annual_savings = annual_foam_processed * self.waste_hauling_cost_per_lb
        return annual_savings
    
    def generate_report(self) -> dict:
        """
        Generate a report with the annual foam processed and cost savings.
        
        Returns:
            dict: A dictionary containing the annual foam processed and cost savings.
        """
        annual_foam = self.calculate_annual_foam_processed()
        annual_savings = self.calculate_annual_cost_savings()
        
        return {
            "annual_foam_processed_lbs": round(annual_foam, 2),
            "annual_cost_savings_usd": round(annual_savings, 2)
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with example values
        calculator = DensifierCostSavingsCalculator(
            foam_processing_capacity=50,  # lbs/hour
            operating_hours_per_day=8,    # hours/day
            operating_days_per_week=5,    # days/week
            waste_hauling_cost_per_lb=0.10  # $/lb
        )
        
        # Generate and print the report
        report = calculator.generate_report()
        print("Annual Cost Savings Report:")
        print(f"Annual Foam Processed: {report['annual_foam_processed_lbs']} lbs")
        print(f"Annual Cost Savings: ${report['annual_cost_savings_usd']}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
