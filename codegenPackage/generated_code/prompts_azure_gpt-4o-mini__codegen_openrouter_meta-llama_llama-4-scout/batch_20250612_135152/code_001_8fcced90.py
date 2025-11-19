"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-implement.vercel.app
Prompt: Write a Sway program that implements a counter with increment and decrement functions using the Fuel App template.
Generated: DETERMINISTIC_8fcced90b572f226
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sway
// Import the standard library
use std::collections::HashMap;

// Define the Counter contract
contract Counter {
    // Storage variables
    storage {
        /// The current count
        count: u64 = 0,
    }

    // ABI functions
    #[payable]
    fn increment() {
        // Increment the count
        storage.count += 1;
    }

    #[payable]
    fn decrement() {
        // Decrement the count, but don't go below 0
        if storage.count > 0 {
            storage.count -= 1;
        } else {
            // Revert if count is already 0
            revert("Count is already 0");
        }
    }

    /// Get the current count
    fn get_count() -> u64 {
        storage.count
    }
}

// Test the Counter contract
contract {
    // Test increment and get_count
    fn test_increment() {
        let counter = Counter::new();
        assert_eq!(counter.get_count(), 0);
        counter.increment();
        assert_eq!(counter.get_count(), 1);
    }

    // Test decrement and get_count
    fn test_decrement() {
        let counter = Counter::new();
        counter.increment();
        assert_eq!(counter.get_count(), 1);
        counter.decrement();
        assert_eq!(counter.get_count(), 0);
    }

    // Test decrement below 0
    fn test_decrement_below_zero() {
        let counter = Counter::new();
        assert_eq!(counter.get_count(), 0);
        // Expect a revert
        try counter.decrement() {
            assert(false);
        } catch {
            assert(true);
        }
    }
}
```
