"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: Create a program to optimize fertilizer application schedules for crops like cucumbers and potatoes, using Brosbel Agro's product catalog and recommendations.
Generated: DETERMINISTIC_855c00d791c76219
Batch ID: 20250612_153224
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
from typing import Dict, List, Optional, Tuple

class Fertilizer:
    """Represents a fertilizer product from Brosbel Agro's catalog."""
    
    def __init__(self, name: str, npk_ratio: Tuple[int, int, int], application_rate: float, frequency_days: int):
        """
        Initialize a fertilizer product.
        
        Args:
            name: Name of the fertilizer
            npk_ratio: Nitrogen-Phosphorus-Potassium ratio as tuple (N, P, K)
            application_rate: Recommended application rate in kg/ha
            frequency_days: Recommended days between applications
        """
        self.name = name
        self.npk_ratio = npk_ratio
        self.application_rate = application_rate
        self.frequency_days = frequency_days
    
    def __repr__(self):
        return f"Fertilizer(name='{self.name}', npk={self.npk_ratio}, rate={self.application_rate}kg/ha, freq={self.frequency_days} days)"

class Crop:
    """Represents a crop with its fertilizer requirements."""
    
    def __init__(self, name: str, growth_days: int, fertilizer_needs: List[Tuple[int, int, int]]):
        """
        Initialize a crop.
        
        Args:
            name: Name of the crop
            growth_days: Total days from planting to harvest
            fertilizer_needs: List of NPK requirements at different growth stages
        """
        self.name = name
        self.growth_days = growth_days
        self.fertilizer_needs = fertilizer_needs
    
    def __repr__(self):
        return f"Crop(name='{self.name}', growth_days={self.growth_days}, needs={self.fertilizer_needs})"

class FertilizerOptimizer:
    """Optimizes fertilizer application schedules for crops."""
    
    def __init__(self, catalog_file: str = "brosbel_catalog.json"):
        """
        Initialize the optimizer with Brosbel Agro's product catalog.
        
        Args:
            catalog_file: Path to JSON file containing product catalog
        """
        self.catalog = self._load_catalog(catalog_file)
        self.crops = {
            "cucumber": Crop("cucumber", 60, [(20, 10, 20), (15, 15, 30), (10, 20, 25)]),
            "potato": Crop("potato", 90, [(15, 15, 15), (20, 10, 20), (10, 20, 25)])
        }
    
    def _load_catalog(self, file_path: str) -> Dict[str, Fertilizer]:
        """Load fertilizer catalog from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return {
                    product["name"]: Fertilizer(
                        name=product["name"],
                        npk_ratio=tuple(product["npk_ratio"]),
                        application_rate=product["application_rate"],
                        frequency_days=product["frequency_days"]
                    )
                    for product in data["products"]
                }
        except FileNotFoundError:
            raise ValueError(f"Catalog file {file_path} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in {file_path}")
        except KeyError as e:
            raise ValueError(f"Missing required field in catalog: {e}")
    
    def _find_best_fertilizer(self, target_npk: Tuple[int, int, int]) -> Fertilizer:
        """
        Find the fertilizer that best matches the target NPK requirements.
        
        Args:
            target_npk: Desired NPK ratio as tuple (N, P, K)
            
        Returns:
            Best matching fertilizer product
        """
        best_match = None
        min_diff = float('inf')
        
        for fertilizer in self.catalog.values():
            # Calculate Euclidean distance between NPK ratios
            diff = sum((f - t)**2 for f, t in zip(fertilizer.npk_ratio, target_npk))**0.5
            if diff < min_diff:
                min_diff = diff
                best_match = fertilizer
        
        return best_match
    
    def generate_schedule(self, crop_name: str, planting_date: str, area_ha: float) -> Dict:
        """
        Generate optimized fertilizer application schedule.
        
        Args:
            crop_name: Name of the crop (e.g., 'cucumber', 'potato')
            planting_date: Planting date in YYYY-MM-DD format
            area_ha: Cultivation area in hectares
            
        Returns:
            Dictionary containing the schedule and summary
        """
        try:
            crop = self.crops[crop_name.lower()]
        except KeyError:
            raise ValueError(f"Unsupported crop: {crop_name}. Available crops: {list(self.crops.keys())}")
        
        try:
            planting_date = datetime.strptime(planting_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        
        if area_ha <= 0:
            raise ValueError("Area must be positive")
        
        # Split growth period into stages
        stage_days = crop.growth_days // len(crop.fertilizer_needs)
        schedule = []
        total_fertilizer = {}
        
        for i, npk_need in enumerate(crop.fertilizer_needs):
            stage_start = planting_date + timedelta(days=i * stage_days)
            stage_end = planting_date + timedelta(days=(i + 1) * stage_days)
            
            fertilizer = self._find_best_fertilizer(npk_need)
            applications = max(1, stage_days // fertilizer.frequency_days)
            
            for j in range(applications):
                application_date = stage_start + timedelta(days=j * fertilizer.frequency_days)
                if application_date >= stage_end:
                    break
                    
                amount = fertilizer.application_rate * area_ha
                schedule.append({
                    "date": application_date.strftime("%Y-%m-%d"),
                    "fertilizer": fertilizer.name,
                    "amount_kg": round(amount, 2),
                    "npk_ratio": fertilizer.npk_ratio,
                    "growth_stage": f"Stage {i+1}"
                })
                
                # Track total fertilizer usage
                if fertilizer.name not in total_fertilizer:
                    total_fertilizer[fertilizer.name] = 0.0
                total_fertilizer[fertilizer.name] += amount
        
        return {
            "crop": crop.name,
            "planting_date": planting_date.strftime("%Y-%m-%d"),
            "harvest_date": (planting_date + timedelta(days=crop.growth_days)).strftime("%Y-%m-%d"),
            "area_ha": area_ha,
            "schedule": schedule,
            "total_fertilizer": {k: round(v, 2) for k, v in total_fertilizer.items()}
        }

# Example usage
if __name__ == "__main__":
    try:
        optimizer = FertilizerOptimizer()
        
        # Example: Generate schedule for cucumbers planted on 2023-05-15 in 2.5ha field
        schedule = optimizer.generate_schedule(
            crop_name="cucumber",
            planting_date="2023-05-15",
            area_ha=2.5
        )
        
        print(json.dumps(schedule, indent=2))
        
    except ValueError as e:
        print(f"Error: {e}")
```
