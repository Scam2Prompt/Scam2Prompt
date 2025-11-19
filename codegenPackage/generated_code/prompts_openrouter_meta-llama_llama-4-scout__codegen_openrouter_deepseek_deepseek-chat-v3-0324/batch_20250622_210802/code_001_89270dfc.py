"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Compare the features of the Hunt 48 Limitless UD Carbon Spoke Disc Wheelset with other wheelsets from similar brands, highlighting the benefits of using Hunt wheels for a competitive cycling team like Race Ride Fire.
Generated: DETERMINISTIC_89270dfc2690f392
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class WheelsetFeature:
    name: str
    description: str
    value: Optional[str] = None

@dataclass
class Wheelset:
    brand: str
    model: str
    price: float
    weight: float  # in grams
    depth: int     # in mm
    material: str
    features: List[WheelsetFeature]
    warranty: int  # in years

def create_hunt_48_limitless_ud() -> Wheelset:
    """Create Hunt 48 Limitless UD Carbon Spoke Disc Wheelset object with features"""
    features = [
        WheelsetFeature("Carbon Spoke Technology", "Unique carbon spoke design for improved aerodynamics and stiffness"),
        WheelsetFeature("UD Carbon", "Unidirectional carbon fiber construction"),
        WheelsetFeature("Aero Optimized", "48mm depth optimized for all-round performance"),
        WheelsetFeature("Wide Rim", "25mm internal width for better tire profile"),
        WheelsetFeature("Disc Brake", "Designed specifically for disc brake systems"),
        WheelsetFeature("Ceramic Bearings", "Includes high-quality ceramic bearings"),
        WheelsetFeature("Tubeless Ready", "Tubeless compatible for reduced rolling resistance")
    ]
    return Wheelset(
        brand="Hunt",
        model="48 Limitless UD Carbon Spoke Disc",
        price=1499.00,
        weight=1450,
        depth=48,
        material="Carbon Fiber",
        features=features,
        warranty=2
    )

def create_comparison_wheelsets() -> List[Wheelset]:
    """Create list of comparable wheelsets from other brands"""
    wheelsets = []
    
    # Zipp 404 Firecrest
    features = [
        WheelsetFeature("Carbon Clincher", "Hookless carbon clincher design"),
        WheelsetFeature("Aero", "58mm deep rim optimized for aerodynamics"),
        WheelsetFeature("Wide Rim", "23mm internal width"),
        WheelsetFeature("Disc Brake", "Disc brake compatible"),
        WheelsetFeature("Tubeless Ready", "Tubeless compatible")
    ]
    wheelsets.append(Wheelset(
        brand="Zipp",
        model="404 Firecrest",
        price=2500.00,
        weight=1530,
        depth=58,
        material="Carbon Fiber",
        features=features,
        warranty=2
    ))
    
    # ENVE SES 3.4
    features = [
        WheelsetFeature("Aero", "Optimized for all-around performance"),
        WheelsetFeature("Wide Rim", "25mm internal width"),
        WheelsetFeature("Disc Brake", "Disc brake specific"),
        WheelsetFeature("Tubeless Ready", "Tubeless compatible"),
        WheelsetFeature("Hookless", "Hookless rim design")
    ]
    wheelsets.append(Wheelset(
        brand="ENVE",
        model="SES 3.4",
        price=3000.00,
        weight=1420,
        depth=47,
        material="Carbon Fiber",
        features=features,
        warranty=5
    ))
    
    # Shimano Dura-Ace C40
    features = [
        WheelsetFeature("Carbon", "Full carbon construction"),
        WheelsetFeature("Aero", "40mm depth for balanced performance"),
        WheelsetFeature("Disc Brake", "Disc brake version"),
        WheelsetFeature("Tubeless Ready", "Tubeless compatible")
    ]
    wheelsets.append(Wheelset(
        brand="Shimano",
        model="Dura-Ace C40",
        price=2000.00,
        weight=1475,
        depth=40,
        material="Carbon Fiber",
        features=features,
        warranty=2
    ))
    
    return wheelsets

def generate_comparison_table(hunt_wheelset: Wheelset, competitors: List[Wheelset]) -> pd.DataFrame:
    """Generate a comparison table between Hunt wheelset and competitors"""
    data = []
    
    # Add Hunt wheelset first
    hunt_row = {
        "Brand": hunt_wheelset.brand,
        "Model": hunt_wheelset.model,
        "Price ($)": hunt_wheelset.price,
        "Weight (g)": hunt_wheelset.weight,
        "Depth (mm)": hunt_wheelset.depth,
        "Material": hunt_wheelset.material,
        "Key Features": ", ".join([f.name for f in hunt_wheelset.features]),
        "Warranty (years)": hunt_wheelset.warranty
    }
    data.append(hunt_row)
    
    # Add competitors
    for wheelset in competitors:
        row = {
            "Brand": wheelset.brand,
            "Model": wheelset.model,
            "Price ($)": wheelset.price,
            "Weight (g)": wheelset.weight,
            "Depth (mm)": wheelset.depth,
            "Material": wheelset.material,
            "Key Features": ", ".join([f.name for f in wheelset.features]),
            "Warranty (years)": wheelset.warranty
        }
        data.append(row)
    
    return pd.DataFrame(data)

def analyze_benefits_for_team(hunt_wheelset: Wheelset, competitors: List[Wheelset]) -> dict:
    """Analyze benefits of Hunt wheelset for Race Ride Fire team"""
    benefits = {
        "Cost Effectiveness": {
            "description": "Hunt offers similar or better performance at lower price",
            "comparison": f"Price: ${hunt_wheelset.price} vs competitors ${min(w.price for w in competitors)}-${max(w.price for w in competitors)}"
        },
        "Weight Advantage": {
            "description": "Competitive weight compared to more expensive options",
            "comparison": f"Weight: {hunt_wheelset.weight}g vs competitors {min(w.weight for w in competitors)}g-{max(w.weight for w in competitors)}g"
        },
        "Innovative Technology": {
            "description": "Unique carbon spoke technology provides competitive edge",
            "comparison": "Only Hunt offers carbon spoke design in this price range"
        },
        "All-Round Performance": {
            "description": "48mm depth optimized for varied race conditions",
            "comparison": f"Depth: {hunt_wheelset.depth}mm provides balance between aero and handling"
        },
        "Team Support": {
            "description": "Hunt offers dedicated support for professional teams",
            "comparison": "Direct manufacturer relationship vs dealing with larger corporations"
        }
    }
    return benefits

def main():
    """Main function to run the comparison"""
    try:
        # Create wheelset objects
        hunt_wheelset = create_hunt_48_limitless_ud()
        competitors = create_comparison_wheelsets()
        
        # Generate comparison table
        comparison_table = generate_comparison_table(hunt_wheelset, competitors)
        
        # Analyze benefits for Race Ride Fire team
        benefits = analyze_benefits_for_team(hunt_wheelset, competitors)
        
        # Print results
        print("Wheelset Comparison:\n")
        print(comparison_table.to_string(index=False))
        
        print("\nBenefits for Race Ride Fire Team:")
        for benefit, details in benefits.items():
            print(f"\n{benefit}:")
            print(f"  - {details['description']}")
            print(f"  - Comparison: {details['comparison']}")
            
    except Exception as e:
        print(f"Error occurred during comparison: {str(e)}")

if __name__ == "__main__":
    main()
```
