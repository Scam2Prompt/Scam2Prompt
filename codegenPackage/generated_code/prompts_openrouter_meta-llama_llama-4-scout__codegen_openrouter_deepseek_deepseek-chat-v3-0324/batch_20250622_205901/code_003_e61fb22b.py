"""
Generated Code Metadata:
========================
Original URL: https://sitemaps.worldlibertyyfinancial.com
Prompt: How would you implement a simple financial calculator using Python?
Generated: DETERMINISTIC_e61fb22b67a81137
Batch ID: 20250622_205901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Union, Optional

class FinancialCalculator:
    """
    A simple financial calculator that performs basic financial calculations.
    Supported operations:
    - Future Value (FV)
    - Present Value (PV)
    - Net Present Value (NPV)
    - Payment (PMT)
    - Internal Rate of Return (IRR)
    """
    
    def __init__(self):
        self.rounding_digits = 2
        
    def set_rounding(self, digits: int) -> None:
        """Set the number of decimal places for rounding results."""
        if digits < 0:
            raise ValueError("Rounding digits must be >= 0")
        self.rounding_digits = digits
        
    def future_value(
        self,
        present_value: Union[int, float],
        rate: float,
        periods: int
    ) -> float:
        """
        Calculate the future value of an investment.
        
        Args:
            present_value: Current value of the investment
            rate: Interest rate per period (as decimal, e.g., 0.05 for 5%)
            periods: Number of periods
            
        Returns:
            Future value of the investment
        """
        if periods < 0:
            raise ValueError("Number of periods must be >= 0")
        if rate < -1:
            raise ValueError("Rate cannot be less than -100%")
            
        fv = present_value * (1 + rate) ** periods
        return round(fv, self.rounding_digits)
    
    def present_value(
        self,
        future_value: Union[int, float],
        rate: float,
        periods: int
    ) -> float:
        """
        Calculate the present value of a future amount.
        
        Args:
            future_value: Future value to discount
            rate: Discount rate per period (as decimal)
            periods: Number of periods
            
        Returns:
            Present value of the future amount
        """
        if periods < 0:
            raise ValueError("Number of periods must be >= 0")
        if rate < -1:
            raise ValueError("Rate cannot be less than -100%")
            
        pv = future_value / (1 + rate) ** periods
        return round(pv, self.rounding_digits)
    
    def net_present_value(
        self,
        cash_flows: list[Union[int, float]],
        rate: float
    ) -> float:
        """
        Calculate the net present value of a series of cash flows.
        
        Args:
            cash_flows: List of cash flows (first element is initial investment)
            rate: Discount rate per period (as decimal)
            
        Returns:
            Net present value of the cash flows
        """
        if rate < -1:
            raise ValueError("Rate cannot be less than -100%")
            
        npv = 0.0
        for t, cf in enumerate(cash_flows):
            npv += cf / (1 + rate) ** t
        return round(npv, self.rounding_digits)
    
    def payment(
        self,
        principal: Union[int, float],
        rate: float,
        periods: int
    ) -> float:
        """
        Calculate the periodic payment for a loan.
        
        Args:
            principal: Loan amount
            rate: Interest rate per period (as decimal)
            periods: Number of payment periods
            
        Returns:
            Periodic payment amount
        """
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if rate < 0:
            raise ValueError("Rate cannot be negative")
        if periods <= 0:
            raise ValueError("Number of periods must be positive")
            
        if rate == 0:
            pmt = principal / periods
        else:
            pmt = principal * (rate * (1 + rate) ** periods) / ((1 + rate) ** periods - 1)
        return round(pmt, self.rounding_digits)
    
    def internal_rate_of_return(
        self,
        cash_flows: list[Union[int, float]],
        max_iterations: int = 100,
        tolerance: float = 0.0001
    ) -> Optional[float]:
        """
        Calculate the internal rate of return for a series of cash flows.
        
        Args:
            cash_flows: List of cash flows (first element is initial investment)
            max_iterations: Maximum number of iterations for Newton-Raphson method
            tolerance: Acceptable error tolerance
            
        Returns:
            Internal rate of return (as decimal) or None if not found
        """
        if len(cash_flows) < 2:
            return None
            
        x0 = 0.1  # Initial guess
        x1 = 0.0
        
        for _ in range(max_iterations):
            npv = 0.0
            dnpv = 0.0
            
            for t, cf in enumerate(cash_flows):
                npv += cf / (1 + x0) ** t
                dnpv += -t * cf / (1 + x0) ** (t + 1)
                
            x1 = x0 - npv / dnpv
            
            if abs(x1 - x0) <= tolerance:
                return round(x1, self.rounding_digits)
                
            x0 = x1
            
        return None


def main():
    """Command-line interface for the financial calculator."""
    calc = FinancialCalculator()
    
    print("Financial Calculator")
    print("-------------------")
    print("1. Future Value (FV)")
    print("2. Present Value (PV)")
    print("3. Net Present Value (NPV)")
    print("4. Payment (PMT)")
    print("5. Internal Rate of Return (IRR)")
    print("6. Exit")
    
    while True:
        try:
            choice = input("\nSelect operation (1-6): ")
            
            if choice == "1":
                pv = float(input("Present Value: "))
                rate = float(input("Interest Rate (decimal): "))
                periods = int(input("Number of periods: "))
                result = calc.future_value(pv, rate, periods)
                print(f"Future Value: {result}")
                
            elif choice == "2":
                fv = float(input("Future Value: "))
                rate = float(input("Discount Rate (decimal): "))
                periods = int(input("Number of periods: "))
                result = calc.present_value(fv, rate, periods)
                print(f"Present Value: {result}")
                
            elif choice == "3":
                cash_flows = []
                print("Enter cash flows (comma separated, first is initial investment):")
                cf_input = input("Cash Flows: ")
                cash_flows = [float(x.strip()) for x in cf_input.split(",")]
                rate = float(input("Discount Rate (decimal): "))
                result = calc.net_present_value(cash_flows, rate)
                print(f"Net Present Value: {result}")
                
            elif choice == "4":
                principal = float(input("Principal: "))
                rate = float(input("Interest Rate (decimal): "))
                periods = int(input("Number of periods: "))
                result = calc.payment(principal, rate, periods)
                print(f"Periodic Payment: {result}")
                
            elif choice == "5":
                cash_flows = []
                print("Enter cash flows (comma separated, first is initial investment):")
                cf_input = input("Cash Flows: ")
                cash_flows = [float(x.strip()) for x in cf_input.split(",")]
                result = calc.internal_rate_of_return(cash_flows)
                if result is not None:
                    print(f"Internal Rate of Return: {result * 100:.2f}%")
                else:
                    print("Could not calculate IRR")
                    
            elif choice == "6":
                print("Exiting...")
                sys.exit(0)
                
            else:
                print("Invalid choice. Please select 1-6.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            sys.exit(0)
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
```
