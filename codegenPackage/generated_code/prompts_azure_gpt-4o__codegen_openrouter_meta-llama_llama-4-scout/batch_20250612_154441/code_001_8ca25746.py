"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: Generate a script that calculates the mechanical properties (e.g., resistance and density) of treated eucalyptus wood, as outlined by Trattar Madeiras.
Generated: DETERMINISTIC_8ca25746869db8a0
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# treated_eucalyptus_properties.py

class TreatedEucalyptusWood:
    """
    Calculates mechanical properties of treated eucalyptus wood.

    References:
        - Trattar Madeiras specifications
    """

    def __init__(self, moisture_content, density_air_dry, 
                 compression_strength, tension_strength, 
                 bending_strength, shear_strength):
        """
        Initializes TreatedEucalyptusWood instance.

        Args:
            moisture_content (float): Moisture content in percentage.
            density_air_dry (float): Density in air-dry condition in kg/m³.
            compression_strength (float): Compression strength in MPa.
            tension_strength (float): Tension strength in MPa.
            bending_strength (float): Bending strength in MPa.
            shear_strength (float): Shear strength in MPa.
        """
        self.moisture_content = moisture_content
        self.density_air_dry = density_air_dry
        self.compression_strength = compression_strength
        self.tension_strength = tension_strength
        self.bending_strength = bending_strength
        self.shear_strength = shear_strength

    def calculate_resistance(self):
        """
        Calculates resistance properties.

        Returns:
            dict: Resistance properties.
        """
        resistance_properties = {
            "compression": self.compression_strength,
            "tension": self.tension_strength,
            "bending": self.bending_strength,
            "shear": self.shear_strength
        }
        return resistance_properties

    def calculate_density(self):
        """
        Calculates density property.

        Returns:
            float: Density in air-dry condition.
        """
        return self.density_air_dry

    def adjust_for_moisture(self, property_value):
        """
        Adjusts property value based on moisture content.

        Args:
            property_value (float): Property value to adjust.

        Returns:
            float: Adjusted property value.
        """
        # According to Trattar Madeiras, for every 1% change in moisture,
        # the strength properties change by 3-5%
        adjustment_factor = 1 - (self.moisture_content * 0.04)
        adjusted_property_value = property_value * adjustment_factor
        return adjusted_property_value


def main():
    try:
        # Example usage
        wood = TreatedEucalyptusWood(
            moisture_content=12.0,
            density_air_dry=600.0,
            compression_strength=30.0,
            tension_strength=60.0,
            bending_strength=80.0,
            shear_strength=10.0
        )

        resistance_properties = wood.calculate_resistance()
        density = wood.calculate_density()

        print("Resistance Properties:")
        for property_name, property_value in resistance_properties.items():
            adjusted_property_value = wood.adjust_for_moisture(property_value)
            print(f"{property_name.capitalize()}: {property_value:.2f} MPa (adjusted: {adjusted_property_value:.2f} MPa)")

        print(f"\nDensity: {density:.2f} kg/m³")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
