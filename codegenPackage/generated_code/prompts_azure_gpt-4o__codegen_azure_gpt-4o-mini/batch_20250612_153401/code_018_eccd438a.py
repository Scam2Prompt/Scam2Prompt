"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Write a smart contract for Aleph Zero that facilitates tokenized securities trading on a decentralized exchange (DEX).
Generated: DETERMINISTIC_eccd438ab2cb3d29
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Aleph Zero Smart Contract for Tokenized Securities Trading on a Decentralized Exchange (DEX)

#![no_std]

use aleph_zero::prelude::*;
use aleph_zero::contract::{Contract, ContractError};
use aleph_zero::storage::{Storage, StorageError};
use aleph_zero::token::{Token, TokenError};

/// Represents a tokenized security
#[derive(Debug, Clone)]
pub struct SecurityToken {
    pub id: u64,
    pub name: String,
    pub total_supply: u64,
    pub owner: Address,
}

/// Represents a trade on the DEX
#[derive(Debug, Clone)]
pub struct Trade {
    pub token_id: u64,
    pub buyer: Address,
    pub seller: Address,
    pub amount: u64,
    pub price: u64,
}

/// Main contract structure
pub struct DexContract {
    securities: Storage<u64, SecurityToken>,
    trades: Storage<u64, Trade>,
    next_security_id: u64,
    next_trade_id: u64,
}

impl DexContract {
    /// Initializes the contract with default values
    pub fn new() -> Self {
        Self {
            securities: Storage::new(),
            trades: Storage::new(),
            next_security_id: 1,
            next_trade_id: 1,
        }
    }

    /// Creates a new security token
    pub fn create_security(&mut self, name: String, total_supply: u64) -> Result<u64, ContractError> {
        let owner = Self::caller();
        let security = SecurityToken {
            id: self.next_security_id,
            name,
            total_supply,
            owner,
        };

        // Store the new security token
        self.securities.insert(self.next_security_id, security)
            .map_err(|_| ContractError::StorageError)?;

        // Increment the security ID for the next token
        self.next_security_id += 1;

        Ok(self.next_security_id - 1)
    }

    /// Executes a trade between buyer and seller
    pub fn execute_trade(&mut self, token_id: u64, amount: u64, price: u64) -> Result<u64, ContractError> {
        let buyer = Self::caller();
        let seller = self.securities.get(token_id)
            .ok_or(ContractError::NotFound)?;

        // Check if the seller has enough tokens
        if seller.total_supply < amount {
            return Err(ContractError::InsufficientBalance);
        }

        // Create a new trade record
        let trade = Trade {
            token_id,
            buyer,
            seller: seller.owner,
            amount,
            price,
        };

        // Store the trade
        self.trades.insert(self.next_trade_id, trade)
            .map_err(|_| ContractError::StorageError)?;

        // Update the seller's total supply
        seller.total_supply -= amount;

        // Increment the trade ID for the next trade
        self.next_trade_id += 1;

        Ok(self.next_trade_id - 1)
    }

    /// Retrieves a security token by its ID
    pub fn get_security(&self, token_id: u64) -> Result<SecurityToken, ContractError> {
        self.securities.get(token_id)
            .ok_or(ContractError::NotFound)
    }

    /// Retrieves a trade by its ID
    pub fn get_trade(&self, trade_id: u64) -> Result<Trade, ContractError> {
        self.trades.get(trade_id)
            .ok_or(ContractError::NotFound)
    }
}

// Implement the contract trait for the DexContract
impl Contract for DexContract {
    fn deploy() -> Self {
        Self::new()
    }
}
```
