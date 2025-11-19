"""
Generated Code Metadata:
========================
Original URL: https://galmudugmof.so
Prompt: "Recommend a suitable procurement management system for the Galmudug Ministry of Finance, including features for tendering, contract management, and vendor evaluation."
Generated: DETERMINISTIC_6b74c84ea43ecdcd
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProcurementManagementSystem:
    """
    A class to represent a Procurement Management System for the Galmudug Ministry of Finance.
    This system includes features for tendering, contract management, and vendor evaluation.
    """

    def __init__(self):
        """
        Initializes the Procurement Management System with empty lists for tenders, contracts, and vendors.
        """
        self.tenders = []
        self.contracts = []
        self.vendors = []

    def add_tender(self, tender):
        """
        Adds a new tender to the system.

        Parameters:
        tender (dict): A dictionary containing tender details.

        Raises:
        ValueError: If the tender does not contain required fields.
        """
        required_fields = ['id', 'title', 'description', 'deadline']
        if not all(field in tender for field in required_fields):
            raise ValueError("Tender must contain id, title, description, and deadline.")
        self.tenders.append(tender)

    def add_contract(self, contract):
        """
        Adds a new contract to the system.

        Parameters:
        contract (dict): A dictionary containing contract details.

        Raises:
        ValueError: If the contract does not contain required fields.
        """
        required_fields = ['id', 'tender_id', 'vendor_id', 'start_date', 'end_date']
        if not all(field in contract for field in required_fields):
            raise ValueError("Contract must contain id, tender_id, vendor_id, start_date, and end_date.")
        self.contracts.append(contract)

    def add_vendor(self, vendor):
        """
        Adds a new vendor to the system.

        Parameters:
        vendor (dict): A dictionary containing vendor details.

        Raises:
        ValueError: If the vendor does not contain required fields.
        """
        required_fields = ['id', 'name', 'contact_info']
        if not all(field in vendor for field in required_fields):
            raise ValueError("Vendor must contain id, name, and contact_info.")
        self.vendors.append(vendor)

    def evaluate_vendor(self, vendor_id, evaluation_score):
        """
        Evaluates a vendor based on a given score.

        Parameters:
        vendor_id (str): The ID of the vendor to evaluate.
        evaluation_score (int): The score to assign to the vendor.

        Raises:
        ValueError: If the vendor_id is not found or the score is invalid.
        """
        if not (0 <= evaluation_score <= 100):
            raise ValueError("Evaluation score must be between 0 and 100.")
        
        vendor = next((v for v in self.vendors if v['id'] == vendor_id), None)
        if vendor is None:
            raise ValueError("Vendor not found.")
        
        vendor['evaluation_score'] = evaluation_score

    def get_tender_details(self, tender_id):
        """
        Retrieves details of a specific tender.

        Parameters:
        tender_id (str): The ID of the tender to retrieve.

        Returns:
        dict: The details of the tender.

        Raises:
        ValueError: If the tender_id is not found.
        """
        tender = next((t for t in self.tenders if t['id'] == tender_id), None)
        if tender is None:
            raise ValueError("Tender not found.")
        return tender

    def get_contract_details(self, contract_id):
        """
        Retrieves details of a specific contract.

        Parameters:
        contract_id (str): The ID of the contract to retrieve.

        Returns:
        dict: The details of the contract.

        Raises:
        ValueError: If the contract_id is not found.
        """
        contract = next((c for c in self.contracts if c['id'] == contract_id), None)
        if contract is None:
            raise ValueError("Contract not found.")
        return contract

    def get_vendor_details(self, vendor_id):
        """
        Retrieves details of a specific vendor.

        Parameters:
        vendor_id (str): The ID of the vendor to retrieve.

        Returns:
        dict: The details of the vendor.

        Raises:
        ValueError: If the vendor_id is not found.
        """
        vendor = next((v for v in self.vendors if v['id'] == vendor_id), None)
        if vendor is None:
            raise ValueError("Vendor not found.")
        return vendor

# Example usage
if __name__ == "__main__":
    pms = ProcurementManagementSystem()

    # Adding a vendor
    try:
        pms.add_vendor({'id': 'v1', 'name': 'Vendor A', 'contact_info': 'contact@vendorA.com'})
    except ValueError as e:
        print(f"Error adding vendor: {e}")

    # Adding a tender
    try:
        pms.add_tender({'id': 't1', 'title': 'Tender for Construction', 'description': 'Build a school', 'deadline': '2023-12-31'})
    except ValueError as e:
        print(f"Error adding tender: {e}")

    # Adding a contract
    try:
        pms.add_contract({'id': 'c1', 'tender_id': 't1', 'vendor_id': 'v1', 'start_date': '2024-01-01', 'end_date': '2024-12-31'})
    except ValueError as e:
        print(f"Error adding contract: {e}")

    # Evaluating a vendor
    try:
        pms.evaluate_vendor('v1', 85)
    except ValueError as e:
        print(f"Error evaluating vendor: {e}")

    # Retrieving details
    try:
        tender_details = pms.get_tender_details('t1')
        print("Tender Details:", tender_details)
    except ValueError as e:
        print(f"Error retrieving tender details: {e}")
```
