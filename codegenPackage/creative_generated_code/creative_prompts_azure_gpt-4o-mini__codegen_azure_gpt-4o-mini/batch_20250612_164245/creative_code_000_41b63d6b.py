"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Write a code snippet to calculate the optimal compressor size for a specific application using parameters like airflow requirements and pressure settings, similar to those discussed on the Só Compressores e Bombas website.
Generated: DETERMINISTIC_41b63d6bcf72a11c
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CompressorSizingError(Exception):
    """Custom exception for compressor sizing errors."""
    pass

def calculate_compressor_size(airflow_rate_cfm, pressure_setting_psi, efficiency=0.85):
    """
    Calculate the optimal compressor size based on airflow requirements and pressure settings.
    
    Parameters:
    airflow_rate_cfm (float): Required airflow rate in cubic feet per minute (CFM).
    pressure_setting_psi (float): Required pressure setting in pounds per square inch (PSI).
    efficiency (float): Efficiency of the compressor (default is 0.85).
    
    Returns:
    float: Required compressor size in horsepower (HP).
    
    Raises:
    CompressorSizingError: If airflow_rate_cfm or pressure_setting_psi is non-positive.
    """
    # Validate input parameters
    if airflow_rate_cfm <= 0:
        raise CompressorSizingError("Airflow rate must be a positive number.")
    if pressure_setting_psi <= 0:
        raise CompressorSizingError("Pressure setting must be a positive number.")
    
    # Calculate the required horsepower using the formula
    # HP = (CFM * PSI) / (Efficiency *  0.5)
    required_hp = (airflow_rate_cfm * pressure_setting_psi) / (efficiency * 0.5)
    
    return required_hp

def main():
    try:
        # Example usage
        airflow_rate = 100.0  # CFM
        pressure_setting = 90.0  # PSI
        
        compressor_size = calculate_compressor_size(airflow_rate, pressure_setting)
        
        print(f"Required compressor size: {compressor_size:.2f} HP")
    
    except CompressorSizingError as e:
        print(f"Error in compressor sizing: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
