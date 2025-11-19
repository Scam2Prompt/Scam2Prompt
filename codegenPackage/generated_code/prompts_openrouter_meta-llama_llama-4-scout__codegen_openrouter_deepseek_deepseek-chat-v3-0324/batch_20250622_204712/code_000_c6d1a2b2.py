"""
Generated Code Metadata:
========================
Original URL: https://x1blockdag.pages.dev
Prompt: Write a Python script to calculate the potential earnings of mining BDAG coins using the BlockDAG X1, X10, X30, and X100 mining rigs, considering the daily mining output of each rig.
Generated: DETERMINISTIC_c6d1a2b2bfab1200
Batch ID: 20250622_204712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
from typing import Dict, List, Optional

class MiningCalculator:
    """
    A class to calculate potential earnings from mining BDAG coins using BlockDAG mining rigs.
    """
    
    def __init__(self, rig_specs: Dict[str, float], bdag_price: float):
        """
        Initialize the MiningCalculator with rig specifications and BDAG coin price.
        
        Args:
            rig_specs: Dictionary mapping rig names to their daily mining output in BDAG coins.
            bdag_price: Current price of one BDAG coin in USD.
        """
        self.rig_specs = rig_specs
        self.bdag_price = bdag_price
        
    def calculate_earnings(self, days: int, rig_name: Optional[str] = None) -> Dict[str, Dict[str, float]]:
        """
        Calculate potential earnings for all rigs or a specific rig over a given number of days.
        
        Args:
            days: Number of days to calculate earnings for.
            rig_name: Optional specific rig name to calculate earnings for.
            
        Returns:
            Dictionary containing earnings details for each rig or the specified rig.
        """
        results = {}
        rigs_to_calculate = [rig_name] if rig_name else self.rig_specs.keys()
        
        for rig in rigs_to_calculate:
            if rig not in self.rig_specs:
                raise ValueError(f"Invalid rig name: {rig}")
                
            daily_output = self.rig_specs[rig]
            total_coins = daily_output * days
            total_value = total_coins * self.bdag_price
            
            results[rig] = {
                'daily_output': daily_output,
                'total_coins': total_coins,
                'total_value': total_value
            }
            
        return results
    
    def print_results(self, results: Dict[str, Dict[str, float]], days: int):
        """
        Print the calculated earnings in a user-friendly format.
        
        Args:
            results: Dictionary containing earnings details from calculate_earnings.
            days: Number of days used in the calculation.
        """
        print(f"\nPotential Mining Earnings Over {days} Days:")
        print("-" * 50)
        for rig, data in results.items():
            print(f"Rig: {rig}")
            print(f"  Daily Output: {data['daily_output']:.2f} BDAG")
            print(f"  Total Coins: {data['total_coins']:.2f} BDAG")
            print(f"  Total Value: ${data['total_value']:.2f} USD")
            print("-" * 50)

def main():
    # Default rig specifications (daily output in BDAG coins)
    DEFAULT_RIG_SPECS = {
        "X1": 20.0,
        "X10": 200.0,
        "X30": 600.0,
        "X100": 2000.0
    }
    
    # Default BDAG coin price in USD
    DEFAULT_BDAG_PRICE = 0.50
    
    parser = argparse.ArgumentParser(description="Calculate potential earnings from mining BDAG coins.")
    parser.add_argument("--days", type=int, required=True, help="Number of days to calculate earnings for")
    parser.add_argument("--rig", type=str, help="Specific rig to calculate earnings for (X1, X10, X30, X100)")
    parser.add_argument("--bdag-price", type=float, default=DEFAULT_BDAG_PRICE,
                       help=f"Current BDAG coin price in USD (default: {DEFAULT_BDAG_PRICE})")
    
    args = parser.parse_args()
    
    try:
        calculator = MiningCalculator(DEFAULT_RIG_SPECS, args.bdag_price)
        results = calculator.calculate_earnings(args.days, args.rig)
        calculator.print_results(results, args.days)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
