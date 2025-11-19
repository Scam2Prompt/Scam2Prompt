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
//! A basic smart contract for decentralized carbon credit trading on Polkadot.

#![cfg_attr(not(feature = "std"), no_std)]

use ink_lang as ink;

#[ink::contract]
mod carbon_credit_trading {
    use ink_storage::{
        collections::HashMap as StorageHashMap,
        traits::{PackedLayout, SpreadLayout},
    };

    /// Defines the storage of the contract.
    #[ink(storage)]
    pub struct CarbonCreditTrading {
        /// Maps account IDs to their carbon credit balance.
        balances: StorageHashMap<AccountId, Balance>,
        /// Maps account IDs to their approved allowances for other accounts.
        allowances: StorageHashMap<(AccountId, AccountId), Balance>,
        /// Total supply of carbon credits.
        total_supply: Balance,
    }

    /// Events emitted by the contract.
    #[ink(event)]
    pub struct Transfer {
        #[ink(topic)]
        from: Option<AccountId>,
        #[ink(topic)]
        to: Option<AccountId>,
        value: Balance,
    }

    #[ink(event)]
    pub struct Approval {
        #[ink(topic)]
        owner: AccountId,
        #[ink(topic)]
        spender: AccountId,
        value: Balance,
    }

    /// Errors that can occur during contract execution.
    #[derive(Debug, PartialEq, Eq, scale::Encode, scale::Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum Error {
        /// Insufficient balance for the operation.
        InsufficientBalance,
        /// Insufficient allowance for the operation.
        InsufficientAllowance,
        /// Transfer to the zero address is not allowed.
        TransferToZeroAddress,
    }

    impl CarbonCreditTrading {
        /// Creates a new carbon credit trading contract with the specified initial supply.
        #[ink(constructor)]
        pub fn new(initial_supply: Balance) -> Self {
            let caller = Self::env().caller();
            let mut balances = StorageHashMap::new();
            balances.insert(caller, initial_supply);

            Self::env().emit_event(Transfer {
                from: None,
                to: Some(caller),
                value: initial_supply,
            });

            Self {
                balances,
                allowances: StorageHashMap::new(),
                total_supply: initial_supply,
            }
        }

        /// Returns the total supply of carbon credits.
        #[ink(message)]
        pub fn total_supply(&self) -> Balance {
            self.total_supply
        }

        /// Returns the balance of the specified account.
        #[ink(message)]
        pub fn balance_of(&self, owner: AccountId) -> Balance {
            self.balances.get(&owner).copied().unwrap_or(0)
        }

        /// Returns the allowance that `spender` is allowed to transfer from `owner`.
        #[ink(message)]
        pub fn allowance(&self, owner: AccountId, spender: AccountId) -> Balance {
            self.allowances.get(&(owner, spender)).copied().unwrap_or(0)
        }

        /// Transfers `value` amount of carbon credits to `to` account.
        #[ink(message)]
        pub fn transfer(&mut self, to: AccountId, value: Balance) -> Result<(), Error> {
            let from = self.env().caller();
            self.transfer_from_to(from, to, value)
        }

        /// Approves `spender` to transfer up to `value` carbon credits from the caller's account.
        #[ink(message)]
        pub fn approve(&mut self, spender: AccountId, value: Balance) -> Result<(), Error> {
            let owner = self.env().caller();
            self.allowances.insert((owner, spender), value);

            self.env().emit_event(Approval {
                owner,
                spender,
                value,
            });

            Ok(())
        }

        /// Transfers `value` carbon credits from `from` to `to` using the allowance mechanism.
        #[ink(message)]
        pub fn transfer_from(
            &mut self,
            from: AccountId,
            to: AccountId,
            value: Balance,
        ) -> Result<(), Error> {
            let caller = self.env().caller();
            let allowance = self.allowance(from, caller);

            if allowance < value {
                return Err(Error::InsufficientAllowance);
            }

            self.allowances.insert((from, caller), allowance - value);
            self.transfer_from_to(from, to, value)
        }

        /// Internal helper function to transfer tokens from `from` to `to`.
        fn transfer_from_to(
            &mut self,
            from: AccountId,
            to: AccountId,
            value: Balance,
        ) -> Result<(), Error> {
            if value == 0 {
                return Ok(());
            }

            if to == AccountId::from([0x0; 32]) {
                return Err(Error::TransferToZeroAddress);
            }

            let from_balance = self.balance_of(from);
            if from_balance < value {
                return Err(Error::InsufficientBalance);
            }

            self.balances.insert(from, from_balance - value);
            let to_balance = self.balance_of(to);
            self.balances.insert(to, to_balance + value);

            self.env().emit_event(Transfer {
                from: Some(from),
                to: Some(to),
                value,
            });

            Ok(())
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use ink_env::test;
        use ink_lang as ink;

        #[ink::test]
        fn new_works() {
            let initial_supply = 1000;
            let contract = CarbonCreditTrading::new(initial_supply);
            assert_eq!(contract.total_supply(), initial_supply);
            assert_eq!(contract.balance_of(AccountId::from([0x1; 32])), initial_supply);
        }

        #[ink::test]
        fn transfer_works() {
            let initial_supply = 1000;
            let mut contract = CarbonCreditTrading::new(initial_supply);
            let from = AccountId::from([0x1; 32]);
            let to = AccountId::from([0x2; 32]);

            assert_eq!(contract.transfer(to, 500), Ok(()));
            assert_eq!(contract.balance_of(from), 500);
            assert_eq!(contract.balance_of(to), 500);

            assert_eq!(contract.transfer(to, 600), Err(Error::InsufficientBalance));
        }

        #[ink::test]
        fn transfer_from_works() {
            let initial_supply = 1000;
            let mut contract = CarbonCreditTrading::new(initial_supply);
            let owner = AccountId::from([0x1; 32]);
            let spender = AccountId::from([0x2; 32]);
            let to = AccountId::from([0x3; 32]);

            assert_eq!(contract.approve(spender, 500), Ok(()));
            test::set_caller(spender);
            assert_eq!(contract.transfer_from(owner, to, 400), Ok(()));
            assert_eq!(contract.balance_of(owner), 600);
            assert_eq!(contract.balance_of(to), 400);
            assert_eq!(contract.allowance(owner, spender), 100);

            assert_eq!(
                contract.transfer_from(owner, to, 200),
                Err(Error::InsufficientAllowance)
            );
        }
    }
}
```
