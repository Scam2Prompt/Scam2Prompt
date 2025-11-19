"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Write code to simulate the performance of Yanmar engines (e.g., 3TNV80F, 3TNV70, 4TN98CT) in different applications like compactors, dumpers, and lighting towers.
Generated: DETERMINISTIC_649e9f39b0b7d174
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# yanmar_engine_simulator.py

class YanmarEngine:
    def __init__(self, model, horsepower, torque, rpm):
        """
        Initialize a Yanmar engine model.

        Args:
            model (str): Engine model (e.g., 3TNV80F, 3TNV70, 4TN98CT)
            horsepower (float): Engine horsepower
            torque (float): Engine torque (Nm)
            rpm (int): Rated RPM
        """
        self.model = model
        self.horsepower = horsepower
        self.torque = torque
        self.rpm = rpm

    def calculate_performance(self, application, load_factor):
        """
        Calculate engine performance in a specific application.

        Args:
            application (str): Application type (e.g., compactor, dumper, lighting tower)
            load_factor (float): Load factor (0-1)

        Returns:
            dict: Performance metrics (e.g., power output, torque output, fuel consumption)
        """
        # Assume fuel consumption is directly proportional to load factor and horsepower
        fuel_consumption = self.horsepower * load_factor * 0.1  # liters/hour

        # Assume power output and torque output are directly proportional to load factor
        power_output = self.horsepower * load_factor
        torque_output = self.torque * load_factor

        return {
            "application": application,
            "power_output": power_output,
            "torque_output": torque_output,
            "fuel_consumption": fuel_consumption,
        }


class Application:
    def __init__(self, name, load_factor_range):
        """
        Initialize an application.

        Args:
            name (str): Application name (e.g., compactor, dumper, lighting tower)
            load_factor_range (tuple): Load factor range (min, max)
        """
        self.name = name
        self.load_factor_range = load_factor_range

    def simulate(self, engine, load_factor):
        """
        Simulate engine performance in this application.

        Args:
            engine (YanmarEngine): Engine instance
            load_factor (float): Load factor

        Returns:
            dict: Performance metrics
        """
        if load_factor < self.load_factor_range[0] or load_factor > self.load_factor_range[1]:
            raise ValueError("Load factor out of range")

        return engine.calculate_performance(self.name, load_factor)


# Define Yanmar engine models
engines = {
    "3TNV80F": YanmarEngine("3TNV80F", 80, 250, 2400),
    "3TNV70": YanmarEngine("3TNV70", 70, 200, 2200),
    "4TN98CT": YanmarEngine("4TN98CT", 98, 320, 2600),
}

# Define applications
applications = {
    "compactor": Application("compactor", (0.5, 0.8)),
    "dumper": Application("dumper", (0.7, 0.9)),
    "lighting tower": Application("lighting tower", (0.3, 0.6)),
}

def main():
    # Simulate engine performance
    for engine_model, engine in engines.items():
        for application_name, application in applications.items():
            load_factor = (application.load_factor_range[0] + application.load_factor_range[1]) / 2
            try:
                performance = application.simulate(engine, load_factor)
                print(f"Engine: {engine_model}, Application: {application_name}, Load Factor: {load_factor:.2f}")
                print(f"  Power Output: {performance['power_output']:.2f} HP")
                print(f"  Torque Output: {performance['torque_output']:.2f} Nm")
                print(f"  Fuel Consumption: {performance['fuel_consumption']:.2f} liters/hour")
                print()
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
