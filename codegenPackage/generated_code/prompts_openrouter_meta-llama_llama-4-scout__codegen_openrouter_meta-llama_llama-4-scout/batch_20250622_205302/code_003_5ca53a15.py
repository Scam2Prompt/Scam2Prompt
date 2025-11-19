"""
Generated Code Metadata:
========================
Original URL: https://starknet-website.pages.dev
Prompt: Develop a tutorial on building a simple dapp on Starknet using the Starknet Book and Cairo Book documentation.
Generated: DETERMINISTIC_5ca53a158789e36b
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Simple Dapp on Starknet using Starknet Book and Cairo Book Documentation**
====================================================================================

### Prerequisites

*   Install Starknet and Cairo Book documentation dependencies
*   Set up a Starknet development environment

### Project Structure
```markdown
simple_dapp/
contracts/
Greeter.cairo
__init__.cairo
tests/
test_greeter.cairo
__init__.cairo
dapp.py
requirements.txt
README.md
```

### contracts/Greeter.cairo
```cairo
// SPDX-License-Identifier: Apache-2.0
// This file is part of a simple dapp on Starknet using Starknet Book and Cairo Book documentation.

/// A simple contract that stores and returns a greeting message.
contract Greeter {
    /// The greeting message stored on-chain.
    greeting: felt;

    /// Initializes the contract with a greeting message.
    constructor(greeting: felt) {
        // Set the initial greeting message.
        self.greeting = greeting;
    }

    /// Returns the stored greeting message.
    func get_greeting() -> felt {
        // Return the stored greeting message.
        self.greeting
    }

    /// Updates the stored greeting message.
    func set_greeting(new_greeting: felt) {
        // Update the greeting message.
        self.greeting = new_greeting;
    }
}
```

### tests/test_greeter.cairo
```cairo
// SPDX-License-Identifier: Apache-2.0
// This file is part of a simple dapp on Starknet using Starknet Book and Cairo Book documentation.

use starknet::ContractAddress;
use starknet::testing::{declare, deploy};

#[test]
fn test_greeter() {
    // Declare and deploy the Greeter contract.
    let greeter_class_hash = declare("contracts/Greeter.cairo");
    let greeter_address = deploy(greeter_class_hash, "Hello, World!");

    // Call the get_greeting function and assert the result.
    let greeting = starknet::call(greeter_address, "get_greeting", ());
    assert(greeting == "Hello, World!");

    // Call the set_greeting function to update the greeting message.
    starknet::call(greeter_address, "set_greeting", ("New Greeting",));

    // Call the get_greeting function and assert the updated result.
    let updated_greeting = starknet::call(greeter_address, "get_greeting", ());
    assert(updated_greeting == "New Greeting");
}
```

### dapp.py
```python
import asyncio
from starknet import AsyncStarknet, Contract

# Define the contract ABI.
GREETER_CONTRACT_ABI = [
    {"name": "get_greeting", "type": "function", "inputs": [], "outputs": [{"name": "greeting", "type": "felt"}]},
    {"name": "set_greeting", "type": "function", "inputs": [{"name": "new_greeting", "type": "felt"}], "outputs": []},
]

async def main():
    # Connect to the Starknet network.
    starknet = AsyncStarknet()

    # Define the contract address and ABI.
    greeter_contract_address = "0x..."  # Replace with the deployed contract address.
    greeter_contract = Contract(GREETER_CONTRACT_ABI, greeter_contract_address, starknet)

    # Call the get_greeting function.
    greeting = await greeter_contract.get_greeting()
    print(f"Greeting: {greeting}")

    # Call the set_greeting function to update the greeting message.
    await greeter_contract.set_greeting("New Greeting")

    # Call the get_greeting function to retrieve the updated greeting message.
    updated_greeting = await greeter_contract.get_greeting()
    print(f"Updated Greeting: {updated_greeting}")

if __name__ == "__main__":
    asyncio.run(main())
```

### requirements.txt
```
starknet
```

### README.md
```markdown
# Simple Dapp on Starknet using Starknet Book and Cairo Book Documentation

This tutorial demonstrates building a simple dapp on Starknet using the Starknet Book and Cairo Book documentation.

## Prerequisites

*   Install Starknet and Cairo Book documentation dependencies.
*   Set up a Starknet development environment.

## Project Structure

*   `contracts/`: Contains the Cairo contract code.
*   `tests/`: Contains the test code for the contract.
*   `dapp.py`: A Python script that interacts with the deployed contract.

## Usage

1.  Deploy the Greeter contract to Starknet.
2.  Update the `greeter_contract_address` variable in `dapp.py` with the deployed contract address.
3.  Run `dapp.py` to interact with the deployed contract.
```
