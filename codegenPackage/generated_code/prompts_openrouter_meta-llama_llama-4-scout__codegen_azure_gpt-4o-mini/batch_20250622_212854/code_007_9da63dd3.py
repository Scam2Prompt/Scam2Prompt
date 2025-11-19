"""
Generated Code Metadata:
========================
Original URL: https://www.unisocks.fi
Prompt: Implement a simple smart contract in Rust for managing the buying, selling, and redeeming of digital assets like Unisocks.
Generated: DETERMINISTIC_9da63dd3f0ebd244
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// A simple smart contract for managing the buying, selling, and redeeming of digital assets.

use ink_lang as ink;

#[ink::contract]
mod digital_asset_manager {
    use ink_storage::collections::HashMap as StorageHashMap;

    #[ink(storage)]
    pub struct DigitalAssetManager {
        // Mapping of asset IDs to their owners
        assets: StorageHashMap<u32, AccountId>,
        // Mapping of asset IDs to their prices
        prices: StorageHashMap<u32, Balance>,
        // Counter for asset IDs
        asset_counter: u32,
    }

    impl DigitalAssetManager {
        /// Creates a new instance of the DigitalAssetManager contract.
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                assets: StorageHashMap::new(),
                prices: StorageHashMap::new(),
                asset_counter: 0,
            }
        }

        /// Allows the owner to create a new digital asset.
        /// Returns the asset ID.
        #[ink(message)]
        pub fn create_asset(&mut self, price: Balance) -> Result<u32, &'static str> {
            // Increment the asset counter to get a new asset ID
            self.asset_counter += 1;
            let asset_id = self.asset_counter;

            // Store the asset with the caller as the owner
            self.assets.insert(asset_id, Self::env().caller());
            self.prices.insert(asset_id, price);

            Ok(asset_id)
        }

        /// Allows the owner of the asset to sell it at a specified price.
        #[ink(message)]
        pub fn sell_asset(&mut self, asset_id: u32, price: Balance) -> Result<(), &'static str> {
            // Check if the asset exists and the caller is the owner
            if let Some(owner) = self.assets.get(&asset_id) {
                if *owner == Self::env().caller() {
                    self.prices.insert(asset_id, price);
                    Ok(())
                } else {
                    Err("Caller is not the owner of the asset")
                }
            } else {
                Err("Asset does not exist")
            }
        }

        /// Allows a user to buy an asset if it is for sale.
        #[ink(message, payable)]
        pub fn buy_asset(&mut self, asset_id: u32) -> Result<(), &'static str> {
            // Check if the asset exists
            if let Some(price) = self.prices.get(&asset_id) {
                // Ensure the sent value matches the price
                if Self::env().transferred_value() == *price {
                    // Transfer ownership of the asset
                    let current_owner = self.assets.get(&asset_id).ok_or("Asset does not exist")?;
                    self.assets.insert(asset_id, Self::env().caller());

                    // Transfer funds to the previous owner
                    let _ = ink_env::transfer(*current_owner, *price).map_err(|_| "Transfer failed")?;
                    Ok(())
                } else {
                    Err("Incorrect value sent")
                }
            } else {
                Err("Asset is not for sale")
            }
        }

        /// Allows the owner to redeem their asset.
        #[ink(message)]
        pub fn redeem_asset(&mut self, asset_id: u32) -> Result<(), &'static str> {
            // Check if the asset exists and the caller is the owner
            if let Some(owner) = self.assets.get(&asset_id) {
                if *owner == Self::env().caller() {
                    // Remove the asset from storage
                    self.assets.remove(&asset_id);
                    self.prices.remove(&asset_id);
                    Ok(())
                } else {
                    Err("Caller is not the owner of the asset")
                }
            } else {
                Err("Asset does not exist")
            }
        }

        /// Returns the owner of a specific asset.
        #[ink(message)]
        pub fn get_asset_owner(&self, asset_id: u32) -> Option<AccountId> {
            self.assets.get(&asset_id).cloned()
        }

        /// Returns the price of a specific asset.
        #[ink(message)]
        pub fn get_asset_price(&self, asset_id: u32) -> Option<Balance> {
            self.prices.get(&asset_id).cloned()
        }
    }
}
```
