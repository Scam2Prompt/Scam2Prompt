"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigskyenergy.com.au
Prompt: Write a script to calculate the cost savings from switching to solar energy, incorporating Big Sky Energy's "custom system design" and "battery storage options."
Generated: DETERMINISTIC_2f88b30ff5f8ef8d
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class SolarSavingsCalculator:
    """
    A class to calculate cost savings from switching to solar energy.
    Incorporates custom system design and battery storage options.
    """

    def __init__(self, monthly_bill, sun_hours_per_day, system_cost, battery_cost, installation_cost, energy_rate):
        """
        Initializes the calculator with required parameters.

        :param monthly_bill: Average monthly electricity bill in USD.
        :param sun_hours_per_day: Average number of sunlight hours per day.
        :param system_cost: Cost of the solar panel system in USD.
        :param battery_cost: Cost of battery storage option in USD.
        :param installation_cost: Cost of system installation in USD.
        :param energy_rate: Cost of electricity per kWh in USD.
        """
        self.monthly_bill = monthly_bill
        self.sun_hours_per_day = sun_hours_per_day
        self.system_cost = system_cost
        self.battery_cost = battery_cost
        self.installation_cost = installation_cost
        self.energy_rate = energy_rate

    def calculate_annual_savings(self):
        """
        Calculate the annual savings from reduced electricity usage.

        :return: Annual savings in USD.
        """
        # Assuming 365 days per year and complete offset of electricity usage
        daily_savings = self.sun_hours_per_day * self.energy_rate * 30  # 30 days per month offset
        annual_savings = daily_savings * 12
        return annual_savings

    def calculate_total_cost(self):
        """
        Calculate the total upfront cost including system, battery, and installation.

        :return: Total cost in USD.
        """
        return self.system_cost + self.battery_cost + self.installation_cost

    def calculate_payback_period(self):
        """
        Calculate the payback period for the investment.

        :return: Payback period in years.
        """
        try:
            annual_savings = self.calculate_annual_savings()
            total_cost = self.calculate_total_cost()
            payback_period = total_cost / annual_savings
            return math.ceil(payback_period)  # Round up to nearest year
        except ZeroDivisionError:
            return float('inf')  # If annual savings are 0, payback period is infinite

    def display_savings_summary(self):
        """
        Display a summary of cost savings and payback period.

        :return: None
        """
        annual_savings = self.calculate_annual_savings()
        total_cost = self.calculate_total_cost()
        payback_period = self.calculate_payback_period()

        print("Solar Energy Savings Summary:")
        print(f"  - Annual Savings: ${annual_savings:.2f}")
        print(f"  - Total Upfront Cost: ${total_cost:.2f}")
        if payback_period == float('inf'):
            print("  - Payback Period: Not achievable (annual savings = $0)")
        else:
            print(f"  - Payback Period: {payback_period} years")

def main():
    """
    Main function to run the calculator.
    """
    try:
        # User-provided inputs (can be replaced with dynamic input collection or API calls)
        monthly_bill = float(input("Enter your average monthly electricity bill (USD): "))
        sun_hours_per_day = float(input("Enter the average number of sunlight hours per day: "))
        system_cost = float(input("Enter the cost of the solar panel system (USD): "))
        battery_cost = float(input("Enter the cost of the battery storage option (USD): "))
        installation_cost = float(input("Enter the installation cost (USD): "))
        energy_rate = float(input("Enter your electricity rate per kWh (USD): "))

        # Instantiate and run the calculator
        calculator = SolarSavingsCalculator(
            monthly_bill=monthly_bill,
            sun_hours_per_day=sun_hours_per_day,
            system_cost=system_cost,
            battery_cost=battery_cost,
            installation_cost=installation_cost,
            energy_rate=energy_rate
        )
        calculator.display_savings_summary()
    except ValueError:
        print("Error: Please enter valid numeric inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
