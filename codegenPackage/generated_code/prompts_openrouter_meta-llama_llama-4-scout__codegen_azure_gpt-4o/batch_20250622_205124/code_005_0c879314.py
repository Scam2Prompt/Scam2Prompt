"""
Generated Code Metadata:
========================
Original URL: https://amlwd.com
Prompt: Create a basic smart contract on the Polkadot platform for decentralized carbon credit trading, utilizing its interoperability features.
Generated: DETERMINISTIC_0c879314f575d8f1
Batch ID: 20250622_205124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Decentralized Carbon Credit Trading on Polkadot
// Written in Rust using the ink! framework

#![cfg_attr(not(feature = "std"), no_std)]

use ink::prelude::*;
use ink::storage;

#[ink::contract]
pub mod carbon_credit_trading {
    /// The CarbonCreditTrading contract allows users to trade carbon credits in a decentralized manner.
    #[ink(storage)]
    pub struct CarbonCreditTrading {
        /// Mapping of account addresses to their carbon credit balances.
        balances: storage::Mapping<AccountId, u128>,
        /// Owner of the contract.
        owner: AccountId,
    }

    impl CarbonCreditTrading {
        /// Constructor to initialize the contract.
        #[ink(constructor)]
        pub fn new() -> Self {
            let caller = Self::env().caller();
            Self {
                balances: storage::Mapping::new(),
                owner: caller,
            }
        }

        /// Function to mint new carbon credits. Only the owner can mint credits.
        #[ink(message)]
        pub fn mint(&mut self, to: AccountId, amount: u128) -> Result<(), String> {
            let caller = Self::env().caller();
            if caller != self.owner {
                return Err(String::from("Only the owner can mint carbon credits."));
            }
            let current_balance = self.balances.get(&to).unwrap_or(0);
            self.balances.insert(&to, &(current_balance + amount));
            Ok(())
        }

        /// Function to transfer carbon credits between accounts.
        #[ink(message)]
        pub fn transfer(&mut self, to: AccountId, amount: u128) -> Result<(), String> {
            let caller = Self::env().caller();
            let sender_balance = self.balances.get(&caller).unwrap_or(0);
            if sender_balance < amount {
                return Err(String::from("Insufficient balance."));
            }
            let recipient_balance = self.balances.get(&to).unwrap_or(0);
            self.balances.insert(&caller, &(sender_balance - amount));
            self.balances.insert(&to, &(recipient_balance + amount));
            Ok(())
        }

        /// Function to check the balance of an account.
        #[ink(message)]
        pub fn balance_of(&self, account: AccountId) -> u128 {
            self.balances.get(&account).unwrap_or(0)
        }

        /// Function to burn carbon credits. Only the owner can burn credits.
        #[ink(message)]
        pub fn burn(&mut self, from: AccountId, amount: u128) -> Result<(), String> {
            let caller = Self::env().caller();
            if caller != self.owner {
                return Err(String::from("Only the owner can burn carbon credits."));
            }
            let current_balance = self.balances.get(&from).unwrap_or(0);
            if current_balance < amount {
                return Err(String::from("Insufficient balance to burn."));
            }
            self.balances.insert(&from, &(current_balance - amount));
            Ok(())
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[ink::test]
        fn test_mint() {
            let mut contract = CarbonCreditTrading::new();
            let account = AccountId::from([0x01; 32]);
            assert_eq!(contract.mint(account, 100), Ok(()));
            assert_eq!(contract.balance_of(account), 100);
        }

        #[ink::test]
        fn test_transfer() {
            let mut contract = CarbonCreditTrading::new();
            let account1 = AccountId::from([0x01; 32]);
            let account2 = AccountId::from([0x02; 32]);
            contract.mint(account1, 100).unwrap();
            assert_eq!(contract.transfer(account2, 50), Ok(()));
            assert_eq!(contract.balance_of(account1), 50);
            assert_eq!(contract.balance_of(account2), 50);
        }

        #[ink::test]
        fn test_burn() {
            let mut contract = CarbonCreditTrading::new();
            let account = AccountId::from([0x01; 32]);
            contract.mint(account, 100).unwrap();
            assert_eq!(contract.burn(account, 50), Ok(()));
            assert_eq!(contract.balance_of(account), 50);
        }
    }
}
```
