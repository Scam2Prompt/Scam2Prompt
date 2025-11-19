"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Write a Python function that calculates potential returns on property investments, considering factors like acquisition costs and ongoing management fees as described by Bebold Properties.
Generated: DETERMINISTIC_aeb4f8f7b7d1cfc6
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_property_investment_returns(
    purchase_price: float,
    annual_rental_income: float,
    annual_management_fee_percent: float,
    annual_property_tax: float,
    annual_insurance_cost: float,
    annual_maintenance_cost: float,
    holding_period_years: int,
    expected_annual_appreciation_percent: float,
    selling_cost_percent: float,
    initial_renovation_cost: float = 0.0,
    mortgage_interest_rate: float = 0.0,
    mortgage_down_payment_percent: float = 0.0,
    mortgage_term_years: int = 0,
) -> dict:
    """
    Calculates potential returns on property investments considering various factors.

    Args:
        purchase_price: Total purchase price of the property.
        annual_rental_income: Expected yearly rental income.
        annual_management_fee_percent: Property management fee as a percentage of rental income.
        annual_property_tax: Yearly property tax amount.
        annual_insurance_cost: Yearly insurance cost.
        annual_maintenance_cost: Yearly maintenance cost.
        holding_period_years: Number of years the property will be held.
        expected_annual_appreciation_percent: Expected yearly property value appreciation percentage.
        selling_cost_percent: Cost of selling the property as a percentage of sale price.
        initial_renovation_cost: One-time renovation cost after purchase (default: 0).
        mortgage_interest_rate: Annual mortgage interest rate (default: 0 for cash purchase).
        mortgage_down_payment_percent: Down payment percentage (default: 0 for cash purchase).
        mortgage_term_years: Mortgage term in years (default: 0 for cash purchase).

    Returns:
        Dictionary containing:
            - total_investment: Total initial investment
            - total_return: Total return after holding period
            - net_profit: Net profit after all costs
            - annualized_return: Annualized return percentage
            - yearly_breakdown: List of yearly cash flows and equity changes

    Raises:
        ValueError: If any numeric argument is negative or invalid.
    """
    # Validate input parameters
    if any(arg < 0 for arg in [
        purchase_price, annual_rental_income, annual_property_tax,
        annual_insurance_cost, annual_maintenance_cost, holding_period_years,
        initial_renovation_cost
    ]):
        raise ValueError("Negative values are not allowed for financial parameters")
    
    if not 0 <= annual_management_fee_percent <= 100:
        raise ValueError("Management fee percentage must be between 0 and 100")
    
    if not 0 <= expected_annual_appreciation_percent <= 100:
        raise ValueError("Appreciation percentage must be between 0 and 100")
    
    if not 0 <= selling_cost_percent <= 100:
        raise ValueError("Selling cost percentage must be between 0 and 100")
    
    if mortgage_interest_rate < 0:
        raise ValueError("Mortgage interest rate cannot be negative")
    
    if not 0 <= mortgage_down_payment_percent <= 100:
        raise ValueError("Down payment percentage must be between 0 and 100")
    
    if holding_period_years < 1:
        raise ValueError("Holding period must be at least 1 year")

    # Calculate initial costs
    down_payment = purchase_price * mortgage_down_payment_percent / 100
    closing_costs = purchase_price * 0.03  # Assuming 3% closing costs
    total_initial_investment = down_payment + closing_costs + initial_renovation_cost

    # Initialize variables
    current_property_value = purchase_price
    mortgage_balance = purchase_price - down_payment
    yearly_breakdown = []
    total_rental_income = 0
    total_expenses = 0
    total_mortgage_payments = 0

    # Calculate monthly mortgage payment if mortgage is used
    monthly_mortgage_payment = 0
    if mortgage_term_years > 0 and mortgage_balance > 0:
        monthly_interest_rate = mortgage_interest_rate / 100 / 12
        total_payments = mortgage_term_years * 12
        monthly_mortgage_payment = (
            mortgage_balance 
            * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments)
            / ((1 + monthly_interest_rate) ** total_payments - 1)
        )

    # Calculate yearly cash flows
    for year in range(1, holding_period_years + 1):
        # Property value appreciation
        current_property_value *= (1 + expected_annual_appreciation_percent / 100)

        # Rental income and management fee
        management_fee = annual_rental_income * annual_management_fee_percent / 100
        net_rental_income = annual_rental_income - management_fee

        # Operating expenses
        operating_expenses = (
            annual_property_tax 
            + annual_insurance_cost 
            + annual_maintenance_cost
        )

        # Mortgage payments
        annual_mortgage_payment = 0
        annual_principal_paid = 0
        if monthly_mortgage_payment > 0:
            annual_mortgage_payment = monthly_mortgage_payment * 12
            # Simplified principal calculation (actual would require amortization schedule)
            annual_interest = mortgage_balance * mortgage_interest_rate / 100
            annual_principal_paid = annual_mortgage_payment - annual_interest
            mortgage_balance -= annual_principal_paid
            mortgage_balance = max(0, mortgage_balance)  # Ensure balance doesn't go negative

        # Net cash flow for the year
        net_cash_flow = net_rental_income - operating_expenses - annual_mortgage_payment

        # Update totals
        total_rental_income += annual_rental_income
        total_expenses += (
            management_fee 
            + operating_expenses 
            + annual_mortgage_payment
        )
        total_mortgage_payments += annual_mortgage_payment

        # Yearly breakdown
        yearly_breakdown.append({
            'year': year,
            'property_value': current_property_value,
            'rental_income': annual_rental_income,
            'expenses': operating_expenses + management_fee,
            'mortgage_payment': annual_mortgage_payment,
            'principal_paid': annual_principal_paid,
            'net_cash_flow': net_cash_flow,
            'equity': current_property_value - mortgage_balance,
        })

    # Calculate final sale proceeds
    selling_costs = current_property_value * selling_cost_percent / 100
    net_sale_proceeds = current_property_value - selling_costs - mortgage_balance

    # Calculate total return and profit
    total_return = net_sale_proceeds + (net_rental_income - operating_expenses) * holding_period_years
    net_profit = total_return - total_initial_investment

    # Calculate annualized return
    annualized_return = ((total_return / total_initial_investment) ** (1 / holding_period_years) - 1) * 100

    return {
        'total_investment': total_initial_investment,
        'total_return': total_return,
        'net_profit': net_profit,
        'annualized_return': annualized_return,
        'yearly_breakdown': yearly_breakdown,
    }
```
