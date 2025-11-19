"""
Generated Code Metadata:
========================
Original URL: https://minebnb.pro
Prompt: Write a Python script that calculates the total earnings from multiple deposits across different tariff plans on MineBNB, factoring in daily rates and durations.
Generated: DETERMINISTIC_8081137ec1e3749a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Union

class TariffPlan:
    """Represents a tariff plan with its daily rate and name."""
    
    def __init__(self, name: str, daily_rate: float):
        """
        Initialize a TariffPlan instance.
        
        Args:
            name: Name of the tariff plan.
            daily_rate: Daily earnings rate for the plan.
        """
        self.name = name
        self.daily_rate = daily_rate

class Deposit:
    """Represents a deposit with its amount, tariff plan, and duration."""
    
    def __init__(self, amount: float, tariff_plan: TariffPlan, start_date: str, end_date: str):
        """
        Initialize a Deposit instance.
        
        Args:
            amount: Deposit amount.
            tariff_plan: Associated tariff plan.
            start_date: Start date in 'YYYY-MM-DD' format.
            end_date: End date in 'YYYY-MM-DD' format.
        """
        self.amount = amount
        self.tariff_plan = tariff_plan
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        
    def calculate_earnings(self) -> float:
        """
        Calculate earnings for the deposit based on duration and daily rate.
        
        Returns:
            Total earnings for the deposit.
        """
        duration_days = (self.end_date - self.start_date).days + 1
        return self.amount * self.tariff_plan.daily_rate * duration_days

class MineBNBEarningsCalculator:
    """Calculates total earnings from multiple deposits across different tariff plans."""
    
    def __init__(self, tariff_plans: Dict[str, TariffPlan]):
        """
        Initialize the calculator with available tariff plans.
        
        Args:
            tariff_plans: Dictionary of tariff plan names to TariffPlan objects.
        """
        self.tariff_plans = tariff_plans
        self.deposits: List[Deposit] = []
    
    def add_deposit(self, amount: float, tariff_plan_name: str, start_date: str, end_date: str) -> None:
        """
        Add a deposit to the calculator.
        
        Args:
            amount: Deposit amount.
            tariff_plan_name: Name of the tariff plan.
            start_date: Start date in 'YYYY-MM-DD' format.
            end_date: End date in 'YYYY-MM-DD' format.
            
        Raises:
            ValueError: If tariff plan is not found or dates are invalid.
        """
        if tariff_plan_name not in self.tariff_plans:
            raise ValueError(f"Tariff plan '{tariff_plan_name}' not found")
        
        try:
            tariff_plan = self.tariff_plans[tariff_plan_name]
            deposit = Deposit(amount, tariff_plan, start_date, end_date)
            if deposit.end_date < deposit.start_date:
                raise ValueError("End date cannot be before start date")
            self.deposits.append(deposit)
        except ValueError as e:
            raise ValueError(f"Invalid date format or values: {e}")
    
    def calculate_total_earnings(self) -> float:
        """
        Calculate total earnings across all deposits.
        
        Returns:
            Total earnings from all deposits.
        """
        return sum(deposit.calculate_earnings() for deposit in self.deposits)
    
    @classmethod
    def from_config_file(cls, config_path: str) -> 'MineBNBEarningsCalculator':
        """
        Create a calculator instance from a JSON config file.
        
        Args:
            config_path: Path to the JSON config file.
            
        Returns:
            MineBNBEarningsCalculator instance.
            
        Raises:
            FileNotFoundError: If config file is not found.
            json.JSONDecodeError: If config file is not valid JSON.
            ValueError: If config data is invalid.
        """
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            
            if 'tariff_plans' not in config:
                raise ValueError("Config file must contain 'tariff_plans' section")
            
            tariff_plans = {}
            for plan_name, plan_data in config['tariff_plans'].items():
                if 'daily_rate' not in plan_data:
                    raise ValueError(f"Tariff plan '{plan_name}' missing 'daily_rate'")
                tariff_plans[plan_name] = TariffPlan(plan_name, plan_data['daily_rate'])
            
            return cls(tariff_plans)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found at {config_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in config file")

def main():
    """Example usage of the MineBNB earnings calculator."""
    try:
        # Example with programmatic setup
        tariff_plans = {
            "Basic": TariffPlan("Basic", 0.05),
            "Premium": TariffPlan("Premium", 0.08),
            "VIP": TariffPlan("VIP", 0.12)
        }
        
        calculator = MineBNBEarningsCalculator(tariff_plans)
        
        # Add deposits
        calculator.add_deposit(1000.0, "Basic", "2023-01-01", "2023-01-31")
        calculator.add_deposit(5000.0, "Premium", "2023-01-15", "2023-02-14")
        calculator.add_deposit(2000.0, "VIP", "2023-02-01", "2023-02-28")
        
        total_earnings = calculator.calculate_total_earnings()
        print(f"Total earnings: ${total_earnings:.2f}")
        
        # Example with config file
        # calculator = MineBNBEarningsCalculator.from_config_file("config.json")
        # total_earnings = calculator.calculate_total_earnings()
        # print(f"Total earnings: ${total_earnings:.2f}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
