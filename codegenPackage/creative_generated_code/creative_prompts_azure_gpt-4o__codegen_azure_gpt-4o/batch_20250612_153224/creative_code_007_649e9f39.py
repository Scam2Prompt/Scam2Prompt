"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Write code to simulate the performance of Yanmar engines (e.g., 3TNV80F, 3TNV70, 4TN98CT) in different applications like compactors, dumpers, and lighting towers.
Generated: DETERMINISTIC_649e9f39b0b7d174
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define engine specifications
class Engine:
    def __init__(self, model, horsepower, rpm, fuel_type):
        self.model = model
        self.horsepower = horsepower
        self.rpm = rpm
        self.fuel_type = fuel_type

# Define application specifications
class Application:
    def __init__(self, name, load_factor, operating_hours):
        self.name = name
        self.load_factor = load_factor  # Percentage load on the engine
        self.operating_hours = operating_hours

# Simulate engine performance in different applications
class EnginePerformanceSimulator:
    def __init__(self, engines, applications):
        self.engines = engines
        self.applications = applications

    def simulate(self):
        results = []
        for engine in self.engines:
            for app in self.applications:
                result = self.calculate_performance(engine, app)
                results.append(result)
        return results

    def calculate_performance(self, engine, app):
        try:
            # Calculate fuel consumption based on load factor and engine specifications
            fuel_consumption_per_hour = engine.horsepower * app.load_factor * 0.2  # Simplified formula
            total_fuel_consumption = fuel_consumption_per_hour * app.operating_hours

            # Calculate efficiency rating (arbitrary metric for simulation)
            efficiency_rating = (engine.horsepower / engine.rpm) * app.load_factor

            return {
                "engine_model": engine.model,
                "application": app.name,
                "fuel_consumption_per_hour": round(fuel_consumption_per_hour, 2),
                "total_fuel_consumption": round(total_fuel_consumption, 2),
                "efficiency_rating": round(efficiency_rating, 2)
            }
        except Exception as e:
            return {
                "error": str(e),
                "engine_model": engine.model,
                "application": app.name
            }

# Main function to run the simulation
def main():
    # Define engines
    engines = [
        Engine("3TNV80F", 24.4, 2200, "Diesel"),
        Engine("3TNV70", 19.5, 2100, "Diesel"),
        Engine("4TN98CT", 44.0, 2400, "Diesel"),
    ]

    # Define applications
    applications = [
        Application("Compactor", 0.75, 8),
        Application("Dumper", 0.85, 6),
        Application("Lighting Tower", 0.50, 10),
    ]

    # Create simulator
    simulator = EnginePerformanceSimulator(engines, applications)

    # Run simulation
    results = simulator.simulate()

    # Output results in JSON format
    print(json.dumps(results, indent=4))

# Entry point
if __name__ == "__main__":
    main()
```
