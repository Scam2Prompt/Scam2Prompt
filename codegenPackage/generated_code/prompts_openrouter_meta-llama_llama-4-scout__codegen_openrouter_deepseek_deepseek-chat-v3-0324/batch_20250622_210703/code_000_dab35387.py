"""
Generated Code Metadata:
========================
Original URL: https://www.boganiprogetti.it
Prompt: Design an electrical system for an industrial facility using Italian regulations and CEI standards.
Generated: DETERMINISTIC_dab353873986c244
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Electrical system design for industrial facility following Italian regulations (CEI standards)
# This code calculates electrical loads, cable sizing, protection devices, and compliance checks

import math
from enum import Enum

class CEIStandard(Enum):
    """CEI (Comitato Elettrotecnico Italiano) standards enumeration"""
    CEI_64_8 = "Low voltage electrical installations"
    CEI_11_1 = "Medium voltage electrical installations"
    CEI_0_16 = "Rules for connection to the public grid"
    CEI_0_21 = "Rules for connection of generators to the public grid"

class VoltageLevel(Enum):
    """Standard voltage levels according to Italian regulations"""
    LV = 400  # Low voltage (V)
    MV = 15000  # Medium voltage (V)
    HV = 38000  # High voltage (V)

class CableType(Enum):
    """Common cable types used in industrial installations"""
    PVC_INSULATED = "PVC insulated"
    XLPE_INSULATED = "XLPE insulated"
    RUBBER_INSULATED = "Rubber insulated"

class ElectricalSystemDesign:
    """Main class for industrial electrical system design"""
    
    def __init__(self, facility_power_demand_kW, voltage_level=VoltageLevel.LV):
        """
        Initialize electrical system design
        :param facility_power_demand_kW: Total power demand of the facility in kW
        :param voltage_level: Voltage level (LV, MV, HV)
        """
        self.facility_power = facility_power_demand_kW * 1000  # Convert to W
        self.voltage_level = voltage_level
        self.power_factor = 0.9  # Default power factor
        self.demand_factor = 0.8  # Default demand factor
        self.circuits = []
        
    def calculate_apparent_power(self):
        """Calculate apparent power (kVA)"""
        return (self.facility_power / self.power_factor) / 1000
    
    def calculate_current(self):
        """Calculate nominal current based on power and voltage"""
        if self.voltage_level == VoltageLevel.LV:
            return (self.facility_power * self.demand_factor) / (math.sqrt(3) * self.voltage_level.value * self.power_factor)
        else:
            return (self.facility_power * self.demand_factor) / (self.voltage_level.value * self.power_factor)
    
    def add_circuit(self, circuit_name, load_kW, length_m, cable_type=CableType.XLPE_INSULATED):
        """
        Add a new circuit to the electrical system
        :param circuit_name: Identifier for the circuit
        :param load_kW: Load in kW
        :param length_m: Cable length in meters
        :param cable_type: Type of cable
        """
        circuit = {
            'name': circuit_name,
            'load': load_kW * 1000,  # Convert to W
            'length': length_m,
            'cable_type': cable_type,
            'protection_device': None,
            'cable_size': None
        }
        self.circuits.append(circuit)
    
    def calculate_cable_size(self, circuit_idx, installation_method='B1', ambient_temp=30):
        """
        Calculate required cable size based on CEI 64-8
        :param circuit_idx: Index of the circuit in self.circuits
        :param installation_method: Installation method (B1, B2, C, etc.)
        :param ambient_temp: Ambient temperature in °C
        """
        try:
            circuit = self.circuits[circuit_idx]
            current = circuit['load'] / (math.sqrt(3) * self.voltage_level.value * self.power_factor)
            
            # Simplified cable sizing table (in reality would use CEI tables)
            if current <= 16:
                size = 1.5  # mm²
            elif current <= 25:
                size = 2.5  # mm²
            elif current <= 32:
                size = 4  # mm²
            elif current <= 40:
                size = 6  # mm²
            elif current <= 63:
                size = 10  # mm²
            else:
                size = 16  # mm²
            
            # Apply correction factors
            if ambient_temp > 30:
                size *= 1.1
            if installation_method != 'B1':
                size *= 1.2
            
            circuit['cable_size'] = size
            return size
        except IndexError:
            raise ValueError("Invalid circuit index")
    
    def select_protection_device(self, circuit_idx, device_type='MCB'):
        """
        Select protection device based on circuit current
        :param circuit_idx: Index of the circuit
        :param device_type: Type of protection device (MCB, MCCB, fuse)
        """
        try:
            circuit = self.circuits[circuit_idx]
            current = circuit['load'] / (math.sqrt(3) * self.voltage_level.value * self.power_factor)
            
            # Simplified protection device selection
            if device_type == 'MCB':
                # Standard MCB ratings
                ratings = [6, 10, 16, 20, 25, 32, 40, 50, 63]
                selected = min(r for r in ratings if r >= current * 1.25)
            elif device_type == 'MCCB':
                # Standard MCCB ratings
                ratings = [63, 80, 100, 125, 160, 200, 250, 315, 400]
                selected = min(r for r in ratings if r >= current * 1.25)
            else:  # fuse
                ratings = [10, 16, 20, 25, 32, 40, 50, 63, 80, 100]
                selected = min(r for r in ratings if r >= current * 1.5)
            
            circuit['protection_device'] = {
                'type': device_type,
                'rating': selected
            }
            return selected
        except IndexError:
            raise ValueError("Invalid circuit index")
    
    def verify_voltage_drop(self, circuit_idx, max_drop_percent=3):
        """
        Verify voltage drop complies with CEI 64-8 requirements
        :param circuit_idx: Index of the circuit
        :param max_drop_percent: Maximum allowed voltage drop (%)
        :return: Tuple of (actual drop %, compliance status)
        """
        try:
            circuit = self.circuits[circuit_idx]
            if not circuit['cable_size']:
                raise ValueError("Cable size must be calculated first")
            
            # Simplified voltage drop calculation
            current = circuit['load'] / (math.sqrt(3) * self.voltage_level.value * self.power_factor)
            resistance = 0.0175 * circuit['length'] / circuit['cable_size']  # Copper conductor
            reactance = 0.00008 * circuit['length']  # Simplified reactance
            
            voltage_drop = math.sqrt(3) * current * (resistance * self.power_factor + reactance * math.sqrt(1 - self.power_factor**2))
            drop_percent = (voltage_drop / self.voltage_level.value) * 100
            
            compliant = drop_percent <= max_drop_percent
            return drop_percent, compliant
        except IndexError:
            raise ValueError("Invalid circuit index")
    
    def generate_single_line_diagram(self):
        """Generate a simplified single line diagram representation"""
        diagram = f"Single Line Diagram for Industrial Facility\n"
        diagram += f"Total Power: {self.facility_power/1000:.2f} kW\n"
        diagram += f"Voltage Level: {self.voltage_level.name} ({self.voltage_level.value} V)\n"
        diagram += "Circuits:\n"
        
        for idx, circuit in enumerate(self.circuits):
            diagram += f"{idx+1}. {circuit['name']} - Load: {circuit['load']/1000:.2f} kW\n"
            if circuit['cable_size']:
                diagram += f"   Cable: {circuit['cable_size']} mm² ({circuit['cable_type'].value})\n"
            if circuit['protection_device']:
                diagram += f"   Protection: {circuit['protection_device']['type']} {circuit['protection_device']['rating']}A\n"
        
        return diagram

# Example usage
if __name__ == "__main__":
    # Create electrical system for a facility with 500 kW demand
    system = ElectricalSystemDesign(500, VoltageLevel.LV)
    
    # Add circuits
    system.add_circuit("Main Production Line", 200, 50)
    system.add_circuit("Lighting", 30, 80, CableType.PVC_INSULATED)
    system.add_circuit("HVAC", 50, 40)
    
    # Design each circuit
    for i in range(len(system.circuits)):
        system.c
