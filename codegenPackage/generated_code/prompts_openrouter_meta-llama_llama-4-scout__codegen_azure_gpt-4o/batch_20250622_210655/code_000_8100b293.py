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
# vacation_rental_description.py

def generate_vacation_rental_description(property_name, distance_to_beach, distance_to_old_port):
    """
    Generates a description for a vacation rental property.

    Args:
        property_name (str): Name of the vacation rental property.
        distance_to_beach (float): Distance to the beach in kilometers.
        distance_to_old_port (float): Distance to the Old Venetian Port in kilometers.

    Returns:
        str: A formatted description of the vacation rental property.
    """
    try:
        # Validate inputs
        if not isinstance(property_name, str) or not property_name.strip():
            raise ValueError("Property name must be a non-empty string.")
        if not isinstance(distance_to_beach, (int, float)) or distance_to_beach < 0:
            raise ValueError("Distance to the beach must be a non-negative number.")
        if not isinstance(distance_to_old_port, (int, float)) or distance_to_old_port < 0:
            raise ValueError("Distance to the Old Venetian Port must be a non-negative number.")

        # Generate the description
        description = (
            f"Welcome to {property_name}, a charming vacation rental located in the beautiful Agioi Apostoloi area of Chania. "
            f"This property is conveniently situated just {distance_to_beach:.1f} km from the pristine beaches, "
            f"and {distance_to_old_port:.1f} km from the historic Old Venetian Port. "
            f"Enjoy a perfect blend of relaxation and cultural exploration during your stay!"
        )
        return description

    except ValueError as e:
        # Handle invalid input errors
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    # Define property details
    property_name = "Seaside Retreat"
    distance_to_beach = 0.5  # in kilometers
    distance_to_old_port = 4.2  # in kilometers

    # Generate and print the description
    description = generate_vacation_rental_description(property_name, distance_to_beach, distance_to_old_port)
    print(description)
```
