"""
Generated Code Metadata:
========================
Original URL: https://1inch.exchange.crlegal.com.co
Prompt: Write a Python script to track and manage pest control services, including technician training, insurance coverage, and disinfectant usage, based on the BPCA's recommendations.
Generated: DETERMINISTIC_249ef0cef71346c6
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime


class PestControlServiceManager:
    """
    A class to manage pest control services, including technician training,
    insurance coverage, and disinfectant usage based on BPCA's recommendations.
    """

    def __init__(self):
        # Initialize data storage
        self.technicians = []  # List of technicians
        self.insurance_policies = []  # List of insurance policies
        self.disinfectant_usage = []  # List of disinfectant usage records

    def add_technician(self, name, training_date, certifications):
        """
        Add a new technician to the system.

        :param name: Name of the technician
        :param training_date: Date of training completion (YYYY-MM-DD)
        :param certifications: List of certifications obtained
        """
        try:
            training_date = datetime.datetime.strptime(training_date, "%Y-%m-%d").date()
            technician = {
                "name": name,
                "training_date": training_date,
                "certifications": certifications,
            }
            self.technicians.append(technician)
            print(f"Technician '{name}' added successfully.")
        except ValueError:
            print("Error: Invalid training date format. Use YYYY-MM-DD.")

    def add_insurance_policy(self, policy_number, provider, coverage_amount, expiry_date):
        """
        Add a new insurance policy to the system.

        :param policy_number: Unique policy number
        :param provider: Insurance provider name
        :param coverage_amount: Coverage amount in USD
        :param expiry_date: Expiry date of the policy (YYYY-MM-DD)
        """
        try:
            expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
            policy = {
                "policy_number": policy_number,
                "provider": provider,
                "coverage_amount": coverage_amount,
                "expiry_date": expiry_date,
            }
            self.insurance_policies.append(policy)
            print(f"Insurance policy '{policy_number}' added successfully.")
        except ValueError:
            print("Error: Invalid expiry date format. Use YYYY-MM-DD.")

    def record_disinfectant_usage(self, disinfectant_name, quantity_used, usage_date):
        """
        Record the usage of a disinfectant.

        :param disinfectant_name: Name of the disinfectant
        :param quantity_used: Quantity used in liters
        :param usage_date: Date of usage (YYYY-MM-DD)
        """
        try:
            usage_date = datetime.datetime.strptime(usage_date, "%Y-%m-%d").date()
            usage_record = {
                "disinfectant_name": disinfectant_name,
                "quantity_used": quantity_used,
                "usage_date": usage_date,
            }
            self.disinfectant_usage.append(usage_record)
            print(f"Disinfectant usage for '{disinfectant_name}' recorded successfully.")
        except ValueError:
            print("Error: Invalid usage date format. Use YYYY-MM-DD.")

    def save_data_to_file(self, filename):
        """
        Save all data to a JSON file.

        :param filename: Name of the file to save data
        """
        try:
            data = {
                "technicians": self.technicians,
                "insurance_policies": self.insurance_policies,
                "disinfectant_usage": self.disinfectant_usage,
            }
            with open(filename, "w") as file:
                json.dump(data, file, default=str, indent=4)
            print(f"Data saved to file '{filename}' successfully.")
        except Exception as e:
            print(f"Error saving data to file: {e}")

    def load_data_from_file(self, filename):
        """
        Load data from a JSON file.

        :param filename: Name of the file to load data
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.technicians = data.get("technicians", [])
                self.insurance_policies = data.get("insurance_policies", [])
                self.disinfectant_usage = data.get("disinfectant_usage", [])
            print(f"Data loaded from file '{filename}' successfully.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON data.")
        except Exception as e:
            print(f"Error loading data from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = PestControlServiceManager()

    # Add sample data
    manager.add_technician("John Doe", "2023-01-15", ["BPCA Level 2", "First Aid"])
    manager.add_insurance_policy("POL12345", "ABC Insurance", 500000, "2024-12-31")
    manager.record_disinfectant_usage("Disinfectant X", 10, "2023-10-01")

    # Save data to file
    manager.save_data_to_file("pest_control_data.json")

    # Load data from file
    manager.load_data_from_file("pest_control_data.json")
```
