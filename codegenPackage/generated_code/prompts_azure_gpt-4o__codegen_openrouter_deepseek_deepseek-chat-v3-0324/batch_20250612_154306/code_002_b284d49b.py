"""
Generated Code Metadata:
========================
Original URL: https://jggbbestforyou.com
Prompt: Generate code to calculate insulin dosage adjustments based on data from Medtrum TouchCare® Nano pump and Abbott FreeStyle Libre CGM.
Generated: DETERMINISTIC_b284d49bef038818
Batch ID: 20250612_154306
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

class InsulinDosageCalculator:
    """
    A class to calculate insulin dosage adjustments based on data from 
    Medtrum TouchCare® Nano pump and Abbott FreeStyle Libre CGM.
    """
    
    def __init__(self, patient_settings: Dict):
        """
        Initialize the calculator with patient-specific settings.
        
        Args:
            patient_settings: Dictionary containing patient settings including:
                - target_glucose_range: Tuple of (min, max) target glucose in mg/dL
                - correction_factor: mg/dL per unit of insulin
                - carb_ratio: grams of carbs covered by 1 unit of insulin
                - insulin_duration: Duration of insulin action in hours
        """
        self.target_min, self.target_max = patient_settings['target_glucose_range']
        self.correction_factor = patient_settings['correction_factor']
        self.carb_ratio = patient_settings['carb_ratio']
        self.insulin_duration = patient_settings['insulin_duration']
        
        # Validate settings
        if not (0 < self.target_min < self.target_max):
            raise ValueError("Invalid target glucose range")
        if self.correction_factor <= 0:
            raise ValueError("Correction factor must be positive")
        if self.carb_ratio <= 0:
            raise ValueError("Carb ratio must be positive")
        if self.insulin_duration <= 0:
            raise ValueError("Insulin duration must be positive")
    
    def calculate_correction_dose(self, current_glucose: float) -> float:
        """
        Calculate correction insulin dose based on current glucose level.
        
        Args:
            current_glucose: Current glucose reading in mg/dL
            
        Returns:
            Correction dose in units of insulin (rounded to nearest 0.1 unit)
        """
        if current_glucose <= self.target_min:
            return 0.0
        
        correction_dose = (current_glucose - self.target_max) / self.correction_factor
        return max(0.0, round(correction_dose, 1))
    
    def calculate_meal_dose(self, carbs: float) -> float:
        """
        Calculate meal insulin dose based on carbohydrate intake.
        
        Args:
            carbs: Grams of carbohydrates to be consumed
            
        Returns:
            Meal dose in units of insulin (rounded to nearest 0.1 unit)
        """
        if carbs <= 0:
            return 0.0
            
        meal_dose = carbs / self.carb_ratio
        return round(meal_dose, 1)
    
    def calculate_total_dose(
        self, 
        current_glucose: float, 
        carbs: float, 
        active_insulin: Optional[float] = None
    ) -> float:
        """
        Calculate total insulin dose considering both correction and meal components,
        and accounting for active insulin if provided.
        
        Args:
            current_glucose: Current glucose reading in mg/dL
            carbs: Grams of carbohydrates to be consumed
            active_insulin: Units of insulin still active from previous doses
            
        Returns:
            Total recommended dose in units of insulin (rounded to nearest 0.1 unit)
        """
        correction = self.calculate_correction_dose(current_glucose)
        meal = self.calculate_meal_dose(carbs)
        
        total = correction + meal
        
        if active_insulin is not None and active_insulin > 0:
            total = max(0, total - active_insulin)
        
        return round(total, 1)
    
    def get_active_insulin(
        self, 
        insulin_history: List[Dict], 
        current_time: Optional[datetime] = None
    ) -> float:
        """
        Calculate active insulin based on insulin delivery history.
        
        Args:
            insulin_history: List of insulin delivery records, each containing:
                - 'time': datetime of delivery
                - 'amount': units of insulin delivered
            current_time: Optional datetime to use as reference (defaults to now)
            
        Returns:
            Total active insulin in units
        """
        if current_time is None:
            current_time = datetime.now()
            
        active_insulin = 0.0
        cutoff_time = current_time - timedelta(hours=self.insulin_duration)
        
        for record in insulin_history:
            if record['time'] >= cutoff_time and record['time'] <= current_time:
                # Calculate remaining insulin based on linear decay
                hours_ago = (current_time - record['time']).total_seconds() / 3600
                remaining_percent = max(0, 1 - (hours_ago / self.insulin_duration))
                active_insulin += record['amount'] * remaining_percent
                
        return round(active_insulin, 1)

# Example usage
if __name__ == "__main__":
    # Sample patient settings
    patient_settings = {
        'target_glucose_range': (80, 120),
        'correction_factor': 50,  # 1 unit lowers glucose by 50 mg/dL
        'carb_ratio': 10,        # 1 unit covers 10g carbs
        'insulin_duration': 4    # Insulin active for 4 hours
    }
    
    # Sample data
    current_glucose = 150  # mg/dL
    carbs = 30             # grams
    insulin_history = [
        {'time': datetime.now() - timedelta(hours=2), 'amount': 2.0},
        {'time': datetime.now() - timedelta(hours=1), 'amount': 1.5}
    ]
    
    try:
        calculator = InsulinDosageCalculator(patient_settings)
        
        active_insulin = calculator.get_active_insulin(insulin_history)
        print(f"Active insulin: {active_insulin} units")
        
        total_dose = calculator.calculate_total_dose(current_glucose, carbs, active_insulin)
        print(f"Recommended dose: {total_dose} units")
        
    except ValueError as e:
        print(f"Error in settings: {e}")
```
