"""
Generated Code Metadata:
========================
Original URL: https://schengenapostille.com
Prompt: Write code to generate a template for a Special Power of Attorney (SPA) for minors, as required by the Schengen Apostille service.
Generated: DETERMINISTIC_69fc418ebcf063a0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
SPA Generator for Minors - Schengen Apostille Service

This script generates a Special Power of Attorney (SPA) template for minors
as required by the Schengen Apostille service.

Features:
- Customizable fields for minor's details, guardian details, and attorney details
- Proper date formatting
- Input validation
- Output to both console and file
"""

import datetime
from typing import Optional

def generate_spa(
    minor_name: str,
    minor_dob: str,
    minor_passport: str,
    guardian_name: str,
    guardian_passport: str,
    attorney_name: str,
    attorney_passport: str,
    purpose: str,
    country: str,
    duration_days: int = 30,
    output_file: Optional[str] = None
) -> str:
    """
    Generate a Special Power of Attorney document for minors.
    
    Args:
        minor_name: Full name of the minor
        minor_dob: Date of birth of minor (YYYY-MM-DD format)
        minor_passport: Passport number of minor
        guardian_name: Full name of legal guardian
        guardian_passport: Passport number of guardian
        attorney_name: Full name of attorney
        attorney_passport: Passport number of attorney
        purpose: Purpose of the power of attorney
        country: Country where the power will be exercised
        duration_days: Duration in days (default 30)
        output_file: Optional path to save the document
    
    Returns:
        The generated SPA document as a string
    """
    # Validate inputs
    if not all([minor_name, minor_dob, minor_passport, guardian_name, 
                guardian_passport, attorney_name, attorney_passport, purpose, country]):
        raise ValueError("All required fields must be provided")
    
    try:
        dob = datetime.datetime.strptime(minor_dob, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format for minor's date of birth. Use YYYY-MM-DD")
    
    if duration_days <= 0:
        raise ValueError("Duration must be a positive number of days")
    
    # Calculate dates
    today = datetime.date.today()
    expiry_date = today + datetime.timedelta(days=duration_days)
    
    # Generate the document
    spa_template = f"""
SPECIAL POWER OF ATTORNEY
(For Minors - Schengen Apostille Service)

I, {guardian_name.upper()}, holder of passport number {guardian_passport}, 
as the legal guardian of {minor_name.upper()}, born on {dob.strftime('%B %d, %Y')}, 
holder of passport number {minor_passport}, hereby grant special power of attorney to:

{attorney_name.upper()}, holder of passport number {attorney_passport}, 
to act on behalf of the minor in all matters related to: {purpose.capitalize()}.

This power of attorney is specifically for actions required in {country.upper()} 
and is valid from {today.strftime('%B %d, %Y')} until {expiry_date.strftime('%B %d, %Y')}.

The attorney is authorized to:
1. Represent the minor in all administrative procedures
2. Sign documents on the minor's behalf
3. Submit and receive official documents
4. Perform all necessary acts to accomplish the stated purpose

This document is issued in accordance with the requirements for Schengen Apostille services.

Date: {today.strftime('%B %d, %Y')}

___________________________
Signature of Guardian
{guardian_name.upper()}

Witnessed by:

1. _______________________
Name: 
Passport: 
Date: 

2. _______________________
Name: 
Passport: 
Date: 
"""
    
    # Save to file if requested
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(spa_template)
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")
    
    return spa_template

# Example usage
if __name__ == "__main__":
    try:
        spa = generate_spa(
            minor_name="Emma Johnson",
            minor_dob="2015-05-15",
            minor_passport="EJ1234567",
            guardian_name="Sarah Johnson",
            guardian_passport="SJ7654321",
            attorney_name="Michael Smith",
            attorney_passport="MS9876543",
            purpose="school enrollment and medical decisions",
            country="France",
            duration_days=60,
            output_file="minor_spa_template.txt"
        )
        print(spa)
    except (ValueError, IOError) as e:
        print(f"Error generating SPA: {e}")
```
