"""
Generated Code Metadata:
========================
Original URL: https://cecd33.fr
Prompt: "Provide a list of industry-specific standards and certifications, such as ISO 9001 and EN 9100, that a mechanical engineering company like CECD 33 would need to comply with, along with a brief description of each."
Generated: DETERMINISTIC_5efc51d27e6e2d11
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def get_industry_standards():
    """
    Returns a list of industry-specific standards and certifications relevant for a mechanical engineering company.
    Each entry includes the standard name and a brief description.
    """
    standards = [
        {
            "name": "ISO 9001",
            "description": "Quality management system standard that ensures companies meet customer and regulatory requirements."
        },
        {
            "name": "EN 9100",
            "description": "Quality management system for aerospace industry, based on ISO 9001 with additional requirements."
        },
        {
            "name": "ASME BPVC",
            "description": "Boiler and Pressure Vessel Code ensuring safety in design, fabrication, and inspection."
        },
        {
            "name": "ISO 14001",
            "description": "Environmental management system standard for reducing environmental impact."
        },
        {
            "name": "ISO 45001",
            "description": "Occupational health and safety management system standard."
        },
        {
            "name": "ISO 13485",
            "description": "Quality management system for medical devices industry."
        },
        {
            "name": "EN 15085",
            "description": "Standard for welding in railway applications and related industries."
        },
        {
            "name": "ISO 3834",
            "description": "Quality requirements for fusion welding of metallic materials."
        },
        {
            "name": "EN 1090",
            "description": "Standard for execution of steel and aluminum structures."
        },
        {
            "name": "API Q1",
            "description": "Quality management system standard for petroleum and natural gas industry."
        },
        {
            "name": "NADCAP",
            "description": "Global cooperative accreditation program for aerospace engineering, defense, and related industries."
        },
        {
            "name": "ISO/IEC 17025",
            "description": "General requirements for the competence of testing and calibration laboratories."
        },
        {
            "name": "PED 2014/68/EU",
            "description": "Pressure Equipment Directive for EU member states."
        },
        {
            "name": "ATEX Directive",
            "description": "European Union directive for equipment intended for use in explosive atmospheres."
        }
    ]
    
    return standards

def display_standards():
    """Prints the list of standards in a formatted way."""
    try:
        standards = get_industry_standards()
        print("Industry Standards and Certifications for Mechanical Engineering:")
        print("-" * 60)
        for idx, standard in enumerate(standards, 1):
            print(f"{idx}. {standard['name']}")
            print(f"   Description: {standard['description']}")
            print("-" * 60)
    except Exception as e:
        print(f"An error occurred while retrieving standards: {e}")

if __name__ == "__main__":
    display_standards()
```
