"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Suggest a semi-custom solution for testing flex-circuits using AlphaTest µ HELIX ® probes, incorporating their four different tip styles.
Generated: DETERMINISTIC_42008c71293526c6
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Any

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FlexCircuitTester:
    """
    A class to represent a tester for flex-circuits using AlphaTest µ HELIX® probes.
    """

    def __init__(self, probe_types: List[str]):
        """
        Initializes the FlexCircuitTester with the specified probe types.

        :param probe_types: A list of probe types to be used for testing.
        """
        self.probe_types = probe_types
        self.test_results: List[Dict[str, Any]] = []

    def test_circuit(self, circuit_id: str, probe_type: str) -> Dict[str, Any]:
        """
        Tests a flex-circuit with the specified probe type.

        :param circuit_id: The identifier for the circuit being tested.
        :param probe_type: The type of probe to use for testing.
        :return: A dictionary containing the test results.
        """
        if probe_type not in self.probe_types:
            logging.error(f"Invalid probe type: {probe_type}. Available types: {self.probe_types}")
            raise ValueError(f"Invalid probe type: {probe_type}. Available types: {self.probe_types}")

        # Simulate testing logic
        logging.info(f"Testing circuit {circuit_id} with probe type {probe_type}.")
        result = {
            'circuit_id': circuit_id,
            'probe_type': probe_type,
            'status': 'PASS',  # Simulated result
            'details': 'Test completed successfully.'
        }
        self.test_results.append(result)
        logging.info(f"Test result for circuit {circuit_id}: {result}")
        return result

    def get_test_results(self) -> List[Dict[str, Any]]:
        """
        Retrieves the test results.

        :return: A list of dictionaries containing all test results.
        """
        return self.test_results

def main():
    """
    Main function to execute the flex-circuit testing.
    """
    # Define available probe types
    probe_types = ['Standard', 'Fine', 'Ultra-Fine', 'Heavy-Duty']

    # Create a FlexCircuitTester instance
    tester = FlexCircuitTester(probe_types)

    # Example circuit IDs to test
    circuit_ids = ['CIRCUIT_001', 'CIRCUIT_002', 'CIRCUIT_003']

    # Perform tests with different probe types
    for circuit_id in circuit_ids:
        for probe_type in probe_types:
            try:
                tester.test_circuit(circuit_id, probe_type)
            except ValueError as e:
                logging.error(f"Error testing circuit {circuit_id} with probe {probe_type}: {e}")

    # Retrieve and print all test results
    results = tester.get_test_results()
    logging.info("All test results:")
    for result in results:
        logging.info(result)

if __name__ == "__main__":
    main()
```
