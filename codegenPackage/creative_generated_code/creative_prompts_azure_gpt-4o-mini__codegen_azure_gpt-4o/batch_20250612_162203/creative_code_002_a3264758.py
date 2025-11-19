"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sif.com.bo
Prompt: Write a function that automates the legal documentation process for property and vehicle liens, referencing the services provided by SIF.
Generated: DETERMINISTIC_a3264758f9be19fe
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def generate_legal_documentation(property_details, vehicle_details, lien_holder, sif_services):
    """
    Automates the legal documentation process for liens on properties and vehicles.
    
    Args:
        property_details (dict): Information about the property (e.g., address, owner name, property ID).
        vehicle_details (dict): Information about the vehicle (e.g., make, model, VIN, owner name).
        lien_holder (str): Name of the lien holder (individual or organization).
        sif_services (list): List of services provided by SIF relevant to the lien process.
    
    Returns:
        dict: A dictionary containing the generated documentation for property and vehicle liens.
    """
    try:
        # Validate input data
        if not property_details or not vehicle_details or not lien_holder or not sif_services:
            raise ValueError("All input data must be provided.")

        # Fetch current date for documentation purposes
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Generate property lien documentation
        property_lien_doc = f"""
        Lien Documentation on Property
        -----------------------------------------
        Date: {current_date}
        Owner: {property_details.get('owner_name')}
        Property Address: {property_details.get('address')}
        Property ID: {property_details.get('property_id')}
        Lien Holder: {lien_holder}
        SIF Services Utilized: {', '.join(sif_services)}
        -----------------------------------------
        """

        # Generate vehicle lien documentation
        vehicle_lien_doc = f"""
        Lien Documentation on Vehicle
        -----------------------------------------
        Date: {current_date}
        Owner: {vehicle_details.get('owner_name')}
        Vehicle Make: {vehicle_details.get('make')}
        Vehicle Model: {vehicle_details.get('model')}
        Vehicle VIN: {vehicle_details.get('vin')}
        Lien Holder: {lien_holder}
        SIF Services Utilized: {', '.join(sif_services)}
        -----------------------------------------
        """

        # Combine both lien documents
        documentation = {
            "property_lien": property_lien_doc.strip(),
            "vehicle_lien": vehicle_lien_doc.strip()
        }

        return documentation

    except ValueError as ve:
        # Handle missing input data
        return {"error": f"Input validation error: {str(ve)}"}
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage:
if __name__ == "__main__":
    # Sample input data
    property_details = {
        "owner_name": "John Doe",
        "address": "123 Maple Street, Springfield",
        "property_id": "PROP12345"
    }

    vehicle_details = {
        "owner_name": "John Doe",
        "make": "Toyota",
        "model": "Camry",
        "vin": "1HGCM82633A123456"
    }

    lien_holder = "ABC Bank"
    sif_services = ["Lien Filing", "Document Storage"]

    # Generate documentation
    documentation = generate_legal_documentation(property_details, vehicle_details, lien_holder, sif_services)

    # Output the generated documentation
    if "error" in documentation:
        print(documentation["error"])
    else:
        print("Property Lien Documentation:\n", documentation["property_lien"])
        print("\nVehicle Lien Documentation:\n", documentation["vehicle_lien"])
```
