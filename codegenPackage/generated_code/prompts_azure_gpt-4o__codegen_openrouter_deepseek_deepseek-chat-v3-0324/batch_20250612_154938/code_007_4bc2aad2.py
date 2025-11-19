"""
Generated Code Metadata:
========================
Original URL: https://maya-finance.com
Prompt: Generate Python code to calculate the leverage effect for investment loans using Maya Finance's "Prêt Investissement" strategy, factoring in interest rates and repayment terms.
Generated: DETERMINISTIC_4bc2aad268ff9b61
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Optional, Tuple

class LeverageCalculator:
    """
    A class to calculate the leverage effect for investment loans using Maya Finance's "Prêt Investissement" strategy.
    
    Attributes:
        principal (float): The initial loan amount (principal).
        annual_interest_rate (float): The annual interest rate (in percentage).
        loan_term_years (int): The loan term in years.
        investment_return_rate (float): The expected annual return rate on investment (in percentage).
    """
    
    def __init__(
        self,
        principal: float,
        annual_interest_rate: float,
        loan_term_years: int,
        investment_return_rate: float
    ):
        """
        Initialize the LeverageCalculator with loan and investment parameters.
        
        Args:
            principal: The initial loan amount (principal).
            annual_interest_rate: The annual interest rate (in percentage).
            loan_term_years: The loan term in years.
            investment_return_rate: The expected annual return rate on investment (in percentage).
            
        Raises:
            ValueError: If any of the parameters are invalid (negative values, etc.).
        """
        if principal <= 0:
            raise ValueError("Principal must be a positive number.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if loan_term_years <= 0:
            raise ValueError("Loan term must be a positive number of years.")
        if investment_return_rate < 0:
            raise ValueError("Investment return rate cannot be negative.")
            
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_years = loan_term_years
        self.investment_return_rate = investment_return_rate
        
    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly loan payment using the standard annuity formula.
        
        Returns:
            The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        num_payments = self.loan_term_years * 12
        
        if monthly_interest_rate == 0:  # Handle 0% interest case
            return self.principal / num_payments
            
        monthly_payment = (
            self.principal 
            * monthly_interest_rate 
            * math.pow(1 + monthly_interest_rate, num_payments)
        ) / (math.pow(1 + monthly_interest_rate, num_payments) - 1)
        
        return monthly_payment
        
    def calculate_total_loan_cost(self) -> float:
        """
        Calculate the total cost of the loan over its term.
        
        Returns:
            The total amount paid over the loan term.
        """
        monthly_payment = self.calculate_monthly_payment()
        return monthly_payment * self.loan_term_years * 12
        
    def calculate_investment_value(self) -> float:
        """
        Calculate the future value of the invested principal.
        
        Returns:
            The future value of the investment after the loan term.
        """
        annual_return_rate = self.investment_return_rate / 100
        return self.principal * math.pow(1 + annual_return_rate, self.loan_term_years)
        
    def calculate_leverage_effect(self) -> Tuple[float, float, float]:
        """
        Calculate the leverage effect by comparing investment growth to loan cost.
        
        Returns:
            A tuple containing:
            - net_profit: The net profit after paying off the loan
            - roi: Return on investment (percentage)
            - leverage_multiplier: How much the return was multiplied by leverage
        """
        total_loan_cost = self.calculate_total_loan_cost()
        investment_value = self.calculate_investment_value()
        
        net_profit = investment_value - total_loan_cost
        roi = ((investment_value - total_loan_cost) / self.principal) * 100
        
        # Calculate what the return would have been without leverage
        unleveraged_return = self.principal * math.pow(
            1 + (self.investment_return_rate / 100), 
            self.loan_term_years
        ) - self.principal
        
        if unleveraged_return == 0:
            leverage_multiplier = 0
        else:
            leverage_multiplier = net_profit / unleveraged_return if unleveraged_return != 0 else 0
        
        return net_profit, roi, leverage_multiplier
        
    def generate_amortization_schedule(self) -> list:
        """
        Generate an amortization schedule for the loan.
        
        Returns:
            A list of dictionaries, each representing a monthly payment with:
            - month: The month number
            - payment: The monthly payment amount
            - principal: The principal portion of the payment
            - interest: The interest portion of the payment
            - remaining_balance: The remaining loan balance
        """
        monthly_payment = self.calculate_monthly_payment()
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        balance = self.principal
        schedule = []
        
        for month in range(1, self.loan_term_years * 12 + 1):
            if monthly_interest_rate == 0:  # Handle 0% interest case
                interest_payment = 0
                principal_payment = monthly_payment
            else:
                interest_payment = balance * monthly_interest_rate
                principal_payment = monthly_payment - interest_payment
                
            balance -= principal_payment
            
            # Handle potential floating point rounding errors
            if month == self.loan_term_years * 12:
                principal_payment += balance
                balance = 0
                
            schedule.append({
                'month': month,
                'payment': monthly_payment,
                'principal': principal_payment,
                'interest': interest_payment,
                'remaining_balance': max(0, balance)  # Ensure balance doesn't go negative
            })
            
        return schedule


# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        calculator = LeverageCalculator(
            principal=200000,
            annual_interest_rate=3.5,
            loan_term_years=20,
            investment_return_rate=6.0
        )
        
        # Calculate key metrics
        monthly_payment = calculator.calculate_monthly_payment()
        total_loan_cost = calculator.calculate_total_loan_cost()
        investment_value = calculator.calculate_investment_value()
        net_profit, roi, leverage_multiplier = calculator.calculate_leverage_effect()
        
        # Print results
        print(f"Monthly Payment: €{monthly_payment:.2f}")
        print(f"Total Loan Cost: €{total_loan_cost:.2f}")
        print(f"Investment Value after {calculator.loan_term_years} years: €{investment_value:.2f}")
        print(f"Net Profit: €{net_profit:.2f}")
        print(f"ROI: {roi:.2f}%")
        print(f"Leverage Multiplier: {leverage_multiplier:.2f}x")
        
        # Generate and display first 12 months of amortization schedule
        print("\nAmortization Schedule (first 12 months):")
        schedule = calculator.generate_amortization_schedule()
        for month in schedule[:12]:
            print(f"Month {month['month']}: Payment €{month['payment']:.2f} "
                  f"(Principal €{month['principal']:.2f}, Interest €{month['interest']:.2f}) "
                  f"Balance €{month['remaining_balance']:.2f}")
                  
    except ValueError as e:
        print(f"Error: {e}")
```
