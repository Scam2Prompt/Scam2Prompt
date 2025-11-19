"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-9ykfjucyr-offchain-labs.vercel.app
Prompt: Write a Rust-based smart contract for an EVM-compatible application using the Arbitrum Stylus framework, as described in the Stylus documentation.
Generated: DETERMINISTIC_ba6fd3b2a5fcbada
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! A simple ERC-20 like token contract implemented using Arbitrum Stylus.

#![no_std]

use stylus_sdk::{alloy_primitives::U256, prelude::*};

sol_storage! {
    /// The contract's storage layout
    pub struct Token {
        /// Total token supply
        uint256 total_supply,
        /// Mapping of addresses to balances
        mapping(address => uint256) balances,
        /// Mapping of addresses to allowances
        mapping(address => mapping(address => uint256)) allowances,
        /// Token name
        string name,
        /// Token symbol
        string symbol,
        /// Token decimals
        uint8 decimals,
    }
}

// Declare events
sol_interface! {
    interface IERC20 {
        event Transfer(address indexed from, address indexed to, uint256 value);
        event Approval(address indexed owner, address indexed spender, uint256 value);
    }
}

#[external]
impl Token {
    /// Initializes the contract with initial supply
    pub fn initialize(
        &mut self,
        name: String,
        symbol: String,
        decimals: u8,
        initial_supply: U256,
    ) -> Result<(), Vec<u8>> {
        if self.total_supply.get() != U256::ZERO {
            return Err(b"Already initialized".to_vec());
        }

        if initial_supply == U256::ZERO {
            return Err(b"Initial supply cannot be zero".to_vec());
        }

        let sender = msg::sender();
        self.name.set_str(&name);
        self.symbol.set_str(&symbol);
        self.decimals.set(decimals);
        self.total_supply.set(initial_supply);
        self.balances.insert(sender, initial_supply);

        IERC20::Transfer {
            from: address::ZERO,
            to: sender,
            value: initial_supply,
        }
        .emit();

        Ok(())
    }

    /// Returns the token name
    pub fn name(&self) -> Result<String, Vec<u8>> {
        Ok(self.name.get_str())
    }

    /// Returns the token symbol
    pub fn symbol(&self) -> Result<String, Vec<u8>> {
        Ok(self.symbol.get_str())
    }

    /// Returns the token decimals
    pub fn decimals(&self) -> Result<u8, Vec<u8>> {
        Ok(self.decimals.get())
    }

    /// Returns the total token supply
    pub fn total_supply(&self) -> Result<U256, Vec<u8>> {
        Ok(self.total_supply.get())
    }

    /// Returns the balance of an account
    pub fn balance_of(&self, owner: Address) -> Result<U256, Vec<u8>> {
        Ok(self.balances.get(owner).unwrap_or(U256::ZERO))
    }

    /// Transfers tokens to a recipient
    pub fn transfer(&mut self, to: Address, value: U256) -> Result<bool, Vec<u8>> {
        let sender = msg::sender();
        self._transfer(sender, to, value)?;
        Ok(true)
    }

    /// Returns the remaining allowance for a spender
    pub fn allowance(&self, owner: Address, spender: Address) -> Result<U256, Vec<u8>> {
        Ok(self
            .allowances
            .get(owner)
            .and_then(|inner| inner.get(spender))
            .unwrap_or(U256::ZERO))
    }

    /// Approves a spender to transfer tokens
    pub fn approve(&mut self, spender: Address, value: U256) -> Result<bool, Vec<u8>> {
        let owner = msg::sender();
        self._approve(owner, spender, value)?;
        Ok(true)
    }

    /// Transfers tokens from one account to another using allowance
    pub fn transfer_from(
        &mut self,
        from: Address,
        to: Address,
        value: U256,
    ) -> Result<bool, Vec<u8>> {
        let spender = msg::sender();
        let allowance = self.allowance(from, spender)?;

        if allowance < value {
            return Err(b"Insufficient allowance".to_vec());
        }

        self._approve(from, spender, allowance - value)?;
        self._transfer(from, to, value)?;
        Ok(true)
    }

    /// Internal transfer function
    fn _transfer(&mut self, from: Address, to: Address, value: U256) -> Result<(), Vec<u8>> {
        if from == to {
            return Err(b"Cannot transfer to self".to_vec());
        }

        if value == U256::ZERO {
            return Err(b"Transfer amount cannot be zero".to_vec());
        }

        let from_balance = self.balance_of(from)?;
        if from_balance < value {
            return Err(b"Insufficient balance".to_vec());
        }

        self.balances.insert(from, from_balance - value);
        self.balances
            .insert(to, self.balance_of(to)? + value);

        IERC20::Transfer {
            from,
            to,
            value,
        }
        .emit();

        Ok(())
    }

    /// Internal approve function
    fn _approve(&mut self, owner: Address, spender: Address, value: U256) -> Result<(), Vec<u8>> {
        if owner == spender {
            return Err(b"Cannot approve to self".to_vec());
        }

        self.allowances
            .entry(owner)
            .or_default()
            .insert(spender, value);

        IERC20::Approval {
            owner,
            spender,
            value,
        }
        .emit();

        Ok(())
    }
}
```
