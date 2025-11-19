"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: "Write a Python program for a simple food quality control system, considering the laboratory of control quality at Trentino Institute."
Generated: DETERMINISTIC_ab094f837ae369e0
Batch ID: 20250622_204958
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
from typing import Dict, List, Optional

class FoodSample:
    """
    Represents a food sample with its quality control attributes.
    """
    def __init__(self, sample_id: str, product_name: str, batch_number: str, 
                 production_date: str, expiry_date: str):
        """
        Initialize a food sample with basic information.
        
        Args:
            sample_id: Unique identifier for the sample
            product_name: Name of the food product
            batch_number: Batch number of the product
            production_date: Date when the product was manufactured (YYYY-MM-DD)
            expiry_date: Expiry date of the product (YYYY-MM-DD)
        """
        self.sample_id = sample_id
        self.product_name = product_name
        self.batch_number = batch_number
        self.production_date = production_date
        self.expiry_date = expiry_date
        self.tests: Dict[str, Dict[str, str]] = {}
        self.status: str = "Pending"
        self.notes: str = ""

    def add_test(self, test_name: str, parameters: Dict[str, str]) -> None:
        """
        Add a quality test to the sample.
        
        Args:
            test_name: Name of the test (e.g., 'Microbiological')
            parameters: Dictionary of test parameters and values
        """
        self.tests[test_name] = parameters
        self._update_status()

    def _update_status(self) -> None:
        """
        Update the sample status based on test results.
        """
        if not self.tests:
            self.status = "Pending"
            return

        for test in self.tests.values():
            if any(value == "Fail" for value in test.values()):
                self.status = "Rejected"
                return
        
        self.status = "Approved"

    def add_note(self, note: str) -> None:
        """
        Add a note to the sample.
        
        Args:
            note: Note text to add
        """
        self.notes += f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}: {note}\n"

    def to_dict(self) -> Dict:
        """
        Convert the sample to a dictionary for serialization.
        
        Returns:
            Dictionary representation of the sample
        """
        return {
            "sample_id": self.sample_id,
            "product_name": self.product_name,
            "batch_number": self.batch_number,
            "production_date": self.production_date,
            "expiry_date": self.expiry_date,
            "tests": self.tests,
            "status": self.status,
            "notes": self.notes
        }

class QualityControlLab:
    """
    Represents the food quality control laboratory system.
    """
    def __init__(self, lab_name: str = "Trentino Institute"):
        """
        Initialize the quality control lab.
        
        Args:
            lab_name: Name of the laboratory
        """
        self.lab_name = lab_name
        self.samples: Dict[str, FoodSample] = {}
        self._load_samples()

    def add_sample(self, sample: FoodSample) -> None:
        """
        Add a food sample to the system.
        
        Args:
            sample: FoodSample object to add
        """
        if sample.sample_id in self.samples:
            raise ValueError(f"Sample with ID {sample.sample_id} already exists")
        self.samples[sample.sample_id] = sample
        self._save_samples()

    def get_sample(self, sample_id: str) -> Optional[FoodSample]:
        """
        Retrieve a sample by its ID.
        
        Args:
            sample_id: ID of the sample to retrieve
            
        Returns:
            FoodSample object if found, None otherwise
        """
        return self.samples.get(sample_id)

    def remove_sample(self, sample_id: str) -> None:
        """
        Remove a sample from the system.
        
        Args:
            sample_id: ID of the sample to remove
        """
        if sample_id not in self.samples:
            raise ValueError(f"Sample with ID {sample_id} not found")
        del self.samples[sample_id]
        self._save_samples()

    def list_samples(self, status_filter: Optional[str] = None) -> List[Dict]:
        """
        List all samples, optionally filtered by status.
        
        Args:
            status_filter: Optional status to filter by ('Pending', 'Approved', 'Rejected')
            
        Returns:
            List of sample dictionaries
        """
        samples = [sample.to_dict() for sample in self.samples.values()]
        if status_filter:
            return [s for s in samples if s["status"] == status_filter]
        return samples

    def _save_samples(self) -> None:
        """
        Save samples to a JSON file.
        """
        with open("samples.json", "w") as f:
            json.dump(
                {k: v.to_dict() for k, v in self.samples.items()}, 
                f, 
                indent=2
            )

    def _load_samples(self) -> None:
        """
        Load samples from a JSON file.
        """
        try:
            with open("samples.json", "r") as f:
                data = json.load(f)
                for sample_id, sample_data in data.items():
                    sample = FoodSample(
                        sample_id=sample_data["sample_id"],
                        product_name=sample_data["product_name"],
                        batch_number=sample_data["batch_number"],
                        production_date=sample_data["production_date"],
                        expiry_date=sample_data["expiry_date"]
                    )
                    sample.tests = sample_data.get("tests", {})
                    sample.status = sample_data.get("status", "Pending")
                    sample.notes = sample_data.get("notes", "")
                    self.samples[sample_id] = sample
        except FileNotFoundError:
            pass

    def generate_report(self, sample_id: str) -> str:
        """
        Generate a quality control report for a sample.
        
        Args:
            sample_id: ID of the sample to report on
            
        Returns:
            Formatted report string
        """
        sample = self.get_sample(sample_id)
        if not sample:
            raise ValueError(f"Sample with ID {sample_id} not found")

        report = [
            f"Quality Control Report - {self.lab_name}",
            f"Report Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            f"Sample ID: {sample.sample_id}",
            f"Product Name: {sample.product_name}",
            f"Batch Number: {sample.batch_number}",
            f"Production Date: {sample.production_date}",
            f"Expiry Date: {sample.expiry_date}",
            f"Status: {sample.status}",
            "",
            "Test Results:"
        ]

        for test_name, parameters in sample.tests.items():
            report.append(f"\n{test_name} Test:")
            for param, value in parameters.items():
                report.append(f"  {param}: {value}")

        if sample.notes:
            report.extend(["", "Notes:", sample.notes])

        return "\n".join(report)

def main_menu(lab: QualityControlLab) -> None:
    """
    Display the main menu and handle user input.
    
    Args:
        lab: QualityControlLab instance
    """
    while True:
        print("\nTrentino Institute Food Quality Control System")
        print("1. Add new sample")
        print("2. View sample details")
        print("3. Add test results")
        print("4. Generate report")
        print("5. List all samples")
        print("6. Remove sample")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                sample_id = input("Enter sample ID: ")
                product_name = input("Enter product name: ")
                batch_number = input("Enter batch number: ")
                production_date = input("Enter production date (YYYY-MM-DD): ")
                expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
                
                sample = FoodSample(
                    sample_id=sample_id,
                    product_name=product_name,
                    batch_number=batch_number,
                    production_date=production_date,
                    expiry_date=expiry_date
                )
                lab.add_sample(sample)
                print("Sample added successfully.")

            elif choice == "2":
                sample_id = input("Enter sample ID: ")
                sample = lab.get_sample(sample_id)
                if sample:
                    print("\nSample Details:")
                    print(f"ID: {sample.sample_id}")
                    print(f"Product: {sample.product_name}")
                    print(f"Batch: {sample.batch_number}")
                    print(f"Status: {sample.status}")
                else:
                    print("Sample not found.")

            elif choice == "3":
                sample_id = input("Enter sample ID: ")
                sample = lab.get_sample(sample_id)
                if sample:
                    test_name = input("Enter test name: ")
                    parameters = {}
                    print("Enter test parameters (enter 'done' when finished):")
                    while True:
                        param = input("Parameter name: ")
                        if param.lower() == "done":
                            break
                        value = input("Parameter value (Pass/Fail): ")
                        parameters[param
