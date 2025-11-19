"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: Develop a program to generate a detailed energy optimization report for solar panel installations, incorporating the "overzichtelijk en passend advies" approach described on Technische Installatiebedrijf van Boxtel's website.
Generated: DETERMINISTIC_6a16303b0d2c888c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import math
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class SolarPanelInstallation:
    """
    Represents a solar panel installation with relevant parameters for energy optimization.
    """
    
    def __init__(
        self,
        location: str,
        panel_count: int,
        panel_wattage: float,
        panel_efficiency: float,
        installation_angle: float,
        orientation: float,
        shading_factor: float = 0.0,
        inverter_efficiency: float = 0.96,
    ):
        """
        Initialize solar panel installation parameters.
        
        Args:
            location: Installation location (city/region)
            panel_count: Number of solar panels
            panel_wattage: Wattage per panel (W)
            panel_efficiency: Panel efficiency (0-1)
            installation_angle: Tilt angle in degrees (0-90)
            orientation: Azimuth angle in degrees (0-360, 180=south)
            shading_factor: Shading loss factor (0-1)
            inverter_efficiency: Inverter efficiency (0-1)
        """
        self.location = location
        self.panel_count = panel_count
        self.panel_wattage = panel_wattage
        self.panel_efficiency = panel_efficiency
        self.installation_angle = installation_angle
        self.orientation = orientation
        self.shading_factor = shading_factor
        self.inverter_efficiency = inverter_efficiency
        self.irradiance_data = self._load_irradiance_data()

    def _load_irradiance_data(self) -> Dict[str, float]:
        """
        Load typical irradiance data for the location (kWh/m²/day).
        In a real implementation, this would fetch from a database or API.
        """
        # Mock data - in production this would come from a reliable source
        irradiance_db = {
            "amsterdam": {"annual": 2.8, "summer": 4.5, "winter": 1.0},
            "rotterdam": {"annual": 2.7, "summer": 4.4, "winter": 0.9},
            "utrecht": {"annual": 2.75, "summer": 4.45, "winter": 0.95},
            "default": {"annual": 2.7, "summer": 4.4, "winter": 0.9},
        }
        
        location_key = self.location.lower()
        return irradiance_db.get(location_key, irradiance_db["default"])

    def calculate_orientation_factor(self) -> float:
        """
        Calculate the orientation correction factor based on panel azimuth.
        
        Returns:
            Orientation factor (0-1)
        """
        # Normalize orientation to 0-180 degrees
        orientation = min(self.orientation, 360 - self.orientation)
        
        if orientation <= 45:
            return 0.95
        elif orientation <= 90:
            return 0.90
        elif orientation <= 135:
            return 0.80
        else:
            return 0.70

    def calculate_tilt_factor(self) -> float:
        """
        Calculate the tilt correction factor based on panel angle.
        
        Returns:
            Tilt factor (0-1)
        """
        # Optimal tilt is roughly equal to latitude (Netherlands ~52°)
        optimal_tilt = 52.0
        tilt_diff = abs(self.installation_angle - optimal_tilt)
        
        if tilt_diff <= 10:
            return 1.0
        elif tilt_diff <= 20:
            return 0.95
        elif tilt_diff <= 30:
            return 0.90
        else:
            return 0.85

    def calculate_daily_production(self, season: str = "annual") -> float:
        """
        Calculate estimated daily energy production in kWh.
        
        Args:
            season: 'annual', 'summer', or 'winter'
            
        Returns:
            Daily energy production in kWh
        """
        if season not in self.irradiance_data:
            raise ValueError(f"Invalid season: {season}. Must be 'annual', 'summer', or 'winter'")
            
        irradiance = self.irradiance_data[season]
        orientation_factor = self.calculate_orientation_factor()
        tilt_factor = self.calculate_tilt_factor()
        
        # Calculate effective irradiance considering orientation and tilt
        effective_irradiance = irradiance * orientation_factor * tilt_factor
        
        # Adjust for shading
        effective_irradiance *= (1 - self.shading_factor)
        
        # Calculate daily production
        panel_area = 1.6  # m² (typical panel size)
        daily_production = (
            self.panel_count *
            effective_irradiance *
            panel_area *
            self.panel_efficiency *
            self.inverter_efficiency
        )
        
        return daily_production

    def calculate_annual_production(self) -> float:
        """
        Calculate estimated annual energy production in kWh.
        
        Returns:
            Annual energy production in kWh
        """
        daily_production = self.calculate_daily_production("annual")
        return daily_production * 365

    def calculate_payback_period(self, installation_cost: float, electricity_price: float) -> float:
        """
        Calculate estimated payback period in years.
        
        Args:
            installation_cost: Total installation cost in EUR
            electricity_price: Current electricity price in EUR/kWh
            
        Returns:
            Payback period in years
        """
        annual_production = self.calculate_annual_production()
        annual_savings = annual_production * electricity_price
        
        if annual_savings <= 0:
            return float('inf')
            
        return installation_cost / annual_savings

    def generate_optimization_report(self, installation_cost: float, electricity_price: float) -> Dict:
        """
        Generate a comprehensive optimization report.
        
        Args:
            installation_cost: Total installation cost in EUR
            electricity_price: Current electricity price in EUR/kWh
            
        Returns:
            Dictionary containing the optimization report
        """
        annual_production = self.calculate_annual_production()
        summer_production = self.calculate_daily_production("summer") * 182
        winter_production = self.calculate_daily_production("winter") * 183
        
        payback_period = self.calculate_payback_period(installation_cost, electricity_price)
        annual_savings = annual_production * electricity_price
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "location": self.location,
            "system_details": {
                "panel_count": self.panel_count,
                "total_capacity_kw": round(self.panel_count * self.panel_wattage / 1000, 2),
                "panel_efficiency": self.panel_efficiency,
                "installation_angle": self.installation_angle,
                "orientation": self.orientation,
                "shading_factor": self.shading_factor,
            },
            "production_estimates": {
                "annual_kwh": round(annual_production, 2),
                "summer_kwh": round(summer_production, 2),
                "winter_kwh": round(winter_production, 2),
                "daily_avg_kwh": round(annual_production / 365, 2),
            },
            "financial_analysis": {
                "installation_cost_eur": round(installation_cost, 2),
                "electricity_price_eur_kwh": electricity_price,
                "annual_savings_eur": round(annual_savings, 2),
                "payback_period_years": round(payback_period, 1),
                "roi_percentage": round((annual_savings / installation_cost) * 100, 1) if installation_cost > 0 else 0,
            },
            "optimization_recommendations": self._generate_recommendations(),
        }
        
        return report

    def _generate_recommendations(self) -> List[str]:
        """
        Generate optimization recommendations based on current installation parameters.
        
        Returns:
            List of recommendation strings
        """
        recommendations = []
        
        # Orientation recommendations
        if self.orientation < 150 or self.orientation > 210:
            recommendations.append(
                "Overweeg panelen meer naar het zuiden te richten (tussen 150° en 210°) "
                "voor betere energieopbrengst."
            )
        
        # Tilt angle recommendations
        if abs(self.installation_angle - 52) > 15:
            recommendations.append(
                f"De huidige hellingshoek van {self.installation_angle}° is niet optimaal. "
                "Een hoek tussen 35° en 55° wordt aanbevolen voor maximale jaaropbrengst."
            )
        
        # Shading recommendations
        if self.shading_factor > 0.1:
            recommendations.append(
                f"Schaduwwerking ({self.shading_factor*100:.0f}%) vermindert de opbrengst aanzienlijk. "
                "Overweeg obstakels te verwijderen of micro-omvormers te gebruiken."
            )
        
        # Panel count
