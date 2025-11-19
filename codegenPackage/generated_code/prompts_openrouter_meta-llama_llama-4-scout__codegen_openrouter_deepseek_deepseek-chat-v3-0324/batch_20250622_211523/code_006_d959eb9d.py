"""
Generated Code Metadata:
========================
Original URL: https://blums-xray.xyz
Prompt: Design a basic smart contract in Rust for Polkadot that manages the allocation and claim of PAWS rewards.
Generated: DETERMINISTIC_d959eb9d00287776
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! PAWS Rewards Smart Contract for Polkadot
//! This contract manages the allocation and claiming of PAWS tokens as rewards.

#![cfg_attr(not(feature = "std"), no_std)]

use ink_lang as ink;

#[ink::contract]
mod paws_rewards {
    use ink_storage::{
        collections::HashMap as StorageHashMap,
        traits::{PackedLayout, SpreadLayout},
    };
    use scale::{Decode, Encode};

    /// Represents the error types for the PAWS rewards contract.
    #[derive(Debug, PartialEq, Eq, Encode, Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum Error {
        /// Reward already claimed
        RewardAlreadyClaimed,
        /// No reward allocated for the account
        NoRewardAllocated,
        /// Transfer failed
        TransferFailed,
    }

    /// Result type for the contract operations
    pub type Result<T> = core::result::Result<T, Error>;

    /// The PAWS rewards contract
    #[ink(storage)]
    pub struct PawsRewards {
        /// Mapping from account to allocated reward amount
        rewards: StorageHashMap<AccountId, Balance>,
        /// Mapping from account to claimed status
        claimed: StorageHashMap<AccountId, bool>,
    }

    impl PawsRewards {
        /// Creates a new PAWS rewards contract
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                rewards: StorageHashMap::new(),
                claimed: StorageHashMap::new(),
            }
        }

        /// Allocate rewards to an account
        #[ink(message)]
        pub fn allocate_reward(&mut self, account: AccountId, amount: Balance) {
            self.rewards.insert(account, amount);
            self.claimed.insert(account, false);
        }

        /// Claim the allocated reward
        #[ink(message)]
        pub fn claim_reward(&mut self) -> Result<()> {
            let caller = self.env().caller();
            
            // Check if reward exists
            let reward = self.rewards.get(&caller).ok_or(Error::NoRewardAllocated)?;
            
            // Check if already claimed
            if *self.claimed.get(&caller).unwrap_or(&false) {
                return Err(Error::RewardAlreadyClaimed);
            }

            // Mark as claimed
            self.claimed.insert(caller, true);

            // Transfer the reward
            if self.env().transfer(caller, *reward).is_err() {
                return Err(Error::TransferFailed);
            }

            Ok(())
        }

        /// Get the allocated reward for an account
        #[ink(message)]
        pub fn get_allocated_reward(&self, account: AccountId) -> Option<Balance> {
            self.rewards.get(&account).copied()
        }

        /// Check if reward has been claimed
        #[ink(message)]
        pub fn is_claimed(&self, account: AccountId) -> bool {
            *self.claimed.get(&account).unwrap_or(&false)
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use ink_env::test;

        #[test]
        fn allocate_and_claim_works() {
            let mut contract = PawsRewards::new();
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();
            
            // Allocate reward
            let reward_amount = 100;
            contract.allocate_reward(accounts.alice, reward_amount);
            
            // Verify allocation
            assert_eq!(
                contract.get_allocated_reward(accounts.alice),
                Some(reward_amount)
            );
            assert!(!contract.is_claimed(accounts.alice));
            
            // Claim reward
            test::set_caller::<ink_env::DefaultEnvironment>(accounts.alice);
            assert_eq!(contract.claim_reward(), Ok(()));
            
            // Verify claim
            assert!(contract.is_claimed(accounts.alice));
            
            // Try to claim again (should fail)
            assert_eq!(
                contract.claim_reward(),
                Err(Error::RewardAlreadyClaimed)
            );
        }

        #[test]
        fn claim_without_allocation_fails() {
            let mut contract = PawsRewards::new();
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();
            
            test::set_caller::<ink_env::DefaultEnvironment>(accounts.alice);
            assert_eq!(
                contract.claim_reward(),
                Err(Error::NoRewardAllocated)
            );
        }
    }
}
```
