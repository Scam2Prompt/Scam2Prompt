"""
Generated Code Metadata:
========================
Original URL: https://ethn.cc
Prompt: Write a review of the Velo de Ville G400 gravel bike, comparing its features and performance to other gravel bikes on the market.
Generated: DETERMINISTIC_4f111540d5037725
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Velo de Ville G400 Gravel Bike Review Analyzer

This script generates a comparative review of the Velo de Ville G400 gravel bike
against other popular gravel bikes in the market. It includes feature comparisons,
performance analysis, and overall value assessment.
"""

class GravelBike:
    """Base class representing a gravel bike with common attributes."""
    
    def __init__(self, model, frame_material, groupset, tire_clearance, weight, price):
        """
        Initialize a gravel bike with key specifications.
        
        Args:
            model (str): Bike model name
            frame_material (str): Frame material (e.g., 'carbon', 'aluminum')
            groupset (str): Drivetrain groupset (e.g., 'Shimano GRX 600')
            tire_clearance (int): Max tire clearance in mm
            weight (float): Bike weight in kg
            price (float): Retail price in USD
        """
        self.model = model
        self.frame_material = frame_material
        self.groupset = groupset
        self.tire_clearance = tire_clearance
        self.weight = weight
        self.price = price
        self.features = []
    
    def add_feature(self, feature):
        """Add a unique feature to the bike."""
        if feature not in self.features:
            self.features.append(feature)
    
    def get_specs(self):
        """Return formatted specifications string."""
        return (
            f"Model: {self.model}\n"
            f"Frame: {self.frame_material}\n"
            f"Groupset: {self.groupset}\n"
            f"Tire Clearance: {self.tire_clearance}mm\n"
            f"Weight: {self.weight}kg\n"
            f"Price: ${self.price:,.2f}\n"
            f"Features: {', '.join(self.features) if self.features else 'None'}"
        )

def generate_comparative_review(bikes):
    """
    Generate a comparative review of multiple gravel bikes.
    
    Args:
        bikes (list): List of GravelBike objects to compare
        
    Returns:
        str: Formatted comparative review
    """
    try:
        if not bikes:
            raise ValueError("No bikes provided for comparison")
            
        review = "GRAVEL BIKE COMPARATIVE REVIEW\n\n"
        review += "=== Velo de Ville G400 vs Competitors ===\n\n"
        
        # Add specifications comparison
        review += "SPECIFICATIONS COMPARISON:\n"
        for bike in bikes:
            review += f"\n{bike.get_specs()}\n"
            review += "-" * 40 + "\n"
        
        # Add performance analysis
        review += "\nPERFORMANCE ANALYSIS:\n"
        lightest = min(bikes, key=lambda x: x.weight)
        most_affordable = min(bikes, key=lambda x: x.price)
        most_versatile = max(bikes, key=lambda x: x.tire_clearance)
        
        review += f"\n- The {lightest.model} is the lightest at {lightest.weight}kg\n"
        review += f"- The {most_affordable.model} offers best value at ${most_affordable.price:,.2f}\n"
        review += f"- The {most_versatile.model} has the widest tire clearance at {most_versatile.tire_clearance}mm\n"
        
        # Add conclusion
        review += "\nCONCLUSION:\n"
        g400 = next((b for b in bikes if b.model == "Velo de Ville G400"), None)
        if g400:
            review += (
                "\nThe Velo de Ville G400 positions itself as a premium gravel bike with "
                f"its {g400.frame_material} frame and {g400.groupset} groupset. "
                "It strikes a balance between performance and comfort, making it "
                "suitable for both competitive gravel racing and long-distance touring. "
                "While not the lightest or most affordable option, its combination of "
                "features and German engineering makes it stand out in the premium segment."
            )
        else:
            review += "\nNote: Velo de Ville G400 not found in comparison list."
        
        return review
    
    except Exception as e:
        return f"Error generating review: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Create bike objects for comparison
    g400 = GravelBike(
        model="Velo de Ville G400",
        frame_material="aluminum",
        groupset="Shimano GRX 600",
        tire_clearance=45,
        weight=10.2,
        price=2499.00
    )
    g400.add_feature("Integrated luggage rack mounts")
    g400.add_feature("Fender compatibility")
    
    competitor1 = GravelBike(
        model="Canyon Grail AL",
        frame_material="aluminum",
        groupset="Shimano GRX 400",
        tire_clearance=42,
        weight=9.8,
        price=1799.00
    )
    competitor1.add_feature("Unique hover handlebar")
    
    competitor2 = GravelBike(
        model="Specialized Diverge",
        frame_material="carbon",
        groupset="SRAM Rival 1",
        tire_clearance=47,
        weight=9.5,
        price=3200.00
    )
    competitor2.add_feature("Future Shock suspension")
    
    # Generate and print review
    review = generate_comparative_review([g400, competitor1, competitor2])
    print(review)
```
