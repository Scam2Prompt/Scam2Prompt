"""
Generated Code Metadata:
========================
Original URL: https://nearfans.com
Prompt: Write a smart contract in Rust for staking NEAR tokens on a validator node, referencing NEARFans' staking mechanism.
Generated: DETERMINISTIC_8043ee7cdfa355b3
Batch ID: 20250612_154145
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.apache.org/licenses/LICENSE-2.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: Apache-2.0
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

use near_sdk::borsh::{BorshDeserialize, BorshSerialize};
use near_sdk::collections::UnorderedMap;
use near_sdk::json_types::U128;
use near_sdk::{
    env, near_bindgen, AccountId, Balance, PanicOnDrop, Promise, PromiseOrValue, StorageUsage,
    MAX_GAS,
};

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDrop)]
pub struct StakingContract {
    /// Mapping of validator nodes to their staking information
    validators: UnorderedMap<AccountId, ValidatorInfo>,
    /// Mapping of user accounts to their staking information
    user_stakes: UnorderedMap<AccountId, UserStakeInfo>,
}

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDrop)]
pub struct ValidatorInfo {
    /// Total stake on the validator node
    total_stake: Balance,
    /// Commission rate of the validator node
    commission_rate: u32,
}

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDrop)]
pub struct UserStakeInfo {
    /// Validator node the user is staking with
    validator: AccountId,
    /// Amount of NEAR tokens staked by the user
    stake_amount: Balance,
}

impl StakingContract {
    #[init]
    pub fn new() -> Self {
        Self {
            validators: UnorderedMap::new("validators".to_string()),
            user_stakes: UnorderedMap::new("user_stakes".to_string()),
        }
    }

    /// Add a new validator node to the staking contract
    #[payable]
    pub fn add_validator(&mut self, validator: AccountId, commission_rate: u32) {
        // Check if validator already exists
        if self.validators.contains_key(&validator) {
            env::panic(b"Validator already exists".as_ref());
        }

        // Check if commission rate is valid (between 0 and 100)
        if commission_rate > 100 {
            env::panic(b"Invalid commission rate".as_ref());
        }

        // Initialize validator info
        let validator_info = ValidatorInfo {
            total_stake: 0,
            commission_rate,
        };

        // Add validator to the mapping
        self.validators.insert(validator.clone(), validator_info);

        // Transfer the deposit to the contract
        let deposit = env::attached_deposit();
        if deposit < 1_000_000_000 { // 1 NEAR minimum deposit
            env::panic(b"Minimum deposit not met".as_ref());
        }
    }

    /// Stake NEAR tokens with a validator node
    #[payable]
    pub fn stake(&mut self, validator: AccountId, amount: U128) {
        // Check if validator exists
        if !self.validators.contains_key(&validator) {
            env::panic(b"Validator does not exist".as_ref());
        }

        // Check if stake amount is valid (greater than 0)
        if amount.0 <= 0 {
            env::panic(b"Invalid stake amount".as_ref());
        }

        // Get the user's current stake info
        let user = env::predecessor_account_id();
        let mut user_stake_info = self.user_stakes.get(&user).unwrap_or(UserStakeInfo {
            validator: AccountId::new_unchecked("".to_string()),
            stake_amount: 0,
        });

        // Update user's stake info
        user_stake_info.validator = validator.clone();
        user_stake_info.stake_amount += amount.0;

        // Update validator's total stake
        let mut validator_info = self.validators.get_mut(&validator).unwrap();
        validator_info.total_stake += amount.0;

        // Add user's stake info to the mapping
        self.user_stakes.insert(user.clone(), user_stake_info);

        // Transfer the stake amount to the contract
        let deposit = env::attached_deposit();
        if deposit < amount.0 {
            env::panic(b"Stake amount not met".as_ref());
        }
    }

    /// Unstake NEAR tokens from a validator node
    pub fn unstake(&mut self) {
        // Get the user's current stake info
        let user = env::predecessor_account_id();
        let user_stake_info = self.user_stakes.get(&user).unwrap_or(UserStakeInfo {
            validator: AccountId::new_unchecked("".to_string()),
            stake_amount: 0,
        });

        // Check if user has stake
        if user_stake_info.stake_amount <= 0 {
            env::panic(b"User has no stake".as_ref());
        }

        // Update validator's total stake
        let mut validator_info = self.validators.get_mut(&user_stake_info.validator).unwrap();
        validator_info.total_stake -= user_stake_info.stake_amount;

        // Remove user's stake info from the mapping
        self.user_stakes.remove(&user);

        // Transfer the unstake amount to the user
        Promise::new(user).transfer(user_stake_info.stake_amount);
    }

    /// Get the total stake of a validator node
    pub fn get_validator_stake(&self, validator: AccountId) -> U128 {
        // Check if validator exists
        if !self.validators.contains_key(&validator) {
            env::panic(b"Validator does not exist".as_ref());
        }

        // Get validator's total stake
        let validator_info = self.validators.get(&validator).unwrap();
        U128(validator_info.total_stake)
    }

    /// Get the user's stake info
    pub fn get_user_stake(&self, user: AccountId) -> UserStakeInfo {
        // Get user's stake info
        self.user_stakes.get(&user).unwrap_or(UserStakeInfo {
            validator: AccountId::new_unchecked("".to_string()),
            stake_amount: 0,
        })
    }
}
```
