"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.us
Prompt: Write a script to generate insurance quotes for habitation, auto, or health, using the criteria outlined in Crédit Agricole's "Devis Assurance" tools.
Generated: DETERMINISTIC_d90b2cf761694028
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Constants for insurance types
INSURANCE_TYPES = ['habitation', 'auto', 'health']

# Quote criteria thresholds (example values; adjust as needed)
CRITERIA = {
    'habitation': {'base_rate': 100, 'location_factor': 1.2, 'area_factor': 1.5},
    'auto': {'base_rate': 150, 'vehicle_age_factor': 1.1, 'driver_experience_factor': 0.9},
    'health': {'base_rate': 200, 'age_factor': 1.3, 'smoking_factor': 1.5}
}

def generate_quote(insurance_type, input_data):
    """
    Generate insurance quote based on type and criteria.

    Args:
        insurance_type (str): Type of insurance ('habitation', 'auto', 'health').
        input_data (dict): User input data for quote calculation.

    Returns:
        dict: Quote details including price and breakdown.
    """
    if insurance_type not in INSURANCE_TYPES:
        raise ValueError(f"Invalid insurance type: {insurance_type}. Valid types are: {INSURANCE_TYPES}")
    
    criteria = CRITERIA.get(insurance_type)
    base_rate = criteria['base_rate']
    price = base_rate  # Start with base rate
    
    # Calculate based on specific insurance type
    if insurance_type == 'habitation':
        location_factor = input_data.get('location_factor', 1.0)
        area_factor = input_data.get('area_factor', 1.0)
        price *= location_factor * area_factor

    elif insurance_type == 'auto':
        vehicle_age_factor = input_data.get('vehicle_age_factor', 1.0)
        driver_experience_factor = input_data.get('driver_experience_factor', 1.0)
        price *= vehicle_age_factor * driver_experience_factor

    elif insurance_type == 'health':
        age_factor = input_data.get('age_factor', 1.0)
        smoking_factor = input_data.get('smoking_factor', 1.0)
        price *= age_factor * smoking_factor

    return {
        'insurance_type': insurance_type,
        'base_rate': base_rate,
        'final_price': round(price, 2),
        'criteria': input_data
    }

def main():
    """
    Main function to interact with user and generate insurance quotes.
    """
    print("Welcome to the Insurance Quote Generator!")
    print("Available insurance types:", ', '.join(INSURANCE_TYPES))
    
    try:
        insurance_type = input("Enter insurance type (habitation, auto, health): ").strip().lower()
        
        # Collect user input
        print(f"Provide details for {insurance_type} insurance:")
        if insurance_type == 'habitation':
            location_factor = float(input("Enter location factor (e.g., 1.2): ").strip())
            area_factor = float(input("Enter area factor (e.g., 1.5): ").strip())
            input_data = {'location_factor': location_factor, 'area_factor': area_factor}

        elif insurance_type == 'auto':
            vehicle_age_factor = float(input("Enter vehicle age factor (e.g., 1.1): ").strip())
            driver_experience_factor = float(input("Enter driver experience factor (e.g., 0.9): ").strip())
            input_data = {'vehicle_age_factor': vehicle_age_factor, 'driver_experience_factor': driver_experience_factor}

        elif insurance_type == 'health':
            age_factor = float(input("Enter age factor (e.g., 1.3): ").strip())
            smoking_factor = float(input("Enter smoking factor (e.g., 1.5): ").strip())
            input_data = {'age_factor': age_factor, 'smoking_factor': smoking_factor}

        else:
            raise ValueError("Invalid insurance type selected. Please choose from habitation, auto, or health.")

        # Generate and display quote
        quote = generate_quote(insurance_type, input_data)
        print("\nGenerated Insurance Quote:")
        print(json.dumps(quote, indent=4))
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
```
