"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Generate a Python script that calculates the performance improvement after cleaning fuel injectors based on contamination levels.
Generated: DETERMINISTIC_95fbfc2e513f1f06
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class FuelInjectorPerformanceCalculator:
    """
    A class to calculate the performance improvement after cleaning fuel injectors.
    
    Attributes:
        contamination_level (float): The contamination level of the fuel injectors (0-100%).
        base_performance (float): The base performance level before cleaning (0-100%).
    """
    
    def __init__(self, contamination_level: float, base_performance: float):
        """
        Initialize the calculator with contamination level and base performance.
        
        Args:
            contamination_level: The contamination level of the fuel injectors (0-100%).
            base_performance: The base performance level before cleaning (0-100%).
            
        Raises:
            ValueError: If contamination_level or base_performance are outside 0-100 range.
        """
        if not (0 <= contamination_level <= 100):
            raise ValueError("Contamination level must be between 0 and 100")
        if not (0 <= base_performance <= 100):
            raise ValueError("Base performance must be between 0 and 100")
            
        self.contamination_level = contamination_level
        self.base_performance = base_performance
    
    def calculate_performance_improvement(self) -> float:
        """
        Calculate the performance improvement after cleaning fuel injectors.
        
        The calculation uses a logarithmic scale to model diminishing returns at higher contamination levels.
        
        Returns:
            float: The performance improvement percentage (0-100%).
        """
        # Logarithmic scaling factor (adjust based on empirical data)
        scaling_factor = 20.0
        
        # Calculate improvement using logarithmic function
        improvement = scaling_factor * math.log1p(self.contamination_level)
        
        # Cap the improvement at 100% - base_performance
        max_possible_improvement = 100 - self.base_performance
        return min(improvement, max_possible_improvement)
    
    def get_new_performance_level(self) -> float:
        """
        Calculate the new performance level after cleaning.
        
        Returns:
            float: The new performance level (0-100%).
        """
        improvement = self.calculate_performance_improvement()
        new_performance = self.base_performance + improvement
        
        # Ensure we don't exceed 100%
        return min(new_performance, 100)


def main():
    """
    Example usage of the FuelInjectorPerformanceCalculator.
    """
    try:
        # Get user input
        contamination = float(input("Enter contamination level (0-100%): "))
        base_perf = float(input("Enter base performance level (0-100%): "))
        
        # Create calculator instance
        calculator = FuelInjectorPerformanceCalculator(contamination, base_perf)
        
        # Calculate and display results
        improvement = calculator.calculate_performance_improvement()
        new_performance = calculator.get_new_performance_level()
        
        print(f"\nPerformance Improvement: {improvement:.2f}%")
        print(f"New Performance Level: {new_performance:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
