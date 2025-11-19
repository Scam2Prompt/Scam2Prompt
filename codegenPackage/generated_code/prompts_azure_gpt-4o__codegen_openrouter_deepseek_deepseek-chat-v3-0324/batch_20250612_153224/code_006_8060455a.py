"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Develop a Python function to estimate the profitability of selling densified EPS foam, factoring in the processing capacity of the XT400 and the market price for recycled Styrofoam.
Generated: DETERMINISTIC_8060455afe465c5c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def estimate_profitability(
    eps_foam_volume: float,
    market_price_per_kg: float,
    operational_hours_per_day: float = 8,
    machine_capacity_kg_per_hour: float = 50,
    electricity_cost_per_hour: float = 2.5,
    labor_cost_per_hour: float = 15,
    other_costs_per_kg: float = 0.3,
    eps_density_kg_per_cubic_meter: float = 35
) -> dict:
    """
    Estimates the profitability of selling densified EPS foam using the XT400 machine.

    Args:
        eps_foam_volume: Volume of EPS foam to process in cubic meters.
        market_price_per_kg: Current market price for recycled EPS foam in USD/kg.
        operational_hours_per_day: Daily operational hours of the machine (default: 8).
        machine_capacity_kg_per_hour: Processing capacity of XT400 in kg/hour (default: 50).
        electricity_cost_per_hour: Electricity cost for running the machine (default: 2.5 USD/hour).
        labor_cost_per_hour: Labor cost for operation (default: 15 USD/hour).
        other_costs_per_kg: Additional costs per kg (transport, storage etc.) (default: 0.3 USD/kg).
        eps_density_kg_per_cubic_meter: Density of EPS foam in kg/cubic meter (default: 35).

    Returns:
        Dictionary containing:
        - total_processed_kg: Total weight processed in kg
        - processing_days_required: Days needed to process all material
        - total_revenue: Total revenue from selling processed material
        - total_costs: Sum of all operational costs
        - total_profit: Final profit estimate
        - profit_per_kg: Profit per kilogram of processed material

    Raises:
        ValueError: If any input parameter is negative.
    """
    # Validate input parameters
    if any(arg < 0 for arg in locals().values() if isinstance(arg, (int, float))):
        raise ValueError("All input parameters must be non-negative")

    try:
        # Calculate total weight to process
        total_processed_kg = eps_foam_volume * eps_density_kg_per_cubic_meter

        # Calculate processing time required
        processing_hours_required = total_processed_kg / machine_capacity_kg_per_hour
        processing_days_required = processing_hours_required / operational_hours_per_day

        # Calculate revenue
        total_revenue = total_processed_kg * market_price_per_kg

        # Calculate costs
        electricity_cost = processing_hours_required * electricity_cost_per_hour
        labor_cost = processing_hours_required * labor_cost_per_hour
        other_costs = total_processed_kg * other_costs_per_kg
        total_costs = electricity_cost + labor_cost + other_costs

        # Calculate profit
        total_profit = total_revenue - total_costs
        profit_per_kg = total_profit / total_processed_kg if total_processed_kg > 0 else 0

        return {
            "total_processed_kg": round(total_processed_kg, 2),
            "processing_days_required": round(processing_days_required, 2),
            "total_revenue": round(total_revenue, 2),
            "total_costs": round(total_costs, 2),
            "total_profit": round(total_profit, 2),
            "profit_per_kg": round(profit_per_kg, 2)
        }

    except ZeroDivisionError:
        return {
            "total_processed_kg": 0,
            "processing_days_required": 0,
            "total_revenue": 0,
            "total_costs": 0,
            "total_profit": 0,
            "profit_per_kg": 0
        }
```
