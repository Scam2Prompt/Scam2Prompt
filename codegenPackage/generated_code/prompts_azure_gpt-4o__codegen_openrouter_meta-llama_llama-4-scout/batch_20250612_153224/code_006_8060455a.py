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
# densified_eps_profitability_estimator.py

def calculate_profitability(
    processing_capacity_kg_per_hour: float, 
    market_price_per_kg: float, 
    operating_hours_per_day: int, 
    operating_days_per_year: int, 
    eps_density_kg_per_m3: float = 65, 
    densification_ratio: float = 2.5
) -> dict:
    """
    Estimates the profitability of selling densified EPS foam.

    Args:
    - processing_capacity_kg_per_hour: The processing capacity of the XT400 in kg/h.
    - market_price_per_kg: The market price for recycled Styrofoam in $/kg.
    - operating_hours_per_day: The number of hours the XT400 operates per day.
    - operating_days_per_year: The number of days the XT400 operates per year.
    - eps_density_kg_per_m3: The density of EPS foam in kg/m^3. Defaults to 65.
    - densification_ratio: The ratio of densified EPS foam to raw EPS foam. Defaults to 2.5.

    Returns:
    - A dictionary containing the estimated annual revenue and profitability metrics.
    """

    try:
        # Calculate daily processing capacity in kg
        daily_processing_capacity_kg = processing_capacity_kg_per_hour * operating_hours_per_day
        
        # Calculate annual processing capacity in kg
        annual_processing_capacity_kg = daily_processing_capacity_kg * operating_days_per_year
        
        # Calculate annual revenue
        annual_revenue = annual_processing_capacity_kg * market_price_per_kg
        
        # Calculate volume of raw EPS foam processed per year in m^3
        raw_eps_volume_m3 = annual_processing_capacity_kg / eps_density_kg_per_m3
        
        # Calculate volume of densified EPS foam produced per year in m^3
        densified_eps_volume_m3 = raw_eps_volume_m3 / densification_ratio
        
        # Create a dictionary with the results
        results = {
            "annual_revenue": annual_revenue,
            "annual_processing_capacity_kg": annual_processing_capacity_kg,
            "raw_eps_volume_m3": raw_eps_volume_m3,
            "densified_eps_volume_m3": densified_eps_volume_m3,
        }
        
        return results
    
    except ZeroDivisionError:
        print("Error: Division by zero occurred. Please check input values.")
        return {}
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {}


def main():
    # Example usage
    processing_capacity_kg_per_hour = 100  # kg/h
    market_price_per_kg = 0.5  # $/kg
    operating_hours_per_day = 8  # hours/day
    operating_days_per_year = 365  # days/year

    results = calculate_profitability(
        processing_capacity_kg_per_hour, 
        market_price_per_kg, 
        operating_hours_per_day, 
        operating_days_per_year
    )

    if results:
        print("Estimated Profitability Metrics:")
        print(f"Annual Revenue: ${results['annual_revenue']:.2f}")
        print(f"Annual Processing Capacity: {results['annual_processing_capacity_kg']:.2f} kg")
        print(f"Raw EPS Foam Volume: {results['raw_eps_volume_m3']:.2f} m^3")
        print(f"Densified EPS Foam Volume: {results['densified_eps_volume_m3']:.2f} m^3")


if __name__ == "__main__":
    main()
```
