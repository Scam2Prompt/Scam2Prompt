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
# laboratory_test_manager.py

class LaboratoryTest:
    """Represents a laboratory test with its name, price, and description."""

    def __init__(self, test_id, name, price, description):
        """
        Initializes a LaboratoryTest object.

        Args:
            test_id (int): Unique identifier for the test.
            name (str): Name of the test.
            price (float): Price of the test.
            description (str): Description of the test.
        """
        self.test_id = test_id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Test ID: {self.test_id}, Name: {self.name}, Price: ${self.price:.2f}"


class LaboratoryTestManager:
    """Manages laboratory tests and their pricing."""

    def __init__(self):
        """Initializes a LaboratoryTestManager object with an empty test catalog."""
        self.test_catalog = {}

    def add_test(self, test):
        """
        Adds a test to the test catalog.

        Args:
            test (LaboratoryTest): Test to add.

        Raises:
            ValueError: If a test with the same ID already exists.
        """
        if test.test_id in self.test_catalog:
            raise ValueError("Test with the same ID already exists.")
        self.test_catalog[test.test_id] = test

    def remove_test(self, test_id):
        """
        Removes a test from the test catalog.

        Args:
            test_id (int): ID of the test to remove.

        Raises:
            KeyError: If the test ID is not found in the catalog.
        """
        if test_id not in self.test_catalog:
            raise KeyError("Test ID not found in the catalog.")
        del self.test_catalog[test_id]

    def update_test_price(self, test_id, new_price):
        """
        Updates the price of a test in the test catalog.

        Args:
            test_id (int): ID of the test to update.
            new_price (float): New price of the test.

        Raises:
            KeyError: If the test ID is not found in the catalog.
        """
        if test_id not in self.test_catalog:
            raise KeyError("Test ID not found in the catalog.")
        self.test_catalog[test_id].price = new_price

    def get_test(self, test_id):
        """
        Retrieves a test from the test catalog.

        Args:
            test_id (int): ID of the test to retrieve.

        Returns:
            LaboratoryTest: The test object if found, otherwise None.
        """
        return self.test_catalog.get(test_id)

    def list_tests(self):
        """Returns a list of all tests in the test catalog."""
        return list(self.test_catalog.values())


def main():
    # Create a laboratory test manager
    test_manager = LaboratoryTestManager()

    # Create tests
    liver_function_test = LaboratoryTest(1, "Liver Function Test", 50.0, "Assesses liver health.")
    lipid_profile_test = LaboratoryTest(2, "Lipid Profile Test", 75.0, "Evaluates cholesterol levels.")
    pregnancy_test = LaboratoryTest(3, "Pregnancy Test", 20.0, "Detects pregnancy.")

    # Add tests to the test catalog
    test_manager.add_test(liver_function_test)
    test_manager.add_test(lipid_profile_test)
    test_manager.add_test(pregnancy_test)

    # List all tests
    print("Available Tests:")
    for test in test_manager.list_tests():
        print(test)

    # Update test price
    test_manager.update_test_price(1, 55.0)
    print("\nUpdated Liver Function Test Price:")
    print(test_manager.get_test(1))

    # Remove a test
    test_manager.remove_test(2)

    # List all tests after removal
    print("\nAvailable Tests after removal:")
    for test in test_manager.list_tests():
        print(test)


if __name__ == "__main__":
    main()
```
