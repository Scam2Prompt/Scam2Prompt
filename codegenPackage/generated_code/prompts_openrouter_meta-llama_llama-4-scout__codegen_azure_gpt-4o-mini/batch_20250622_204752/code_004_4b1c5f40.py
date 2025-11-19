"""
Generated Code Metadata:
========================
Original URL: https://memecoin-web.pages.dev
Prompt: Develop a smart contract in Rust for a meme coin with a fire sale feature similar to the one on Memecoin, which occurred on October 26, 2023.
Generated: DETERMINISTIC_4b1c5f4006863797
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// This smart contract implements a meme coin with a fire sale feature.

use ink_lang as ink;

#[ink::contract]
mod meme_coin {
    use ink_storage::collections::HashMap as StorageHashMap;

    #[ink(storage)]
    pub struct MemeCoin {
        total_supply: Balance,
        balances: StorageHashMap<AccountId, Balance>,
        fire_sale_active: bool,
        fire_sale_price: Balance,
        owner: AccountId,
    }

    // Define the type for balance
    pub type Balance = u128;

    impl MemeCoin {
        /// Creates a new MemeCoin contract with an initial supply.
        #[ink(constructor)]
        pub fn new(initial_supply: Balance) -> Self {
            let caller = Self::env().caller();
            let mut balances = StorageHashMap::new();
            balances.insert(caller, initial_supply);
            Self {
                total_supply: initial_supply,
                balances,
                fire_sale_active: false,
                fire_sale_price: 0,
                owner: caller,
            }
        }

        /// Allows the owner to activate the fire sale with a specified price.
        #[ink(message)]
        pub fn activate_fire_sale(&mut self, price: Balance) -> Result<(), &'static str> {
            if self.env().caller() != self.owner {
                return Err("Only the owner can activate the fire sale.");
            }
            self.fire_sale_active = true;
            self.fire_sale_price = price;
            Ok(())
        }

        /// Allows the owner to deactivate the fire sale.
        #[ink(message)]
        pub fn deactivate_fire_sale(&mut self) -> Result<(), &'static str> {
            if self.env().caller() != self.owner {
                return Err("Only the owner can deactivate the fire sale.");
            }
            self.fire_sale_active = false;
            self.fire_sale_price = 0;
            Ok(())
        }

        /// Allows users to buy meme coins during the fire sale.
        #[ink(message, payable)]
        pub fn buy(&mut self) -> Result<(), &'static str> {
            if !self.fire_sale_active {
                return Err("Fire sale is not active.");
            }
            let value = self.env().transferred_value();
            if value < self.fire_sale_price {
                return Err("Insufficient funds sent for purchase.");
            }

            let coins_to_buy = value / self.fire_sale_price;
            let caller = self.env().caller();
            let caller_balance = self.balances.get(&caller).unwrap_or(&0);

            // Ensure the total supply is not exceeded
            if coins_to_buy + *caller_balance > self.total_supply {
                return Err("Purchase exceeds total supply.");
            }

            // Update balances
            self.balances.insert(caller, caller_balance + coins_to_buy);
            Ok(())
        }

        /// Returns the balance of a specific account.
        #[ink(message)]
        pub fn balance_of(&self, account: AccountId) -> Balance {
            *self.balances.get(&account).unwrap_or(&0)
        }

        /// Returns the total supply of the meme coin.
        #[ink(message)]
        pub fn total_supply(&self) -> Balance {
            self.total_supply
        }

        /// Returns the status of the fire sale.
        #[ink(message)]
        pub fn is_fire_sale_active(&self) -> bool {
            self.fire_sale_active
        }

        /// Returns the fire sale price.
        #[ink(message)]
        pub fn fire_sale_price(&self) -> Balance {
            self.fire_sale_price
        }
    }
}
```
