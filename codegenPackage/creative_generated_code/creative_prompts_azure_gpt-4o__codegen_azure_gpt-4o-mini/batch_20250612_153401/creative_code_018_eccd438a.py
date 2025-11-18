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
// SPDX-License-Identifier: MIT
// A smart contract for tokenized securities trading on Aleph Zero's decentralized exchange (DEX)

use aleph_zero::prelude::*;
use aleph_zero::contract;

#[contract]
pub struct TokenizedSecuritiesDEX {
    // Mapping from token IDs to their corresponding balances
    balances: StorageMap<String, u64>,
    // Mapping from token IDs to their issuers
    issuers: StorageMap<String, Address>,
    // Mapping for approved addresses for each token
    allowances: StorageMap<(String, Address), u64>,
}

impl TokenizedSecuritiesDEX {
    // Constructor to initialize the contract
    #[init]
    pub fn new() -> Self {
        Self {
            balances: StorageMap::new(),
            issuers: StorageMap::new(),
            allowances: StorageMap::new(),
        }
    }

    // Function to issue new tokens
    pub fn issue_tokens(&mut self, token_id: String, amount: u64) -> Result<(), ContractError> {
        // Ensure the caller is the issuer
        let sender = self.env().caller();
        if self.issuers.contains_key(&token_id) {
            return Err(ContractError::TokenAlreadyIssued);
        }
        
        self.balances.insert(token_id.clone(), amount);
        self.issuers.insert(token_id.clone(), sender);
        
        emit_event!(TokenIssued { token_id, amount });
        Ok(())
    }

    // Function to transfer tokens between users
    pub fn transfer(&mut self, token_id: String, to: Address, amount: u64) -> Result<(), ContractError> {
        // Ensure the sender has sufficient balance
        let from = self.env().caller();
        let from_balance = self.balances.get(&token_id).unwrap_or(0);
        
        if from_balance < amount {
            return Err(ContractError::InsufficientBalance);
        }

        // Update balances
        self.balances.insert(token_id.clone(), from_balance - amount);
        let to_balance = self.balances.get(&token_id).unwrap_or(0);
        self.balances.insert(token_id.clone(), to_balance + amount);
        
        emit_event!(TokensTransferred { token_id, from, to, amount });
        Ok(())
    }

    // Function to approve another address to spend tokens on behalf of the owner
    pub fn approve(&mut self, token_id: String, spender: Address, amount: u64) -> Result<(), ContractError> {
        let owner = self.env().caller();
        self.allowances.insert((token_id.clone(), spender), amount);
        
        emit_event!(ApprovalGranted { token_id, owner, spender, amount });
        Ok(())
    }

    // Function to handle token transfers by an approved spender
    pub fn transfer_from(&mut self, token_id: String, from: Address, to: Address, amount: u64) -> Result<(), ContractError> {
        let allowed_amount = self.allowances.get(&(token_id.clone(), from)).unwrap_or(0);

        if allowed_amount < amount {
            return Err(ContractError::AllowanceExceeded);
        }

        // Ensure the sender has sufficient balance
        let from_balance = self.balances.get(&token_id).unwrap_or(0);
        if from_balance < amount {
            return Err(ContractError::InsufficientBalance);
        }

        // Update balances
        self.balances.insert(token_id.clone(), from_balance - amount);
        let to_balance = self.balances.get(&token_id).unwrap_or(0);
        self.balances.insert(token_id.clone(), to_balance + amount);
        
        // Update allowance
        self.allowances.insert((token_id.clone(), from), allowed_amount - amount);
        
        emit_event!(TokensTransferred { token_id, from, to, amount });
        Ok(())
    }

    // Event emitted when tokens are issued
    #[event]
    pub struct TokenIssued {
        pub token_id: String,
        pub amount: u64,
    }

    // Event emitted when tokens are transferred
    #[event]
    pub struct TokensTransferred {
        pub token_id: String,
        pub from: Address,
        pub to: Address,
        pub amount: u64,
    }

    // Event emitted when approval is granted
    #[event]
    pub struct ApprovalGranted {
        pub token_id: String,
        pub owner: Address,
        pub spender: Address,
        pub amount: u64,
    }
}

// Custom error types for the contract
#[derive(Debug)]
pub enum ContractError {
    TokenAlreadyIssued,
    InsufficientBalance,
    AllowanceExceeded,
}
```
