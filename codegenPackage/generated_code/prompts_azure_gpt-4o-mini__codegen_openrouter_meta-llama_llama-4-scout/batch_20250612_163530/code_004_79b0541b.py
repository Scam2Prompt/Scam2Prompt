"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: Create a project proposal template for installing a solar energy system at a commercial facility, inspired by Chico Electric's case studies.
Generated: DETERMINISTIC_79b0541b17bfe0b5
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_energy_proposal.py

class SolarEnergyProposal:
    """
    A class representing a project proposal for installing a solar energy system at a commercial facility.
    """

    def __init__(self, facility_name, facility_address, energy_usage_kwh, 
                 system_size_kw, installation_cost, incentive_percentage):
        """
        Initializes a SolarEnergyProposal object.

        Args:
            facility_name (str): The name of the commercial facility.
            facility_address (str): The address of the commercial facility.
            energy_usage_kwh (float): The current energy usage of the facility in kWh.
            system_size_kw (float): The proposed size of the solar energy system in kW.
            installation_cost (float): The estimated cost of installing the solar energy system.
            incentive_percentage (float): The percentage of incentives available for the project.
        """
        self.facility_name = facility_name
        self.facility_address = facility_address
        self.energy_usage_kwh = energy_usage_kwh
        self.system_size_kw = system_size_kw
        self.installation_cost = installation_cost
        self.incentive_percentage = incentive_percentage

    def calculate_incentive_amount(self):
        """
        Calculates the incentive amount available for the project.

        Returns:
            float: The incentive amount.
        """
        return self.installation_cost * (self.incentive_percentage / 100)

    def calculate_roi(self):
        """
        Calculates the return on investment (ROI) for the project.

        Returns:
            float: The ROI.
        """
        # Assume a fixed energy cost of $0.15/kWh
        energy_cost_per_kwh = 0.15
        annual_energy_savings = self.system_size_kw * 1000 * energy_cost_per_kwh
        return (annual_energy_savings / self.installation_cost) * 100

    def generate_proposal(self):
        """
        Generates a project proposal template.

        Returns:
            str: The proposal template.
        """
        proposal = f"""
# Project Proposal: Solar Energy System Installation at {self.facility_name}

## Executive Summary

This proposal outlines the plan to install a solar energy system at {self.facility_name}, 
located at {self.facility_address}. The proposed system will reduce the facility's reliance 
on traditional energy sources and lower its energy costs.

## Facility Information

* Facility Name: {self.facility_name}
* Facility Address: {self.facility_address}
* Current Energy Usage: {self.energy_usage_kwh} kWh

## Solar Energy System Details

* System Size: {self.system_size_kw} kW
* Installation Cost: ${self.installation_cost:,.2f}
* Incentive Amount: ${self.calculate_incentive_amount():,.2f} ({self.incentive_percentage}%)

## Financial Analysis

* Return on Investment (ROI): {self.calculate_roi():.2f}%

## Conclusion

The installation of a solar energy system at {self.facility_name} offers a compelling opportunity 
to reduce energy costs and contribute to a sustainable future.

        """
        return proposal


def main():
    try:
        facility_name = input("Enter facility name: ")
        facility_address = input("Enter facility address: ")
        energy_usage_kwh = float(input("Enter current energy usage (kWh): "))
        system_size_kw = float(input("Enter proposed system size (kW): "))
        installation_cost = float(input("Enter installation cost: $"))
        incentive_percentage = float(input("Enter incentive percentage (%): "))

        proposal = SolarEnergyProposal(facility_name, facility_address, energy_usage_kwh, 
                                       system_size_kw, installation_cost, incentive_percentage)

        print(proposal.generate_proposal())

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
