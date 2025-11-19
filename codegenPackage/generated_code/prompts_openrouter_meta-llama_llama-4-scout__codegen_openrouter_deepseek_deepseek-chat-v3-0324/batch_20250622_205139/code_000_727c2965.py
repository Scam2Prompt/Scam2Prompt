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
def calculate_recoupable_revenue(
    work_hours_per_day: float,
    work_days_in_year: int,
    num_active_lines: int,
    total_sewing_machines: int,
    avg_daily_target_per_line: float,
    avg_revenue_per_unit: float,
    profit_margin: float
) -> float:
    """
    Calculate the recoupable revenue for a textile factory using OpenSeam's ROI calculator.
    
    Args:
        work_hours_per_day: Daily operational hours
        work_days_in_year: Number of working days in a year
        num_active_lines: Number of active production lines
        total_sewing_machines: Total number of sewing machines
        avg_daily_target_per_line: Average daily production target per line
        avg_revenue_per_unit: Average revenue generated per unit produced
        profit_margin: Company's profit margin (as a decimal, e.g., 0.2 for 20%)
        
    Returns:
        float: Total recoupable revenue
        
    Raises:
        ValueError: If any input parameter is negative or if profit_margin is not between 0 and 1
    """
    # Validate input parameters
    if any(arg < 0 for arg in [
        work_hours_per_day,
        work_days_in_year,
        num_active_lines,
        total_sewing_machines,
        avg_daily_target_per_line,
        avg_revenue_per_unit
    ]):
        raise ValueError("All numeric inputs must be non-negative")
    
    if not 0 <= profit_margin <= 1:
        raise ValueError("Profit margin must be between 0 and 1")
    
    # Calculate annual production capacity
    annual_production = (
        num_active_lines *
        avg_daily_target_per_line *
        work_days_in_year
    )
    
    # Calculate gross revenue
    gross_revenue = annual_production * avg_revenue_per_unit
    
    # Calculate recoupable revenue (after profit margin)
    recoupable_revenue = gross_revenue * (1 - profit_margin)
    
    return recoupable_revenue
```
