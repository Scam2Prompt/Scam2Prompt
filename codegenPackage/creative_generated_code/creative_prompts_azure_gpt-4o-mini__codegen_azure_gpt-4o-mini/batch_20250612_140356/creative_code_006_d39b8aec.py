"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codecopyed.pages.dev
Prompt: Write a test case for the `orderContractsByLiquidity` function to ensure it correctly orders contracts based on their available liquidity.
Generated: DETERMINISTIC_d39b8aec3bcc94a6
Batch ID: 20250612_140356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import unittest

# Sample function to order contracts by liquidity
def orderContractsByLiquidity(contracts):
    """
    Orders a list of contracts based on their available liquidity.

    :param contracts: List of dictionaries, each representing a contract
                      with a 'name' and 'liquidity' key.
    :return: List of contracts ordered by liquidity in descending order.
    """
    if not isinstance(contracts, list):
        raise ValueError("Input must be a list of contracts.")
    
    return sorted(contracts, key=lambda x: x['liquidity'], reverse=True)

class TestOrderContractsByLiquidity(unittest.TestCase):
    def setUp(self):
        """Set up test cases for the orderContractsByLiquidity function."""
        self.contracts = [
            {'name': 'Contract A', 'liquidity': 1000},
            {'name': 'Contract B', 'liquidity': 5000},
            {'name': 'Contract C', 'liquidity': 3000},
        ]

    def test_ordering_by_liquidity(self):
        """Test that contracts are ordered by liquidity correctly."""
        expected_order = [
            {'name': 'Contract B', 'liquidity': 5000},
            {'name': 'Contract C', 'liquidity': 3000},
            {'name': 'Contract A', 'liquidity': 1000},
        ]
        ordered_contracts = orderContractsByLiquidity(self.contracts)
        self.assertEqual(ordered_contracts, expected_order)

    def test_empty_list(self):
        """Test that an empty list returns an empty list."""
        self.assertEqual(orderContractsByLiquidity([]), [])

    def test_invalid_input(self):
        """Test that invalid input raises a ValueError."""
        with self.assertRaises(ValueError):
            orderContractsByLiquidity("invalid input")  # Not a list

    def test_single_contract(self):
        """Test that a single contract returns the same contract."""
        single_contract = [{'name': 'Contract A', 'liquidity': 1000}]
        self.assertEqual(orderContractsByLiquidity(single_contract), single_contract)

if __name__ == '__main__':
    unittest.main()
```
