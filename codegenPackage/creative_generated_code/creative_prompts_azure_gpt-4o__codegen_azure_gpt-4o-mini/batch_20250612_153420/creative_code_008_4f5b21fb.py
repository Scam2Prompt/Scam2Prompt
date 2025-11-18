"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-gummyonsol.pages.dev
Prompt: Create a smart contract in Rust for managing $GUMMY token distribution, adhering to the tokenomics percentages outlined on the website.
Generated: DETERMINISTIC_4f5b21fb4f3a95db
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT

use ink_lang as ink;

#[ink::contract]
mod gummy_token {
    use ink_storage::collections::HashMap as StorageMap;

    #[ink(storage)]
    pub struct GummyToken {
        total_supply: Balance,
        balances: StorageMap<AccountId, Balance>,
        distributions: Distribution,
    }

    #[derive(Debug, Clone, Copy)]
    pub struct Distribution {
        pub team: u64,
        pub marketing: u64,
        pub development: u64,
        pub community: u64,
        pub reserves: u64,
    }

    impl Default for Distribution {
        fn default() -> Self {
            Self {
                team: 10,
                marketing: 15,
                development: 25,
                community: 30,
                reserves: 20,
            }
        }
    }

    #[ink(event)]
    pub struct Transfer {
        #[ink(topic)]
        from: AccountId,
        #[ink(topic)]
        to: AccountId,
        value: Balance,
    }

    impl GummyToken {
        /// Creates a new GummyToken instance with the specified total supply.
        #[ink(constructor)]
        pub fn new(total_supply: Balance) -> Self {
            let mut distributions = Distribution::default();
            let total_distribution = distributions.team
                + distributions.marketing
                + distributions.development
                + distributions.community
                + distributions.reserves;

            assert!(total_distribution == 100, "Total distribution must equal 100%");

            let mut instance = Self {
                total_supply,
                balances: StorageMap::new(),
                distributions,
            };

            // Allocate initial distributions
            instance.balances.insert(ink_env::account_id(), total_supply);
            instance
        }

        /// Transfers tokens from the caller to a specified account.
        #[ink(message)]
        pub fn transfer(&mut self, to: AccountId, value: Balance) -> Result<(), &'static str> {
            let caller = self.env().caller();
            let caller_balance = self.balance_of(caller);

            // Ensure the caller has enough balance to transfer
            if caller_balance < value {
                return Err("Insufficient balance");
            }

            // Update balances
            self.balances.insert(caller, caller_balance - value);
            let recipient_balance = self.balance_of(to);
            self.balances.insert(to, recipient_balance + value);

            // Emit transfer event
            self.env().emit_event(Transfer {
                from: caller,
                to,
                value,
            });

            Ok(())
        }

        /// Returns the balance of the specified account.
        #[ink(message)]
        pub fn balance_of(&self, account: AccountId) -> Balance {
            *self.balances.get(&account).unwrap_or(&0)
        }

        /// Returns the total supply of the token.
        #[ink(message)]
        pub fn total_supply(&self) -> Balance {
            self.total_supply
        }

        /// Returns the distribution percentages.
        #[ink(message)]
        pub fn get_distribution(&self) -> Distribution {
            self.distributions
        }
    }
}
```
