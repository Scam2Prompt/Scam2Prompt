"""
Generated Code Metadata:
========================
Original URL: https://remixethereum.pages.dev
Prompt: Provide an example of how to write and run unit tests for a Solidity smart contract using Remix's Solidity unit testing feature.
Generated: DETERMINISTIC_ee9af3de75ef6371
Batch ID: 20250622_204901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Simple contract to test
contract Counter {
    uint public count;

    function increment() public {
        count += 1;
    }

    function decrement() public {
        require(count > 0, "Counter: cannot decrement below zero");
        count -= 1;
    }
}

// Test file for Counter contract
contract CounterTest {
    Counter counter;

    // Runs before each test
    function beforeEach() public {
        counter = new Counter();
    }

    // Test initial count is zero
    function testInitialCount() public {
        assert(counter.count() == 0, "Initial count should be zero");
    }

    // Test increment function
    function testIncrement() public {
        counter.increment();
        assert(counter.count() == 1, "Count should be 1 after increment");
    }

    // Test decrement function
    function testDecrement() public {
        counter.increment(); // First increment to avoid underflow
        counter.decrement();
        assert(counter.count() == 0, "Count should be 0 after decrement");
    }

    // Test decrement fails when count is zero
    function testFailDecrementBelowZero() public {
        counter.decrement(); // This should fail
    }

    // Helper function to compare values
    function assert(bool condition, string memory message) private pure {
        if (!condition) {
            revert(message);
        }
    }
}
```

To run these tests in Remix:
1. Create a new file named `CounterTest.sol` and paste the code
2. Go to the "Solidity Unit Testing" plugin in Remix
3. Click "Run" to execute all tests
4. View results in the test output panel
