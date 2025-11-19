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
// SPDX-License-Identifier: MIT
// This smart contract is a simple example of a token contract on the FuelVM.

contract Token {
    // State variable to store the total supply of tokens
    let total_supply: u64;

    // Mapping to keep track of balances for each address
    let balances: map<address, u64>;

    // Event to log token transfers
    event Transfer(sender: address, recipient: address, amount: u64);

    // Constructor to initialize the total supply and allocate it to the contract creator
    public fun new(initial_supply: u64) {
        // Ensure the initial supply is greater than zero
        assert(initial_supply > 0, "Initial supply must be greater than zero.");
        
        total_supply = initial_supply;
        balances[caller()] = initial_supply; // Allocate initial supply to the contract creator
    }

    // Function to transfer tokens from the caller to a recipient
    public fun transfer(recipient: address, amount: u64) {
        // Ensure the recipient address is valid
        assert(recipient != address(0), "Invalid recipient address.");
        
        // Ensure the caller has enough balance to transfer
        assert(balances[caller()] >= amount, "Insufficient balance.");

        // Update balances
        balances[caller()] -= amount;
        balances[recipient] += amount;

        // Emit the transfer event
        emit Transfer(caller(), recipient, amount);
    }

    // Function to check the balance of a specific address
    public fun balance_of(account: address) -> u64 {
        return balances[account];
    }

    // Function to get the total supply of tokens
    public fun total_supply() -> u64 {
        return total_supply;
    }
}
```
