"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doggodao.web.app
Prompt: Generate a smart contract in Rust for distributing $DOGGO tokens during an airdrop event, with a cap of 1,000,000,000 tokens.
Generated: DETERMINISTIC_a3951a7b0b0a7b5b
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries for smart contract development in Rust
use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::{env, near_bindgen, AccountId, PanicOnDefault, Promise};
use std::collections::HashMap;

// Define constants
const TOTAL_SUPPLY: u128 = 1_000_000_000; // Total supply of $DOGGO tokens

// Define the $DOGGO token smart contract
#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct DoggoToken {
    // Mapping of account IDs to their token balances
    balances: HashMap<AccountId, u128>,
    // Total tokens distributed
    distributed_tokens: u128,
}

#[near_bindgen]
impl DoggoToken {
    /// Initializes the contract with no distributed tokens.
    #[init]
    pub fn new() -> Self {
        assert!(!env::state_exists(), "Contract is already initialized");
        Self {
            balances: HashMap::new(),
            distributed_tokens: 0,
        }
    }

    /// Airdrops tokens to a list of accounts with specified amounts.
    /// - `recipients`: A vector of tuples containing account ID and token amount.
    pub fn airdrop(&mut self, recipients: Vec<(AccountId, u128)>) {
        // Ensure caller is the owner of the contract (security measure).
        let caller = env::predecessor_account_id();
        assert_eq!(caller, env::current_account_id(), "Only the contract owner can perform an airdrop");

        for (account_id, amount) in recipients {
            // Validate that the total distributed tokens will not exceed the total supply.
            assert!(
                self.distributed_tokens + amount <= TOTAL_SUPPLY,
                "Airdrop exceeds token supply"
            );

            // Update the recipient's balance.
            let balance = self.balances.entry(account_id.clone()).or_insert(0);
            *balance += amount;

            // Update the total distributed tokens.
            self.distributed_tokens += amount;

            // Log the airdrop transaction.
            env::log(format!("Airdropped {} $DOGGO tokens to {}", amount, account_id).as_bytes());
        }
    }

    /// Retrieves the balance of a specific account.
    /// - `account_id`: The account ID whose balance is being queried.
    pub fn get_balance(&self, account_id: AccountId) -> u128 {
        self.balances.get(&account_id).copied().unwrap_or(0)
    }

    /// Retrieves the total distributed tokens.
    pub fn get_total_distributed(&self) -> u128 {
        self.distributed_tokens
    }
}

// Unit tests for the smart contract
#[cfg(test)]
mod tests {
    use super::*;
    use near_sdk::test_utils::{accounts, VMContextBuilder};
    use near_sdk::{testing_env, MockedBlockchain};

    #[test]
    fn test_airdrop() {
        // Set up the mock context and environment
        let mut context = VMContextBuilder::new();
        testing_env!(context.predecessor_account_id(accounts(0)).build());

        let mut contract = DoggoToken::new();

        // Perform an airdrop
        contract.airdrop(vec![
            (accounts(1), 100),
            (accounts(2), 200),
            (accounts(3), 300),
        ]);

        // Assert the balances
        assert_eq!(contract.get_balance(accounts(1)), 100);
        assert_eq!(contract.get_balance(accounts(2)), 200);
        assert_eq!(contract.get_balance(accounts(3)), 300);

        // Assert the total distributed tokens
        assert_eq!(contract.get_total_distributed(), 600);
    }

    #[test]
    #[should_panic(expected = "Airdrop exceeds token supply")]
    fn test_airdrop_exceeds_supply() {
        // Set up the mock context and environment
        let mut context = VMContextBuilder::new();
        testing_env!(context.predecessor_account_id(accounts(0)).build());

        let mut contract = DoggoToken::new();

        // Attempt to airdrop more tokens than the total supply
        contract.airdrop(vec![
            (accounts(1), TOTAL_SUPPLY + 1),
        ]);
    }
}
```
