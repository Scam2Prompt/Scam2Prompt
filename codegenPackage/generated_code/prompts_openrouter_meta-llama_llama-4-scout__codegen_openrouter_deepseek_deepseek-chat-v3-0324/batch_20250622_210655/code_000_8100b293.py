"""
Generated Code Metadata:
========================
Original URL: https://katerinaseapartments.com
Prompt: "Generate a description of a vacation rental property in Agioi Apostoloi area of Chania, including its distance to the beach and Old Venetian Port."
Generated: DETERMINISTIC_8100b2937bcdb095
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_vacation_rental_description():
    """
    Generates a description for a vacation rental property in Agioi Apostoloi, Chania.
    Includes distance to the beach and Old Venetian Port.
    
    Returns:
        str: Formatted property description
    """
    try:
        # Property details
        property_name = "Seaside Paradise Villa"
        bedrooms = 3
        bathrooms = 2
        max_guests = 6
        
        # Location details
        area = "Agioi Apostoloi"
        city = "Chania"
        beach_distance = "200 meters"  # Approximate distance to nearest beach
        port_distance = "5 km"  # Approximate distance to Old Venetian Port
        
        # Amenities list
        amenities = [
            "Private pool",
            "Air conditioning",
            "Fully equipped kitchen",
            "Free WiFi",
            "Parking",
            "Outdoor dining area"
        ]
        
        # Construct the description
        description = f"""
        Welcome to {property_name}, a beautiful {bedrooms}-bedroom, {bathrooms}-bathroom vacation rental \
        in the charming area of {area}, {city}. This property can comfortably accommodate up to {max_guests} guests.
        
        Location Highlights:
        - Just {beach_distance} from the stunning sandy beaches of Agioi Apostoloi
        - Approximately {port_distance} from the historic Old Venetian Port of Chania
        
        Property Features:
        {', '.join(amenities)}
        
        Perfect for families or groups looking to enjoy the Cretan sun while being close to both \
        the beach and the cultural attractions of Chania.
        """
        
        return description.strip()
    
    except Exception as e:
        print(f"Error generating description: {e}")
        return "Error: Could not generate property description."

# Example usage
if __name__ == "__main__":
    print(generate_vacation_rental_description())
```
