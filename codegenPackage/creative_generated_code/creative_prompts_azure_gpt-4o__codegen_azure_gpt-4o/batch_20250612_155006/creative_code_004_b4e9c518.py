"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-dapps.vercel.app
Prompt: Write a tutorial-style code snippet to deploy a smart contract on the Sui blockchain using the Move programming language.
Generated: DETERMINISTIC_b4e9c518c77bfb39
Batch ID: 20250612_155006
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://docs.sui.io/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```move
// File: MyFirstContract.move

module MyFirstContract {
    use sui::coin;
    use sui::transfer;
    use sui::error;

    // Struct that represents the data stored in the contract.
    struct MyData has key, store {
        value: u64,
    }

    // Initialize a new instance of MyData.
    public entry fun initialize_data(account: &signer, value: u64): MyData {
        // Ensure the input value is valid (example check: value > 0)
        assert!(value > 0, error::INVALID_ARGUMENT, "Value must be greater than zero");

        // Create and publish the structure.
        let data = MyData { value };
        transfer::share_object(data, account);

        data
    }

    // Function to update the value in MyData.
    public entry fun update_data(account: &signer, data: &mut MyData, new_value: u64) {
        // Ensure the new value is valid.
        assert!(new_value > 0, error::INVALID_ARGUMENT, "New value must be greater than zero");

        // Ensure only the owner can update the data.
        transfer::ensure_owner(data, account);

        // Update the value.
        data.value = new_value;
    }

    // Function to retrieve the value from MyData.
    public fun get_data(data: &MyData): u64 {
        data.value
    }
}
```

```shell
# Step 1: Install the Sui CLI if you haven't already.
# Visit https://docs.sui.io/ for installation instructions.

# Step 2: Compile the Move code.
sui move build

# Step 3: Run the following command to publish the smart contract on the Sui blockchain.
sui client publish --gas-budget 10000

# Step 4: Interact with the contract using the Sui CLI or a custom front-end.
```
