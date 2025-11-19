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
# Pump Optimizer Algorithm

class Pump:
    def __init__(self, name, flow_rate, head, efficiency, power):
        """
        Initialize a Pump object.

        Args:
            name (str): Pump name (e.g., QS or WQ)
            flow_rate (float): Flow rate in m³/h
            head (float): Head in meters
            efficiency (float): Efficiency as a decimal value
            power (float): Power consumption in kW
        """
        self.name = name
        self.flow_rate = flow_rate
        self.head = head
        self.efficiency = efficiency
        self.power = power

class PumpOptimizer:
    def __init__(self, required_flow_rate, required_head):
        """
        Initialize a PumpOptimizer object.

        Args:
            required_flow_rate (float): Required flow rate in m³/h
            required_head (float): Required head in meters
        """
        self.required_flow_rate = required_flow_rate
        self.required_head = required_head
        self.available_pumps = []

    def add_pump(self, pump):
        """
        Add a pump to the optimizer.

        Args:
            pump (Pump): Pump object to add
        """
        self.available_pumps.append(pump)

    def optimize_pump_selection(self):
        """
        Optimize pump selection based on required flow rate and head.

        Returns:
            list: List of optimal pumps
        """
        optimal_pumps = []
        min_power = float('inf')

        for pump in self.available_pumps:
            if pump.flow_rate >= self.required_flow_rate and pump.head >= self.required_head:
                if pump.power < min_power:
                    min_power = pump.power
                    optimal_pumps = [pump]
                elif pump.power == min_power:
                    optimal_pumps.append(pump)

        return optimal_pumps

def main():
    try:
        # Define available pumps
        qs_pump1 = Pump("QS-100", 100, 10, 0.7, 15)
        qs_pump2 = Pump("QS-150", 150, 12, 0.75, 20)
        wq_pump1 = Pump("WQ-120", 120, 11, 0.72, 18)
        wq_pump2 = Pump("WQ-180", 180, 13, 0.78, 25)

        # Create pump optimizer
        optimizer = PumpOptimizer(140, 12)

        # Add pumps to optimizer
        optimizer.add_pump(qs_pump1)
        optimizer.add_pump(qs_pump2)
        optimizer.add_pump(wq_pump1)
        optimizer.add_pump(wq_pump2)

        # Optimize pump selection
        optimal_pumps = optimizer.optimize_pump_selection()

        # Print optimal pumps
        if optimal_pumps:
            print("Optimal Pumps:")
            for pump in optimal_pumps:
                print(f"Name: {pump.name}, Flow Rate: {pump.flow_rate} m³/h, Head: {pump.head} m, Power: {pump.power} kW")
        else:
            print("No optimal pumps found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
