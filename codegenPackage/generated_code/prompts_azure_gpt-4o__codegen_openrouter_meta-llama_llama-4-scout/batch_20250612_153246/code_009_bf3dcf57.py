"""
Generated Code Metadata:
========================
Original URL: https://myhealthcarebilling.com
Prompt: Write a script to consolidate billing functions into a single system, reducing overhead costs and minimizing errors, as emphasized on My Healthcare Billing's website.
Generated: DETERMINISTIC_bf3dcf5776fe2976
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# billing_system.py

class BillingSystem:
    """
    A class to consolidate billing functions into a single system.

    Attributes:
    ----------
    patients : dict
        A dictionary of patients with their billing information.
    services : dict
        A dictionary of services with their corresponding costs.

    Methods:
    -------
    add_patient(patient_id, name, insurance)
        Adds a patient to the billing system.
    add_service(service_id, name, cost)
        Adds a service to the billing system.
    generate_bill(patient_id, services_used)
        Generates a bill for a patient based on the services used.
    """

    def __init__(self):
        """
        Initializes the billing system.
        """
        self.patients = {}
        self.services = {}

    def add_patient(self, patient_id, name, insurance):
        """
        Adds a patient to the billing system.

        Args:
        ----
        patient_id (str): The ID of the patient.
        name (str): The name of the patient.
        insurance (str): The insurance provider of the patient.

        Raises:
        ------
        ValueError: If the patient ID already exists.
        """
        if patient_id in self.patients:
            raise ValueError("Patient ID already exists")
        self.patients[patient_id] = {"name": name, "insurance": insurance, "bills": []}

    def add_service(self, service_id, name, cost):
        """
        Adds a service to the billing system.

        Args:
        ----
        service_id (str): The ID of the service.
        name (str): The name of the service.
        cost (float): The cost of the service.

        Raises:
        ------
        ValueError: If the service ID already exists.
        """
        if service_id in self.services:
            raise ValueError("Service ID already exists")
        self.services[service_id] = {"name": name, "cost": cost}

    def generate_bill(self, patient_id, services_used):
        """
        Generates a bill for a patient based on the services used.

        Args:
        ----
        patient_id (str): The ID of the patient.
        services_used (list): A list of service IDs used by the patient.

        Returns:
        -------
        dict: The generated bill.

        Raises:
        ------
        ValueError: If the patient ID does not exist.
        """
        if patient_id not in self.patients:
            raise ValueError("Patient ID does not exist")

        bill = {"patient_id": patient_id, "services": [], "total": 0.0}
        for service_id in services_used:
            if service_id not in self.services:
                raise ValueError("Service ID does not exist")
            service = self.services[service_id]
            bill["services"].append({"service_id": service_id, "name": service["name"], "cost": service["cost"]})
            bill["total"] += service["cost"]

        self.patients[patient_id]["bills"].append(bill)
        return bill

    def get_patient_bills(self, patient_id):
        """
        Gets the bills for a patient.

        Args:
        ----
        patient_id (str): The ID of the patient.

        Returns:
        -------
        list: The bills for the patient.

        Raises:
        ------
        ValueError: If the patient ID does not exist.
        """
        if patient_id not in self.patients:
            raise ValueError("Patient ID does not exist")
        return self.patients[patient_id]["bills"]


def main():
    billing_system = BillingSystem()

    # Add patients
    billing_system.add_patient("P001", "John Doe", "Insurance Provider A")
    billing_system.add_patient("P002", "Jane Doe", "Insurance Provider B")

    # Add services
    billing_system.add_service("S001", "Consultation", 100.0)
    billing_system.add_service("S002", "Surgery", 1000.0)

    # Generate bills
    bill1 = billing_system.generate_bill("P001", ["S001", "S002"])
    bill2 = billing_system.generate_bill("P002", ["S001"])

    # Print bills
    print("Bill for Patient P001:")
    for service in bill1["services"]:
        print(f"Service: {service['name']}, Cost: ${service['cost']:.2f}")
    print(f"Total: ${bill1['total']:.2f}")

    print("\nBill for Patient P002:")
    for service in bill2["services"]:
        print(f"Service: {service['name']}, Cost: ${service['cost']:.2f}")
    print(f"Total: ${bill2['total']:.2f}")

    # Get patient bills
    patient_bills = billing_system.get_patient_bills("P001")
    print("\nBills for Patient P001:")
    for i, bill in enumerate(patient_bills):
        print(f"Bill {i+1}:")
        for service in bill["services"]:
            print(f"Service: {service['name']}, Cost: ${service['cost']:.2f}")
        print(f"Total: ${bill['total']:.2f}")


if __name__ == "__main__":
    main()
```
