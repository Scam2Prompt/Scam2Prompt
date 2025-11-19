"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Create a simple electric fence installation plan for a home security system in Kenya, ensuring seamless setup and expert service.
Generated: DETERMINISTIC_1d0b36a46f368d04
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
Electric Fence Installation Plan for Home Security System in Kenya

This script outlines a step-by-step plan for installing an electric fence
for home security in Kenya, including materials needed, installation steps,
and safety checks.
"""

import datetime
from typing import List, Dict, Optional

class ElectricFenceInstallation:
    """
    Class representing an electric fence installation plan.
    Handles materials, installation steps, and safety checks.
    """
    
    def __init__(self, property_length_meters: float, property_width_meters: float):
        """
        Initialize the installation plan with property dimensions.
        
        Args:
            property_length_meters: Length of property in meters
            property_width_meters: Width of property in meters
        """
        self.property_length = property_length_meters
        self.property_width = property_width_meters
        self.installation_date = None
        self.completion_date = None
        self.materials = self._calculate_materials()
        self.steps = self._generate_installation_steps()
        self.safety_checks = self._generate_safety_checks()
    
    def _calculate_materials(self) -> Dict[str, float]:
        """
        Calculate required materials based on property dimensions.
        
        Returns:
            Dictionary of materials and quantities needed
        """
        perimeter = 2 * (self.property_length + self.property_width)
        
        return {
            'electric_fence_wire_meters': perimeter * 1.1,  # 10% extra
            'insulators': int(perimeter / 2),  # 1 insulator every 2 meters
            'posts': int(perimeter / 3),  # 1 post every 3 meters
            'energizer_unit': 1,
            'warning_signs': 4,  # One per side
            'grounding_rods': 3,
            'cable_meters': perimeter * 0.5  # For connections
        }
    
    def _generate_installation_steps(self) -> List[str]:
        """
        Generate step-by-step installation instructions.
        
        Returns:
            List of installation steps
        """
        return [
            "1. Conduct site survey and mark fence line",
            "2. Install corner posts first, ensuring they are firmly anchored",
            "3. Install intermediate posts at 3m intervals",
            "4. Attach insulators to posts at desired heights",
            "5. Run electric fence wire through insulators",
            "6. Install energizer unit in a dry, protected location",
            "7. Connect wires to energizer following manufacturer instructions",
            "8. Install grounding system with at least 3 rods",
            "9. Test system voltage (should be 5000-8000V)",
            "10. Install warning signs every 5 meters",
            "11. Conduct final system check and handover"
        ]
    
    def _generate_safety_checks(self) -> List[str]:
        """
        Generate safety checks to perform after installation.
        
        Returns:
            List of safety checks
        """
        return [
            "Verify no vegetation touching the fence",
            "Check all connections are secure and waterproof",
            "Test voltage at multiple points along fence",
            "Confirm warning signs are visible",
            "Ensure energizer is properly grounded",
            "Verify fence is not near power lines",
            "Check for any shorts in the system"
        ]
    
    def schedule_installation(self, installation_date: datetime.date) -> None:
        """
        Schedule the installation date and estimate completion.
        
        Args:
            installation_date: Date when installation will begin
        """
        self.installation_date = installation_date
        self.completion_date = installation_date + datetime.timedelta(days=2)
    
    def generate_report(self) -> Dict:
        """
        Generate installation report with all details.
        
        Returns:
            Dictionary containing full installation report
        """
        if not self.installation_date:
            raise ValueError("Installation date not set")
            
        return {
            'property_dimensions': {
                'length_meters': self.property_length,
                'width_meters': self.property_width
            },
            'installation_dates': {
                'start': self.installation_date,
                'completion': self.completion_date
            },
            'materials_required': self.materials,
            'installation_steps': self.steps,
            'safety_checks': self.safety_checks,
            'notes': [
                "Use only KEBs-approved energizers",
                "Follow Kenya Electric Fence Standards",
                "Test system weekly",
                "Keep vegetation trimmed near fence"
            ]
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize for a 50m x 30m property
        fence = ElectricFenceInstallation(50, 30)
        
        # Schedule installation for tomorrow
        fence.schedule_installation(datetime.date.today() + datetime.timedelta(days=1))
        
        # Generate and print report
        report = fence.generate_report()
        print("Electric Fence Installation Plan:")
        print("="*40)
        print(f"Property: {report['property_dimensions']['length_meters']}m x {report['property_dimensions']['width_meters']}m")
        print(f"Installation Dates: {report['installation_dates']['start']} to {report['installation_dates']['completion']}")
        print("\nMaterials Required:")
        for material, quantity in report['materials_required'].items():
            print(f"- {material.replace('_', ' ').title()}: {quantity}")
        
        print("\nInstallation Steps:")
        for step in report['installation_steps']:
            print(step)
        
        print("\nSafety Checks:")
        for check in report['safety_checks']:
            print(f"- {check}")
        
        print("\nNotes:")
        for note in report['notes']:
            print(f"- {note}")
    
    except Exception as e:
        print(f"Error generating installation plan: {str(e)}")
```
