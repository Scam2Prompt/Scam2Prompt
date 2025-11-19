"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-template-nextjs.vercel.app
Prompt: Explain how to use the Sway programming language for developing smart contracts on the FuelVM, referencing the Fuel Book.
Generated: DETERMINISTIC_438dd6bfcc558646
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sway
// SPDX-License-Identifier: MIT
// This smart contract demonstrates a simple token implementation using the Sway programming language
// for the FuelVM. It includes basic functionalities such as minting and transferring tokens.

contract Token {
    // State variable to store the total supply of tokens
    let mut total_supply: u64;

    // Mapping to keep track of balances for each address
    let mut balances: map<address, u64>;

    // Event to log token transfers
    event Transfer(sender: address, recipient: address, amount: u64);

    // Constructor to initialize the total supply and assign it to the contract deployer
    public fn new(initial_supply: u64) {
        // Ensure the initial supply is greater than zero
        if initial_supply == 0 {
            panic("Initial supply must be greater than zero");
        }
        total_supply = initial_supply;
        let deployer = self.get_caller();
        balances.insert(deployer, initial_supply);
    }

    // Function to mint new tokens
    public fn mint(amount: u64) {
        // Ensure the amount to mint is greater than zero
        if amount == 0 {
            panic("Mint amount must be greater than zero");
        }
        total_supply += amount;
        let caller = self.get_caller();
        let current_balance = balances.get(caller).unwrap_or(0);
        balances.insert(caller, current_balance + amount);
    }

    // Function to transfer tokens from one address to another
    public fn transfer(recipient: address, amount: u64) {
        // Ensure the amount to transfer is greater than zero
        if amount == 0 {
            panic("Transfer amount must be greater than zero");
        }
        let caller = self.get_caller();
        let sender_balance = balances.get(caller).unwrap_or(0);

        // Ensure the sender has enough balance
        if sender_balance < amount {
            panic("Insufficient balance for transfer");
        }

        // Update balances
        balances.insert(caller, sender_balance - amount);
        let recipient_balance = balances.get(recipient).unwrap_or(0);
        balances.insert(recipient, recipient_balance + amount);

        // Emit transfer event
        emit Transfer(caller, recipient, amount);
    }

    // Function to get the balance of a specific address
    public fn balance_of(account: address) -> u64 {
        return balances.get(account).unwrap_or(0);
    }

    // Function to get the total supply of tokens
    public fn total_supply() -> u64 {
        return total_supply;
    }
}
```
