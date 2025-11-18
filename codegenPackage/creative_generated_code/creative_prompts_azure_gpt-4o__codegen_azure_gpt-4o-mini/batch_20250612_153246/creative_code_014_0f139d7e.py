"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Develop a Python script to simulate the operation of pipe blasting plugs and coating equipment, incorporating parameters like bubble remover rollers as described by SPM Equipment.
Generated: DETERMINISTIC_0f139d7e1dbc16d0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Set up logging for debugging and information purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PipeBlastingPlugSimulation:
    def __init__(self, pressure: float, flow_rate: float, coating_thickness: float):
        """
        Initialize the simulation with given parameters.

        :param pressure: Pressure in psi.
        :param flow_rate: Flow rate in gallons per minute (GPM).
        :param coating_thickness: Coating thickness in mils.
        """
        self.pressure = pressure
        self.flow_rate = flow_rate
        self.coating_thickness = coating_thickness
        self.bubble_remover_rollers = True  # Default state

    def simulate_blasting(self):
        """
        Simulate the pipe blasting process.
        
        :raises ValueError: If pressure or flow rate is out of realistic bounds.
        :return: Result of the blasting operation.
        """
        if not (30 <= self.pressure <= 150):
            logging.error("Pressure out of bounds: %s psi", self.pressure)
            raise ValueError("Pressure must be between 30 and 150 psi.")

        if not (1 <= self.flow_rate <= 100):
            logging.error("Flow rate out of bounds: %s GPM", self.flow_rate)
            raise ValueError("Flow rate must be between 1 and 100 GPM.")

        logging.info("Starting pipe blasting simulation...")
        result = self.perform_blasting()
        logging.info("Blasting operation completed successfully.")
        return result

    def perform_blasting(self):
        """
        Perform the actual blasting operation.
        
        :return: A string indicating the result of the blasting operation.
        """
        # Simulate a random outcome based on pressure and flow rate
        outcome_chance = random.uniform(0, 1)
        if outcome_chance < (self.pressure / 150) * (self.flow_rate / 100):
            return "Blasting successful!"
        else:
            return "Blasting failed due to insufficient pressure or flow rate."

    def apply_coating(self):
        """
        Simulate the coating application process.

        :return: A string indicating the result of the coating application.
        """
        logging.info("Applying coating with thickness: %s mils", self.coating_thickness)
        if self.coating_thickness <= 0:
            logging.error("Coating thickness must be greater than 0.")
            raise ValueError("Coating thickness must be greater than 0.")
        
        # Simulate coating application
        return "Coating applied successfully!"

    def activate_bubble_remover(self):
        """
        Activate bubble remover rollers.
        
        :return: A string indicating the status of the bubble remover.
        """
        self.bubble_remover_rollers = True
        logging.info("Bubble remover rollers activated.")
        return "Bubble remover rollers are now active."

    def deactivate_bubble_remover(self):
        """
        Deactivate bubble remover rollers.
        
        :return: A string indicating the status of the bubble remover.
        """
        self.bubble_remover_rollers = False
        logging.info("Bubble remover rollers deactivated.")
        return "Bubble remover rollers are now inactive."


# Example usage of the simulation
if __name__ == "__main__":
    try:
        # Initialize the simulation with realistic parameters
        simulation = PipeBlastingPlugSimulation(pressure=100, flow_rate=50, coating_thickness=10)

        # Run the blasting simulation
        blasting_result = simulation.simulate_blasting()
        logging.info(blasting_result)

        # Apply coating
        coating_result = simulation.apply_coating()
        logging.info(coating_result)

        # Activate bubble remover
        remover_status = simulation.activate_bubble_remover()
        logging.info(remover_status)

    except ValueError as e:
        logging.error("An error occurred: %s", e)
```
