"""
Generated Code Metadata:
========================
Original URL: https://moxie.credit
Prompt: Compare the Moxie Protocol's bonding curves with other tokenomics models, highlighting the benefits of emphasizing utility over speculation.
Generated: DETERMINISTIC_cf691ca9c90e6b18
Batch ID: 20250622_211436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict, Tuple

class BondingCurve:
    """
    A class to model and compare different bonding curves and tokenomics models.
    """
    
    def __init__(self):
        self.curves: Dict[str, callable] = {
            'linear': self.linear_curve,
            'exponential': self.exponential_curve,
            'logistic': self.logistic_curve,
            'moxie': self.moxie_curve
        }
    
    def linear_curve(self, x: float) -> float:
        """Linear bonding curve: price increases linearly with supply."""
        return x
    
    def exponential_curve(self, x: float) -> float:
        """Exponential bonding curve: price increases exponentially with supply."""
        return np.exp(x / 10) - 1
    
    def logistic_curve(self, x: float) -> float:
        """Logistic bonding curve: price follows an S-curve, limiting growth."""
        return 1 / (1 + np.exp(-x / 5))
    
    def moxie_curve(self, x: float) -> float:
        """
        Moxie Protocol's bonding curve: emphasizes utility over speculation.
        Price increases sublinearly, promoting stability and utility.
        """
        return np.log(x + 1)
    
    def calculate_prices(self, supply_range: List[float], curve_type: str) -> List[float]:
        """
        Calculate prices for a given supply range and curve type.
        
        Args:
            supply_range: List of supply values.
            curve_type: Type of curve ('linear', 'exponential', 'logistic', 'moxie').
        
        Returns:
            List of prices corresponding to the supply range.
        
        Raises:
            ValueError: If curve_type is not supported.
        """
        if curve_type not in self.curves:
            raise ValueError(f"Unsupported curve type: {curve_type}")
        
        curve_func = self.curves[curve_type]
        return [curve_func(x) for x in supply_range]
    
    def plot_curves(self, supply_range: List[float], curve_types: List[str]) -> None:
        """
        Plot multiple bonding curves for comparison.
        
        Args:
            supply_range: List of supply values.
            curve_types: List of curve types to plot.
        """
        plt.figure(figsize=(10, 6))
        
        for curve_type in curve_types:
            prices = self.calculate_prices(supply_range, curve_type)
            plt.plot(supply_range, prices, label=curve_type)
        
        plt.title("Comparison of Bonding Curves")
        plt.xlabel("Token Supply")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.show()

    def compare_utility_vs_speculation(self) -> Dict[str, Tuple[float, float]]:
        """
        Compare utility-focused (Moxie) vs speculation-focused (exponential) models.
        
        Returns:
            Dictionary with metrics for each model:
            - price_at_low_supply: Price at low supply (utility phase).
            - price_at_high_supply: Price at high supply (speculation phase).
        """
        low_supply = 1.0
        high_supply = 20.0
        
        metrics = {}
        for curve_type in ['moxie', 'exponential']:
            price_low = self.calculate_prices([low_supply], curve_type)[0]
            price_high = self.calculate_prices([high_supply], curve_type)[0]
            metrics[curve_type] = (price_low, price_high)
        
        return metrics


def main():
    """Main function to demonstrate bonding curve comparison."""
    try:
        bc = BondingCurve()
        supply_range = np.linspace(0.1, 20, 100)
        
        # Plot all curves for comparison
        bc.plot_curves(supply_range, ['linear', 'exponential', 'logistic', 'moxie'])
        
        # Compare utility vs speculation
        metrics = bc.compare_utility_vs_speculation()
        print("\nUtility vs Speculation Comparison:")
        for curve_type, (low, high) in metrics.items():
            print(f"{curve_type}: Low Supply Price={low:.2f}, High Supply Price={high:.2f}")
        
        # Highlight Moxie's benefits
        print("\nMoxie Protocol Benefits:")
        print("- Sublinear price growth reduces speculation incentives")
        print("- Stable pricing promotes utility and long-term usage")
        print("- Lower volatility compared to exponential models")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
