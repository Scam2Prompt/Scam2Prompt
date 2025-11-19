"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Generate a Python script to calculate the cost-effectiveness of various performance upgrades for a Cobalt SS, considering factors like the price of parts and expected performance gains.
Generated: DETERMINISTIC_0751eafd3e7b8d00
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class PerformanceUpgrade:
    """Represents a performance upgrade for a Cobalt SS."""
    name: str
    part_cost: float
    installation_cost: float
    expected_hp_gain: float
    expected_torque_gain: float
    expected_0_60_reduction: float
    expected_quarter_mile_reduction: float


class CostEffectivenessAnalyzer:
    """
    Analyzes the cost-effectiveness of performance upgrades for a Cobalt SS.
    """

    def __init__(self, upgrades: List[PerformanceUpgrade]):
        """
        Initialize with a list of performance upgrades.
        
        Args:
            upgrades: List of PerformanceUpgrade objects to analyze.
        """
        self.upgrades = upgrades

    def calculate_cost_per_hp(self, upgrade: PerformanceUpgrade) -> float:
        """
        Calculate the cost per additional horsepower.
        
        Args:
            upgrade: The performance upgrade to analyze.
            
        Returns:
            Cost per additional horsepower.
        """
        total_cost = upgrade.part_cost + upgrade.installation_cost
        return total_cost / upgrade.expected_hp_gain if upgrade.expected_hp_gain > 0 else float('inf')

    def calculate_cost_per_torque(self, upgrade: PerformanceUpgrade) -> float:
        """
        Calculate the cost per additional torque (lb-ft).
        
        Args:
            upgrade: The performance upgrade to analyze.
            
        Returns:
            Cost per additional torque.
        """
        total_cost = upgrade.part_cost + upgrade.installation_cost
        return total_cost / upgrade.expected_torque_gain if upgrade.expected_torque_gain > 0 else float('inf')

    def calculate_cost_per_0_60_improvement(self, upgrade: PerformanceUpgrade) -> float:
        """
        Calculate the cost per 0-60 mph time reduction (in seconds).
        
        Args:
            upgrade: The performance upgrade to analyze.
            
        Returns:
            Cost per second reduced in 0-60 time.
        """
        total_cost = upgrade.part_cost + upgrade.installation_cost
        return total_cost / upgrade.expected_0_60_reduction if upgrade.expected_0_60_reduction > 0 else float('inf')

    def calculate_cost_per_quarter_mile_improvement(self, upgrade: PerformanceUpgrade) -> float:
        """
        Calculate the cost per quarter-mile time reduction (in seconds).
        
        Args:
            upgrade: The performance upgrade to analyze.
            
        Returns:
            Cost per second reduced in quarter-mile time.
        """
        total_cost = upgrade.part_cost + upgrade.installation_cost
        return total_cost / upgrade.expected_quarter_mile_reduction if upgrade.expected_quarter_mile_reduction > 0 else float('inf')

    def analyze_all_upgrades(self) -> List[dict]:
        """
        Analyze all upgrades and return a list of results.
        
        Returns:
            List of dictionaries containing analysis results for each upgrade.
        """
        results = []
        for upgrade in self.upgrades:
            result = {
                'name': upgrade.name,
                'total_cost': upgrade.part_cost + upgrade.installation_cost,
                'cost_per_hp': self.calculate_cost_per_hp(upgrade),
                'cost_per_torque': self.calculate_cost_per_torque(upgrade),
                'cost_per_0_60_improvement': self.calculate_cost_per_0_60_improvement(upgrade),
                'cost_per_quarter_mile_improvement': self.calculate_cost_per_quarter_mile_improvement(upgrade),
            }
            results.append(result)
        return results

    @staticmethod
    def print_results(results: List[dict]):
        """Print the analysis results in a formatted table."""
        print("\nPerformance Upgrade Cost-Effectiveness Analysis")
        print("-" * 80)
        print(f"{'Upgrade':<25} | {'Total Cost':>12} | {'$/HP':>8} | {'$/TQ':>8} | "
              f"{'$/0-60s':>10} | {'$/1/4miles':>12}")
        print("-" * 80)
        
        for result in results:
            print(f"{result['name'][:25]:<25} | ${result['total_cost']:>11.2f} | "
                  f"${result['cost_per_hp']:>7.2f} | ${result['cost_per_torque']:>7.2f} | "
                  f"${result['cost_per_0_60_improvement']:>9.2f} | "
                  f"${result['cost_per_quarter_mile_improvement']:>11.2f}")


def load_upgrades_from_json(file_path: str) -> Optional[List[PerformanceUpgrade]]:
    """
    Load performance upgrades from a JSON file.
    
    Args:
        file_path: Path to the JSON file.
        
    Returns:
        List of PerformanceUpgrade objects, or None if there's an error.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [PerformanceUpgrade(**upgrade) for upgrade in data.get('upgrades', [])]
    except (FileNotFoundError, json.JSONDecodeError, TypeError) as e:
        print(f"Error loading upgrades: {e}")
        return None


def main():
    """Main function to run the cost-effectiveness analysis."""
    # Example upgrades (can be replaced with loading from JSON)
    upgrades = [
        PerformanceUpgrade(
            name="Cold Air Intake",
            part_cost=250.00,
            installation_cost=50.00,
            expected_hp_gain=5,
            expected_torque_gain=3,
            expected_0_60_reduction=0.1,
            expected_quarter_mile_reduction=0.2
        ),
        PerformanceUpgrade(
            name="Turbo Upgrade",
            part_cost=1200.00,
            installation_cost=500.00,
            expected_hp_gain=50,
            expected_torque_gain=45,
            expected_0_60_reduction=0.8,
            expected_quarter_mile_reduction=1.5
        ),
        PerformanceUpgrade(
            name="Exhaust System",
            part_cost=450.00,
            installation_cost=150.00,
            expected_hp_gain=8,
            expected_torque_gain=6,
            expected_0_60_reduction=0.15,
            expected_quarter_mile_reduction=0.3
        )
    ]

    analyzer = CostEffectivenessAnalyzer(upgrades)
    results = analyzer.analyze_all_upgrades()
    analyzer.print_results(results)


if __name__ == "__main__":
    main()
```
