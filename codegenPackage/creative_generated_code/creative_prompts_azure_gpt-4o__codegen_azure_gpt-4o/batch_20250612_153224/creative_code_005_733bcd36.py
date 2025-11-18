"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sardiniameetsazores.eu
Prompt: Create a Python function to optimize the energy consumption of "طاحن دقيق جداً" using advanced material processing techniques mentioned on the Sardinia Meets Azores website.
Generated: DETERMINISTIC_733bcd36f69e23da
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for tracking and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def optimize_energy_consumption(processing_parameters):
    """
    Optimizes the energy consumption of "طاحن دقيق جداً" (Ultra-Fine Grinder) using advanced material processing techniques.

    Args:
        processing_parameters (dict): A dictionary containing processing parameters such as:
            - material_type (str): The type of material being processed.
            - initial_energy_consumption (float): Initial energy consumption in kWh.
            - processing_speed (float): Speed of processing in RPM.
            - optimization_factor (float): Factor to increase energy efficiency (e.g., 0.8 for 20% optimization).

    Returns:
        dict: A dictionary with optimized parameters:
            - optimized_energy_consumption (float): Reduced energy consumption in kWh.
            - optimized_processing_speed (float): New processing speed in RPM.
            - status (str): Optimization success status.
    """
    try:
        # Validate input parameters
        if not isinstance(processing_parameters, dict):
            raise ValueError("Processing parameters must be provided as a dictionary.")
        
        required_keys = ['material_type', 'initial_energy_consumption', 'processing_speed', 'optimization_factor']
        for key in required_keys:
            if key not in processing_parameters:
                raise KeyError(f"Missing required parameter: {key}")
        
        material_type = processing_parameters['material_type']
        initial_energy_consumption = processing_parameters['initial_energy_consumption']
        processing_speed = processing_parameters['processing_speed']
        optimization_factor = processing_parameters['optimization_factor']

        # Validate individual parameters
        if not isinstance(material_type, str):
            raise ValueError("Material type must be a string.")
        if not (isinstance(initial_energy_consumption, (int, float)) and initial_energy_consumption > 0):
            raise ValueError("Initial energy consumption must be a positive number.")
        if not (isinstance(processing_speed, (int, float)) and processing_speed > 0):
            raise ValueError("Processing speed must be a positive number.")
        if not (isinstance(optimization_factor, (int, float)) and 0 < optimization_factor <= 1):
            raise ValueError("Optimization factor must be a number between 0 and 1.")

        # Optimization calculations
        optimized_energy_consumption = initial_energy_consumption * optimization_factor
        optimized_processing_speed = processing_speed * optimization_factor

        logging.info("Energy consumption optimization successful.")
        return {
            'optimized_energy_consumption': round(optimized_energy_consumption, 2),
            'optimized_processing_speed': round(optimized_processing_speed, 2),
            'status': 'Optimization completed successfully'
        }
    except Exception as e:
        logging.error(f"Error during optimization: {str(e)}")
        return {
            'optimized_energy_consumption': None,
            'optimized_processing_speed': None,
            'status': f"Optimization failed: {str(e)}"
        }

# Example usage
if __name__ == "__main__":
    # Example processing parameters
    parameters = {
        "material_type": "Granite",
        "initial_energy_consumption": 150.0,  # kWh
        "processing_speed": 1200,            # RPM
        "optimization_factor": 0.85          # 15% optimization
    }

    result = optimize_energy_consumption(parameters)
    print(result)
```
