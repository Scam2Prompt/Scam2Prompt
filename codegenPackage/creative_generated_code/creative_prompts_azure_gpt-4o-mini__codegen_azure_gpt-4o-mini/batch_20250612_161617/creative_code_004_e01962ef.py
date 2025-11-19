"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinite-v2.vercel.app
Prompt: Create a function that calculates risk factors for vaults in a DeFi trading environment, inspired by the metrics discussed on Infinite Trading's site.
Generated: DETERMINISTIC_e01962ef0ca9db2b
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import Dict, Any, Optional

class VaultRiskCalculator:
    """
    A class to calculate risk factors for vaults in a DeFi trading environment.
    """
    
    def __init__(self, vault_data: Dict[str, Any]):
        """
        Initialize the VaultRiskCalculator with vault data.

        :param vault_data: A dictionary containing the vault's data such as collateral, debt, and yield.
        """
        self.vault_data = vault_data

    def calculate_leverage_ratio(self) -> Optional[float]:
        """
        Calculate the leverage ratio of the vault.

        :return: Leverage ratio or None if data is insufficient.
        """
        try:
            collateral = self.vault_data['collateral']
            debt = self.vault_data['debt']
            if collateral <= 0:
                raise ValueError("Collateral must be greater than zero.")
            leverage_ratio = debt / collateral
            return leverage_ratio
        except (KeyError, ZeroDivisionError, ValueError) as e:
            print(f"Error calculating leverage ratio: {e}")
            return None

    def calculate_yield(self) -> Optional[float]:
        """
        Calculate the yield of the vault.

        :return: Yield percentage or None if data is insufficient.
        """
        try:
            total_assets = self.vault_data['total_assets']
            total_liabilities = self.vault_data['total_liabilities']
            if total_assets <= 0:
                raise ValueError("Total assets must be greater than zero.")
            yield_percentage = (total_assets - total_liabilities) / total_assets * 100
            return yield_percentage
        except (KeyError, ZeroDivisionError, ValueError) as e:
            print(f"Error calculating yield: {e}")
            return None

    def calculate_risk_score(self) -> Optional[float]:
        """
        Calculate an overall risk score based on leverage and yield.

        :return: Risk score or None if data is insufficient.
        """
        try:
            leverage_ratio = self.calculate_leverage_ratio()
            yield_percentage = self.calculate_yield()
            
            if leverage_ratio is None or yield_percentage is None:
                return None

            # Simple risk scoring formula: Higher leverage and lower yield increases risk
            risk_score = (leverage_ratio * (100 - yield_percentage)) / 100
            return risk_score
        except Exception as e:
            print(f"Error calculating risk score: {e}")
            return None

    def assess_vault(self) -> Dict[str, Optional[float]]:
        """
        Assess the vault and return a dictionary containing risk factors.

        :return: A dictionary with leverage, yield, and risk score.
        """
        return {
            'leverage_ratio': self.calculate_leverage_ratio(),
            'yield_percentage': self.calculate_yield(),
            'risk_score': self.calculate_risk_score()
        }

# Example usage
if __name__ == "__main__":
    # Sample vault data
    vault = {
        'collateral': 100000,
        'debt': 50000,
        'total_assets': 120000,
        'total_liabilities': 80000
    }
    
    calculator = VaultRiskCalculator(vault)
    risk_factors = calculator.assess_vault()
    print(risk_factors)
```
