"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plm.cr
Prompt: Write code to calculate transportation efficiency for logistics operations using 59-foot units, as described in PLM's logistics model.
Generated: DETERMINISTIC_cbae7cbb0680fede
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransportationEfficiency:
    """
    A class to calculate transportation efficiency for logistics operations using 59-foot units.
    """

    def __init__(self, total_distance, total_weight, unit_capacity):
        """
        Initializes the TransportationEfficiency instance.

        Args:
            total_distance (float): The total distance traveled in miles.
            total_weight (float): The total weight transported in pounds.
            unit_capacity (float): The capacity of a 59-foot unit in pounds.

        Raises:
            ValueError: If any of the input values are negative or zero.
        """
        if total_distance <= 0 or total_weight <= 0 or unit_capacity <= 0:
            raise ValueError("Distance, weight, and unit capacity must be positive values.")
        
        self.total_distance = total_distance
        self.total_weight = total_weight
        self.unit_capacity = unit_capacity

    def calculate_units_used(self):
        """
        Calculates the number of 59-foot units used for transportation.

        Returns:
            float: The number of units used.
        """
        units_used = self.total_weight / self.unit_capacity
        return units_used

    def calculate_efficiency(self):
        """
        Calculates transportation efficiency as a ratio of weight transported per mile.

        Returns:
            float: The transportation efficiency.
        """
        try:
            units_used = self.calculate_units_used()
            efficiency = self.total_weight / self.total_distance
            return efficiency
        except ZeroDivisionError:
            raise ValueError("Total distance must not be zero to calculate efficiency.")

    def report(self):
        """
        Generates a report of the transportation efficiency.

        Returns:
            str: A formatted string report.
        """
        try:
            units_used = self.calculate_units_used()
            efficiency = self.calculate_efficiency()
            report = (
                f"Transportation Efficiency Report:\n"
                f"Total Distance: {self.total_distance} miles\n"
                f"Total Weight: {self.total_weight} lbs\n"
                f"Unit Capacity: {self.unit_capacity} lbs\n"
                f"Units Used: {units_used:.2f}\n"
                f"Efficiency (lbs/mile): {efficiency:.2f}\n"
            )
            return report
        except ValueError as e:
            return str(e)


# Example usage
if __name__ == "__main__":
    try:
        # Input values for the logistics operation
        total_distance = 500.0  # in miles
        total_weight = 10000.0   # in pounds
        unit_capacity = 20000.0  # capacity of a 59-foot unit in pounds

        # Create an instance of the TransportationEfficiency class
        efficiency_calculator = TransportationEfficiency(total_distance, total_weight, unit_capacity)
        
        # Generate and print the report
        print(efficiency_calculator.report())
    
    except ValueError as e:
        print(f"Error in transportation efficiency calculation: {e}")
```
