"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jggbbestforyou.com
Prompt: Generate code to calculate insulin dosage adjustments based on data from Medtrum TouchCare® Nano pump and Abbott FreeStyle Libre CGM.
Generated: DETERMINISTIC_b284d49bef038818
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime

# Define constants for insulin dosage calculations
INSULIN_SENSITIVITY_FACTOR = 50  # How much 1 unit of insulin lowers blood glucose (mg/dL)
CARB_RATIO = 10                 # Grams of carbs covered by 1 unit of insulin
TARGET_BG = 120                 # Target blood glucose level (mg/dL)

# Define error classes for custom exceptions
class DeviceDataError(Exception):
    """Custom exception for device data errors"""
    pass

class DosageCalculationError(Exception):
    """Custom exception for dosage calculation errors"""
    pass

def load_device_data(medtrum_file: str, freestyle_file: str):
    """
    Load data from Medtrum TouchCare Nano pump and Abbott FreeStyle Libre CGM.
    
    Args:
        medtrum_file (str): File path to Medtrum device data (JSON format).
        freestyle_file (str): File path to FreeStyle CGM data (JSON format).
    
    Returns:
        dict: Combined dictionary of relevant data.
    
    Raises:
        DeviceDataError: If there's an issue loading or parsing the data.
    """
    try:
        # Load data from Medtrum device
        with open(medtrum_file, 'r') as medtrum_data_file:
            medtrum_data = json.load(medtrum_data_file)
        
        # Load data from FreeStyle CGM
        with open(freestyle_file, 'r') as freestyle_data_file:
            freestyle_data = json.load(freestyle_data_file)
        
        # Extract relevant data from both sources
        insulin_on_board = medtrum_data.get("insulin_on_board", 0)  # Units of insulin currently active
        current_bg = freestyle_data.get("current_bg")              # Current blood glucose value (mg/dL)
        
        if current_bg is None:
            raise DeviceDataError("Current blood glucose value is missing in CGM data.")
        
        return {
            "insulin_on_board": insulin_on_board,
            "current_bg": current_bg
        }
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise DeviceDataError(f"Error loading device data: {e}")

def calculate_insulin_dosage(device_data: dict, carbs: float):
    """
    Calculate insulin dosage adjustment based on device data and carb intake.
    
    Args:
        device_data (dict): Dictionary containing 'insulin_on_board' and 'current_bg'.
        carbs (float): Number of grams of carbohydrates consumed.
    
    Returns:
        float: Recommended insulin dosage adjustment (units).
    
    Raises:
        DosageCalculationError: If there is an issue with the calculation.
    """
    try:
        current_bg = device_data["current_bg"]
        insulin_on_board = device_data["insulin_on_board"]
        
        # Calculate correction dosage for blood glucose levels
        correction_dosage = max((current_bg - TARGET_BG) / INSULIN_SENSITIVITY_FACTOR, 0)
        
        # Calculate meal dosage for carbohydrate intake
        meal_dosage = carbs / CARB_RATIO
        
        # Total dosage adjustment, accounting for insulin on board
        total_dosage = correction_dosage + meal_dosage - insulin_on_board
        return max(total_dosage, 0)  # Ensure dosage is not negative
    except KeyError as e:
        raise DosageCalculationError(f"Missing data for dosage calculation: {e}")

def main():
    """
    Main function to calculate insulin dosage adjustments.
    """
    medtrum_file = "medtrum_data.json"  # Replace with actual file path
    freestyle_file = "freestyle_data.json"  # Replace with actual file path
    
    try:
        # Load device data
        device_data = load_device_data(medtrum_file, freestyle_file)
        
        # Input carb count from user or another source
        carbs = float(input("Enter the grams of carbohydrates consumed: "))
        
        # Calculate insulin dosage adjustment
        recommended_dosage = calculate_insulin_dosage(device_data, carbs)
        
        # Output the recommended dosage
        print(f"Recommended insulin dosage adjustment: {recommended_dosage:.2f} units")
    except (DeviceDataError, DosageCalculationError) as e:
        print(f"Error: {e}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for carbohydrates.")

if __name__ == "__main__":
    main()
```
