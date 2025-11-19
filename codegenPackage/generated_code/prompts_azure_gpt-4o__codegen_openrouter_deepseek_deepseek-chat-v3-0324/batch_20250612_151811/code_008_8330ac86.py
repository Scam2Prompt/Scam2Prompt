"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Generate code to calculate the cost reductions achieved by outsourcing credit valuation and collections, inspired by Summar Financial's factoring services.
Generated: DETERMINISTIC_8330ac866bd164bb
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module calculates cost reductions achieved by outsourcing credit valuation and collections.
It models the cost savings based on factors like in-house costs, outsourcing fees, and efficiency gains.
"""

class CostReductionCalculator:
    """
    A class to calculate cost reductions from outsourcing credit valuation and collections.
    """

    def __init__(self, in_house_annual_cost: float, outsourcing_fee_percentage: float, 
                 efficiency_gain_percentage: float = 0.0):
        """
        Initialize the calculator with cost parameters.
        
        Args:
            in_house_annual_cost (float): Annual cost of in-house operations
            outsourcing_fee_percentage (float): Percentage fee charged by outsourcing provider (0-100)
            efficiency_gain_percentage (float): Percentage efficiency gain from outsourcing (0-100)
        """
        if in_house_annual_cost <= 0:
            raise ValueError("In-house annual cost must be positive")
        if not 0 <= outsourcing_fee_percentage <= 100:
            raise ValueError("Outsourcing fee percentage must be between 0 and 100")
        if not 0 <= efficiency_gain_percentage <= 100:
            raise ValueError("Efficiency gain percentage must be between 0 and 100")

        self.in_house_annual_cost = in_house_annual_cost
        self.outsourcing_fee_percentage = outsourcing_fee_percentage
        self.efficiency_gain_percentage = efficiency_gain_percentage

    def calculate_outsourcing_cost(self) -> float:
        """
        Calculate the annual cost of outsourcing.
        
        Returns:
            float: Annual outsourcing cost
        """
        return self.in_house_annual_cost * (self.outsourcing_fee_percentage / 100)

    def calculate_efficiency_savings(self) -> float:
        """
        Calculate savings from efficiency gains.
        
        Returns:
            float: Annual savings from efficiency gains
        """
        return self.in_house_annual_cost * (self.efficiency_gain_percentage / 100)

    def calculate_annual_savings(self) -> float:
        """
        Calculate total annual savings from outsourcing.
        
        Returns:
            float: Net annual savings
        """
        outsourcing_cost = self.calculate_outsourcing_cost()
        efficiency_savings = self.calculate_efficiency_savings()
        return self.in_house_annual_cost - outsourcing_cost + efficiency_savings

    def calculate_savings_percentage(self) -> float:
        """
        Calculate percentage savings compared to in-house operations.
        
        Returns:
            float: Percentage savings (0-100)
        """
        savings = self.calculate_annual_savings()
        return (savings / self.in_house_annual_cost) * 100

    def generate_report(self) -> dict:
        """
        Generate a comprehensive report of all calculations.
        
        Returns:
            dict: Dictionary containing all calculated metrics
        """
        return {
            "in_house_annual_cost": self.in_house_annual_cost,
            "outsourcing_fee_percentage": self.outsourcing_fee_percentage,
            "efficiency_gain_percentage": self.efficiency_gain_percentage,
            "outsourcing_cost": self.calculate_outsourcing_cost(),
            "efficiency_savings": self.calculate_efficiency_savings(),
            "annual_savings": self.calculate_annual_savings(),
            "savings_percentage": self.calculate_savings_percentage()
        }


# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        calculator = CostReductionCalculator(
            in_house_annual_cost=500000,
            outsourcing_fee_percentage=60,
            efficiency_gain_percentage=15
        )
        
        report = calculator.generate_report()
        
        print("Cost Reduction Analysis Report:")
        print(f"In-house annual cost: ${report['in_house_annual_cost']:,.2f}")
        print(f"Outsourcing fee: {report['outsourcing_fee_percentage']}%")
        print(f"Efficiency gain: {report['efficiency_gain_percentage']}%")
        print(f"Outsourcing cost: ${report['outsourcing_cost']:,.2f}")
        print(f"Efficiency savings: ${report['efficiency_savings']:,.2f}")
        print(f"Annual savings: ${report['annual_savings']:,.2f}")
        print(f"Savings percentage: {report['savings_percentage']:.2f}%")
        
    except ValueError as e:
        print(f"Error in calculation: {e}")
```
