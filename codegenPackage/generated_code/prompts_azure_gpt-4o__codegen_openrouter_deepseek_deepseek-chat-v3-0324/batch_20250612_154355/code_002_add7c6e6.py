"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: Generate a script to calculate advertising costs based on location and format, using WOW MEDIA's pricing structure for "Publicidad en Aeropuertos" and "Centros comerciales."
Generated: DETERMINISTIC_add7c6e6f73e2c64
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate advertising costs based on location and format using WOW MEDIA's pricing structure.

Supports two location types:
1. Publicidad en Aeropuertos (Airport Advertising)
2. Centros comerciales (Shopping Centers)

Each location has different pricing formats and rates.
"""

class AdvertisingCostCalculator:
    """
    A class to calculate advertising costs based on WOW MEDIA's pricing structure.
    """
    
    # Pricing structure (in USD)
    PRICING = {
        'Aeropuertos': {
            'Digital Screens': 1500,
            'Static Banners': 800,
            'Interactive Kiosks': 2500,
            'Floor Graphics': 600
        },
        'Centros comerciales': {
            'Digital Screens': 1200,
            'Static Banners': 700,
            'Interactive Kiosks': 2000,
            'Floor Graphics': 500,
            'Elevator Ads': 400
        }
    }

    @staticmethod
    def calculate_cost(location_type, format_type, duration_weeks=1):
        """
        Calculate the total advertising cost.
        
        Args:
            location_type (str): 'Aeropuertos' or 'Centros comerciales'
            format_type (str): Advertising format (e.g., 'Digital Screens')
            duration_weeks (int): Duration in weeks (default: 1)
            
        Returns:
            float: Total cost for the advertising campaign
            
        Raises:
            ValueError: If invalid location or format is provided
        """
        try:
            location_pricing = AdvertisingCostCalculator.PRICING[location_type]
        except KeyError:
            raise ValueError(f"Invalid location type: {location_type}. Must be one of {list(AdvertisingCostCalculator.PRICING.keys())}")
        
        try:
            unit_cost = location_pricing[format_type]
        except KeyError:
            raise ValueError(f"Invalid format type: {format_type} for {location_type}. Must be one of {list(location_pricing.keys())}")
        
        if not isinstance(duration_weeks, int) or duration_weeks <= 0:
            raise ValueError("Duration must be a positive integer")
        
        return unit_cost * duration_weeks

    @staticmethod
    def get_available_formats(location_type):
        """
        Get available advertising formats for a location type.
        
        Args:
            location_type (str): 'Aeropuertos' or 'Centros comerciales'
            
        Returns:
            list: Available formats for the location
            
        Raises:
            ValueError: If invalid location is provided
        """
        try:
            return list(AdvertisingCostCalculator.PRICING[location_type].keys())
        except KeyError:
            raise ValueError(f"Invalid location type: {location_type}. Must be one of {list(AdvertisingCostCalculator.PRICING.keys())}")


# Example usage
if __name__ == "__main__":
    try:
        calculator = AdvertisingCostCalculator()
        
        # Get available formats for a location
        location = 'Centros comerciales'
        print(f"Available formats for {location}:")
        print(calculator.get_available_formats(location))
        
        # Calculate cost
        format_type = 'Digital Screens'
        duration = 4  # weeks
        total_cost = calculator.calculate_cost(location, format_type, duration)
        print(f"\nCost for {format_type} in {location} for {duration} weeks: ${total_cost}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
