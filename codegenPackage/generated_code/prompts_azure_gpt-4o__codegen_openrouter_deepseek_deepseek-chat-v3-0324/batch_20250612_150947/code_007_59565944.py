"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Generate a script to calculate the cost and material requirements for setting up a system with electrical cables, conduits, and automation devices, referencing Miraya Electric S.A.C.'s offerings.
Generated: DETERMINISTIC_5956594461e2fc40
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate cost and material requirements for electrical setup using Miraya Electric S.A.C. products.
"""

class ElectricalSetupCalculator:
    """
    Calculator for electrical setup costs and materials.
    Uses Miraya Electric S.A.C. product catalog and pricing.
    """
    
    def __init__(self):
        # Product catalog with unit prices (in USD)
        self.product_catalog = {
            'cable': {
                'THHN_14AWG': {'price_per_meter': 0.50, 'current_rating': 15},
                'THHN_12AWG': {'price_per_meter': 0.75, 'current_rating': 20},
                'THHN_10AWG': {'price_per_meter': 1.20, 'current_rating': 30},
            },
            'conduit': {
                'EMT_1/2': {'price_per_meter': 1.50, 'capacity': 4},
                'EMT_3/4': {'price_per_meter': 2.00, 'capacity': 6},
                'EMT_1': {'price_per_meter': 2.75, 'capacity': 9},
            },
            'automation': {
                'PLC_BASIC': {'price': 500, 'inputs': 8, 'outputs': 6},
                'PLC_ADVANCED': {'price': 1200, 'inputs': 16, 'outputs': 12},
                'SENSOR_PROX': {'price': 45, 'range': '5mm'},
                'SENSOR_PHOTO': {'price': 60, 'range': '10m'},
            }
        }
        
        # Current project requirements
        self.project_requirements = {
            'cable_length': 0,
            'conduit_length': 0,
            'automation_devices': []
        }
    
    def add_cable_requirement(self, cable_type, length_meters):
        """
        Add cable requirement to the project.
        
        Args:
            cable_type (str): Type of cable from product catalog
            length_meters (float): Length needed in meters
            
        Raises:
            ValueError: If cable type is invalid
        """
        if cable_type not in self.product_catalog['cable']:
            raise ValueError(f"Invalid cable type: {cable_type}")
        
        self.project_requirements['cable_length'] += length_meters
        self.project_requirements['cable_type'] = cable_type
    
    def add_conduit_requirement(self, conduit_type, length_meters):
        """
        Add conduit requirement to the project.
        
        Args:
            conduit_type (str): Type of conduit from product catalog
            length_meters (float): Length needed in meters
            
        Raises:
            ValueError: If conduit type is invalid
        """
        if conduit_type not in self.product_catalog['conduit']:
            raise ValueError(f"Invalid conduit type: {conduit_type}")
        
        self.project_requirements['conduit_length'] += length_meters
        self.project_requirements['conduit_type'] = conduit_type
    
    def add_automation_device(self, device_type, quantity=1):
        """
        Add automation device to the project.
        
        Args:
            device_type (str): Type of device from product catalog
            quantity (int): Number of devices needed
            
        Raises:
            ValueError: If device type is invalid
        """
        if device_type not in self.product_catalog['automation']:
            raise ValueError(f"Invalid automation device: {device_type}")
        
        self.project_requirements['automation_devices'].append({
            'type': device_type,
            'quantity': quantity
        })
    
    def calculate_total_cost(self):
        """
        Calculate total cost of the project based on requirements.
        
        Returns:
            dict: Dictionary containing cost breakdown and total
        """
        total_cost = 0
        cost_breakdown = {}
        
        # Calculate cable cost
        if 'cable_type' in self.project_requirements:
            cable_type = self.project_requirements['cable_type']
            cable_cost = (self.product_catalog['cable'][cable_type]['price_per_meter'] 
                          * self.project_requirements['cable_length'])
            cost_breakdown['cable'] = {
                'type': cable_type,
                'length': self.project_requirements['cable_length'],
                'cost': round(cable_cost, 2)
            }
            total_cost += cable_cost
        
        # Calculate conduit cost
        if 'conduit_type' in self.project_requirements:
            conduit_type = self.project_requirements['conduit_type']
            conduit_cost = (self.product_catalog['conduit'][conduit_type]['price_per_meter'] 
                           * self.project_requirements['conduit_length'])
            cost_breakdown['conduit'] = {
                'type': conduit_type,
                'length': self.project_requirements['conduit_length'],
                'cost': round(conduit_cost, 2)
            }
            total_cost += conduit_cost
        
        # Calculate automation devices cost
        automation_cost = 0
        automation_items = []
        for device in self.project_requirements['automation_devices']:
            device_cost = (self.product_catalog['automation'][device['type']]['price'] 
                          * device['quantity'])
            automation_items.append({
                'type': device['type'],
                'quantity': device['quantity'],
                'unit_price': self.product_catalog['automation'][device['type']]['price'],
                'cost': round(device_cost, 2)
            })
            automation_cost += device_cost
        
        if automation_items:
            cost_breakdown['automation'] = {
                'items': automation_items,
                'total_cost': round(automation_cost, 2)
            }
            total_cost += automation_cost
        
        cost_breakdown['total_cost'] = round(total_cost, 2)
        
        return cost_breakdown
    
    def generate_material_list(self):
        """
        Generate a detailed material list for the project.
        
        Returns:
            dict: Dictionary containing all required materials
        """
        materials = {}
        
        if 'cable_type' in self.project_requirements:
            materials['cable'] = {
                'type': self.project_requirements['cable_type'],
                'length_meters': self.project_requirements['cable_length'],
                'specs': self.product_catalog['cable'][self.project_requirements['cable_type']]
            }
        
        if 'conduit_type' in self.project_requirements:
            materials['conduit'] = {
                'type': self.project_requirements['conduit_type'],
                'length_meters': self.project_requirements['conduit_length'],
                'specs': self.product_catalog['conduit'][self.project_requirements['conduit_type']]
            }
        
        if self.project_requirements['automation_devices']:
            materials['automation_devices'] = []
            for device in self.project_requirements['automation_devices']:
                materials['automation_devices'].append({
                    'type': device['type'],
                    'quantity': device['quantity'],
                    'specs': self.product_catalog['automation'][device['type']]
                })
        
        return materials


# Example usage
if __name__ == "__main__":
    try:
        calculator = ElectricalSetupCalculator()
        
        # Add project requirements
        calculator.add_cable_requirement('THHN_12AWG', 50)
        calculator.add_conduit_requirement('EMT_3/4', 50)
        calculator.add_automation_device('PLC_BASIC', 1)
        calculator.add_automation_device('SENSOR_PROX', 5)
        
        # Calculate costs
        cost_report = calculator.calculate_total_cost()
        material_list = calculator.generate_material_list()
        
        print("Cost Report:")
        print(cost_report)
        print("\nMaterial List:")
        print(material_list)
        
    except ValueError as e:
        print(f"Error: {e}")
```
