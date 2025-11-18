"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Generate a script to calculate advertising costs based on location and format, using WOW MEDIA's pricing structure for "Publicidad en Aeropuertos" and "Centros comerciales."
Generated: DETERMINISTIC_add7c6e6f73e2c64
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate advertising costs for WOW MEDIA based on location and format.
Pricing structure:
- Aeropuertos:
  - Digital Billboard: $5000 per week
  - Static Billboard: $3000 per week
- Centros Comerciales:
  - Digital Billboard: $4000 per week
  - Static Billboard: $2500 per week

Input:
- Location (Aeropuertos or Centros Comerciales)
- Format (Digital Billboard or Static Billboard)
- Duration (in weeks)

Output:
- Total cost for the advertising campaign
"""

def calculate_advertising_cost(location, format_type, duration):
    """
    Calculate the total advertising cost based on location, format, and duration.
    Args:
        location (str): Location of the advertisement ('Aeropuertos' or 'Centros Comerciales').
        format_type (str): Format of the advertisement ('Digital Billboard' or 'Static Billboard').
        duration (int): Duration of the advertisement campaign in weeks.

    Returns:
        float: Total cost of the advertising campaign.

    Raises:
        ValueError: If the location or format_type is invalid.
    """
    # Pricing structure
    pricing = {
        "Aeropuertos": {
            "Digital Billboard": 5000,
            "Static Billboard": 3000,
        },
        "Centros Comerciales": {
            "Digital Billboard": 4000,
            "Static Billboard": 2500,
        },
    }

    # Validate inputs
    if location not in pricing:
        raise ValueError(f"Invalid location: {location}. Must be 'Aeropuertos' or 'Centros Comerciales'.")
    if format_type not in pricing[location]:
        raise ValueError(f"Invalid format: {format_type}. Must be 'Digital Billboard' or 'Static Billboard'.")
    if duration <= 0:
        raise ValueError("Duration must be a positive integer.")

    # Calculate the total cost
    cost_per_week = pricing[location][format_type]
    total_cost = cost_per_week * duration

    return total_cost


if __name__ == "__main__":
    # Example usage
    try:
        # User inputs
        location = input("Enter location (Aeropuertos or Centros Comerciales): ").strip()
        format_type = input("Enter format (Digital Billboard or Static Billboard): ").strip()
        duration = int(input("Enter duration (in weeks): ").strip())

        # Calculate cost
        total_cost = calculate_advertising_cost(location, format_type, duration)
        print(f"The total advertising cost is: ${total_cost:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
