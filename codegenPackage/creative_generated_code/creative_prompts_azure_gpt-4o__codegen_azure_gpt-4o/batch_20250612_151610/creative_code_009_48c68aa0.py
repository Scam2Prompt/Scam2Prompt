"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oxicap.com
Prompt: Create Python code to simulate the failure modes of Niobium Oxide capacitors, focusing on their high resistance and non-burning characteristics, as outlined in KYOCERA AVX's technical documentation.
Generated: DETERMINISTIC_48c68aa042d7e5d9
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class NiobiumOxideCapacitor:
    """
    Simulates the behavior and failure modes of Niobium Oxide capacitors.
    These capacitors are known for their high resistance and non-burning characteristics.
    """

    def __init__(self, rated_voltage: float, leakage_current: float):
        """
        Initialize the Niobium Oxide capacitor with its rated voltage and leakage current.

        :param rated_voltage: The maximum voltage the capacitor can handle safely (in Volts).
        :param leakage_current: Nominal leakage current of the capacitor (in microamps).
        """
        self.rated_voltage = rated_voltage
        self.leakage_current = leakage_current
        self.is_failed = False

    def simulate_failure_mode(self):
        """
        Simulates failure modes specific to Niobium Oxide capacitors.
        Failure modes include:
        - High resistance failure (non-burning short)
        - Increased leakage current

        :return: A string describing the failure mode, or "No Failure".
        """
        if self.is_failed:
            return "Capacitor has already failed."

        # Simulate random failure based on probability
        failure_probability = random.uniform(0, 1)
        
        # Niobium Oxide capacitors typically experience high resistance failure
        if failure_probability < 0.1:  # 10% chance of failure
            self.is_failed = True
            return "Failure Mode: High resistance failure (non-burning short)."
        
        # Simulate increased leakage current
        if failure_probability < 0.2:  # Additional 10% chance of elevated leakage
            self.leakage_current *= random.uniform(1.1, 2.0)  # Increase leakage current randomly
            return f"Warning: Increased leakage current detected. Current = {self.leakage_current:.2f} µA."

        return "No Failure"

    def test_voltage(self, applied_voltage: float):
        """
        Test the capacitor under a specific applied voltage to check if it exceeds the rated voltage.

        :param applied_voltage: Voltage applied to the capacitor (in Volts).
        :return: A string describing the test result.
        """
        if applied_voltage > self.rated_voltage:
            self.is_failed = True
            return "Failure Mode: Voltage breakdown due to exceeding rated voltage."
        return "Voltage test passed successfully."


def main():
    """
    Main function to simulate and test Niobium Oxide capacitors.
    """
    try:
        # Create a Niobium Oxide capacitor with given specifications
        capacitor = NiobiumOxideCapacitor(rated_voltage=6.3, leakage_current=0.5)

        print("Testing Niobium Oxide Capacitor...")
        
        # Simulate failure modes multiple times
        for _ in range(5):
            result = capacitor.simulate_failure_mode()
            print(result)

        # Test the capacitor under various voltages
        applied_voltages = [5.0, 7.0]  # Voltages to test (within and above rated voltage)
        for voltage in applied_voltages:
            test_result = capacitor.test_voltage(voltage)
            print(f"Applied Voltage: {voltage} V - {test_result}")

    except Exception as e:
        print(f"An error occurred during simulation: {e}")


if __name__ == "__main__":
    # Run the simulation
    main()
```
