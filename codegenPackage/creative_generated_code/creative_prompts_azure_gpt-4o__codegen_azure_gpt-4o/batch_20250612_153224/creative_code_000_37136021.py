"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://organic.yirgacheffeunion.com
Prompt: Write Python code to validate compliance with EN71 Part 3 toy safety standards using toxicity testing data, referencing the services provided by Northern Testhouse in Leicester.
Generated: DETERMINISTIC_3713602162ad220b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv

class EN71ComplianceValidator:
    """
    A class to validate compliance with EN71 Part 3 toy safety standards using toxicity testing data.
    References the services provided by Northern Testhouse in Leicester.
    """

    def __init__(self, standard_limits):
        """
        Initialize the validator with defined limits for EN71 Part 3.
        
        :param standard_limits: Dictionary containing maximum allowable limits for each substance.
        Example:
        {
            "Lead": 90.0,
            "Cadmium": 75.0,
            "Mercury": 60.0,
        }
        """
        self.standard_limits = standard_limits

    def validate_compliance(self, test_results):
        """
        Validate the compliance of test results against EN71 Part 3 safety standards.
        
        :param test_results: Dictionary containing substance test results.
        Example:
        {
            "Lead": 85.0,
            "Cadmium": 50.0,
            "Mercury": 70.0,
        }
        :return: Tuple containing compliance status (True or False) and a list of non-compliant substances.
        """
        non_compliant_substances = []
        for substance, value in test_results.items():
            limit = self.standard_limits.get(substance)
            if limit is None:
                raise ValueError(f"Substance '{substance}' is not defined in the standard limits.")
            if value > limit:
                non_compliant_substances.append(substance)
        
        compliance_status = len(non_compliant_substances) == 0
        return compliance_status, non_compliant_substances

    def load_test_data_from_csv(self, file_path):
        """
        Load toxicity testing data from a CSV file.
        
        :param file_path: Path to the CSV file containing test results.
        :return: Dictionary of test results where keys are substance names and values are their measured quantities.
        """
        test_results = {}
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    for substance, value in row.items():
                        try:
                            test_results[substance] = float(value)
                        except ValueError:
                            raise ValueError(f"Invalid value for {substance}: {value}. Must be a numeric value.")
            return test_results
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{file_path}' was not found.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while reading the test data: {e}")

def main():
    """
    Main function to validate EN71 Part 3 compliance using test data.
    """
    # Define standard limits for EN71 Part 3
    standard_limits = {
        "Lead": 90.0,  # mg/kg
        "Cadmium": 75.0,  # mg/kg
        "Mercury": 60.0,  # mg/kg
        "Arsenic": 25.0,  # mg/kg
    }

    # Initialize the validator
    validator = EN71ComplianceValidator(standard_limits)

    # Path to the test data CSV file
    csv_file_path = 'toxicity_test_results.csv'

    try:
        # Load test results from CSV
        test_results = validator.load_test_data_from_csv(csv_file_path)

        # Validate compliance
        compliance_status, non_compliant_substances = validator.validate_compliance(test_results)

        # Display results
        if compliance_status:
            print("The toy is compliant with EN71 Part 3 standards.")
        else:
            print("The toy is NOT compliant with EN71 Part 3 standards.")
            print("Non-compliant substances:", ', '.join(non_compliant_substances))

    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
