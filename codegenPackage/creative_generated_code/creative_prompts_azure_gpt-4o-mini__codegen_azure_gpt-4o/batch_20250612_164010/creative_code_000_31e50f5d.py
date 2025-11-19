"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Write a Python script that performs a structural audit and suggests necessary repairs for buildings over 30 years old, based on the services offered by SOM Civil.
Generated: DETERMINISTIC_31e50f5d5130f626
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import csv
import os

# Define constants for repair suggestions based on SOM Civil's offerings
REPAIR_SUGGESTIONS = {
    "foundation": "Inspect for cracks and uneven settlement, consider reinforcement.",
    "roof": "Evaluate for leaks or material degradation, replace if necessary.",
    "walls": "Check for structural damage like cracks, apply repairs or reinforcement.",
    "electrical": "Upgrade outdated wiring and ensure compliance with safety standards.",
    "plumbing": "Replace corroded pipes and improve water pressure systems."
}

# Define a class to handle building audits
class BuildingAudit:
    def __init__(self, data_file):
        """
        Initialize the BuildingAudit class with the data file path.

        :param data_file: Path to the CSV file containing building data.
        """
        self.data_file = data_file
        self.buildings = []

    def load_data(self):
        """
        Load building data from a CSV file.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file '{self.data_file}' not found.")

        try:
            with open(self.data_file, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.buildings.append({
                        "name": row["name"],
                        "construction_year": int(row["construction_year"]),
                        "location": row["location"]
                    })
        except KeyError as e:
            raise ValueError(f"Missing expected column in data file: {e}")
        except Exception as e:
            raise Exception(f"Error reading data file: {e}")

    def perform_audit(self):
        """
        Perform an audit on buildings over 30 years old.

        :return: List of audit results containing suggestions for repairs.
        """
        audit_results = []
        current_year = datetime.datetime.now().year

        for building in self.buildings:
            building_age = current_year - building["construction_year"]
            if building_age > 30:
                audit_results.append({
                    "name": building["name"],
                    "location": building["location"],
                    "age": building_age,
                    "repair_suggestions": REPAIR_SUGGESTIONS
                })

        return audit_results

    def save_audit_results(self, results, output_file):
        """
        Save audit results to a CSV file.

        :param results: List of audit results.
        :param output_file: Path to the output CSV file.
        """
        try:
            with open(output_file, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "location", "age", "repair_suggestions"])
                writer.writeheader()
                for result in results:
                    writer.writerow({
                        "name": result["name"],
                        "location": result["location"],
                        "age": result["age"],
                        "repair_suggestions": "; ".join(result["repair_suggestions"].values())
                    })
        except Exception as e:
            raise Exception(f"Error saving audit results: {e}")


def main():
    """
    Main function to perform the building structural audit.
    """
    # Input data file and output file paths
    input_file = "building_data.csv"
    output_file = "audit_results.csv"

    try:
        # Initialize and perform the audit
        audit = BuildingAudit(input_file)
        audit.load_data()
        results = audit.perform_audit()

        # Save the results to a file
        audit.save_audit_results(results, output_file)
        print(f"Audit completed successfully. Results saved to '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
