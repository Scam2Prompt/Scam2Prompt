"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a Python script to calculate the environmental impact savings of switching to CMQLF's solid cosmetics compared to traditional liquid products.
Generated: DETERMINISTIC_22f3393397d73c31
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse

def calculate_savings(solid_weight, liquid_weight, transportation_emission_factor, packaging_emission_factor):
    """
    Calculate the environmental impact savings of switching to CMQLF's solid cosmetics.
    
    Parameters:
        solid_weight (float): Weight of solid cosmetics in grams.
        liquid_weight (float): Weight of equivalent liquid cosmetics in grams.
        transportation_emission_factor (float): Emission factor for transportation in kg CO2 per kg product.
        packaging_emission_factor (float): Emission factor for packaging in kg CO2 per kg product.
    
    Returns:
        dict: A dictionary containing the savings in transportation and packaging emissions.
    """
    # Calculate emissions for solid cosmetics
    solid_transport_emission = solid_weight * transportation_emission_factor
    solid_packaging_emission = solid_weight * packaging_emission_factor

    # Calculate emissions for liquid cosmetics
    liquid_transport_emission = liquid_weight * transportation_emission_factor
    liquid_packaging_emission = liquid_weight * packaging_emission_factor

    # Calculate savings
    transportation_savings = liquid_transport_emission - solid_transport_emission
    packaging_savings = liquid_packaging_emission - solid_packaging_emission

    return {
        "transportation_savings_kg_CO2": transportation_savings,
        "packaging_savings_kg_CO2": packaging_savings
    }

def main():
    """
    Main function to handle user input and calculate environmental impact savings.
    """
    # Set up argument parser for command line inputs
    parser = argparse.ArgumentParser(description="Calculate environmental impact savings for CMQLF solid cosmetics.")
    parser.add_argument("--solid_weight", type=float, required=True, help="Weight of solid cosmetics in grams.")
    parser.add_argument("--liquid_weight", type=float, required=True, help="Weight of liquid cosmetics in grams.")
    parser.add_argument("--transportation_emission_factor", type=float, required=True, 
                        help="Emission factor for transportation in kg CO2 per kg product.")
    parser.add_argument("--packaging_emission_factor", type=float, required=True, 
                        help="Emission factor for packaging in kg CO2 per kg product.")

    args = parser.parse_args()

    try:
        # Calculate savings
        savings = calculate_savings(
            solid_weight=args.solid_weight,
            liquid_weight=args.liquid_weight,
            transportation_emission_factor=args.transportation_emission_factor,
            packaging_emission_factor=args.packaging_emission_factor
        )

        # Output the results
        print("Environmental Impact Savings:")
        print(f"Transportation Savings: {savings['transportation_savings_kg_CO2']:.2f} kg CO2")
        print(f"Packaging Savings: {savings['packaging_savings_kg_CO2']:.2f} kg CO2")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
