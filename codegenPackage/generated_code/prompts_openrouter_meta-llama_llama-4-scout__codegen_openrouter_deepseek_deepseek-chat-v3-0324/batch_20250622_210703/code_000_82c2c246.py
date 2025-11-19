"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: "Write a Python code to calculate the energy efficiency of a building using StoTherm thermal insulation system."
Generated: DETERMINISTIC_82c2c2469c5dd33f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class BuildingEnergyEfficiencyCalculator:
    """
    A class to calculate the energy efficiency of a building using StoTherm thermal insulation system.
    
    Attributes:
        building_area (float): Total area of the building in square meters.
        u_value (float): Thermal transmittance (U-value) of the building envelope in W/m²K.
        heating_degree_days (float): Heating degree days for the location in K·days.
        heating_system_efficiency (float): Efficiency of the heating system (0 to 1).
        insulation_thickness (float): Thickness of StoTherm insulation in meters.
        insulation_conductivity (float): Thermal conductivity of StoTherm insulation in W/mK.
    """
    
    def __init__(self, building_area, u_value, heating_degree_days, heating_system_efficiency,
                 insulation_thickness=0.1, insulation_conductivity=0.04):
        """
        Initialize the calculator with building parameters.
        
        Args:
            building_area: Total area of the building in square meters.
            u_value: Thermal transmittance (U-value) of the building envelope in W/m²K.
            heating_degree_days: Heating degree days for the location in K·days.
            heating_system_efficiency: Efficiency of the heating system (0 to 1).
            insulation_thickness: Thickness of StoTherm insulation in meters (default: 0.1).
            insulation_conductivity: Thermal conductivity of StoTherm insulation in W/mK (default: 0.04).
        """
        self.building_area = building_area
        self.u_value = u_value
        self.heating_degree_days = heating_degree_days
        self.heating_system_efficiency = heating_system_efficiency
        self.insulation_thickness = insulation_thickness
        self.insulation_conductivity = insulation_conductivity
        
        self._validate_inputs()
    
    def _validate_inputs(self):
        """Validate input parameters to ensure they are within reasonable ranges."""
        if self.building_area <= 0:
            raise ValueError("Building area must be positive.")
        if self.u_value <= 0:
            raise ValueError("U-value must be positive.")
        if self.heating_degree_days <= 0:
            raise ValueError("Heating degree days must be positive.")
        if not 0 < self.heating_system_efficiency <= 1:
            raise ValueError("Heating system efficiency must be between 0 and 1.")
        if self.insulation_thickness <= 0:
            raise ValueError("Insulation thickness must be positive.")
        if self.insulation_conductivity <= 0:
            raise ValueError("Insulation conductivity must be positive.")
    
    def calculate_heat_loss(self):
        """
        Calculate the annual heat loss through the building envelope.
        
        Returns:
            float: Annual heat loss in kWh.
        """
        # Convert heating degree days from K·days to K·seconds
        hdd_seconds = self.heating_degree_days * 24 * 3600
        
        # Calculate heat loss: Q = U * A * ΔT * t
        heat_loss_joules = self.u_value * self.building_area * hdd_seconds
        heat_loss_kwh = heat_loss_joules / (3600 * 1000)
        
        return heat_loss_kwh
    
    def calculate_insulated_u_value(self):
        """
        Calculate the improved U-value after adding StoTherm insulation.
        
        Returns:
            float: Improved U-value in W/m²K.
        """
        # R-value of the insulation: R = thickness / conductivity
        r_insulation = self.insulation_thickness / self.insulation_conductivity
        
        # Original R-value: R = 1 / U
        r_original = 1 / self.u_value
        
        # Total R-value after insulation
        r_total = r_original + r_insulation
        
        # New U-value: U = 1 / R
        return 1 / r_total
    
    def calculate_energy_savings(self):
        """
        Calculate the annual energy savings after insulation.
        
        Returns:
            tuple: (energy_savings_kwh, percentage_savings)
        """
        original_heat_loss = self.calculate_heat_loss()
        new_u_value = self.calculate_insulated_u_value()
        
        # Create a temporary instance with the new U-value
        temp_calculator = BuildingEnergyEfficiencyCalculator(
            self.building_area,
            new_u_value,
            self.heating_degree_days,
            self.heating_system_efficiency,
            self.insulation_thickness,
            self.insulation_conductivity
        )
        
        new_heat_loss = temp_calculator.calculate_heat_loss()
        
        energy_savings_kwh = original_heat_loss - new_heat_loss
        percentage_savings = (energy_savings_kwh / original_heat_loss) * 100
        
        return (energy_savings_kwh, percentage_savings)
    
    def calculate_required_energy(self):
        """
        Calculate the required energy input considering heating system efficiency.
        
        Returns:
            float: Required energy input in kWh.
        """
        heat_loss = self.calculate_heat_loss()
        return heat_loss / self.heating_system_efficiency
    
    def calculate_insulated_required_energy(self):
        """
        Calculate the required energy input after insulation.
        
        Returns:
            float: Required energy input after insulation in kWh.
        """
        new_u_value = self.calculate_insulated_u_value()
        
        temp_calculator = BuildingEnergyEfficiencyCalculator(
            self.building_area,
            new_u_value,
            self.heating_degree_days,
            self.heating_system_efficiency,
            self.insulation_thickness,
            self.insulation_conductivity
        )
        
        insulated_heat_loss = temp_calculator.calculate_heat_loss()
        return insulated_heat_loss / self.heating_system_efficiency


# Example usage
if __name__ == "__main__":
    try:
        # Example building parameters
        calculator = BuildingEnergyEfficiencyCalculator(
            building_area=150,          # 150 m²
            u_value=1.5,               # W/m²K
            heating_degree_days=2500,  # K·days
            heating_system_efficiency=0.85,
            insulation_thickness=0.1,  # 10 cm
            insulation_conductivity=0.04
        )
        
        # Calculate and print results
        heat_loss = calculator.calculate_heat_loss()
        new_u_value = calculator.calculate_insulated_u_value()
        savings_kwh, savings_percent = calculator.calculate_energy_savings()
        required_energy = calculator.calculate_required_energy()
        insulated_energy = calculator.calculate_insulated_required_energy()
        
        print(f"Original annual heat loss: {heat_loss:.2f} kWh")
        print(f"Improved U-value after insulation: {new_u_value:.4f} W/m²K")
        print(f"Annual energy savings: {savings_kwh:.2f} kWh ({savings_percent:.1f}%)")
        print(f"Original required energy input: {required_energy:.2f} kWh")
        print(f"Required energy after insulation: {insulated_energy:.2f} kWh")
        
    except ValueError as e:
        print(f"Error: {e}")
```
