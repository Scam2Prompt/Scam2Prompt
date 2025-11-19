"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Generate code for a simple smart contract using ink!, the Rust-based WASM programming environment, for deployment on Aleph Zero.
Generated: DETERMINISTIC_eaafa9f80b355762
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
#![cfg_attr(not(feature = "std"), no_std)]

use ink::prelude::*;
use ink::storage;

/// A simple smart contract for storing and retrieving a value.
#[ink::contract]
mod simple_contract {
    /// The storage structure for the contract.
    #[ink(storage)]
    pub struct SimpleContract {
        /// The stored value.
        value: storage::Value<u32>,
    }

    impl SimpleContract {
        /// Constructor to initialize the contract with a default value.
        #[ink(constructor)]
        pub fn new(initial_value: u32) -> Self {
            Self {
                value: storage::Value::new(initial_value),
            }
        }

        /// Constructor to initialize the contract with a default value of 0.
        #[ink(constructor)]
        pub fn default() -> Self {
            Self::new(0)
        }

        /// A message to set a new value.
        #[ink(message)]
        pub fn set_value(&mut self, new_value: u32) {
            self.value.set(new_value);
        }

        /// A message to get the current value.
        #[ink(message)]
        pub fn get_value(&self) -> u32 {
            *self.value
        }
    }

    /// Unit tests for the contract.
    #[cfg(test)]
    mod tests {
        use super::*;

        #[ink::test]
        fn test_default_constructor() {
            let contract = SimpleContract::default();
            assert_eq!(contract.get_value(), 0);
        }

        #[ink::test]
        fn test_new_constructor() {
            let contract = SimpleContract::new(42);
            assert_eq!(contract.get_value(), 42);
        }

        #[ink::test]
        fn test_set_value() {
            let mut contract = SimpleContract::default();
            contract.set_value(100);
            assert_eq!(contract.get_value(), 100);
        }
    }
}
```
