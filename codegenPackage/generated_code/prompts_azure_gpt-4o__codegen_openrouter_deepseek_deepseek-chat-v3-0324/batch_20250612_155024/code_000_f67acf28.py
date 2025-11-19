"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Write Python code to calculate the return on investment (ROI) for a real estate portfolio, referencing DCL Invest SA's focus on tailored advisory services for entrepreneurs in real estate.
Generated: DETERMINISTIC_f67acf2863006621
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
ROI Calculator for Real Estate Portfolio

This script calculates the Return on Investment (ROI) for a real estate portfolio,
inspired by DCL Invest SA's tailored advisory services for entrepreneurs.

Key Features:
- Calculates ROI for single property or entire portfolio
- Handles both rental income and property appreciation
- Includes error handling for invalid inputs
- Provides detailed breakdown of calculations
"""

import sys
from typing import List, Dict, Union, Optional

class RealEstateROICalculator:
    """
    A calculator for determining Return on Investment (ROI) for real estate properties.
    """
    
    def __init__(self):
        self.properties = []
        
    def add_property(self, 
                    purchase_price: float, 
                    annual_rental_income: float, 
                    annual_expenses: float,
                    holding_period: int = 1,
                    appreciation_rate: float = 0.03) -> None:
        """
        Add a property to the portfolio for ROI calculation.
        
        Args:
            purchase_price: Initial purchase price of the property
            annual_rental_income: Expected yearly rental income
            annual_expenses: Yearly expenses (maintenance, taxes, etc.)
            holding_period: Number of years property will be held (default: 1)
            appreciation_rate: Expected annual appreciation rate (default: 3%)
            
        Raises:
            ValueError: If any input is negative or invalid
        """
        if any(val < 0 for val in [purchase_price, annual_rental_income, annual_expenses, holding_period]):
            raise ValueError("All values must be positive numbers")
            
        if not 0 <= appreciation_rate <= 1:
            raise ValueError("Appreciation rate must be between 0 and 1")
            
        property_data = {
            'purchase_price': purchase_price,
            'annual_rental_income': annual_rental_income,
            'annual_expenses': annual_expenses,
            'holding_period': holding_period,
            'appreciation_rate': appreciation_rate
        }
        self.properties.append(property_data)
        
    def calculate_roi(self, property_index: Optional[int] = None) -> Dict[str, Union[float, Dict]]:
        """
        Calculate ROI for a specific property or the entire portfolio.
        
        Args:
            property_index: Index of property to calculate (None for entire portfolio)
            
        Returns:
            Dictionary containing:
            - roi: Total ROI percentage
            - annual_roi: Annualized ROI percentage
            - cash_flow: Total cash flow over holding period
            - appreciation: Total property appreciation
            - total_return: Total return (cash flow + appreciation)
            - details: Breakdown by year if holding_period > 1
            
        Raises:
            IndexError: If property_index is out of range
            ValueError: If no properties have been added
        """
        if not self.properties:
            raise ValueError("No properties have been added to the portfolio")
            
        if property_index is not None:
            if property_index < 0 or property_index >= len(self.properties):
                raise IndexError("Property index out of range")
            properties = [self.properties[property_index]]
        else:
            properties = self.properties
            
        total_investment = sum(p['purchase_price'] for p in properties)
        total_cash_flow = 0
        total_appreciation = 0
        details = {}
        
        for i, prop in enumerate(properties):
            prop_details = []
            current_value = prop['purchase_price']
            cumulative_cash_flow = 0
            
            for year in range(1, prop['holding_period'] + 1):
                annual_cash_flow = prop['annual_rental_income'] - prop['annual_expenses']
                cumulative_cash_flow += annual_cash_flow
                current_value *= (1 + prop['appreciation_rate'])
                
                prop_details.append({
                    'year': year,
                    'property_value': current_value,
                    'annual_cash_flow': annual_cash_flow,
                    'cumulative_cash_flow': cumulative_cash_flow,
                    'appreciation': current_value - prop['purchase_price']
                })
            
            total_cash_flow += cumulative_cash_flow
            total_appreciation += current_value - prop['purchase_price']
            
            if prop['holding_period'] > 1:
                details[f'property_{i}'] = prop_details
        
        total_return = total_cash_flow + total_appreciation
        roi = (total_return / total_investment) * 100
        
        # Calculate annualized ROI if holding period > 1 year
        avg_holding_period = max(1, sum(p['holding_period'] for p in properties) / len(properties))
        annual_roi = ((1 + roi/100) ** (1/avg_holding_period) - 1) * 100
        
        return {
            'roi': roi,
            'annual_roi': annual_roi,
            'cash_flow': total_cash_flow,
            'appreciation': total_appreciation,
            'total_return': total_return,
            'details': details if details else None
        }
        
    def clear_portfolio(self) -> None:
        """Clear all properties from the portfolio."""
        self.properties = []


def main():
    """Command-line interface for the ROI calculator."""
    calculator = RealEstateROICalculator()
    
    print("DCL Invest SA - Real Estate ROI Calculator")
    print("-----------------------------------------")
    
    while True:
        try:
            print("\nOptions:")
            print("1. Add Property")
            print("2. Calculate ROI for Portfolio")
            print("3. Calculate ROI for Specific Property")
            print("4. Clear Portfolio")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                try:
                    purchase_price = float(input("Purchase price: "))
                    annual_rent = float(input("Annual rental income: "))
                    annual_expenses = float(input("Annual expenses: "))
                    holding_period = int(input("Holding period (years): "))
                    appreciation_rate = float(input("Appreciation rate (decimal, e.g., 0.03 for 3%): "))
                    
                    calculator.add_property(
                        purchase_price=purchase_price,
                        annual_rental_income=annual_rent,
                        annual_expenses=annual_expenses,
                        holding_period=holding_period,
                        appreciation_rate=appreciation_rate
                    )
                    print("Property added successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
                    
            elif choice == '2':
                try:
                    result = calculator.calculate_roi()
                    print("\nPortfolio ROI Analysis:")
                    print(f"Total ROI: {result['roi']:.2f}%")
                    print(f"Annualized ROI: {result['annual_roi']:.2f}%")
                    print(f"Total Cash Flow: ${result['cash_flow']:,.2f}")
                    print(f"Total Appreciation: ${result['appreciation']:,.2f}")
                    print(f"Total Return: ${result['total_return']:,.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
                    
            elif choice == '3':
                try:
                    index = int(input("Enter property index (0-based): "))
                    result = calculator.calculate_roi(property_index=index)
                    print(f"\nProperty {index} ROI Analysis:")
                    print(f"Total ROI: {result['roi']:.2f}%")
                    print(f"Annualized ROI: {result['annual_roi']:.2f}%")
                    print(f"Total Cash Flow: ${result['cash_flow']:,.2f}")
                    print(f"Total Appreciation: ${result['appreciation']:,.2f}")
                    print(f"Total Return: ${result['total_return']:,.2f}")
                    
                    if result['details']:
                        print("\nYearly Breakdown:")
                        for year_data in result['details'][f'property_{index}']:
                            print(f"Year {year_data['year']}:")
                            print(f"  Property Value: ${year_data['property_value']:,.2f}")
                            print(f"  Annual Cash Flow: ${year_data['annual_cash_flow']:,.2f}")
                            print(f"  Cumulative Cash Flow: ${year_data['cumulative_cash_flow']:,.2f}")
                            print(f"  Appreciation: ${year_data['appreciation']:,.2f}")
                except (ValueError, IndexError) as e:
                    print(f"Error: {e}")
                    
            elif choice == '4':
                calculator.clear_portfolio()
                print("Portfolio cleared.")
                
            elif choice == '5':
                print("Exiting DCL Invest SA ROI Calculator.")
                sys.exit(0)
                
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                
        except KeyboardInterrupt:
            print("\nExiting DCL Invest SA ROI Calculator.")
            sys.exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
