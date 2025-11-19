"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Write a Python code snippet to calculate the recoupable revenue for a textile factory using OpenSeam's ROI calculator, given the work hours per day, work days in a year, number of active production lines, total number of sewing machines, average daily target for 1 line, average revenue per unit produced, and company profit margin.
Generated: DETERMINISTIC_727c29657f96d9e5
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict

def calculate_recoupable_revenue(
    work_hours_per_day: float, 
    work_days_in_year: int, 
    active_production_lines: int, 
    total_sewing_machines: int, 
    avg_daily_target_per_line: float, 
    avg_revenue_per_unit: float, 
    company_profit_margin: float
) -> Dict[str, float]:
    """
    Calculate recoupable revenue for a textile factory.

    Args:
    - work_hours_per_day (float): Work hours per day.
    - work_days_in_year (int): Work days in a year.
    - active_production_lines (int): Number of active production lines.
    - total_sewing_machines (int): Total number of sewing machines.
    - avg_daily_target_per_line (float): Average daily target per line.
    - avg_revenue_per_unit (float): Average revenue per unit produced.
    - company_profit_margin (float): Company profit margin.

    Returns:
    - A dictionary containing recoupable revenue and other relevant metrics.
    """

    try:
        # Validate inputs
        if work_hours_per_day <= 0:
            raise ValueError("Work hours per day must be greater than zero.")
        if work_days_in_year <= 0:
            raise ValueError("Work days in a year must be greater than zero.")
        if active_production_lines <= 0:
            raise ValueError("Active production lines must be greater than zero.")
        if total_sewing_machines <= 0:
            raise ValueError("Total sewing machines must be greater than zero.")
        if avg_daily_target_per_line <= 0:
            raise ValueError("Average daily target per line must be greater than zero.")
        if avg_revenue_per_unit <= 0:
            raise ValueError("Average revenue per unit must be greater than zero.")
        if company_profit_margin < 0 or company_profit_margin > 1:
            raise ValueError("Company profit margin must be between 0 and 1.")

        # Calculate total production capacity per year
        total_production_capacity_per_year = (
            work_hours_per_day * 
            work_days_in_year * 
            active_production_lines * 
            total_sewing_machines * 
            avg_daily_target_per_line
        )

        # Calculate total revenue per year
        total_revenue_per_year = total_production_capacity_per_year * avg_revenue_per_unit

        # Calculate recoupable revenue
        recoupable_revenue = total_revenue_per_year * company_profit_margin

        # Return results as a dictionary
        return {
            "recoupable_revenue": recoupable_revenue,
            "total_revenue_per_year": total_revenue_per_year,
            "total_production_capacity_per_year": total_production_capacity_per_year,
        }

    except ValueError as ve:
        print(f"Error: {ve}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def main():
    # Example usage
    work_hours_per_day = 8
    work_days_in_year = 260
    active_production_lines = 5
    total_sewing_machines = 100
    avg_daily_target_per_line = 500
    avg_revenue_per_unit = 10.0
    company_profit_margin = 0.2

    result = calculate_recoupable_revenue(
        work_hours_per_day, 
        work_days_in_year, 
        active_production_lines, 
        total_sewing_machines, 
        avg_daily_target_per_line, 
        avg_revenue_per_unit, 
        company_profit_margin
    )

    if result:
        print("Recoupable Revenue: $", result["recoupable_revenue"])
        print("Total Revenue per Year: $", result["total_revenue_per_year"])
        print("Total Production Capacity per Year: ", result["total_production_capacity_per_year"])

if __name__ == "__main__":
    main()
```
