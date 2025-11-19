"""
Generated Code Metadata:
========================
Original URL: https://codecopyed.pages.dev
Prompt: Write a test case for the `orderContractsByLiquidity` function to ensure it correctly orders contracts based on their available liquidity.
Generated: DETERMINISTIC_d39b8aec3bcc94a6
Batch ID: 20250612_140356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import unittest
from typing import List, Dict
from your_module import orderContractsByLiquidity  # Replace with actual import

class TestOrderContractsByLiquidity(unittest.TestCase):
    def test_order_contracts_by_liquidity(self):
        """
        Test that contracts are correctly ordered by available liquidity in descending order.
        """
        # Test case 1: Normal case with different liquidity values
        contracts = [
            {"symbol": "A", "available_liquidity": 1000},
            {"symbol": "B", "available_liquidity": 5000},
            {"symbol": "C", "available_liquidity": 2500}
        ]
        expected = [
            {"symbol": "B", "available_liquidity": 5000},
            {"symbol": "C", "available_liquidity": 2500},
            {"symbol": "A", "available_liquidity": 1000}
        ]
        result = orderContractsByLiquidity(contracts)
        self.assertEqual(result, expected)
        
        # Test case 2: Empty input list
        self.assertEqual(orderContractsByLiquidity([]), [])
        
        # Test case 3: Single contract
        single_contract = [{"symbol": "D", "available_liquidity": 3000}]
        self.assertEqual(orderContractsByLiquidity(single_contract), single_contract)
        
        # Test case 4: Contracts with equal liquidity (should maintain original order for ties)
        equal_liquidity = [
            {"symbol": "E", "available_liquidity": 1000},
            {"symbol": "F", "available_liquidity": 1000},
            {"symbol": "G", "available_liquidity": 1000}
        ]
        result = orderContractsByLiquidity(equal_liquidity)
        self.assertEqual(result, equal_liquidity)
        
        # Test case 5: Contracts with missing liquidity field (should raise exception)
        invalid_contracts = [
            {"symbol": "H", "volume": 2000},
            {"symbol": "I", "available_liquidity": 1500}
        ]
        with self.assertRaises(KeyError):
            orderContractsByLiquidity(invalid_contracts)

if __name__ == '__main__':
    unittest.main()
```
