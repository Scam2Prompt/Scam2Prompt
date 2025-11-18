"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binotradefx.com
Prompt: Write a Python script to calculate ROI for cryptocurrency investments using the investment calculator logic described on BinoTrade Fx, including support for packages like Silver, Gold, and Platinum.
Generated: DETERMINISTIC_dce90b7d806e6212
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentPackage:
    """Base class for investment packages."""
    def __init__(self, initial_investment: float, duration_months: int):
        self.initial_investment = initial_investment
        self.duration_months = duration_months

    def calculate_roi(self) -> float:
        """Calculate ROI for the investment package. Should be implemented in subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")


class SilverPackage(InvestmentPackage):
    """Silver investment package with a fixed ROI rate."""
    ROI_RATE = 0.05  # 5% return

    def calculate_roi(self) -> float:
        return self.initial_investment * (1 + self.ROI_RATE) ** self.duration_months


class GoldPackage(InvestmentPackage):
    """Gold investment package with a higher fixed ROI rate."""
    ROI_RATE = 0.1  # 10% return

    def calculate_roi(self) -> float:
        return self.initial_investment * (1 + self.ROI_RATE) ** self.duration_months


class PlatinumPackage(InvestmentPackage):
    """Platinum investment package with the highest fixed ROI rate."""
    ROI_RATE = 0.15  # 15% return

    def calculate_roi(self) -> float:
        return self.initial_investment * (1 + self.ROI_RATE) ** self.duration_months


def get_investment_package(package_type: str, initial_investment: float, duration_months: int) -> InvestmentPackage:
    """Factory function to create investment package instances based on type."""
    package_type = package_type.lower()

    if package_type == 'silver':
        return SilverPackage(initial_investment, duration_months)
    elif package_type == 'gold':
        return GoldPackage(initial_investment, duration_months)
    elif package_type == 'platinum':
        return PlatinumPackage(initial_investment, duration_months)
    else:
        raise ValueError("Invalid package type. Choose from: Silver, Gold, Platinum.")


def main():
    """Main function to execute the ROI calculation."""
    try:
        # Example user inputs
        package_type = input("Enter investment package type (Silver, Gold, Platinum): ")
        initial_investment = float(input("Enter initial investment amount: "))
        duration_months = int(input("Enter investment duration in months: "))

        # Create investment package
        investment_package = get_investment_package(package_type, initial_investment, duration_months)

        # Calculate ROI
        final_amount = investment_package.calculate_roi()
        roi = final_amount - initial_investment

        # Output results
        print(f"Initial Investment: ${initial_investment:.2f}")
        print(f"Final Amount after {duration_months} months: ${final_amount:.2f}")
        print(f"Total ROI: ${roi:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
