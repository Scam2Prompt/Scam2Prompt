"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cabinet-customs.com.ua
Prompt: Create a function that calculates customs duties for importing a vehicle based on the guidelines provided by the State Customs Service of Ukraine.
Generated: DETERMINISTIC_907f7a48544d5e39
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_vehicle_customs_duty(base_value, engine_volume, vehicle_age):
    """
    Calculates customs duties for importing a vehicle based on Ukrainian guidelines.

    Args:
        base_value (float): The base value of the vehicle in Euros.
        engine_volume (int): The engine volume of the vehicle in cubic centimeters (cc).
        vehicle_age (int): The age of the vehicle in years.

    Returns:
        float: The total customs duty in Euros.

    Raises:
        ValueError: If any of the inputs are invalid.
    """
    try:
        # Input validation
        if base_value <= 0:
            raise ValueError("Base value must be greater than zero.")
        if engine_volume <= 0:
            raise ValueError("Engine volume must be greater than zero.")
        if vehicle_age < 0:
            raise ValueError("Vehicle age cannot be negative.")

        # Constants for customs duty calculation (fictional example values)
        excise_tax_rate_per_cc = 0.05  # Euros per cubic centimeter (cc)
        vehicle_age_multiplier = 0.1  # Age multiplier for excise tax
        import_duty_rate = 0.10       # 10% of base value
        VAT_rate = 0.20              # 20% of (base value + import duty + excise tax)

        # Calculate excise tax
        excise_tax = engine_volume * excise_tax_rate_per_cc * (1 + vehicle_age_multiplier * vehicle_age)

        # Calculate import duty
        import_duty = base_value * import_duty_rate

        # Calculate VAT
        VAT = (base_value + import_duty + excise_tax) * VAT_rate

        # Calculate total customs duty
        total_customs_duty = excise_tax + import_duty + VAT

        logging.info("Customs duty calculated successfully.")
        return round(total_customs_duty, 2)
    except ValueError as ve:
        logging.error(f"Input error: {ve}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

# Example usage (uncomment to test):
# try:
#     duty = calculate_vehicle_customs_duty(base_value=10000, engine_volume=2000, vehicle_age=5)
#     print(f"The total customs duty is: {duty} Euros")
# except Exception as e:
#     print(f"Error calculating customs duty: {e}")
```
