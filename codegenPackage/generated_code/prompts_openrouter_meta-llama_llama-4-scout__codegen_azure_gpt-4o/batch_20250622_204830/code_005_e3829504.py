"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Design a basic smart contract in Rust for a similar token that rewards holders with a dynamic rate based on the total tokens staked, inspired by the Bitcoin ETF Token's staking mechanism.
Generated: DETERMINISTIC_e3829504b387cfa2
Batch ID: 20250622_204830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary dependencies
use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::{env, near_bindgen, AccountId, Balance, PanicOnDefault};
use std::collections::HashMap;

// Define the contract structure
#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct TokenContract {
    // Total supply of the token
    total_supply: Balance,
    // Mapping of account balances
    balances: HashMap<AccountId, Balance>,
    // Mapping of staked balances
    staked_balances: HashMap<AccountId, Balance>,
    // Total staked tokens
    total_staked: Balance,
}

// Implement the contract
#[near_bindgen]
impl TokenContract {
    // Initialize the contract with a total supply
    #[init]
    pub fn new(total_supply: Balance) -> Self {
        let mut balances = HashMap::new();
        let owner = env::predecessor_account_id();
        balances.insert(owner.clone(), total_supply);

        Self {
            total_supply,
            balances,
            staked_balances: HashMap::new(),
            total_staked: 0,
        }
    }

    // Get the balance of an account
    pub fn get_balance(&self, account_id: AccountId) -> Balance {
        *self.balances.get(&account_id).unwrap_or(&0)
    }

    // Stake tokens
    pub fn stake_tokens(&mut self, amount: Balance) {
        let account_id = env::predecessor_account_id();
        let balance = self.balances.entry(account_id.clone()).or_insert(0);

        // Ensure the user has enough tokens to stake
        assert!(*balance >= amount, "Insufficient balance to stake");

        // Deduct the staked amount from the user's balance
        *balance -= amount;

        // Add the staked amount to the user's staked balance
        let staked_balance = self.staked_balances.entry(account_id.clone()).or_insert(0);
        *staked_balance += amount;

        // Update the total staked tokens
        self.total_staked += amount;
    }

    // Unstake tokens
    pub fn unstake_tokens(&mut self, amount: Balance) {
        let account_id = env::predecessor_account_id();
        let staked_balance = self.staked_balances.entry(account_id.clone()).or_insert(0);

        // Ensure the user has enough staked tokens to unstake
        assert!(*staked_balance >= amount, "Insufficient staked balance to unstake");

        // Deduct the unstaked amount from the user's staked balance
        *staked_balance -= amount;

        // Add the unstaked amount back to the user's balance
        let balance = self.balances.entry(account_id.clone()).or_insert(0);
        *balance += amount;

        // Update the total staked tokens
        self.total_staked -= amount;
    }

    // Calculate rewards for an account based on the dynamic rate
    pub fn calculate_rewards(&self, account_id: AccountId) -> Balance {
        let staked_balance = *self.staked_balances.get(&account_id).unwrap_or(&0);

        // If no tokens are staked, rewards are zero
        if staked_balance == 0 {
            return 0;
        }

        // Dynamic reward rate based on the proportion of total staked tokens
        let reward_rate = staked_balance as f64 / self.total_staked as f64;

        // Calculate rewards (example: 10% of staked balance multiplied by reward rate)
        (staked_balance as f64 * 0.1 * reward_rate) as Balance
    }

    // Claim rewards
    pub fn claim_rewards(&mut self) {
        let account_id = env::predecessor_account_id();
        let rewards = self.calculate_rewards(account_id.clone());

        // Ensure there are rewards to claim
        assert!(rewards > 0, "No rewards available to claim");

        // Add rewards to the user's balance
        let balance = self.balances.entry(account_id.clone()).or_insert(0);
        *balance += rewards;

        // Log the reward claim
        env::log_str(&format!("{} claimed {} rewards", account_id, rewards));
    }
}
```

This Rust smart contract is designed for the NEAR blockchain and implements a basic token with staking and dynamic reward calculation. It includes proper error handling, follows best practices, and is well-documented with comments.
