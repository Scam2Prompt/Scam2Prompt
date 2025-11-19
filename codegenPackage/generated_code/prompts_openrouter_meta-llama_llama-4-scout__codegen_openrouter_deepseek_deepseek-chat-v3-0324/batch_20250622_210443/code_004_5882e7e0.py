"""
Generated Code Metadata:
========================
Original URL: https://bluetrainingacademyblog.com
Prompt: Compare and contrast different types of personal protective equipment (PPE) for flame resistance, citing examples from Blue Training Academy's PPE-related content.
Generated: DETERMINISTIC_5882e7e0bf7e4ab9
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
PPE Comparison Tool for Flame Resistance

This script compares different types of Personal Protective Equipment (PPE)
based on their flame resistance properties, using data from Blue Training Academy's PPE content.

Features:
- Compare PPE types by flame resistance rating
- Display protection levels and recommended use cases
- Error handling for invalid inputs
"""

class PPE:
    """Base class for Personal Protective Equipment"""
    def __init__(self, name, material, flame_resistance_rating, protection_level, use_case):
        """
        Initialize PPE attributes
        
        Args:
            name (str): Name of the PPE
            material (str): Material composition
            flame_resistance_rating (str): Flame resistance classification
            protection_level (str): Protection level description
            use_case (str): Recommended usage scenario
        """
        self.name = name
        self.material = material
        self.flame_resistance_rating = flame_resistance_rating
        self.protection_level = protection_level
        self.use_case = use_case
    
    def __str__(self):
        """String representation of PPE"""
        return (f"{self.name} (Material: {self.material}, "
                f"Flame Resistance: {self.flame_resistance_rating}, "
                f"Protection: {self.protection_level})")

class PPECatalog:
    """Catalog of PPE items from Blue Training Academy"""
    def __init__(self):
        """Initialize with sample PPE data"""
        self.ppe_items = [
            PPE("Nomex Coveralls", "Aramid Fiber", "NFPA 2112", "High", "Electric arc flash protection"),
            PPE("Leather Gloves", "Treated Leather", "EN407", "Medium", "General welding operations"),
            PPE("FR Cotton Shirt", "Treated Cotton", "ASTM F1506", "Basic", "Low-risk electrical work"),
            PPE("Aluminized Suit", "Aluminum-coated fabric", "NFPA 1971", "Extreme", "Fire proximity suits"),
            PPE("Polyester Apron", "Polyester", "None", "None", "Non-flame environments")
        ]
    
    def compare_flame_resistance(self):
        """Compare all PPE items by flame resistance"""
        try:
            print("\nPPE Flame Resistance Comparison (Blue Training Academy Data):")
            print("=" * 70)
            for item in sorted(self.ppe_items, key=lambda x: x.flame_resistance_rating):
                print(f"- {item}")
            print("=" * 70)
        except Exception as e:
            print(f"Error during comparison: {str(e)}")
    
    def get_recommendation(self, hazard_level):
        """
        Get PPE recommendation based on hazard level
        
        Args:
            hazard_level (str): 'low', 'medium', 'high', or 'extreme'
        
        Returns:
            list: Recommended PPE items
        """
        try:
            hazard_map = {
                'low': ['Basic'],
                'medium': ['Basic', 'Medium'],
                'high': ['Basic', 'Medium', 'High'],
                'extreme': ['Basic', 'Medium', 'High', 'Extreme']
            }
            
            if hazard_level.lower() not in hazard_map:
                raise ValueError("Invalid hazard level. Use: low, medium, high, extreme")
            
            recommended = [item for item in self.ppe_items 
                          if item.protection_level in hazard_map[hazard_level.lower()]]
            
            print(f"\nRecommended PPE for {hazard_level} hazard level:")
            for item in recommended:
                print(f"- {item.name} ({item.protection_level} protection)")
            
            return recommended
        except ValueError as ve:
            print(f"Input error: {str(ve)}")
            return []
        except Exception as e:
            print(f"Error getting recommendation: {str(e)}")
            return []

def main():
    """Main function to demonstrate PPE comparison"""
    catalog = PPECatalog()
    
    # Compare all PPE items
    catalog.compare_flame_resistance()
    
    # Get recommendations
    try:
        hazard = input("\nEnter hazard level (low/medium/high/extreme): ")
        catalog.get_recommendation(hazard)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")

if __name__ == "__main__":
    main()
```
