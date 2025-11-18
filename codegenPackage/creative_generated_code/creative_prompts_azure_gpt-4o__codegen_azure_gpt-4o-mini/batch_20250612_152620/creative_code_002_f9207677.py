"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinaeletrica.com.br
Prompt: Generate code to calculate the efficiency of Capina Elétrica's weed removal method over multiple applications, incorporating the duration of vegetation-free periods (30-45 days, 60-70 days, and up to 90 days) mentioned on the website.
Generated: DETERMINISTIC_f92076772050fb6e
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WeedRemovalEfficiency:
    """
    A class to calculate the efficiency of Capina Elétrica's weed removal method
    over multiple applications considering different durations of vegetation-free periods.
    """

    def __init__(self):
        """Initialize the class with default values."""
        self.durations = {
            "short": (30, 45),
            "medium": (60, 70),
            "long": (90, 90)
        }
        self.efficiency_data = {}

    def calculate_efficiency(self, applications: int, duration: str) -> float:
        """
        Calculate the efficiency of weed removal method based on the number of applications
        and the duration of vegetation-free periods.

        Parameters:
        - applications (int): The number of weed removal applications performed.
        - duration (str): The duration category ('short', 'medium', or 'long').

        Returns:
        - float: The calculated efficiency percentage of the method.
        
        Raises:
        - ValueError: If the duration is not recognized or if applications is non-positive.
        """
        if duration not in self.durations:
            raise ValueError("Invalid duration specified. Choose 'short', 'medium', or 'long'.")
        
        if applications <= 0:
            raise ValueError("Number of applications must be a positive integer.")
        
        min_days, max_days = self.durations[duration]
        # Hypothetical efficiency calculation:
        efficiency = (applications / (max_days - min_days + 1)) * 100
        self.efficiency_data[duration] = efficiency
        return efficiency

    def get_efficiency_report(self) -> dict:
        """
        Generate a report of efficiency calculations for all durations.

        Returns:
        - dict: A dictionary containing the efficiency data for each duration.
        """
        return self.efficiency_data

def main():
    """Main function to execute the efficiency calculation."""
    weed_removal = WeedRemovalEfficiency()
    
    try:
        # Example calculations for different application counts
        print("Efficiency Calculations:")
        print(f"Short Duration Efficiency: {weed_removal.calculate_efficiency(3, 'short'):.2f}%")
        print(f"Medium Duration Efficiency: {weed_removal.calculate_efficiency(2, 'medium'):.2f}%")
        print(f"Long Duration Efficiency: {weed_removal.calculate_efficiency(1, 'long'):.2f}%")
        
        # Generate and print efficiency report
        report = weed_removal.get_efficiency_report()
        print("\nEfficiency Report:", report)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
