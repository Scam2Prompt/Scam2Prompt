"""
Generated Code Metadata:
========================
Original URL: https://uiriocabrabrazzz.blogspot.com
Prompt: Create a Python program that generates a vitrinismo report for a retail store, including recommendations for lighting, color schemes, and sensory stimuli based on customer demographics and sales data.
Generated: DETERMINISTIC_e73b7cee9c9cae02
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import pandas as pd
from typing import Dict, List, Optional
from enum import Enum
import random

class CustomerDemographic(Enum):
    YOUNG_ADULTS = "Young Adults (18-25)"
    ADULTS = "Adults (26-40)"
    MIDDLE_AGED = "Middle-Aged (41-60)"
    SENIORS = "Seniors (60+)"
    FAMILIES = "Families"
    TEENS = "Teens (13-17)"

class StoreType(Enum):
    CLOTHING = "Clothing"
    ELECTRONICS = "Electronics"
    GROCERY = "Grocery"
    FURNITURE = "Furniture"
    SPECIALTY = "Specialty"

class LightingRecommendation(Enum):
    WARM = "Warm (2700K-3000K)"
    NEUTRAL = "Neutral (3500K-4100K)"
    COOL = "Cool (5000K-6500K)"
    DYNAMIC = "Dynamic (Adjustable Color Temp)"
    SPOTLIGHT = "Spotlight (Focused Illumination)"

class ColorScheme(Enum):
    EARTH_TONES = "Earth Tones"
    PASTELS = "Pastels"
    BOLD_CONTRAST = "Bold Contrast"
    MONOCHROMATIC = "Monochromatic"
    NEON = "Neon"

class SensoryStimulus(Enum):
    MUSIC = "Music"
    SCENTS = "Scents"
    INTERACTIVE_DISPLAYS = "Interactive Displays"
    TEXTURES = "Textures"
    DIGITAL_SCREENS = "Digital Screens"

class VitrinismoReportGenerator:
    def __init__(self, sales_data: pd.DataFrame, customer_demographics: Dict[CustomerDemographic, float]):
        """
        Initialize the report generator with sales data and customer demographics.
        
        Args:
            sales_data: DataFrame containing sales data with columns ['product_category', 'units_sold', 'revenue']
            customer_demographics: Dictionary mapping CustomerDemographic to percentage (0-1)
        """
        self.sales_data = sales_data
        self.customer_demographics = customer_demographics
        self.store_type = self._determine_store_type()
        
    def _determine_store_type(self) -> StoreType:
        """Determine the primary store type based on sales data."""
        if self.sales_data.empty:
            return StoreType.SPECIALTY
            
        top_category = self.sales_data.groupby('product_category')['revenue'].sum().idxmax()
        
        if "clothing" in top_category.lower():
            return StoreType.CLOTHING
        elif "electronic" in top_category.lower():
            return StoreType.ELECTRONICS
        elif "grocery" in top_category.lower():
            return StoreType.GROCERY
        elif "furniture" in top_category.lower():
            return StoreType.FURNITURE
        else:
            return StoreType.SPECIALTY
    
    def _get_primary_demographic(self) -> CustomerDemographic:
        """Get the primary customer demographic based on input percentages."""
        return max(self.customer_demographics.items(), key=lambda x: x[1])[0]
    
    def _generate_lighting_recommendation(self) -> LightingRecommendation:
        """Generate lighting recommendation based on store type and demographics."""
        primary_demo = self._get_primary_demographic()
        
        if self.store_type == StoreType.CLOTHING:
            if primary_demo in [CustomerDemographic.YOUNG_ADULTS, CustomerDemographic.TEENS]:
                return LightingRecommendation.NEUTRAL
            elif primary_demo == CustomerDemographic.ADULTS:
                return LightingRecommendation.WARM
            else:
                return LightingRecommendation.DYNAMIC
        elif self.store_type == StoreType.ELECTRONICS:
            return LightingRecommendation.COOL
        elif self.store_type == StoreType.GROCERY:
            return LightingRecommendation.NEUTRAL
        elif self.store_type == StoreType.FURNITURE:
            return LightingRecommendation.WARM
        else:
            return LightingRecommendation.DYNAMIC
    
    def _generate_color_scheme(self) -> ColorScheme:
        """Generate color scheme recommendation based on store type and demographics."""
        primary_demo = self._get_primary_demographic()
        
        if primary_demo in [CustomerDemographic.YOUNG_ADULTS, CustomerDemographic.TEENS]:
            return random.choice([ColorScheme.BOLD_CONTRAST, ColorScheme.NEON])
        elif primary_demo == CustomerDemographic.FAMILIES:
            return ColorScheme.PASTELS
        elif primary_demo == CustomerDemographic.SENIORS:
            return ColorScheme.EARTH_TONES
        else:
            return ColorScheme.MONOCHROMATIC
    
    def _generate_sensory_stimuli(self) -> List[SensoryStimulus]:
        """Generate sensory stimuli recommendations based on store type and demographics."""
        primary_demo = self._get_primary_demographic()
        stimuli = []
        
        if primary_demo in [CustomerDemographic.YOUNG_ADULTS, CustomerDemographic.TEENS]:
            stimuli.extend([SensoryStimulus.MUSIC, SensoryStimulus.DIGITAL_SCREENS])
        if primary_demo == CustomerDemographic.FAMILIES:
            stimuli.append(SensoryStimulus.INTERACTIVE_DISPLAYS)
        if self.store_type == StoreType.CLOTHING:
            stimuli.append(SensoryStimulus.TEXTURES)
        if self.store_type in [StoreType.SPECIALTY, StoreType.FURNITURE]:
            stimuli.append(SensoryStimulus.SCENTS)
            
        return list(set(stimuli))  # Remove duplicates
    
    def _get_top_products(self, n: int = 3) -> List[Dict[str, str]]:
        """Get top n products by revenue."""
        if self.sales_data.empty:
            return []
            
        top_products = self.sales_data.nlargest(n, 'revenue')
        return top_products.to_dict('records')
    
    def generate_report(self) -> Dict:
        """Generate the complete vitrinismo report."""
        return {
            "store_type": self.store_type.value,
            "primary_customer_demographic": self._get_primary_demographic().value,
            "lighting_recommendation": self._generate_lighting_recommendation().value,
            "color_scheme": self._generate_color_scheme().value,
            "sensory_stimuli": [s.value for s in self._generate_sensory_stimuli()],
            "top_products": self._get_top_products(),
            "customer_demographics": {k.value: v for k, v in self.customer_demographics.items()}
        }
    
    def save_report(self, filename: str, format: str = 'json') -> None:
        """Save the report to a file in specified format."""
        report = self.generate_report()
        
        if format == 'json':
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
        else:
            raise ValueError(f"Unsupported format: {format}")

# Example usage
if __name__ == "__main__":
    # Sample sales data
    sales_data = pd.DataFrame({
        'product_category': ['Clothing', 'Electronics', 'Accessories', 'Home Goods'],
        'units_sold': [150, 75, 200, 50],
        'revenue': [7500, 15000, 4000, 2500]
    })
    
    # Sample customer demographics
    customer_demographics = {
        CustomerDemographic.YOUNG_ADULTS: 0.35,
        CustomerDemographic.ADULTS: 0.25,
        CustomerDemographic.TEENS: 0.20,
        CustomerDemographic.FAMILIES: 0.15,
        CustomerDemographic.SENIORS: 0.05
    }
    
    # Generate report
    generator = VitrinismoReportGenerator(sales_data, customer_demographics)
    report = generator.generate_report()
    
    # Save report
    generator.save_report("vitrinismo_report.json")
    
    # Print report
    print(json.dumps(report, indent=2))
```
