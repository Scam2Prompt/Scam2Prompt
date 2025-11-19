"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Explain how to implement a private fundraising mechanism using Aleph Zero's smart contracts while ensuring confidentiality.
Generated: DETERMINISTIC_4faa53ae98cc8821
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
#![no_std]

use ink::prelude::*;
use ink::storage::Mapping;

/// A private fundraising smart contract using Aleph Zero's ink! framework.
#[ink::contract]
mod private_fundraising {
    /// The main contract structure.
    #[ink(storage)]
    pub struct PrivateFundraising {
        /// Mapping to store contributions by account.
        contributions: Mapping<AccountId, Balance>,
        /// The owner of the fundraising campaign.
        owner: AccountId,
        /// The fundraising goal.
        goal: Balance,
        /// Whether the fundraising is active.
        is_active: bool,
    }

    impl PrivateFundraising {
        /// Constructor to initialize the fundraising contract.
        #[ink(constructor)]
        pub fn new(goal: Balance) -> Self {
            let caller = Self::env().caller();
            Self {
                contributions: Mapping::default(),
                owner: caller,
                goal,
                is_active: true,
            }
        }

        /// Contribute to the fundraising campaign.
        #[ink(message)]
        pub fn contribute(&mut self) -> Result<(), String> {
            // Ensure the fundraising is active.
            if !self.is_active {
                return Err("Fundraising is no longer active.".into());
            }

            // Get the caller and the transferred value.
            let caller = self.env().caller();
            let value = self.env().transferred_value();

            // Ensure a valid contribution amount.
            if value == 0 {
                return Err("Contribution must be greater than zero.".into());
            }

            // Update the caller's contribution.
            let current_contribution = self.contributions.get(&caller).unwrap_or(0);
            self.contributions.insert(&caller, &(current_contribution + value));

            Ok(())
        }

        /// End the fundraising campaign (only callable by the owner).
        #[ink(message)]
        pub fn end_fundraising(&mut self) -> Result<(), String> {
            // Ensure only the owner can call this function.
            if self.env().caller() != self.owner {
                return Err("Only the owner can end the fundraising.".into());
            }

            // Mark the fundraising as inactive.
            self.is_active = false;
            Ok(())
        }

        /// Withdraw funds (only callable by the owner).
        #[ink(message)]
        pub fn withdraw(&mut self) -> Result<(), String> {
            // Ensure only the owner can call this function.
            if self.env().caller() != self.owner {
                return Err("Only the owner can withdraw funds.".into());
            }

            // Ensure the fundraising is no longer active.
            if self.is_active {
                return Err("Cannot withdraw funds while fundraising is active.".into());
            }

            // Transfer the contract's balance to the owner.
            let balance = self.env().balance();
            if balance > 0 {
                self.env()
                    .transfer(self.owner, balance)
                    .map_err(|_| "Failed to transfer funds.".to_string())?;
            }

            Ok(())
        }

        /// Get the total contribution of a specific account.
        #[ink(message)]
        pub fn get_contribution(&self, account: AccountId) -> Balance {
            self.contributions.get(&account).unwrap_or(0)
        }

        /// Get the current status of the fundraising campaign.
        #[ink(message)]
        pub fn get_status(&self) -> (Balance, Balance, bool) {
            let total_raised: Balance = self
                .contributions
                .iter()
                .map(|(_, value)| value)
                .sum();
            (total_raised, self.goal, self.is_active)
        }
    }

    /// Unit tests for the contract.
    #[cfg(test)]
    mod tests {
        use super::*;
        use ink::env::test;

        #[ink::test]
        fn test_contribution() {
            let mut contract = PrivateFundraising::new(1000);
            let accounts = test::default_accounts::<ink::env::DefaultEnvironment>();

            // Simulate a contribution.
            test::set_caller::<ink::env::DefaultEnvironment>(accounts.alice);
            test::set_value_transferred::<ink::env::DefaultEnvironment>(500);
            assert!(contract.contribute().is_ok());

            // Verify the contribution.
            assert_eq!(contract.get_contribution(accounts.alice), 500);
        }

        #[ink::test]
        fn test_withdraw() {
            let mut contract = PrivateFundraising::new(1000);
            let accounts = test::default_accounts::<ink::env::DefaultEnvironment>();

            // Simulate contributions.
            test::set_caller::<ink::env::DefaultEnvironment>(accounts.alice);
            test::set_value_transferred::<ink::env::DefaultEnvironment>(500);
            assert!(contract.contribute().is_ok());

            // End the fundraising.
            test::set_caller::<ink::env::DefaultEnvironment>(accounts.bob);
            assert!(contract.end_fundraising().is_err()); // Only owner can end.

            test::set_caller::<ink::env::DefaultEnvironment>(accounts.alice);
            assert!(contract.end_fundraising().is_ok());

            // Withdraw funds.
            assert!(contract.withdraw().is_ok());
        }
    }
}
```
