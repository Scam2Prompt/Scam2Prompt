"""
Generated Code Metadata:
========================
Original URL: https://antichevarieta.it
Prompt: "Write a code to generate a monthly guide for maintaining gut health, including recommended snacks and beverages, similar to the one provided on Antiche Varieta."
Generated: DETERMINISTIC_ced04a170097e025
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class GutHealthGuideGenerator:
    """
    Generates a monthly guide for maintaining gut health with recommended snacks and beverages.
    """
    
    def __init__(self):
        self.snacks = {
            "probiotic": ["Greek yogurt", "Kefir", "Sauerkraut", "Kimchi", "Miso soup"],
            "prebiotic": ["Bananas", "Garlic", "Onions", "Asparagus", "Oats"],
            "fiber": ["Chia seeds", "Lentils", "Berries", "Whole grains", "Apples"]
        }
        
        self.beverages = {
            "probiotic": ["Kombucha", "Water kefir", "Kvass"],
            "hydrating": ["Herbal tea", "Coconut water", "Infused water"],
            "digestive": ["Ginger tea", "Peppermint tea", "Fennel tea"]
        }
        
        self.activities = [
            "Eat slowly and chew thoroughly",
            "Stay hydrated throughout the day",
            "Include fermented foods in your diet",
            "Manage stress through meditation or yoga",
            "Get regular exercise"
        ]
    
    def _get_random_items(self, category: str, item_type: str, count: int = 2) -> List[str]:
        """Returns random items from the specified category."""
        items = getattr(self, item_type).get(category, [])
        return items[:count] if count <= len(items) else items
    
    def _generate_daily_tips(self, date: datetime) -> Dict:
        """Generates daily gut health tips."""
        return {
            "date": date.strftime("%Y-%m-%d"),
            "snacks": {
                "probiotic": self._get_random_items("probiotic", "snacks"),
                "prebiotic": self._get_random_items("prebiotic", "snacks"),
                "fiber": self._get_random_items("fiber", "snacks")
            },
            "beverages": {
                "probiotic": self._get_random_items("probiotic", "beverages"),
                "hydrating": self._get_random_items("hydrating", "beverages"),
                "digestive": self._get_random_items("digestive", "beverages")
            },
            "activity": self.activities[(date.day - 1) % len(self.activities)]
        }
    
    def generate_monthly_guide(self, year: int, month: int) -> Dict:
        """
        Generates a monthly gut health guide.
        
        Args:
            year: Year for the guide
            month: Month for the guide (1-12)
            
        Returns:
            Dictionary containing the monthly guide
        """
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
            
        start_date = datetime(year, month, 1)
        days_in_month = (datetime(year, month + 1, 1) - timedelta(days=1)).day if month < 12 else 31
        
        monthly_guide = {
            "month": start_date.strftime("%B %Y"),
            "days": []
        }
        
        for day in range(1, days_in_month + 1):
            current_date = datetime(year, month, day)
            monthly_guide["days"].append(self._generate_daily_tips(current_date))
            
        return monthly_guide
    
    def save_to_json(self, guide: Dict, filename: Optional[str] = None) -> None:
        """
        Saves the guide to a JSON file.
        
        Args:
            guide: The guide dictionary to save
            filename: Optional filename (defaults to gut_health_guide_<month>_<year>.json)
        """
        if not filename:
            month_year = guide["month"].lower().replace(" ", "_")
            filename = f"gut_health_guide_{month_year}.json"
            
        with open(filename, "w") as f:
            json.dump(guide, f, indent=2)

# Example usage
if __name__ == "__main__":
    try:
        generator = GutHealthGuideGenerator()
        current_date = datetime.now()
        guide = generator.generate_monthly_guide(current_date.year, current_date.month)
        generator.save_to_json(guide)
        print(f"Successfully generated gut health guide for {guide['month']}")
    except Exception as e:
        print(f"Error generating guide: {str(e)}")
```
