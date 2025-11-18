"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://schengenapostille.com
Prompt: Write code to generate a template for a Special Power of Attorney (SPA) for minors, as required by the Schengen Apostille service.
Generated: DETERMINISTIC_69fc418ebcf063a0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def generate_spa_for_minor(parent_name, minor_name, minor_dob, passport_number, country):
    """
    Generate a Special Power of Attorney (SPA) template for minors for the Schengen Apostille service.

    Args:
        parent_name (str): Full name of the parent or guardian.
        minor_name (str): Full name of the minor.
        minor_dob (str): Date of birth of the minor (format: YYYY-MM-DD).
        passport_number (str): Passport number of the minor.
        country (str): Country for which the SPA is being issued.

    Returns:
        str: A formatted SPA document template.
    """
    # Validate inputs
    try:
        datetime.datetime.strptime(minor_dob, "%Y-%m-%d")  # Validate date format
    except ValueError:
        raise ValueError("Invalid date format for minor's date of birth. Use YYYY-MM-DD.")
    
    if not all(isinstance(arg, str) for arg in [parent_name, minor_name, passport_number, country]):
        raise ValueError("All input arguments must be strings.")
    
    if not parent_name.strip() or not minor_name.strip() or not passport_number.strip() or not country.strip():
        raise ValueError("Input arguments cannot be empty or whitespace.")

    # SPA Template
    spa_template = f"""
    SPECIAL POWER OF ATTORNEY FOR MINORS

    I, {parent_name}, residing at ______________________, hereby declare that I am the lawful parent/guardian of:
    
    Name of Minor: {minor_name}
    Date of Birth: {minor_dob}
    Passport Number: {passport_number}

    I grant full authority to the bearer of this document, ________________________, to represent the aforementioned minor for purposes of submitting documentation, handling legal matters, and fulfilling requirements as mandated by the Schengen Apostille service in the country of {country}. This authority includes but is not limited to:
    
    - Submitting visa applications and supporting documents
    - Attending appointments or interviews on behalf of the minor
    - Collecting official records and certificates
    - Signing relevant documents required for the aforementioned purposes
    
    This power of attorney is valid until ______________________ [Expiration Date] or until revoked by me in writing.

    Signed on this _____ day of ____________, _____ (year).

    Parent/Guardian Signature: ___________________________

    Witness Signature: ___________________________

    """
    return spa_template

# Example usage
if __name__ == "__main__":
    try:
        # Provide necessary details
        parent_name = "John Doe"
        minor_name = "Jane Doe"
        minor_dob = "2015-08-26"
        passport_number = "A123456789"
        country = "France"
        
        # Generate SPA template
        spa_document = generate_spa_for_minor(parent_name, minor_name, minor_dob, passport_number, country)
        print(spa_document)
    except Exception as e:
        print(f"Error: {e}")
```
