"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Write a Python script that calculates the fees for various notarial services, including union stable and apostilamento, based on the provided tabela de emolumentos.
Generated: DETERMINISTIC_317784a3fc3e3da4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class NotarialServiceFeeCalculator:
    """
    A class to calculate fees for various notarial services based on a fee schedule.
    """

    def __init__(self, fee_schedule_file):
        """
        Initializes the fee calculator with a fee schedule.

        :param fee_schedule_file: Path to the JSON file containing the fee schedule.
        """
        self.fee_schedule = self.load_fee_schedule(fee_schedule_file)

    def load_fee_schedule(self, file_path):
        """
        Loads the fee schedule from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing the fee schedule.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Fee schedule file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from the file: {file_path}")

    def calculate_fee(self, service_name):
        """
        Calculates the fee for a given notarial service.

        :param service_name: The name of the notarial service.
        :return: The fee for the service.
        :raises ValueError: If the service is not found in the fee schedule.
        """
        try:
            fee = self.fee_schedule[service_name]
            return fee
        except KeyError:
            raise ValueError(f"Service '{service_name}' not found in the fee schedule.")

def main():
    """
    Main function to execute the fee calculation.
    """
    fee_schedule_file = 'fee_schedule.json'  # Path to the fee schedule JSON file
    calculator = NotarialServiceFeeCalculator(fee_schedule_file)

    # List of services to calculate fees for
    services = ['union_stable', 'apostilamento']

    for service in services:
        try:
            fee = calculator.calculate_fee(service)
            print(f"The fee for {service.replace('_', ' ').title()} is: {fee}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a `fee_schedule.json` file in the same directory as this script, containing the fee structure in JSON format, for example:

```json
{
    "union_stable": 100,
    "apostilamento": 50
}
```
