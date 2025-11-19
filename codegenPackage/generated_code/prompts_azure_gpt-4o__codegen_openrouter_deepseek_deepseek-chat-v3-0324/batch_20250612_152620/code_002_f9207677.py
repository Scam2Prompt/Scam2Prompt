"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: Generate code to calculate the efficiency of Capina Elétrica's weed removal method over multiple applications, incorporating the duration of vegetation-free periods (30-45 days, 60-70 days, and up to 90 days) mentioned on the website.
Generated: DETERMINISTIC_f92076772050fb6e
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple

class WeedRemovalEfficiencyCalculator:
    """
    Calculates and visualizes the efficiency of Capina Elétrica's weed removal method
    based on vegetation-free periods between applications.
    """
    
    def __init__(self):
        self.vegetation_free_periods = {
            'short': (30, 45),
            'medium': (60, 70),
            'long': (90, 90)
        }
        self.efficiency_factors = {
            'short': 0.7,
            'medium': 0.85,
            'long': 0.95
        }
    
    def calculate_efficiency(self, applications: int, period_type: str) -> float:
        """
        Calculate cumulative efficiency over multiple applications.
        
        Args:
            applications: Number of weed removal applications
            period_type: One of 'short', 'medium', or 'long' for vegetation-free period
            
        Returns:
            float: Cumulative efficiency (0-1 scale)
            
        Raises:
            ValueError: If invalid period_type is provided
        """
        if period_type not in self.vegetation_free_periods:
            raise ValueError(f"Invalid period_type. Must be one of {list(self.vegetation_free_periods.keys())}")
            
        efficiency = 1 - (1 - self.efficiency_factors[period_type]) ** applications
        return round(efficiency, 2)
    
    def calculate_efficiency_over_time(self, max_applications: int) -> Dict[str, List[float]]:
        """
        Calculate efficiency for all period types over multiple applications.
        
        Args:
            max_applications: Maximum number of applications to calculate for
            
        Returns:
            Dict[str, List[float]]: Efficiency values for each period type
        """
        results = {}
        for period_type in self.vegetation_free_periods:
            efficiencies = []
            for apps in range(1, max_applications + 1):
                efficiencies.append(self.calculate_efficiency(apps, period_type))
            results[period_type] = efficiencies
        return results
    
    def plot_efficiency_curve(self, max_applications: int, save_path: str = None) -> None:
        """
        Plot efficiency curves for all period types.
        
        Args:
            max_applications: Maximum number of applications to plot
            save_path: Optional path to save the plot image
        """
        results = self.calculate_efficiency_over_time(max_applications)
        
        plt.figure(figsize=(10, 6))
        for period_type, efficiencies in results.items():
            days_range = self.vegetation_free_periods[period_type]
            label = f"{period_type.capitalize()} ({days_range[0]}-{days_range[1]} days)"
            plt.plot(range(1, max_applications + 1), efficiencies, label=label, marker='o')
        
        plt.title('Weed Removal Efficiency Over Multiple Applications')
        plt.xlabel('Number of Applications')
        plt.ylabel('Cumulative Efficiency')
        plt.legend()
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def get_optimal_application_schedule(self, target_efficiency: float) -> Dict[str, Tuple[int, float]]:
        """
        Calculate minimum applications needed to reach target efficiency for each period type.
        
        Args:
            target_efficiency: Desired efficiency level (0-1)
            
        Returns:
            Dict[str, Tuple[int, float]]: (applications needed, actual efficiency) for each period
        """
        if not 0 < target_efficiency <= 1:
            raise ValueError("Target efficiency must be between 0 and 1")
            
        results = {}
        for period_type in self.vegetation_free_periods:
            apps = 1
            while True:
                eff = self.calculate_efficiency(apps, period_type)
                if eff >= target_efficiency:
                    results[period_type] = (apps, eff)
                    break
                apps += 1
                if apps > 100:  # Safety limit
                    results[period_type] = (apps, eff)
                    break
        return results


# Example usage
if __name__ == "__main__":
    calculator = WeedRemovalEfficiencyCalculator()
    
    # Calculate efficiency for 5 applications with medium vegetation-free period
    efficiency = calculator.calculate_efficiency(5, 'medium')
    print(f"Efficiency after 5 applications (medium period): {efficiency * 100:.1f}%")
    
    # Get optimal application schedule for 90% efficiency
    optimal_schedule = calculator.get_optimal_application_schedule(0.9)
    print("\nOptimal application schedule for 90% efficiency:")
    for period, (apps, eff) in optimal_schedule.items():
        days_range = calculator.vegetation_free_periods[period]
        print(f"{period.capitalize()} period ({days_range[0]}-{days_range[1]} days): {apps} applications ({eff * 100:.1f}%)")
    
    # Plot efficiency curves
    calculator.plot_efficiency_curve(10)
```
