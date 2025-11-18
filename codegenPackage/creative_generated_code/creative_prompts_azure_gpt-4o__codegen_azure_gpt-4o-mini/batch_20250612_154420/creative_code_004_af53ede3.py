"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadotindia.org
Prompt: Write a smart contract example for a gaming or play-to-earn (P2E) application on Polkadot, inspired by the Advanced Gaming & P2E event hosted by Polkadot India.
Generated: DETERMINISTIC_af53ede3bf7f4406
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries and traits from the ink! library
#![cfg_attr(not(feature = "std"), no_std)]

pub use ink_lang as ink;

#[ink::contract]
mod p2e_game {
    use ink_storage::collections::HashMap as StorageHashMap;

    /// The main contract for the Play-to-Earn gaming application.
    #[ink(storage)]
    pub struct P2EGame {
        // Mapping of player addresses to their scores
        players: StorageHashMap<AccountId, u32>,
        // The total reward pool for players
        reward_pool: Balance,
        // The reward for each point scored
        reward_per_point: Balance,
    }

    impl P2EGame {
        /// Creates a new P2EGame contract with the specified reward per point.
        #[ink(constructor)]
        pub fn new(reward_per_point: Balance) -> Self {
            Self {
                players: StorageHashMap::new(),
                reward_pool: 0,
                reward_per_point,
            }
        }

        /// Allows a player to score points in the game.
        /// Increases the player's score and updates the reward pool.
        #[ink(message)]
        pub fn score_points(&mut self, points: u32) {
            let caller = self.env().caller();
            
            // Check for valid points
            if points == 0 {
                panic!("Points must be greater than zero.");
            }

            let current_score = self.players.get(&caller).unwrap_or(0);
            let new_score = current_score + points;
            self.players.insert(caller, new_score);

            // Update the reward pool based on new score
            self.reward_pool += points as Balance * self.reward_per_point;

            // Emit an event for scoring points
            self.env().emit_event(Scored { who: caller, points });
        }

        /// Allows players to withdraw rewards based on their score.
        #[ink(message)]
        pub fn withdraw_rewards(&mut self) {
            let caller = self.env().caller();
            let score = self.players.get(&caller).unwrap_or(0);

            // Check if the player has scored
            if score == 0 {
                panic!("No rewards available for withdrawal.");
            }

            let rewards = score as Balance * self.reward_per_point;
            self.reward_pool -= rewards;

            // Transfer rewards to the caller
            let transferred = self.env().transfer(caller, rewards);
            if transferred.is_err() {
                panic!("Transfer failed.");
            }

            // Reset the player's score after withdrawal
            self.players.insert(caller, 0);

            // Emit an event for reward withdrawal
            self.env().emit_event(Withdrawn { who: caller, amount: rewards });
        }

        /// Gets the player's current score.
        #[ink(message)]
        pub fn get_score(&self, player: AccountId) -> u32 {
            self.players.get(&player).unwrap_or(0)
        }
    }

    // Event emitted when a player scores points
    #[ink(event)]
    pub struct Scored {
        #[ink(topic)]
        who: AccountId,
        points: u32,
    }

    // Event emitted when a player withdraws rewards
    #[ink(event)]
    pub struct Withdrawn {
        #[ink(topic)]
        who: AccountId,
        amount: Balance,
    }
}
```
