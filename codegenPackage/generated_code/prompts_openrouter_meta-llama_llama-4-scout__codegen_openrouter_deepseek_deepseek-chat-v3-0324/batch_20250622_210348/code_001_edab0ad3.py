"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: "Write a Python script to manage laboratory test orders and pricing for a clinical laboratory like Laboratorio Savaz, including tests for liver function, lipid profiles, and pregnancy."
Generated: DETERMINISTIC_edab0ad30c4e01b0
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class LaboratoryTest:
    """Represents a laboratory test with its details."""
    
    def __init__(self, test_id: str, name: str, price: float, description: str = ""):
        """
        Initialize a laboratory test.
        
        Args:
            test_id: Unique identifier for the test
            name: Name of the test
            price: Price of the test in local currency
            description: Optional description of the test
        """
        self.test_id = test_id
        self.name = name
        self.price = price
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert test details to dictionary for serialization."""
        return {
            'test_id': self.test_id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'LaboratoryTest':
        """Create a LaboratoryTest from a dictionary."""
        return cls(
            test_id=data['test_id'],
            name=data['name'],
            price=data['price'],
            description=data.get('description', "")
        )

class TestOrder:
    """Represents an order for one or more laboratory tests."""
    
    def __init__(self, order_id: str, patient_id: str, tests: List[LaboratoryTest]):
        """
        Initialize a test order.
        
        Args:
            order_id: Unique identifier for the order
            patient_id: Identifier for the patient
            tests: List of LaboratoryTest objects in the order
        """
        self.order_id = order_id
        self.patient_id = patient_id
        self.tests = tests
    
    def calculate_total(self) -> float:
        """Calculate the total price of all tests in the order."""
        return sum(test.price for test in self.tests)
    
    def to_dict(self) -> Dict:
        """Convert order details to dictionary for serialization."""
        return {
            'order_id': self.order_id,
            'patient_id': self.patient_id,
            'tests': [test.to_dict() for test in self.tests],
            'total': self.calculate_total()
        }
    
    @classmethod
    def from_dict(cls, data: Dict, available_tests: Dict[str, LaboratoryTest]) -> 'TestOrder':
        """Create a TestOrder from a dictionary."""
        test_ids = [test['test_id'] for test in data['tests']]
        tests = [available_tests[test_id] for test_id in test_ids]
        return cls(
            order_id=data['order_id'],
            patient_id=data['patient_id'],
            tests=tests
        )

class LaboratoryManager:
    """Manages laboratory tests and orders."""
    
    def __init__(self, data_file: str = "laboratory_data.json"):
        """
        Initialize the laboratory manager.
        
        Args:
            data_file: Path to JSON file for storing data
        """
        self.data_file = data_file
        self.tests: Dict[str, LaboratoryTest] = {}
        self.orders: Dict[str, TestOrder] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load data from the JSON file if it exists."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.tests = {
                        test_id: LaboratoryTest.from_dict(test_data)
                        for test_id, test_data in data.get('tests', {}).items()
                    }
                    self.orders = {
                        order_id: TestOrder.from_dict(order_data, self.tests)
                        for order_id, order_data in data.get('orders', {}).items()
                    }
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """Save data to the JSON file."""
        data = {
            'tests': {test_id: test.to_dict() for test_id, test in self.tests.items()},
            'orders': {order_id: order.to_dict() for order_id, order in self.orders.items()}
        }
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_test(self, test: LaboratoryTest) -> None:
        """Add a new laboratory test."""
        if test.test_id in self.tests:
            raise ValueError(f"Test with ID {test.test_id} already exists")
        self.tests[test.test_id] = test
        self._save_data()
    
    def get_test(self, test_id: str) -> Optional[LaboratoryTest]:
        """Retrieve a test by its ID."""
        return self.tests.get(test_id)
    
    def list_tests(self) -> List[LaboratoryTest]:
        """List all available tests."""
        return list(self.tests.values())
    
    def create_order(self, order_id: str, patient_id: str, test_ids: List[str]) -> TestOrder:
        """Create a new test order."""
        tests = []
        for test_id in test_ids:
            test = self.get_test(test_id)
            if not test:
                raise ValueError(f"Test with ID {test_id} not found")
            tests.append(test)
        
        order = TestOrder(order_id, patient_id, tests)
        self.orders[order_id] = order
        self._save_data()
        return order
    
    def get_order(self, order_id: str) -> Optional[TestOrder]:
        """Retrieve an order by its ID."""
        return self.orders.get(order_id)
    
    def list_orders(self) -> List[TestOrder]:
        """List all orders."""
        return list(self.orders.values())

def initialize_default_tests(manager: LaboratoryManager) -> None:
    """Initialize the system with default test offerings."""
    default_tests = [
        LaboratoryTest("LFT01", "Liver Function Test (Basic)", 1200.00, 
                      "Measures liver enzymes and proteins"),
        LaboratoryTest("LFT02", "Liver Function Test (Comprehensive)", 1800.00,
                      "Extended liver function panel"),
        LaboratoryTest("LIP01", "Lipid Profile (Basic)", 900.00,
                      "Total cholesterol, HDL, LDL, triglycerides"),
        LaboratoryTest("LIP02", "Lipid Profile (Advanced)", 1500.00,
                      "Includes VLDL and lipoprotein analysis"),
        LaboratoryTest("PRE01", "Pregnancy Test (Urine)", 500.00,
                      "Qualitative hCG detection"),
        LaboratoryTest("PRE02", "Pregnancy Test (Blood)", 800.00,
                      "Quantitative hCG measurement")
    ]
    
    for test in default_tests:
        try:
            manager.add_test(test)
        except ValueError:
            continue  # Skip if test already exists

def main_menu() -> None:
    """Display the main menu and handle user interactions."""
    manager = LaboratoryManager()
    initialize_default_tests(manager)
    
    while True:
        print("\nLaboratory Test Management System")
        print("1. List Available Tests")
        print("2. Create New Order")
        print("3. View Order Details")
        print("4. List All Orders")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\nAvailable Tests:")
            for test in manager.list_tests():
                print(f"{test.test_id}: {test.name} - ${test.price:.2f}")
                if test.description:
                    print(f"   {test.description}")
        
        elif choice == "2":
            try:
                order_id = input("Enter order ID: ")
                patient_id = input("Enter patient ID: ")
                print("Available Tests:")
                for test in manager.list_tests():
                    print(f"{test.test_id}: {test.name}")
                
                test_ids = []
                while True:
                    test_id = input("Enter test ID to add (or 'done' to finish): ")
                    if test_id.lower() == 'done':
                        break
                    test_ids.append(test_id)
                
                if not test_ids:
                    print("No tests selected. Order not created.")
                    continue
                
                order = manager.create_order(order_id, patient_id, test_ids)
                print(f"\nOrder created successfully. Total: ${order.calculate_total():.2f}")
                print(f"Order ID: {order.order_id}")
                print(f"Patient ID: {order.patient_id}")
                print("Tests:")
                for test in order.tests:
                    print(f"- {test.name}: ${test.price:.2f}")
            
            except ValueError as e:
                print(f"Error creating order: {e}")
        
        elif choice == "3":
            order_id = input("Enter order ID: ")
            order = manager.get_order(order_id)
            if order:
                print("\nOrder Details:")
                print(f"Order ID: {order.order_id}")
                print(f"Patient ID: {order.patient_id}")
                print("Tests:")
                for test in order.tests:
                    print(f"- {test.name}: ${test.price:.2f}")
