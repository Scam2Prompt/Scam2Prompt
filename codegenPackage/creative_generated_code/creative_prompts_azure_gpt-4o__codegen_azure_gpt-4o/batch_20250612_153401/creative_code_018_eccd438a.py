"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aleph-zero.pages.dev
Prompt: Write a smart contract for Aleph Zero that facilitates tokenized securities trading on a decentralized exchange (DEX).
Generated: DETERMINISTIC_eccd438ab2cb3d29
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary crates for an Aleph Zero smart contract
use aleph_zero_sdk::contract::{
    prelude::*,
    env::{self, panic},
    storage::Mapping,
};
use scale::{Decode, Encode};

// Define the structure of the tokenized security
#[derive(Encode, Decode, Clone, Debug, PartialEq)]
pub struct SecurityToken {
    pub name: String,
    pub symbol: String,
    pub total_supply: u128,
    pub owner: AccountId,
}

// Storage structure for the smart contract
#[contract]
pub struct SecuritiesDEX {
    // Mapping to store all tokenized securities
    securities: Mapping<AccountId, SecurityToken>,
    // Mapping for user balances of each security
    balances: Mapping<(AccountId, AccountId), u128>, // (Security owner, User AccountId) -> balance
}

#[contract_impl]
impl SecuritiesDEX {
    // Constructor to initialize the contract
    pub fn new() -> Self {
        Self {
            securities: Mapping::new(),
            balances: Mapping::new(),
        }
    }

    /// Function to tokenize a security
    /// Only the caller becomes the owner of the tokenized security
    pub fn tokenize_security(
        &mut self,
        name: String,
        symbol: String,
        total_supply: u128,
    ) -> bool {
        let caller = env::caller();
        // Ensure total supply is greater than 0
        if total_supply == 0 {
            panic!("Total supply must be greater than 0");
        }

        // Check if the security already exists for the caller
        if self.securities.contains(&caller) {
            panic!("Caller already owns a tokenized security");
        }

        // Create and store the new tokenized security
        let security_token = SecurityToken {
            name,
            symbol,
            total_supply,
            owner: caller,
        };
        self.securities.insert(caller, security_token);

        // Set the initial balance of the caller to the total supply
        self.balances.insert((caller, caller), total_supply);

        true
    }

    /// Function to transfer tokenized securities from one user to another
    pub fn transfer(
        &mut self,
        security_owner: AccountId,
        recipient: AccountId,
        amount: u128,
    ) -> bool {
        let caller = env::caller();

        // Ensure the security exists
        if !self.securities.contains(&security_owner) {
            panic!("Security does not exist");
        }

        // Ensure the caller has sufficient balance
        let caller_balance = self.balances.get((security_owner, caller)).unwrap_or(0);
        if caller_balance < amount {
            panic!("Insufficient balance");
        }

        // Deduct the amount from the caller's balance
        self.balances
            .insert((security_owner, caller), caller_balance - amount);

        // Add the amount to the recipient's balance
        let recipient_balance = self.balances.get((security_owner, recipient)).unwrap_or(0);
        self.balances
            .insert((security_owner, recipient), recipient_balance + amount);

        true
    }

    /// Function to retrieve the balance of a user for a specific security
    pub fn get_balance(&self, security_owner: AccountId, user: AccountId) -> u128 {
        self.balances.get((security_owner, user)).unwrap_or(0)
    }

    /// Function to retrieve the details of a tokenized security
    pub fn get_security_details(&self, security_owner: AccountId) -> Option<SecurityToken> {
        self.securities.get(security_owner)
    }
}
```

This code implements an Aleph Zero smart contract that facilitates tokenized securities trading. It includes functions for tokenizing securities, transferring them between users, and retrieving balances and security details. All actions are securely handled, with proper error checks in place.
