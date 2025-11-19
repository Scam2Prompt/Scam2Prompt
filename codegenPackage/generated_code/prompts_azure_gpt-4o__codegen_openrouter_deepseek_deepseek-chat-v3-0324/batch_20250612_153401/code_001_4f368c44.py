"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Generate code for deploying a decentralized application (dApp) on Aleph Zero using its WASM-based programming environment and Substrate framework.
Generated: DETERMINISTIC_4f368c44b6948be6
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! A simple decentralized application (dApp) for Aleph Zero blockchain
//! using Substrate and WASM smart contracts.

#![cfg_attr(not(feature = "std"), no_std)]

use ink_lang as ink;

#[ink::contract]
mod simple_dapp {
    use ink_storage::{
        collections::HashMap as StorageHashMap,
        traits::{PackedLayout, SpreadLayout},
    };

    /// Defines the storage of your contract.
    #[ink(storage)]
    pub struct SimpleDapp {
        /// Stores a single `bool` value on the blockchain.
        value: bool,
        /// Stores a map of account IDs to their balances.
        balances: StorageHashMap<AccountId, Balance>,
    }

    /// Events emitted by the contract
    #[ink(event)]
    pub struct ValueChanged {
        #[ink(topic)]
        by: AccountId,
        new_value: bool,
    }

    #[ink(event)]
    pub struct Transfer {
        #[ink(topic)]
        from: Option<AccountId>,
        #[ink(topic)]
        to: AccountId,
        amount: Balance,
    }

    /// Errors that can occur upon calling the contract.
    #[derive(Debug, PartialEq, Eq, scale::Encode, scale::Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum Error {
        /// Returned if the transfer failed because balance was insufficient.
        InsufficientBalance,
        /// Returned if the transfer failed because the sender is the same as receiver.
        SameSenderAndReceiver,
    }

    impl SimpleDapp {
        /// Constructor that initializes the `bool` value to `false`.
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                value: false,
                balances: StorageHashMap::new(),
            }
        }

        /// Constructor that initializes the `bool` value to `init_value`.
        #[ink(constructor)]
        pub fn new_with_value(init_value: bool) -> Self {
            Self {
                value: init_value,
                balances: StorageHashMap::new(),
            }
        }

        /// Flips the current value of the `bool`.
        #[ink(message)]
        pub fn flip(&mut self) {
            self.value = !self.value;
            self.env().emit_event(ValueChanged {
                by: self.env().caller(),
                new_value: self.value,
            });
        }

        /// Returns the current value of the `bool`.
        #[ink(message)]
        pub fn get(&self) -> bool {
            self.value
        }

        /// Transfers `amount` from the caller to `to`.
        #[ink(message)]
        pub fn transfer(&mut self, to: AccountId, amount: Balance) -> Result<(), Error> {
            let caller = self.env().caller();
            if caller == to {
                return Err(Error::SameSenderAndReceiver);
            }

            let caller_balance = self.balance_of(caller);
            if caller_balance < amount {
                return Err(Error::InsufficientBalance);
            }

            self.balances.insert(caller, caller_balance - amount);
            let to_balance = self.balance_of(to);
            self.balances.insert(to, to_balance + amount);

            self.env().emit_event(Transfer {
                from: Some(caller),
                to,
                amount,
            });

            Ok(())
        }

        /// Returns the balance of the given account.
        #[ink(message)]
        pub fn balance_of(&self, owner: AccountId) -> Balance {
            self.balances.get(&owner).copied().unwrap_or(0)
        }

        /// Deposits some amount of tokens into the contract.
        #[ink(message, payable)]
        pub fn deposit(&mut self) {
            let caller = self.env().caller();
            let amount = self.env().transferred_value();
            let balance = self.balance_of(caller);
            self.balances.insert(caller, balance + amount);

            self.env().emit_event(Transfer {
                from: None,
                to: caller,
                amount,
            });
        }
    }

    /// Unit tests in Rust are normally defined within such a `#[cfg(test)]`
    /// module and test functions are marked with a `#[test]` attribute.
    #[cfg(test)]
    mod tests {
        use super::*;
        use ink_env::test;
        use ink_lang as ink;

        #[ink::test]
        fn default_works() {
            let simple_dapp = SimpleDapp::new();
            assert_eq!(simple_dapp.get(), false);
        }

        #[ink::test]
        fn flip_works() {
            let mut simple_dapp = SimpleDapp::new();
            assert_eq!(simple_dapp.get(), false);
            simple_dapp.flip();
            assert_eq!(simple_dapp.get(), true);
        }

        #[ink::test]
        fn transfer_works() {
            let mut simple_dapp = SimpleDapp::new();
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();

            // Deposit some funds to the contract
            test::set_caller::<ink_env::DefaultEnvironment>(accounts.alice);
            test::set_value_transferred::<ink_env::DefaultEnvironment>(100);
            simple_dapp.deposit();

            // Transfer funds from Alice to Bob
            assert_eq!(simple_dapp.balance_of(accounts.alice), 100);
            assert_eq!(simple_dapp.balance_of(accounts.bob), 0);
            assert_eq!(simple_dapp.transfer(accounts.bob, 50), Ok(()));
            assert_eq!(simple_dapp.balance_of(accounts.alice), 50);
            assert_eq!(simple_dapp.balance_of(accounts.bob), 50);
        }

        #[ink::test]
        fn transfer_fails_insufficient_balance() {
            let mut simple_dapp = SimpleDapp::new();
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();

            test::set_caller::<ink_env::DefaultEnvironment>(accounts.alice);
            test::set_value_transferred::<ink_env::DefaultEnvironment>(100);
            simple_dapp.deposit();

            assert_eq!(
                simple_dapp.transfer(accounts.bob, 101),
                Err(Error::InsufficientBalance)
            );
        }

        #[ink::test]
        fn transfer_fails_same_sender_receiver() {
            let mut simple_dapp = SimpleDapp::new();
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();

            test::set_caller::<ink_env::DefaultEnvironment>(accounts.alice);
            test::set_value_transferred::<ink_env::DefaultEnvironment>(100);
            simple_dapp.deposit();

            assert_eq!(
                simple_dapp.transfer(accounts.alice, 50),
                Err(Error::SameSenderAndReceiver)
            );
        }
    }
}
```
