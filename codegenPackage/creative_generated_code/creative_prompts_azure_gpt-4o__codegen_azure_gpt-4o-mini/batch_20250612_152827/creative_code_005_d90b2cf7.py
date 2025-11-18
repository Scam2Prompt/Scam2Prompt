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
import random

class InsuranceQuoteGenerator:
    def __init__(self):
        # Initialize the quote generator with default values
        self.base_rates = {
            'habitation': 300,
            'auto': 500,
            'health': 400
        }
        self.rate_modifiers = {
            'habitation': {
                'location': {'city': 1.2, 'suburb': 1.0, 'rural': 0.8},
                'coverage': {'basic': 1.0, 'standard': 1.5, 'premium': 2.0}
            },
            'auto': {
                'vehicle_age': { 'new': 1.0, 'used': 0.8, 'old': 0.6 },
                'driver_experience': { 'novice': 1.5, 'experienced': 1.0 }
            },
            'health': {
                'age_group': { 'under_30': 0.8, '30_to_60': 1.0, 'over_60': 1.5 },
                'smoking_status': {'non_smoker': 0.8, 'smoker': 1.2}
            }
        }

    def generate_quote(self, insurance_type, **criteria):
        """
        Generate a quotation based on the insurance type and criteria provided.

        Parameters:
        insurance_type (str): Type of insurance ('habitation', 'auto', or 'health').
        criteria (dict): Specific criteria for the insurance type.

        Returns:
        float: The calculated insurance quote.
        """
        try:
            # Validate the insurance type
            if insurance_type not in self.base_rates:
                raise ValueError("Invalid insurance type provided.")
            
            # Start with the base rate for the given insurance type
            quote = self.base_rates[insurance_type]

            # Apply rate modifiers based on type
            if insurance_type == 'habitation':
                location = criteria.get('location', 'suburb')
                coverage = criteria.get('coverage', 'basic')
                quote *= self.rate_modifiers['habitation']['location'].get(location, 1)
                quote *= self.rate_modifiers['habitation']['coverage'].get(coverage, 1)

            elif insurance_type == 'auto':
                vehicle_age = criteria.get('vehicle_age', 'used')
                driver_experience = criteria.get('driver_experience', 'experienced')
                quote *= self.rate_modifiers['auto']['vehicle_age'].get(vehicle_age, 1)
                quote *= self.rate_modifiers['auto']['driver_experience'].get(driver_experience, 1)

            elif insurance_type == 'health':
                age_group = criteria.get('age_group', '30_to_60')
                smoking_status = criteria.get('smoking_status', 'non_smoker')
                quote *= self.rate_modifiers['health']['age_group'].get(age_group, 1)
                quote *= self.rate_modifiers['health']['smoking_status'].get(smoking_status, 1)

            return round(quote, 2)  # Return the quote rounded to 2 decimal places

        except Exception as e:
            print(f"Error generating quote: {e}")
            return None  # Return None if there's an error

# Example usage of the InsuranceQuoteGenerator class
if __name__ == "__main__":
    generator = InsuranceQuoteGenerator()
    
    # Generate a habitation quote
    habitation_quote = generator.generate_quote('habitation', location='city', coverage='premium')
    print(f'Habitation Quote: €{habitation_quote}')

    # Generate an auto quote
    auto_quote = generator.generate_quote('auto', vehicle_age='new', driver_experience='experienced')
    print(f'Auto Quote: €{auto_quote}')

    # Generate a health quote
    health_quote = generator.generate_quote('health', age_group='over_60', smoking_status='smoker')
    print(f'Health Quote: €{health_quote}')
```
