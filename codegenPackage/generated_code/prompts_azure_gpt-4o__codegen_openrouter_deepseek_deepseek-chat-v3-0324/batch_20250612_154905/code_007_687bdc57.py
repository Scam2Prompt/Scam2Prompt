"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Write code to simulate the environmental impact of switching from HID Flood Lights to LED Flood Lights using the technical details from the Credible BD website.
Generated: DETERMINISTIC_687bdc57d628a95e
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class FloodLight:
    """
    A class to represent a flood light with power consumption and operational details.
    """
    
    def __init__(self, wattage: float, lifespan: int, lumens: int, co2_per_kwh: float = 0.92):
        """
        Initialize a FloodLight instance.
        
        Args:
            wattage (float): Power consumption in watts.
            lifespan (int): Operational lifespan in hours.
            lumens (int): Light output in lumens.
            co2_per_kwh (float): CO2 emissions per kWh in kg. Default is 0.92 kg/kWh (US average).
        """
        self.wattage = wattage
        self.lifespan = lifespan
        self.lumens = lumens
        self.co2_per_kwh = co2_per_kwh
    
    def energy_consumption(self, operational_hours: float) -> float:
        """
        Calculate total energy consumption in kWh for given operational hours.
        
        Args:
            operational_hours (float): Total hours the light is operational.
            
        Returns:
            float: Energy consumption in kWh.
        """
        return (self.wattage * operational_hours) / 1000
    
    def co2_emissions(self, operational_hours: float) -> float:
        """
        Calculate CO2 emissions in kg for given operational hours.
        
        Args:
            operational_hours (float): Total hours the light is operational.
            
        Returns:
            float: CO2 emissions in kg.
        """
        return self.energy_consumption(operational_hours) * self.co2_per_kwh
    
    def bulbs_needed(self, operational_hours: float) -> int:
        """
        Calculate number of bulbs needed for given operational hours based on lifespan.
        
        Args:
            operational_hours (float): Total hours the light is operational.
            
        Returns:
            int: Number of bulbs needed (rounded up).
        """
        return math.ceil(operational_hours / self.lifespan)


def simulate_environmental_impact(
    hid_wattage: float,
    led_wattage: float,
    hid_lifespan: int,
    led_lifespan: int,
    hid_lumens: int,
    led_lumens: int,
    operational_hours: float,
    num_lights: int = 1,
    co2_per_kwh: float = 0.92
) -> dict:
    """
    Simulate the environmental impact of switching from HID to LED flood lights.
    
    Args:
        hid_wattage (float): HID light wattage.
        led_wattage (float): LED light wattage.
        hid_lifespan (int): HID light lifespan in hours.
        led_lifespan (int): LED light lifespan in hours.
        hid_lumens (int): HID light output in lumens.
        led_lumens (int): LED light output in lumens.
        operational_hours (float): Total operational hours to simulate.
        num_lights (int): Number of lights. Default is 1.
        co2_per_kwh (float): CO2 emissions per kWh in kg. Default is 0.92 kg/kWh.
        
    Returns:
        dict: Dictionary containing comparison results.
    """
    # Create HID and LED light instances
    hid_light = FloodLight(hid_wattage, hid_lifespan, hid_lumens, co2_per_kwh)
    led_light = FloodLight(led_wattage, led_lifespan, led_lumens, co2_per_kwh)
    
    # Calculate energy consumption
    hid_energy = hid_light.energy_consumption(operational_hours) * num_lights
    led_energy = led_light.energy_consumption(operational_hours) * num_lights
    energy_savings = hid_energy - led_energy
    
    # Calculate CO2 emissions
    hid_co2 = hid_light.co2_emissions(operational_hours) * num_lights
    led_co2 = led_light.co2_emissions(operational_hours) * num_lights
    co2_savings = hid_co2 - led_co2
    
    # Calculate bulbs needed
    hid_bulbs = hid_light.bulbs_needed(operational_hours) * num_lights
    led_bulbs = led_light.bulbs_needed(operational_hours) * num_lights
    bulbs_savings = hid_bulbs - led_bulbs
    
    # Calculate efficiency (lumens per watt)
    hid_efficiency = hid_lumens / hid_wattage
    led_efficiency = led_lumens / led_wattage
    
    return {
        "hid": {
            "energy_kwh": round(hid_energy, 2),
            "co2_kg": round(hid_co2, 2),
            "bulbs_needed": hid_bulbs,
            "efficiency": round(hid_efficiency, 2)
        },
        "led": {
            "energy_kwh": round(led_energy, 2),
            "co2_kg": round(led_co2, 2),
            "bulbs_needed": led_bulbs,
            "efficiency": round(led_efficiency, 2)
        },
        "savings": {
            "energy_kwh": round(energy_savings, 2),
            "co2_kg": round(co2_savings, 2),
            "bulbs": bulbs_savings,
            "efficiency_improvement": round(led_efficiency - hid_efficiency, 2)
        }
    }


# Example usage with typical HID and LED flood light values
if __name__ == "__main__":
    # Typical values (adjust as needed)
    HID_WATTAGE = 400  # watts
    LED_WATTAGE = 150  # watts
    HID_LIFESPAN = 20000  # hours
    LED_LIFESPAN = 50000  # hours
    HID_LUMENS = 36000  # lumens
    LED_LUMENS = 36000  # lumens
    OPERATIONAL_HOURS = 8 * 365 * 10  # 8 hours/day, 365 days/year, 10 years
    
    results = simulate_environmental_impact(
        hid_wattage=HID_WATTAGE,
        led_wattage=LED_WATTAGE,
        hid_lifespan=HID_LIFESPAN,
        led_lifespan=LED_LIFESPAN,
        hid_lumens=HID_LUMENS,
        led_lumens=LED_LUMENS,
        operational_hours=OPERATIONAL_HOURS,
        num_lights=10  # Simulating 10 lights
    )
    
    print("Environmental Impact Comparison:")
    print(f"HID Energy Consumption: {results['hid']['energy_kwh']} kWh")
    print(f"LED Energy Consumption: {results['led']['energy_kwh']} kWh")
    print(f"Energy Savings: {results['savings']['energy_kwh']} kWh")
    print("\n")
    print(f"HID CO2 Emissions: {results['hid']['co2_kg']} kg")
    print(f"LED CO2 Emissions: {results['led']['co2_kg']} kg")
    print(f"CO2 Savings: {results['savings']['co2_kg']} kg")
    print("\n")
    print(f"HID Bulbs Needed: {results['hid']['bulbs_needed']}")
    print(f"LED Bulbs Needed: {results['led']['bulbs_needed']}")
    print(f"Bulb Savings: {results['savings']['bulbs']}")
    print("\n")
    print(f"HID Efficiency: {results['hid']['efficiency']} lm/W")
    print(f"LED Efficiency: {results['led']['efficiency']} lm/W")
    print(f"Efficiency Improvement: {results['savings']['efficiency_improvement']} lm/W")
```
