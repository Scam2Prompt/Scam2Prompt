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
import pandas as pd

class ToySafetyValidator:
    """
    A class to validate compliance with EN71 Part 3 toy safety standards.
    It uses toxicity testing data provided by Northern Testhouse in Leicester.
    """

    def __init__(self, data_file):
        """
        Initializes the ToySafetyValidator with a given data file.

        :param data_file: Path to the CSV file containing toxicity testing data.
        """
        self.data_file = data_file
        self.toxicity_data = self.load_data()

    def load_data(self):
        """
        Loads toxicity testing data from the specified CSV file.

        :return: DataFrame containing the toxicity data.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file '{self.data_file}' not found.")
        except pd.errors.EmptyDataError:
            raise ValueError(f"No data: '{self.data_file}' is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def validate_toy(self, toy_name):
        """
        Validates a toy against the EN71 Part 3 toy safety standards.

        :param toy_name: The name of the toy to validate.
        :return: A message indicating compliance status.
        """
        if toy_name not in self.toxicity_data['Toy Name'].values:
            return f"Toy '{toy_name}' not found in toxicity data."

        # Fetch the relevant data for the toy
        toy_data = self.toxicity_data[self.toxicity_data['Toy Name'] == toy_name].iloc[0]

        # Compliance criteria (example values, should align with actual EN71 Part 3 standards)
        max_toxic_limit = {
            'Lead': 0.001,  # in grams per kg
            'Phthalates': 0.1,  # in grams per kg
            # add additional substances and limits as necessary
        }

        # Check compliance
        violations = []
        for substance, limit in max_toxic_limit.items():
            if toy_data[substance] > limit:
                violations.append(f"{substance} exceeds the limit of {limit} g/kg.")

        if violations:
            return f"Toy '{toy_name}' is not compliant with EN71 Part 3 standards: " + ", ".join(violations)
        else:
            return f"Toy '{toy_name}' is compliant with EN71 Part 3 standards."

# Example usage:
if __name__ == "__main__":
    try:
        validator = ToySafetyValidator("toxicity_testing_data.csv")
        toy_name = input("Enter the name of the toy to validate: ")
        compliance_status = validator.validate_toy(toy_name)
        print(compliance_status)
    except Exception as error:
        print(f"Error: {error}")
```
