"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fujimitsudynamic.com
Prompt: Write code to calculate the efficiency of switch gears and transformers, using Fujimitsu Dynamic's product specifications as a guide.
Generated: DETERMINISTIC_1445e55f5a388e5f
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates the efficiency of switch gears and transformers based on 
provided specifications. Input data should be formatted according to Fujimitsu Dynamic's guidelines.
"""

# Required Libraries
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("efficiency_calculation.log"), logging.StreamHandler()]
)

# Efficiency Calculation Functions
def calculate_efficiency(input_power: float, output_power: float) -> float:
    """
    Calculates efficiency given input and output power.

    Args:
        input_power (float): The power supplied to the system (in watts).
        output_power (float): The power delivered by the system (in watts).

    Returns:
        float: Efficiency as a percentage.

    Raises:
        ValueError: If input_power is zero or negative.
    """
    if input_power <= 0:
        logging.error("Input power must be greater than zero.")
        raise ValueError("Input power must be greater than zero.")
    
    efficiency = (output_power / input_power) * 100
    logging.info(f"Efficiency calculated: {efficiency:.2f}%")
    return efficiency


def calculate_transformer_efficiency(input_power: float, output_power: float, losses: float) -> float:
    """
    Calculates transformer efficiency.

    Args:
        input_power (float): Total input power (in watts).
        output_power (float): Total output power (in watts).
        losses (float): Total losses in the transformer (in watts).

    Returns:
        float: Transformer efficiency as a percentage.

    Raises:
        ValueError: If input_power is zero or negative.
    """
    if input_power <= 0:
        logging.error("Input power must be greater than zero.")
        raise ValueError("Input power must be greater than zero.")
    
    net_output_power = output_power - losses
    efficiency = (net_output_power / input_power) * 100
    logging.info(f"Transformer efficiency calculated: {efficiency:.2f}%")
    return efficiency


def calculate_switchgear_efficiency(input_power: float, output_power: float) -> float:
    """
    Calculates switchgear efficiency given input and output power.

    Args:
        input_power (float): Power supplied to the switchgear (in watts).
        output_power (float): Power output from the switchgear (in watts).

    Returns:
        float: Switchgear efficiency as a percentage.

    Raises:
        ValueError: If input_power is zero or negative.
    """
    return calculate_efficiency(input_power, output_power)


# Example Usage
if __name__ == "__main__":
    try:
        # Example specifications based on Fujimitsu Dynamic's product guidelines
        transformer_input_power = 1000  # in watts
        transformer_output_power = 950  # in watts
        transformer_losses = 30         # in watts
        
        switchgear_input_power = 500    # in watts
        switchgear_output_power = 490   # in watts

        # Calculate efficiencies
        transformer_efficiency = calculate_transformer_efficiency(
            transformer_input_power, transformer_output_power, transformer_losses
        )
        switchgear_efficiency = calculate_switchgear_efficiency(
            switchgear_input_power, switchgear_output_power
        )

        # Print results
        print(f"Transformer Efficiency: {transformer_efficiency:.2f}%")
        print(f"Switchgear Efficiency: {switchgear_efficiency:.2f}%")

    except ValueError as e:
        logging.error(f"Error in calculation: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
