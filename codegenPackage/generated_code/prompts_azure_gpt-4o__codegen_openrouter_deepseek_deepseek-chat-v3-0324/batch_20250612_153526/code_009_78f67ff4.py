"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Write a script to generate a packing list for high-altitude treks like the Manaslu Circuit Trek, referencing the challenges described on Khaptad Tours.
Generated: DETERMINISTIC_78f67ff4bbb3cd2c
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Packing List Generator for High-Altitude Treks
Author: Khaptad Tours
Description: Generates a comprehensive packing list for high-altitude treks
             like the Manaslu Circuit Trek, considering altitude challenges.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional

class PackingListGenerator:
    """
    Generates a packing list for high-altitude treks with categories and items.
    """
    
    def __init__(self):
        self.categories = {
            "clothing": self._get_clothing_items(),
            "footwear": self._get_footwear_items(),
            "gear": self._get_gear_items(),
            "health": self._get_health_items(),
            "documents": self._get_document_items(),
            "miscellaneous": self._get_misc_items()
        }
        self.essential_items = [
            "down jacket", "thermal layers", "trekking boots",
            "sleeping bag (-20°C)", "first aid kit", "water purification",
            "headlamp", "sunglasses (UV protection)", "sunscreen (SPF 50+)",
            "passport/permits"
        ]
    
    def _get_clothing_items(self) -> List[str]:
        """Returns clothing items for high-altitude trekking"""
        return [
            "down jacket (preferably -10°C rated)",
            "thermal base layers (top and bottom)",
            "fleece jacket or pullover",
            "waterproof and windproof shell jacket",
            "trekking pants (convertible recommended)",
            "quick-dry t-shirts (2-3)",
            "thermal gloves (inner and outer)",
            "woolen hat or balaclava",
            "neck gaiter or buff",
            "underwear (quick-dry, 4-5 pairs)",
            "thermal socks (4-5 pairs)",
            "liner socks (optional)"
        ]
    
    def _get_footwear_items(self) -> List[str]:
        """Returns footwear items for high-altitude trekking"""
        return [
            "sturdy trekking boots (broken-in, waterproof)",
            "camp shoes (lightweight sandals or sneakers)",
            "gaiters (for snow or muddy conditions)",
            "microspikes or crampons (seasonal)"
        ]
    
    def _get_gear_items(self) -> List[str]:
        """Returns gear items for high-altitude trekking"""
        return [
            "backpack (50-70L with rain cover)",
            "daypack (20-30L)",
            "sleeping bag (-20°C rating recommended)",
            "sleeping bag liner (optional)",
            "trekking poles (collapsible)",
            "headlamp with extra batteries",
            "water bottles or hydration bladder (3L capacity)",
            "water purification tablets or filter",
            "duffel bag (for porters, if applicable)",
            "dry bags (various sizes)",
            "solar charger or power bank",
            "camera (optional)"
        ]
    
    def _get_health_items(self) -> List[str]:
        """Returns health and medical items"""
        return [
            "first aid kit (including blister treatment)",
            "diamox (for altitude sickness)",
            "pain relievers (ibuprofen, paracetamol)",
            "anti-diarrheal medication",
            "rehydration salts",
            "antibiotic ointment",
            "bandages and gauze",
            "medical tape",
            "hand sanitizer",
            "toilet paper (in ziplock bag)",
            "sunscreen (SPF 50+)",
            "lip balm with SPF",
            "sunglasses (UV protection, category 4)",
            "prescription medications (if any)"
        ]
    
    def _get_document_items(self) -> List[str]:
        """Returns required documents"""
        return [
            "passport (with visa if required)",
            "trekking permits",
            "travel insurance documents",
            "emergency contact information",
            "copies of important documents",
            "cash (local currency and USD)"
        ]
    
    def _get_misc_items(self) -> List[str]:
        """Returns miscellaneous items"""
        return [
            "snacks (energy bars, nuts, chocolate)",
            "electrolyte tablets or powder",
            "quick-dry towel",
            "toiletries (biodegradable soap, toothbrush, etc.)",
            "wet wipes",
            "notebook and pen",
            "book or e-reader",
            "ear plugs",
            "playing cards or small games",
            "trash bags (for carrying waste)"
        ]
    
    def generate_list(self, trek_name: str, duration_days: int, max_altitude: int) -> Dict:
        """
        Generates a complete packing list for the trek.
        
        Args:
            trek_name: Name of the trek
            duration_days: Duration in days
            max_altitude: Maximum altitude in meters
            
        Returns:
            Dictionary containing the complete packing list
        """
        if not isinstance(duration_days, int) or duration_days <= 0:
            raise ValueError("Duration must be a positive integer")
            
        if not isinstance(max_altitude, int) or max_altitude < 1000:
            raise ValueError("Max altitude must be an integer >= 1000 meters")
        
        seasonal_items = self._get_seasonal_items(max_altitude)
        
        return {
            "trek": trek_name,
            "generated_on": datetime.now().strftime("%Y-%m-%d"),
            "duration_days": duration_days,
            "max_altitude_meters": max_altitude,
            "essential_items": self.essential_items,
            "categories": self.categories,
            "seasonal_items": seasonal_items,
            "notes": [
                "Adjust quantities based on trek duration",
                "Layer clothing for temperature variations",
                "Test all gear before departure",
                "Pack light but don't compromise on essentials",
                "Consult with your doctor about altitude medication"
            ]
        }
    
    def _get_seasonal_items(self, max_altitude: int) -> Dict:
        """Returns seasonal items based on altitude"""
        seasonal = {
            "winter": [
                "heavyweight down jacket (-20°C or lower)",
                "expedition-weight thermal layers",
                "insulated pants",
                "heavyweight gloves",
                "snow goggles",
                "additional hand/foot warmers"
            ],
            "summer": [
                "lightweight rain jacket",
                "sun hat with neck cover",
                "lightweight gloves",
                "bug repellent"
            ]
        }
        
        if max_altitude > 5000:
            seasonal["high_altitude"] = [
                "supplemental oxygen (consult guide)",
                "altitude-specific medications",
                "expedition-weight sleeping bag",
                "four-season tent (if camping)"
            ]
        
        return seasonal
    
    def save_to_file(self, packing_list: Dict, filename: Optional[str] = None) -> str:
        """
        Saves the packing list to a JSON file.
        
        Args:
            packing_list: The packing list dictionary
            filename: Optional custom filename
            
        Returns:
            The filename used
        """
        if not filename:
            trek_name = packing_list["trek"].replace(" ", "_").lower()
            filename = f"packing_list_{trek_name}.json"
        
        with open(filename, "w") as f:
            json.dump(packing_list, f, indent=4)
        
        return filename

def main():
    """Main function to demonstrate the packing list generator"""
    try:
        generator = PackingListGenerator()
        
        # Example for Manaslu Circuit Trek
        packing_list = generator.generate_list(
            trek_name="Manaslu Circuit Trek",
            duration_days=14,
            max_altitude=5160  # Larkya La Pass
        )
        
        filename = generator.save_to_file(packing_list)
        print(f"Packing list generated successfully: {filename}")
        
    except Exception as e:
        print(f"Error generating packing list: {str(e)}")

if __name__ == "__main__":
    main()
```
