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
#![no_std]
#![feature(allocator_api)]

use ink_lang as ink;

#[ink::contract]
mod doggo_airdrop {
    use ink_storage::collections::HashMap as StorageMap;
    use ink_prelude::string::String;

    #[ink(storage)]
    pub struct DoggoAirdrop {
        total_supply: Balance,
        airdrop_cap: Balance,
        airdropped_tokens: Balance,
        recipients: StorageMap<AccountId, Balance>,
    }

    impl DoggoAirdrop {
        /// Constructor that initializes the contract with a total supply and airdrop cap.
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                total_supply: 1_000_000_000, // Total supply of tokens
                airdrop_cap: 1_000_000_000,  // Cap for airdrop tokens
                airdropped_tokens: 0,         // Tracks the amount of tokens airdropped
                recipients: StorageMap::new(), // Initializes the recipients map
            }
        }

        /// Function to airdrop tokens to a recipient.
        /// Ensures that the total airdropped does not exceed the cap.
        #[ink(message)]
        pub fn airdrop(&mut self, recipient: AccountId, amount: Balance) -> Result<(), String> {
            // Check if the recipient already received tokens
            if self.recipients.contains_key(&recipient) {
                return Err("Recipient has already received tokens".into());
            }

            // Check if the requested amount would exceed the airdrop cap
            if self.airdropped_tokens + amount > self.airdrop_cap {
                return Err("Airdrop cap exceeded".into());
            }

            // Update the state
            self.recipients.insert(recipient, amount);
            self.airdropped_tokens += amount;

            // Emit an event indicating that an airdrop has occurred
            Self::env().emit_event(AirdropEvent {
                recipient,
                amount,
            });

            Ok(())
        }

        /// Function to check the balance of a recipient.
        #[ink(message)]
        pub fn balance_of(&self, recipient: AccountId) -> Balance {
            self.recipients.get(&recipient).unwrap_or(0)
        }

        /// Function to retrieve the total amount of tokens airdropped.
        #[ink(message)]
        pub fn total_airdropped(&self) -> Balance {
            self.airdropped_tokens
        }
    }

    /// Event emitted when an airdrop occurs.
    #[ink(event)]
    pub struct AirdropEvent {
        #[ink(topic)]
        recipient: AccountId,
        amount: Balance,
    }
}
```
