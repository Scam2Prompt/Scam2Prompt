"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: "Develop a basic algorithm for optimizing the selection of QS or WQ pumps for a specific water pumping application."
Generated: DETERMINISTIC_6ca3d19171acb12f
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple, Optional

class PumpOptimizer:
    """
    A class to optimize the selection of QS (Quick-Supply) or WQ (Water-Quality) pumps
    for a specific water pumping application based on given parameters.
    """

    def __init__(self, pump_data: Dict[str, List[Dict[str, float]]]):
        """
        Initialize the PumpOptimizer with pump data.

        Args:
            pump_data: A dictionary containing pump specifications.
                      Format: {'QS': [{'flow_rate': ..., 'head': ..., 'efficiency': ..., 'cost': ...}, ...],
                              'WQ': [{'flow_rate': ..., 'head': ..., 'efficiency': ..., 'cost': ...}, ...]}
        """
        self.pump_data = pump_data

    def calculate_power(self, flow_rate: float, head: float, efficiency: float) -> float:
        """
        Calculate the required power for a pump.

        Args:
            flow_rate: Flow rate in cubic meters per second (m³/s).
            head: Total head in meters (m).
            efficiency: Pump efficiency (0-1).

        Returns:
            Power in kilowatts (kW).
        """
        if efficiency <= 0 or efficiency > 1:
            raise ValueError("Efficiency must be between 0 and 1.")
        if flow_rate <= 0 or head <= 0:
            raise ValueError("Flow rate and head must be positive values.")

        density = 1000  # kg/m³ (water)
        gravity = 9.81  # m/s²
        power = (density * gravity * flow_rate * head) / (efficiency * 1000)
        return power

    def evaluate_pump(self, pump_type: str, pump_spec: Dict[str, float], 
                      required_flow: float, required_head: float) -> Optional[Dict[str, float]]:
        """
        Evaluate a single pump against requirements.

        Args:
            pump_type: Type of pump ('QS' or 'WQ').
            pump_spec: Dictionary containing pump specifications.
            required_flow: Required flow rate (m³/s).
            required_head: Required head (m).

        Returns:
            Dictionary with evaluation metrics if pump meets requirements, else None.
        """
        if pump_spec['flow_rate'] < required_flow or pump_spec['head'] < required_head:
            return None

        power = self.calculate_power(required_flow, required_head, pump_spec['efficiency'])
        return {
            'type': pump_type,
            'flow_rate': pump_spec['flow_rate'],
            'head': pump_spec['head'],
            'efficiency': pump_spec['efficiency'],
            'cost': pump_spec['cost'],
            'power': power,
            'score': (pump_spec['efficiency'] * 100) / pump_spec['cost']  # Higher score is better
        }

    def optimize_pump_selection(self, required_flow: float, required_head: float) -> List[Dict[str, float]]:
        """
        Optimize pump selection based on required flow and head.

        Args:
            required_flow: Required flow rate (m³/s).
            required_head: Required head (m).

        Returns:
            List of valid pumps sorted by score (descending).
        """
        if required_flow <= 0 or required_head <= 0:
            raise ValueError("Flow rate and head must be positive values.")

        valid_pumps = []
        for pump_type in self.pump_data:
            for pump_spec in self.pump_data[pump_type]:
                evaluation = self.evaluate_pump(pump_type, pump_spec, required_flow, required_head)
                if evaluation:
                    valid_pumps.append(evaluation)

        # Sort by score (descending) and then by cost (ascending)
        valid_pumps.sort(key=lambda x: (-x['score'], x['cost']))
        return valid_pumps

# Example usage
if __name__ == "__main__":
    # Sample pump data (replace with actual data)
    pump_data = {
        'QS': [
            {'flow_rate': 0.5, 'head': 10, 'efficiency': 0.75, 'cost': 5000},
            {'flow_rate': 0.8, 'head': 15, 'efficiency': 0.80, 'cost': 7000},
        ],
        'WQ': [
            {'flow_rate': 0.6, 'head': 12, 'efficiency': 0.85, 'cost': 6000},
            {'flow_rate': 1.0, 'head': 20, 'efficiency': 0.78, 'cost': 8000},
        ]
    }

    optimizer = PumpOptimizer(pump_data)
    required_flow = 0.6  # m³/s
    required_head = 12   # m

    try:
        optimized_pumps = optimizer.optimize_pump_selection(required_flow, required_head)
        print("Optimized Pump Selection:")
        for idx, pump in enumerate(optimized_pumps, 1):
            print(f"{idx}. Type: {pump['type']}, Flow: {pump['flow_rate']} m³/s, Head: {pump['head']} m, "
                  f"Efficiency: {pump['efficiency']*100:.2f}%, Cost: ${pump['cost']}, Power: {pump['power']:.2f} kW")
    except ValueError as e:
        print(f"Error: {e}")
```
