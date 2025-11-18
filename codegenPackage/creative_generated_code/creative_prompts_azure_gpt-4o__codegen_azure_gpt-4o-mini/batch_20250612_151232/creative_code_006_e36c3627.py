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
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Cargo:
    def __init__(self, cargo_id, weight, content_description):
        self.cargo_id = cargo_id
        self.weight = weight
        self.content_description = content_description

class SafetyCheck:
    def __init__(self):
        self.checks = []

    def add_check(self, check):
        """Add a safety check to the list."""
        self.checks.append(check)

    def perform_checks(self, cargo):
        """Perform safety checks on the given cargo."""
        results = {}
        for check in self.checks:
            result = check(cargo)
            results[check.__name__] = result
        return results

def weight_check(cargo):
    """Check if cargo weight is within acceptable limits."""
    if cargo.weight > 1000:  # Assume 1000 kg is the max limit for this example
        logging.warning(f"Cargo {cargo.cargo_id} exceeds weight limit: {cargo.weight} kg")
        return False
    return True

def content_check(cargo):
    """Check if the content description is acceptable."""
    hazardous_materials = ["explosive", "flammable", "toxic"]
    if any(material in cargo.content_description.lower() for material in hazardous_materials):
        logging.warning(f"Cargo {cargo.cargo_id} contains hazardous material: {cargo.content_description}")
        return False
    return True

class SecurityCheck:
    def __init__(self):
        self.checks = []

    def add_check(self, check):
        """Add a security check to the list."""
        self.checks.append(check)

    def perform_checks(self, cargo):
        """Perform security checks on the given cargo."""
        results = {}
        for check in self.checks:
            result = check(cargo)
            results[check.__name__] = result
        return results

def documentation_check(cargo):
    """Check if all necessary documentation is provided for the cargo."""
    # In a real scenario, we would check against a database or external system
    needed_docs = ["bill_of_lading", "insurance_certificate"]
    # Simulating documentation presence
    docs_present = ["bill_of_lading"]  # Simulated presence of only one document
    missing_docs = [doc for doc in needed_docs if doc not in docs_present]
    if missing_docs:
        logging.warning(f"Cargo {cargo.cargo_id} is missing documentation: {missing_docs}")
        return False
    return True

def validate_cargo(cargo):
    """Validate cargo by performing safety and security checks."""
    safety_checker = SafetyCheck()
    safety_checker.add_check(weight_check)
    safety_checker.add_check(content_check)

    security_checker = SecurityCheck()
    security_checker.add_check(documentation_check)

    safety_results = safety_checker.perform_checks(cargo)
    security_results = security_checker.perform_checks(cargo)

    return {
        "safety_checks": safety_results,
        "security_checks": security_results
    }

def log_results(cargo, results):
    """Log results of the checks to a JSON file."""
    log_entry = {
        "cargo_id": cargo.cargo_id,
        "timestamp": datetime.now().isoformat(),
        "results": results
    }
    with open("cargo_check_log.json", "a") as log_file:
        json.dump(log_entry, log_file)
        log_file.write('\n')

def main():
    try:
        # Example cargo to check
        cargo = Cargo(cargo_id="CARGO123", weight=1200, content_description="Non-flammable materials")

        # Validate the cargo
        results = validate_cargo(cargo)

        # Log the results
        log_results(cargo, results)

        logging.info("Cargo validation completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during cargo validation: {e}")

if __name__ == "__main__":
    main()
```
