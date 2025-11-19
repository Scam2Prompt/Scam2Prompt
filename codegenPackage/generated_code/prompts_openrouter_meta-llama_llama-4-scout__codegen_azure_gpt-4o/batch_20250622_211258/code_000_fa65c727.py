"""
Generated Code Metadata:
========================
Original URL: https://fuel-explorer.vercel.app
Prompt: "Write a tutorial on how to create a smart contract using FuelVM and the Fuel Explorer platform."
Generated: DETERMINISTIC_fa65c727b4cb88f9
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Smart Contract Example for FuelVM
// This contract demonstrates a simple counter implementation using FuelVM.

// Import necessary libraries and modules
use fuel_vm::prelude::*;

// Define the contract
contract Counter {
    // State variable to store the counter value
    storage counter: u64;

    // Constructor to initialize the counter
    fn constructor(initial_value: u64) {
        // Ensure the initial value is valid
        require(initial_value >= 0, "Initial value must be non-negative");
        self.counter = initial_value;
    }

    // Function to increment the counter
    fn increment() {
        self.counter += 1;
    }

    // Function to decrement the counter
    fn decrement() {
        // Ensure the counter does not go below zero
        require(self.counter > 0, "Counter cannot be negative");
        self.counter -= 1;
    }

    // Function to get the current counter value
    fn get_counter() -> u64 {
        self.counter
    }
}

// Error handling utility function
fn require(condition: bool, error_message: &str) {
    if !condition {
        panic!(error_message);
    }
}

// Unit tests for the contract
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_counter() {
        // Initialize the contract with a value of 10
        let mut contract = Counter::constructor(10);

        // Test increment functionality
        contract.increment();
        assert_eq!(contract.get_counter(), 11);

        // Test decrement functionality
        contract.decrement();
        assert_eq!(contract.get_counter(), 10);

        // Test error handling for decrement below zero
        contract.decrement();
        contract.decrement();
        contract.decrement();
        assert_eq!(contract.get_counter(), 0);
        // Uncommenting the next line will cause a panic due to the require condition
        // contract.decrement();
    }
}
```
