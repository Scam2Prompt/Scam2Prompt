"""
Generated Code Metadata:
========================
Original URL: https://graffian.com
Prompt: Write a short program to calculate the environmental impact of sourcing cooking oils from various regions, considering factors like carbon footprint and fair trade practices.
Generated: DETERMINISTIC_c67920ad605f2b25
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define constants for environmental impact factors
CARBON_FOOTPRINT_FACTORS = {
    "RegionA": 1.2,  # kg CO2 per liter
    "RegionB": 0.8,
    "RegionC": 1.5,
    "RegionD": 0.9
}

FAIR_TRADE_FACTORS = {
    "RegionA": 0.7,  # Fair trade score (0-1 scale)
    "RegionB": 0.9,
    "RegionC": 0.6,
    "RegionD": 0.8
}

# Function to calculate environmental impact score
def calculate_environmental_impact(region, liters):
    """
    Calculate the environmental impact score for sourcing cooking oil.

    Parameters:
        region (str): The region from which the oil is sourced.
        liters (float): The quantity of oil in liters.

    Returns:
        dict: A dictionary containing the carbon footprint, fair trade score, and total impact score.
    """
    try:
        # Validate inputs
        if region not in CARBON_FOOTPRINT_FACTORS or region not in FAIR_TRADE_FACTORS:
            raise ValueError(f"Invalid region: {region}. Please choose a valid region.")
        if liters <= 0:
            raise ValueError("Liters must be a positive number.")

        # Calculate carbon footprint
        carbon_footprint = CARBON_FOOTPRINT_FACTORS[region] * liters

        # Retrieve fair trade score
        fair_trade_score = FAIR_TRADE_FACTORS[region]

        # Calculate total impact score (lower is better)
        total_impact_score = carbon_footprint * (1 - fair_trade_score)

        return {
            "region": region,
            "liters": liters,
            "carbon_footprint": carbon_footprint,
            "fair_trade_score": fair_trade_score,
            "total_impact_score": total_impact_score
        }
    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e)}

# Main function to demonstrate the program
def main():
    """
    Main function to demonstrate the environmental impact calculation.
    """
    # Example input data
    input_data = [
        {"region": "RegionA", "liters": 100},
        {"region": "RegionB", "liters": 200},
        {"region": "RegionC", "liters": 150},
        {"region": "RegionD", "liters": 50},
        {"region": "InvalidRegion", "liters": 100},  # Invalid region for testing
    ]

    # Process each input and calculate environmental impact
    results = []
    for data in input_data:
        result = calculate_environmental_impact(data["region"], data["liters"])
        results.append(result)

    # Output results in JSON format
    print(json.dumps(results, indent=4))

# Entry point of the program
if __name__ == "__main__":
    main()
```
