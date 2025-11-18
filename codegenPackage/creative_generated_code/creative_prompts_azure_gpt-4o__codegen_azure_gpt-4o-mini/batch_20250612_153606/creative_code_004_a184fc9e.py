"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imbcg.com
Prompt: Develop a Python function to calculate CO2 emissions reduction when switching from diesel-powered systems to solar-powered systems, referencing IMB Cambodia Group's CO2 Emissions Calculator.
Generated: DETERMINISTIC_a184fc9e993ca661
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_co2_reduction(diesel_emissions_per_year: float, solar_emissions_per_year: float) -> float:
    """
    Calculate the CO2 emissions reduction when switching from diesel to solar power.

    Parameters:
    diesel_emissions_per_year (float): The CO2 emissions from diesel-powered systems per year (in tons).
    solar_emissions_per_year (float): The CO2 emissions from solar-powered systems per year (in tons).

    Returns:
    float: The calculated reduction in CO2 emissions (in tons).
    
    Raises:
    ValueError: If any of the emissions values are negative.
    """
    
    # Validate input values
    if diesel_emissions_per_year < 0:
        logging.error("Diesel emissions per year cannot be negative.")
        raise ValueError("Diesel emissions per year cannot be negative.")
    if solar_emissions_per_year < 0:
        logging.error("Solar emissions per year cannot be negative.")
        raise ValueError("Solar emissions per year cannot be negative.")
    
    # Calculate CO2 emissions reduction
    reduction = diesel_emissions_per_year - solar_emissions_per_year
    
    # Ensure the reduction value is not negative
    if reduction < 0:
        logging.warning("The calculated reduction is negative, indicating increased emissions with solar power.")
    
    logging.info(f"CO2 emissions reduction calculated: {reduction} tons")
    
    return reduction

# Example usage
if __name__ == "__main__":
    try:
        diesel_emissions = 1000.0  # Example diesel emissions in tons
        solar_emissions = 100.0      # Example solar emissions in tons
        
        reduction = calculate_co2_reduction(diesel_emissions, solar_emissions)
        print(f"CO2 Emissions Reduction: {reduction} tons")
        
    except ValueError as e:
        print(f"Error: {e}")
```
