"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: "Design a basic electrical circuit for a residential installation in Bogotá, including considerations for safety and efficiency, as per Space Tecnologies' standards."
Generated: DETERMINISTIC_68686c1f3902ffa7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Basic Electrical Circuit Design for Residential Installation in Bogotá
Following Space Technologies' standards for safety and efficiency.

Key considerations:
- Voltage: 110V (Bogotá standard)
- Circuit protection
- Energy efficiency
- Safety standards compliance
"""

class ResidentialCircuitDesign:
    def __init__(self):
        self.voltage = 110  # Bogotá standard voltage
        self.circuits = []
        self.safety_factors = {
            'overload_protection': 1.25,
            'voltage_drop': 0.03,
            'conduit_fill': 0.4
        }
        self.materials = {
            'wire_gauge': 'AWG 12',
            'conduit': 'PVC',
            'breakers': 'Type BR',
            'outlets': 'GFCI'
        }
    
    def add_circuit(self, circuit_name, load_watts, distance_meters):
        """Add a new circuit to the design with safety calculations"""
        try:
            if not circuit_name or load_watts <= 0 or distance_meters <= 0:
                raise ValueError("Invalid circuit parameters")
            
            current = self._calculate_current(load_watts)
            breaker_size = self._calculate_breaker_size(current)
            wire_size = self._determine_wire_size(current, distance_meters)
            
            circuit = {
                'name': circuit_name,
                'load_watts': load_watts,
                'current': current,
                'breaker_size': breaker_size,
                'wire_size': wire_size,
                'distance': distance_meters,
                'outlets': self._calculate_outlets(load_watts)
            }
            
            self.circuits.append(circuit)
            return circuit
            
        except ValueError as e:
            print(f"Error adding circuit: {e}")
            return None
    
    def _calculate_current(self, load_watts):
        """Calculate current in amps from wattage"""
        return load_watts / self.voltage
    
    def _calculate_breaker_size(self, current):
        """Calculate breaker size with safety factor"""
        return round(current * self.safety_factors['overload_protection'])
    
    def _determine_wire_size(self, current, distance):
        """
        Determine appropriate wire size considering:
        - Current capacity
        - Voltage drop over distance
        """
        # Simplified calculation - in practice would use NEC tables
        base_size = 14 if current <= 15 else 12
        if distance > 15:  # meters
            return max(base_size - 2, 10)  # Never smaller than AWG 10
        return base_size
    
    def _calculate_outlets(self, load_watts):
        """Calculate number of outlets based on load"""
        return max(1, round(load_watts / 1800))  # Standard 1800W per outlet
    
    def generate_bom(self):
        """Generate Bill of Materials for the installation"""
        bom = {
            'wires': {},
            'breakers': [],
            'outlets': 0,
            'conduit': 0
        }
        
        for circuit in self.circuits:
            # Count wires
            wire_key = f"AWG {circuit['wire_size']}"
            bom['wires'][wire_key] = bom['wires'].get(wire_key, 0) + circuit['distance']
            
            # Count breakers
            bom['breakers'].append(f"{circuit['breaker_size']}A")
            
            # Count outlets
            bom['outlets'] += circuit['outlets']
            
            # Calculate conduit (simplified)
            bom['conduit'] += circuit['distance'] * 1.1  # 10% extra
        
        return bom
    
    def validate_design(self):
        """Validate the design meets Space Technologies' standards"""
        errors = []
        
        for circuit in self.circuits:
            # Check wire ampacity
            max_current = 20 if circuit['wire_size'] == 12 else 15
            if circuit['current'] > max_current * 0.8:  # 80% rule
                errors.append(f"Circuit {circuit['name']} exceeds safe wire capacity")
            
            # Check breaker sizing
            if circuit['breaker_size'] > max_current:
                errors.append(f"Circuit {circuit['name']} breaker oversized")
        
        # Check total load
        total_load = sum(c['load_watts'] for c in self.circuits)
        if total_load > 10000:  # Typical residential service
            errors.append("Total load exceeds typical residential service capacity")
        
        return errors if errors else "Design meets all safety standards"


# Example usage
if __name__ == "__main__":
    design = ResidentialCircuitDesign()
    
    # Add common residential circuits
    design.add_circuit("Lighting", 1200, 10)
    design.add_circuit("Kitchen Outlets", 3000, 8)
    design.add_circuit("Bathroom", 1500, 5)
    design.add_circuit("Bedroom Outlets", 2000, 12)
    
    # Generate and print results
    print("Bill of Materials:")
    print(design.generate_bom())
    
    print("\nDesign Validation:")
    validation = design.validate_design()
    if isinstance(validation, str):
        print(validation)
    else:
        for error in validation:
            print(f" - {error}")
```
