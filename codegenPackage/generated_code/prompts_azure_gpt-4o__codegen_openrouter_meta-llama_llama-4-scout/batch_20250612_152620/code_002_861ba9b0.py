"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: Generate code to simulate energy savings from installing solar-powered whirly birds, incorporating features like "solar-powered operation" and "improved home ventilation."
Generated: DETERMINISTIC_861ba9b0d3de0725
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_whirly_bird.py

class SolarWhirlyBird:
    """
    Simulates energy savings from installing solar-powered whirly birds.

    Attributes:
        installation_cost (float): The initial cost of installing the solar-powered whirly bird.
        energy_savings_per_year (float): The estimated energy savings per year.
        ventilation_improvement_factor (float): The factor by which the whirly bird improves home ventilation.
    """

    def __init__(self, installation_cost, energy_savings_per_year, ventilation_improvement_factor):
        """
        Initializes a SolarWhirlyBird object.

        Args:
            installation_cost (float): The initial cost of installing the solar-powered whirly bird.
            energy_savings_per_year (float): The estimated energy savings per year.
            ventilation_improvement_factor (float): The factor by which the whirly bird improves home ventilation.

        Raises:
            ValueError: If any of the input values are negative.
        """
        if installation_cost < 0 or energy_savings_per_year < 0 or ventilation_improvement_factor < 0:
            raise ValueError("Input values cannot be negative")

        self.installation_cost = installation_cost
        self.energy_savings_per_year = energy_savings_per_year
        self.ventilation_improvement_factor = ventilation_improvement_factor

    def calculate_payback_period(self):
        """
        Calculates the payback period of the solar-powered whirly bird.

        Returns:
            float: The payback period in years.
        """
        if self.energy_savings_per_year == 0:
            return float('inf')  # Return infinity if energy savings is zero

        return self.installation_cost / self.energy_savings_per_year

    def calculate_total_energy_savings(self, years):
        """
        Calculates the total energy savings over a given number of years.

        Args:
            years (int): The number of years.

        Returns:
            float: The total energy savings.

        Raises:
            ValueError: If the number of years is negative.
        """
        if years < 0:
            raise ValueError("Number of years cannot be negative")

        return self.energy_savings_per_year * years

    def calculate_improved_ventilation(self):
        """
        Calculates the improved ventilation factor.

        Returns:
            float: The improved ventilation factor.
        """
        return self.ventilation_improvement_factor


class SolarWhirlyBirdSimulator:
    """
    Simulates the installation of multiple solar-powered whirly birds.

    Attributes:
        whirly_birds (list): A list of SolarWhirlyBird objects.
    """

    def __init__(self):
        self.whirly_birds = []

    def add_whirly_bird(self, whirly_bird):
        """
        Adds a solar-powered whirly bird to the simulator.

        Args:
            whirly_bird (SolarWhirlyBird): The whirly bird to add.
        """
        self.whirly_birds.append(whirly_bird)

    def calculate_total_payback_period(self):
        """
        Calculates the total payback period of all whirly birds.

        Returns:
            float: The total payback period in years.
        """
        total_installation_cost = sum(whirly_bird.installation_cost for whirly_bird in self.whirly_birds)
        total_energy_savings_per_year = sum(whirly_bird.energy_savings_per_year for whirly_bird in self.whirly_birds)

        if total_energy_savings_per_year == 0:
            return float('inf')  # Return infinity if total energy savings is zero

        return total_installation_cost / total_energy_savings_per_year

    def calculate_total_energy_savings(self, years):
        """
        Calculates the total energy savings of all whirly birds over a given number of years.

        Args:
            years (int): The number of years.

        Returns:
            float: The total energy savings.

        Raises:
            ValueError: If the number of years is negative.
        """
        if years < 0:
            raise ValueError("Number of years cannot be negative")

        return sum(whirly_bird.calculate_total_energy_savings(years) for whirly_bird in self.whirly_birds)


def main():
    try:
        # Create a solar-powered whirly bird
        whirly_bird = SolarWhirlyBird(
            installation_cost=1000.0,
            energy_savings_per_year=200.0,
            ventilation_improvement_factor=1.5
        )

        # Create a simulator and add the whirly bird
        simulator = SolarWhirlyBirdSimulator()
        simulator.add_whirly_bird(whirly_bird)

        # Calculate and print the payback period
        payback_period = whirly_bird.calculate_payback_period()
        print(f"Payback period: {payback_period:.2f} years")

        # Calculate and print the total energy savings
        years = 10
        total_energy_savings = simulator.calculate_total_energy_savings(years)
        print(f"Total energy savings over {years} years: ${total_energy_savings:.2f}")

        # Calculate and print the improved ventilation factor
        improved_ventilation = whirly_bird.calculate_improved_ventilation()
        print(f"Improved ventilation factor: {improved_ventilation:.2f}")

        # Calculate and print the total payback period
        total_payback_period = simulator.calculate_total_payback_period()
        print(f"Total payback period: {total_payback_period:.2f} years")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
