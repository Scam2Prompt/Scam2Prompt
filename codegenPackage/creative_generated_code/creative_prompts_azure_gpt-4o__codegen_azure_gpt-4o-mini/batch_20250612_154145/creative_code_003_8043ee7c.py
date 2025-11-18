"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nearfans.com
Prompt: Write a smart contract in Rust for staking NEAR tokens on a validator node, referencing NEARFans' staking mechanism.
Generated: DETERMINISTIC_8043ee7cdfa355b3
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Define the NEAR token staking smart contract
#![no_std]
#![feature(allocator_api)]

extern crate alloc;

use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::json_types::U128;
use near_sdk::serde::{Deserialize, Serialize};
use near_sdk::near_bindgen;
use near_sdk::{env, log, PanicOnDefault, Promise, AccountId};

mod models {
    use super::*;

    // Structure to hold staking information
    #[derive(BorshDeserialize, BorshSerialize, Clone, Default)]
    pub struct Staker {
        pub amount: u128,
        pub validator_id: AccountId,
    }

    // Structure to hold the staking contract's state
    #[derive(BorshDeserialize, BorshSerialize)]
    pub struct StakingContract {
        pub stakes: std::collections::HashMap<AccountId, Staker>,
    }

    impl Default for StakingContract {
        fn default() -> Self {
            Self {
                stakes: std::collections::HashMap::new(),
            }
        }
    }
}

// Define the main contract structure and its methods
#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct Staking {
    stakes: std::collections::HashMap<AccountId, models::Staker>,
}

#[near_bindgen]
impl Staking {
    // Initialize the contract
    #[init]
    pub fn new() -> Self {
        Self {
            stakes: std::collections::HashMap::new(),
        }
    }

    // Stake NEAR tokens to a validator
    #[payable]
    pub fn stake(&mut self, validator_id: AccountId) {
        let amount = env::attached_deposit();
        assert!(amount > 0, "Must stake a positive amount");

        // Log the staking action
        log!("Staking {} to {}", amount, validator_id);

        // Update the stakes map
        let account_id = env::signer_account_id();
        let staker = self
            .stakes
            .entry(account_id.clone())
            .or_insert(models::Staker::default());

        staker.amount += amount;
        staker.validator_id = validator_id.clone();

        // Here you would interact with the validator to actually stake the NEAR
        // For example, sending a promise to the validator's contract to handle the stake

        log!("Staked {} NEAR to {}", amount, validator_id);
    }

    // Unstake NEAR tokens from the validator
    pub fn unstake(&mut self) {
        let account_id = env::signer_account_id();
        let staker = self.stakes.get_mut(&account_id).expect("You have no stake");

        // Log the unstaking action
        log!("Unstaking {} from {}", staker.amount, staker.validator_id);

        // Here you would interact with the validator to actually unstake the NEAR

        // Remove staker info
        self.stakes.remove(&account_id);
        log!("Unstaked {} NEAR from {}", staker.amount, staker.validator_id);
    }

    // Query total staked amount for a specific account
    #[getter]
    pub fn get_staked_amount(&self, account_id: AccountId) -> U128 {
        match self.stakes.get(&account_id) {
            Some(staker) => U128(staker.amount),
            None => U128(0),
        }
    }
}
```
