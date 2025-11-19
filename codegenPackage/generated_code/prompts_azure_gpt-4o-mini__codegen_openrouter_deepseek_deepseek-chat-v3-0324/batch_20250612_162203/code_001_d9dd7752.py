"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Write a sample code snippet for a smart contract using Aleph Zero's consensus protocol, AlephBFT, that demonstrates transaction finality.
Generated: DETERMINISTIC_d9dd7752c85248eb
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! A simple smart contract demonstrating transaction finality using AlephBFT.

#![cfg_attr(not(feature = "std"), no_std)]

use ink_lang as ink;

#[ink::contract]
mod transaction_finality_demo {
    use ink_prelude::string::String;
    use ink_storage::traits::{PackedLayout, SpreadLayout};
    use scale::{Decode, Encode};

    /// Custom error types for the contract
    #[derive(Debug, PartialEq, Eq, Encode, Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum Error {
        /// Transaction already finalized
        AlreadyFinalized,
        /// Unauthorized access
        Unauthorized,
    }

    /// Result type for contract operations
    pub type Result<T> = core::result::Result<T, Error>;

    /// The contract's storage
    #[ink(storage)]
    pub struct TransactionFinalityDemo {
        /// The owner of the contract
        owner: AccountId,
        /// Mapping of transaction IDs to their finality status
        finalized_transactions: ink_storage::Mapping<Hash, bool>,
    }

    impl TransactionFinalityDemo {
        /// Creates a new instance of the contract
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                owner: Self::env().caller(),
                finalized_transactions: Default::default(),
            }
        }

        /// Marks a transaction as finalized (only callable by owner)
        #[ink(message)]
        pub fn finalize_transaction(&mut self, tx_hash: Hash) -> Result<()> {
            if self.env().caller() != self.owner {
                return Err(Error::Unauthorized);
            }

            if self.finalized_transactions.get(&tx_hash).unwrap_or(false) {
                return Err(Error::AlreadyFinalized);
            }

            self.finalized_transactions.insert(&tx_hash, &true);
            Ok(())
        }

        /// Checks if a transaction is finalized
        #[ink(message)]
        pub fn is_transaction_finalized(&self, tx_hash: Hash) -> bool {
            self.finalized_transactions.get(&tx_hash).unwrap_or(false)
        }

        /// Returns the contract owner
        #[ink(message)]
        pub fn get_owner(&self) -> AccountId {
            self.owner
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use ink_env::test;
        use ink_lang as ink;

        #[ink::test]
        fn new_works() {
            let contract = TransactionFinalityDemo::new();
            assert_eq!(contract.get_owner(), test::default_accounts::<ink_env::DefaultEnvironment>().alice);
        }

        #[ink::test]
        fn finalize_transaction_works() {
            let mut contract = TransactionFinalityDemo::new();
            let tx_hash = Hash::from([0x1; 32]);

            // Only owner can finalize
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();
            test::set_caller::<ink_env::DefaultEnvironment>(accounts.bob);
            assert_eq!(contract.finalize_transaction(tx_hash), Err(Error::Unauthorized));

            // Owner can finalize
            test::set_caller::<ink_env::DefaultEnvironment>(accounts.alice);
            assert_eq!(contract.finalize_transaction(tx_hash), Ok(()));
            assert!(contract.is_transaction_finalized(tx_hash));

            // Can't finalize twice
            assert_eq!(contract.finalize_transaction(tx_hash), Err(Error::AlreadyFinalized));
        }
    }
}
```
