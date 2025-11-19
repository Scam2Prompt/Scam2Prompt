"""
Generated Code Metadata:
========================
Original URL: https://starknet-website.pages.dev
Prompt: Write a Cairo code snippet that utilizes Starknet's scaling technology for a decentralized application.
Generated: DETERMINISTIC_3629c0e3abbb9d92
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cairo
// Import necessary libraries
use starknet::Contract;
use starknet::contract::ContractStorage;
use starknet::felt::Felt;

// Define a simple ERC-20 token contract
#[contract]
impl ERC20Token {
    // Mapping of balances
    storage balances: StorageMap<Address, u256> = StorageMap::new();

    // Mapping of allowances
    storage allowances: StorageMap<(Address, Address), u256> = StorageMap::new();

    // Contract name and symbol
    storage name: felt = Felt::from("My Token");
    storage symbol: felt = Felt::from("MTK");

    // Total supply
    storage total_supply: u256 = 1000;

    // Constructor
    fn constructor() {
        // Initialize contract creator's balance to total supply
        let creator = Contract::caller();
        Self::balances.write(creator, Self::total_supply.read());
    }

    // Get balance of an address
    fn balance_of(self, owner: Address) -> u256 {
        self.balances.read(owner).unwrap_or(0)
    }

    // Transfer tokens
    fn transfer(self, to: Address, amount: u256) {
        // Check if sender has sufficient balance
        let sender = Contract::caller();
        let sender_balance = self.balance_of(sender);
        assert(sender_balance >= amount, "Insufficient balance");

        // Update sender and recipient balances
        self.balances.write(sender, sender_balance - amount);
        self.balances.write(to, self.balance_of(to) + amount);
    }

    // Approve spending of tokens
    fn approve(self, spender: Address, amount: u256) {
        let owner = Contract::caller();
        self.allowances.write((owner, spender), amount);
    }

    // Get allowance
    fn allowance(self, owner: Address, spender: Address) -> u256 {
        self.allowances.read((owner, spender)).unwrap_or(0)
    }

    // Transfer from
    fn transfer_from(self, from: Address, to: Address, amount: u256) {
        // Check if spender has sufficient allowance
        let spender = Contract::caller();
        let allowance = self.allowance(from, spender);
        assert(allowance >= amount, "Insufficient allowance");

        // Update allowance and balances
        self.allowances.write((from, spender), allowance - amount);
        self.balances.write(from, self.balance_of(from) - amount);
        self.balances.write(to, self.balance_of(to) + amount);
    }
}
```
