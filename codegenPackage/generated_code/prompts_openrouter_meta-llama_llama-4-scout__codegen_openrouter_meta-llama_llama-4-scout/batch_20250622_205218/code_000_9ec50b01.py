"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-template-nextjs.vercel.app
Prompt: Write a Sway Book code snippet for a smart contract on the FuelVM.
Generated: DETERMINISTIC_9ec50b01850917c1
Batch ID: 20250622_205218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sway
// SPDX-License-Identifier: Apache-2.0
// This file is part of Fuel-Contracts.

// Import the standard library.
use std::collections::Vec;

// Define the contract.
contract MyContract {
    // Storage variables.
    storage {
        /// The counter value.
        counter: u64 = 0,
    }

    // ABI functions.
    #[payable(false)]
    fn initialize() {
        // Initialize the counter to 1.
        counter = 1;
    }

    #[payable(false)]
    fn get_counter() -> u64 {
        // Return the current counter value.
        counter
    }

    #[payable(false)]
    fn increment_counter() {
        // Increment the counter by 1.
        counter += 1;
    }
}

// Script to test the contract.
script {
    // Deploy the contract.
    fn deploy_contract() -> Address {
        let contract = MyContract::new();
        contract.address
    }

    // Test the contract functions.
    fn test_contract() {
        let contract_addr = deploy_contract();
        let contract = MyContract::at(contract_addr);

        // Initialize the contract.
        contract.initialize();

        // Get the initial counter value.
        let counter = contract.get_counter();
        assert(counter == 1);

        // Increment the counter.
        contract.increment_counter();

        // Get the updated counter value.
        let counter = contract.get_counter();
        assert(counter == 2);
    }
}
```
