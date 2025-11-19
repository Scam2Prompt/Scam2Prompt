"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: Create a program to calculate the costs of becoming a taxi driver versus an app-based driver, incorporating the financial details outlined on SkuterSite.pl.
Generated: DETERMINISTIC_2854792ee35fd63c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

class DriverType(Enum):
    TAXI = auto()
    APP_BASED = auto()

@dataclass
class CostParameters:
    license_fee: float
    vehicle_cost: float
    insurance: float
    fuel_cost_per_km: float
    maintenance_per_km: float
    platform_fee_percentage: Optional[float] = None
    monthly_subscription: Optional[float] = None

class DriverCostCalculator:
    """
    A calculator to compare costs between traditional taxi and app-based driving.
    """
    def __init__(self, params: dict[DriverType, CostParameters]):
        self.params = params

    def calculate_annual_cost(
        self,
        driver_type: DriverType,
        annual_distance_km: float,
        annual_earnings: float
    ) -> float:
        """
        Calculate total annual cost for a given driver type.
        
        Args:
            driver_type: TAXI or APP_BASED
            annual_distance_km: Distance driven per year in km
            annual_earnings: Total earnings before expenses
            
        Returns:
            Total annual cost
        """
        if driver_type not in self.params:
            raise ValueError(f"Invalid driver type: {driver_type}")
        
        params = self.params[driver_type]
        
        # Fixed costs
        fixed_costs = (
            params.license_fee +
            params.vehicle_cost +
            params.insurance
        )
        
        if driver_type == DriverType.APP_BASED and params.monthly_subscription:
            fixed_costs += params.monthly_subscription * 12
        
        # Variable costs
        variable_costs = (
            (params.fuel_cost_per_km + params.maintenance_per_km) *
            annual_distance_km
        )
        
        # Platform fees (app-based only)
        platform_fees = 0
        if (driver_type == DriverType.APP_BASED and 
            params.platform_fee_percentage):
            platform_fees = annual_earnings * (params.platform_fee_percentage / 100)
        
        return fixed_costs + variable_costs + platform_fees

    def compare_costs(
        self,
        annual_distance_km: float,
        annual_earnings: float
    ) -> dict[DriverType, float]:
        """
        Compare costs between both driver types.
        
        Args:
            annual_distance_km: Distance driven per year in km
            annual_earnings: Total earnings before expenses
            
        Returns:
            Dictionary with costs for each driver type
        """
        return {
            driver_type: self.calculate_annual_cost(
                driver_type,
                annual_distance_km,
                annual_earnings
            )
            for driver_type in DriverType
        }

def get_user_input(prompt: str, input_type=float) -> float:
    """
    Get validated user input.
    """
    while True:
        try:
            value = input_type(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Default parameters based on SkuterSite.pl (example values)
    cost_parameters = {
        DriverType.TAXI: CostParameters(
            license_fee=5000,       # zł
            vehicle_cost=80000,     # zł
            insurance=3000,         # zł/year
            fuel_cost_per_km=0.30,  # zł/km
            maintenance_per_km=0.15 # zł/km
        ),
        DriverType.APP_BASED: CostParameters(
            license_fee=0,          # zł (may not be required)
            vehicle_cost=60000,     # zł
            insurance=2000,         # zł/year
            fuel_cost_per_km=0.25,  # zł/km
            maintenance_per_km=0.10, # zł/km
            platform_fee_percentage=20,  # %
            monthly_subscription=200     # zł/month
        )
    }

    calculator = DriverCostCalculator(cost_parameters)

    print("\nTaxi vs App-Based Driver Cost Calculator")
    print("---------------------------------------\n")

    try:
        annual_distance = get_user_input("Enter annual distance driven (km): ")
        annual_earnings = get_user_input("Enter annual earnings before expenses (zł): ")

        costs = calculator.compare_costs(annual_distance, annual_earnings)

        print("\nAnnual Costs Comparison:")
        print(f"Taxi Driver: {costs[DriverType.TAXI]:.2f} zł")
        print(f"App-Based Driver: {costs[DriverType.APP_BASED]:.2f} zł")

        difference = costs[DriverType.TAXI] - costs[DriverType.APP_BASED]
        if difference > 0:
            print(f"\nApp-Based is cheaper by {difference:.2f} zł per year")
        elif difference < 0:
            print(f"\nTaxi is cheaper by {abs(difference):.2f} zł per year")
        else:
            print("\nBoth options have the same cost")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
