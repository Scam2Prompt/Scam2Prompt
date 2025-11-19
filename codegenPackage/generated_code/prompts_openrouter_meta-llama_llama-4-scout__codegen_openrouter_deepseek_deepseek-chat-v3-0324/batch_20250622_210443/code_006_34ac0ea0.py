"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-web.pages.dev
Prompt: Create a detailed report on the tokenomics of $SCOTTY, including the supply distribution, presale details, and planned use cases for the token.
Generated: DETERMINISTIC_34ac0ea024925129
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class TokenomicsReport:
    """
    A class to generate a detailed report on the tokenomics of $SCOTTY token.
    Includes supply distribution, presale details, and planned use cases.
    """
    
    def __init__(self, token_name: str = "SCOTTY"):
        """
        Initialize the TokenomicsReport with default values.
        
        Args:
            token_name (str): Name of the token (default: "SCOTTY")
        """
        self.token_name = token_name
        self.total_supply = 1_000_000_000  # 1 billion tokens
        self.supply_distribution = {}
        self.presale_details = {}
        self.use_cases = []
        self.report_date = datetime.now().strftime("%Y-%m-%d")
        
    def set_supply_distribution(self, distribution: Dict[str, float]) -> None:
        """
        Set the token supply distribution percentages.
        
        Args:
            distribution (Dict[str, float]): Dictionary of allocation names and percentages
        """
        if not self._validate_percentages(distribution.values()):
            raise ValueError("Supply distribution percentages must sum to 100%")
        
        self.supply_distribution = {
            "total_supply": self.total_supply,
            "distribution": distribution
        }
    
    def set_presale_details(
        self,
        start_date: str,
        end_date: str,
        price: float,
        hard_cap: float,
        soft_cap: float,
        tokens_allocated: int,
        vesting_schedule: Optional[Dict[str, float]] = None
    ) -> None:
        """
        Set the presale details for the token.
        
        Args:
            start_date (str): Presale start date (YYYY-MM-DD)
            end_date (str): Presale end date (YYYY-MM-DD)
            price (float): Token price in USD
            hard_cap (float): Maximum funding goal in USD
            soft_cap (float): Minimum funding goal in USD
            tokens_allocated (int): Number of tokens allocated for presale
            vesting_schedule (Optional[Dict[str, float]]): Vesting schedule if applicable
        """
        self.presale_details = {
            "start_date": start_date,
            "end_date": end_date,
            "price": price,
            "hard_cap": hard_cap,
            "soft_cap": soft_cap,
            "tokens_allocated": tokens_allocated,
            "vesting_schedule": vesting_schedule or {}
        }
    
    def add_use_case(self, title: str, description: str) -> None:
        """
        Add a use case for the token.
        
        Args:
            title (str): Title of the use case
            description (str): Description of the use case
        """
        self.use_cases.append({
            "title": title,
            "description": description
        })
    
    def generate_report(self) -> Dict:
        """
        Generate the complete tokenomics report.
        
        Returns:
            Dict: Complete tokenomics report in dictionary format
        """
        return {
            "token_name": self.token_name,
            "report_date": self.report_date,
            "supply_distribution": self.supply_distribution,
            "presale_details": self.presale_details,
            "use_cases": self.use_cases
        }
    
    def save_report(self, filename: str) -> None:
        """
        Save the report to a JSON file.
        
        Args:
            filename (str): Name of the file to save the report
        """
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)
    
    def _validate_percentages(self, percentages: List[float]) -> bool:
        """
        Validate that the percentages sum to 100.
        
        Args:
            percentages (List[float]): List of percentages to validate
            
        Returns:
            bool: True if percentages sum to 100, False otherwise
        """
        return abs(sum(percentages) - 100) < 0.001

# Example usage
if __name__ == "__main__":
    try:
        # Initialize report
        report = TokenomicsReport()
        
        # Set supply distribution
        distribution = {
            "Presale": 30.0,
            "Liquidity": 20.0,
            "Team": 15.0,
            "Advisors": 5.0,
            "Marketing": 10.0,
            "Development": 10.0,
            "Community Rewards": 10.0
        }
        report.set_supply_distribution(distribution)
        
        # Set presale details
        report.set_presale_details(
            start_date="2023-11-01",
            end_date="2023-12-15",
            price=0.05,
            hard_cap=5_000_000,
            soft_cap=1_000_000,
            tokens_allocated=300_000_000,
            vesting_schedule={
                "TGE": 20.0,
                "Monthly over 12 months": 80.0
            }
        )
        
        # Add use cases
        report.add_use_case(
            "Staking Rewards",
            "Token holders can stake $SCOTTY to earn additional tokens as rewards."
        )
        report.add_use_case(
            "Governance",
            "$SCOTTY holders can participate in governance decisions for the protocol."
        )
        report.add_use_case(
            "Fee Discounts",
            "Using $SCOTTY for transactions provides fee discounts on the platform."
        )
        
        # Generate and save report
        report.save_report("scotty_tokenomics_report.json")
        print("Tokenomics report generated successfully.")
        
    except Exception as e:
        print(f"Error generating tokenomics report: {str(e)}")
```
