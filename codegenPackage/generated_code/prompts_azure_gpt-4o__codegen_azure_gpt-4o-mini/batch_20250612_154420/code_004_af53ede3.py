"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: Write a smart contract example for a gaming or play-to-earn (P2E) application on Polkadot, inspired by the Advanced Gaming & P2E event hosted by Polkadot India.
Generated: DETERMINISTIC_af53ede3bf7f4406
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries from the Substrate framework
use frame_support::{decl_module, decl_storage, decl_event, dispatch::DispatchResult};
use frame_system::ensure_signed;
use sp_std::vec::Vec;

// Define the module's configuration trait
pub trait Config: frame_system::Config {
    // Define the event type for this module
    type Event: From<Event<Self>> + Into<<Self as frame_system::Config>::Event>;
}

// Declare the module
decl_storage! {
    trait Store for Module<T: Config> as GameModule {
        // Store player balances
        PlayerBalances get(fn player_balance): map hasher(blake2_128_concat) T::AccountId => u64;
        // Store game rewards
        GameRewards get(fn game_reward): map hasher(blake2_128_concat) T::AccountId => u64;
    }
}

// Declare events for the module
decl_event! {
    pub enum Event<T> where AccountId = <T as frame_system::Config>::AccountId {
        // Event emitted when a player earns rewards
        RewardEarned(AccountId, u64),
        // Event emitted when a player withdraws their balance
        BalanceWithdrawn(AccountId, u64),
    }
}

// Implement the module's functionality
decl_module! {
    pub struct Module<T: Config> for enum Call where origin: T::Origin {
        // Define the event type
        fn deposit_event() = default;

        // Function to earn rewards
        #[weight = 10_000]
        pub fn earn_reward(origin, amount: u64) -> DispatchResult {
            // Ensure the caller is a signed user
            let sender = ensure_signed(origin)?;

            // Update the player's balance
            let new_balance = Self::player_balance(&sender).checked_add(amount).ok_or("Overflow occurred while adding reward")?;
            PlayerBalances::<T>::insert(&sender, new_balance);

            // Emit the reward earned event
            Self::deposit_event(RawEvent::RewardEarned(sender.clone(), amount));
            Ok(())
        }

        // Function to withdraw balance
        #[weight = 10_000]
        pub fn withdraw_balance(origin) -> DispatchResult {
            // Ensure the caller is a signed user
            let sender = ensure_signed(origin)?;

            // Get the player's balance
            let balance = Self::player_balance(&sender);
            ensure!(balance > 0, "Insufficient balance to withdraw");

            // Reset the player's balance to zero
            PlayerBalances::<T>::insert(&sender, 0);

            // Emit the balance withdrawn event
            Self::deposit_event(RawEvent::BalanceWithdrawn(sender.clone(), balance));
            Ok(())
        }
    }
}
```
