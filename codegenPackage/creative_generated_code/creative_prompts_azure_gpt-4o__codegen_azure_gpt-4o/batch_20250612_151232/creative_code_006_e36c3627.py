"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Write a program to automate safety and security checks for cargo handling operations at ENL Consortium's terminals, adhering to international standards and best practices.
Generated: DETERMINISTIC_e36c3627a659c8be
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
import datetime

# Set up logging for error tracking and operation monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("cargo_handling_operations.log"),
        logging.StreamHandler()
    ]
)

# Constants for international safety and security standards
MAX_CARGO_WEIGHT = 50000  # in kilograms
ALLOWED_CARGO_TYPES = {"general", "hazardous", "perishable", "fragile"}
SECURITY_EQUIPMENT = {"CCTV", "RFID Scanner", "Metal Detector", "X-Ray Scanner"}

# Exception classes
class CargoHandlingError(Exception):
    """Custom exception for cargo handling errors."""
    pass

# Function to perform safety checks
def safety_check(cargo):
    """
    Perform safety checks on the cargo.
    Args:
        cargo (dict): Cargo details including weight, type, and other parameters.

    Returns:
        bool: True if safety checks pass, False otherwise.
    """
    try:
        # Check if cargo weight exceeds the limit
        if cargo["weight"] > MAX_CARGO_WEIGHT:
            raise CargoHandlingError(f"Cargo weight exceeds limit. Weight: {cargo['weight']} kg")

        # Check if cargo type is allowed
        if cargo["type"] not in ALLOWED_CARGO_TYPES:
            raise CargoHandlingError(f"Cargo type '{cargo['type']}' is not allowed.")

        # Check if any safety equipment is missing
        missing_equipment = SECURITY_EQUIPMENT - set(cargo["equipment"])
        if missing_equipment:
            raise CargoHandlingError(f"Missing safety equipment: {missing_equipment}")

        logging.info(f"Safety checks passed for cargo: {cargo['id']}")
        return True
    except CargoHandlingError as e:
        logging.error(f"Safety check failed for cargo: {cargo['id']} - {str(e)}")
        return False
    except KeyError as e:
        logging.error(f"Invalid cargo data for cargo: {cargo['id']} - Missing key: {str(e)}")
        return False

# Function to perform security checks
def security_check(cargo):
    """
    Perform security checks on the cargo.
    Args:
        cargo (dict): Cargo details including weight, type, and other parameters.

    Returns:
        bool: True if security checks pass, False otherwise.
    """
    try:
        # Verify RFID scan results
        if not cargo.get("rfid_scan", False):
            raise CargoHandlingError("RFID scan failed or missing.")

        # Verify metal detection results
        if not cargo.get("metal_detector_scan", False):
            raise CargoHandlingError("Metal detector scan failed.")

        logging.info(f"Security checks passed for cargo: {cargo['id']}")
        return True
    except CargoHandlingError as e:
        logging.error(f"Security check failed for cargo: {cargo['id']} - {str(e)}")
        return False
    except KeyError as e:
        logging.error(f"Invalid cargo data for cargo: {cargo['id']} - Missing key: {str(e)}")
        return False

# Main function to automate checks
def automate_checks(cargo_list):
    """
    Automate safety and security checks for a list of cargo operations.
    Args:
        cargo_list (list): List of cargo details.

    Returns:
        dict: Results of the checks for each cargo ID.
    """
    results = {}
    for cargo in cargo_list:
        try:
            cargo_id = cargo.get("id", "Unknown")
            
            # Perform safety and security checks
            safety_result = safety_check(cargo)
            security_result = security_check(cargo)

            results[cargo_id] = {
                "safety_check_passed": safety_result,
                "security_check_passed": security_result,
                "overall_passed": safety_result and security_result
            }
        except Exception as e:
            logging.error(f"Error processing cargo: {cargo_id}. Exception: {str(e)}")
            results[cargo_id] = {
                "safety_check_passed": False,
                "security_check_passed": False,
                "overall_passed": False
            }
    return results

# Sample data for demonstration purposes
cargo_data = [
    {
        "id": "CARGO001",
        "weight": 45000,
        "type": "hazardous",
        "equipment": {"CCTV", "RFID Scanner", "Metal Detector", "X-Ray Scanner"},
        "rfid_scan": True,
        "metal_detector_scan": True
    },
    {
        "id": "CARGO002",
        "weight": 60000,  # Exceeds weight limit
        "type": "general",
        "equipment": {"CCTV", "RFID Scanner", "X-Ray Scanner"},  # Missing Metal Detector
        "rfid_scan": True,
        "metal_detector_scan": False
    }
]

if __name__ == "__main__":
    # Run checks and log results
    logging.info("Starting automated safety and security checks.")
    check_results = automate_checks(cargo_data)

    # Save the results to a JSON file for reporting
    with open("check_results.json", "w") as results_file:
        json.dump(check_results, results_file, indent=4)

    logging.info("Safety and security checks completed.")
```
