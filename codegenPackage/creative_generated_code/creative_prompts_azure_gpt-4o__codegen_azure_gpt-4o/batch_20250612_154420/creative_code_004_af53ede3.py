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
// This smart contract is written using the ink! framework for the Polkadot ecosystem.
// It is a simple example of a Play-to-Earn (P2E) gaming application where players can earn tokens by playing and completing game challenges.

#![cfg_attr(not(feature = "std"), no_std)]

use ink::prelude::*;
use ink::storage;

/// A smart contract for a Play-to-Earn (P2E) gaming application.
#[ink::contract]
mod p2e_game {
    use ink::env::Error as EnvError;

    /// The main struct that represents the P2E game.
    #[ink(storage)]
    pub struct P2EGame {
        /// A mapping of player addresses to their token balances.
        token_balances: ink::storage::Mapping<AccountId, u128>,
        
        /// The amount of tokens rewarded per challenge completion.
        reward_per_challenge: u128,
        
        /// The owner of the contract.
        owner: AccountId,
    }

    /// Custom errors for the contract.
    #[derive(Debug, PartialEq, Eq, ink::scale::Encode, ink::scale::Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum Error {
        /// Unauthorized access error.
        UnauthorizedAccess,
        
        /// Insufficient token balance error.
        InsufficientBalance,
        
        /// Failed to transfer tokens.
        TokenTransferFailed,
    }

    #[ink(event)]
    pub struct ChallengeCompleted {
        #[ink(topic)]
        player: AccountId,
        #[ink(topic)]
        reward: u128,
    }

    #[ink(event)]
    pub struct TokensTransferred {
        #[ink(topic)]
        from: AccountId,
        #[ink(topic)]
        to: AccountId,
        #[ink(topic)]
        amount: u128,
    }

    impl P2EGame {
        /// Constructor to initialize the contract state.
        /// Only the owner can set the reward-per-challenge amount.
        #[ink(constructor)]
        pub fn new(reward_per_challenge: u128) -> Self {
            let caller = Self::env().caller();
            Self {
                token_balances: ink::storage::Mapping::default(),
                reward_per_challenge,
                owner: caller,
            }
        }

        /// Allows a player to complete a challenge and earn tokens.
        #[ink(message)]
        pub fn complete_challenge(&mut self) -> Result<(), Error> {
            let caller = self.env().caller();
            let reward = self.reward_per_challenge;

            let new_balance = self.token_balances.get(&caller).unwrap_or(0) + reward;
            self.token_balances.insert(&caller, &new_balance);

            self.env().emit_event(ChallengeCompleted {
                player: caller,
                reward,
            });

            Ok(())
        }

        /// Allows the owner of the contract to transfer tokens to a specific player.
        #[ink(message)]
        pub fn transfer_tokens(
            &mut self,
            to: AccountId,
            amount: u128,
        ) -> Result<(), Error> {
            let caller = self.env().caller();

            if caller != self.owner {
                return Err(Error::UnauthorizedAccess);
            }

            let sender_balance = self.token_balances.get(&caller).unwrap_or(0);

            if sender_balance < amount {
                return Err(Error::InsufficientBalance);
            }

            let recipient_balance = self.token_balances.get(&to).unwrap_or(0);
            self.token_balances.insert(&caller, &(sender_balance - amount));
            self.token_balances.insert(&to, &(recipient_balance + amount));

            self.env().emit_event(TokensTransferred {
                from: caller,
                to,
                amount,
            });

            Ok(())
        }

        /// Returns the token balance of a player.
        #[ink(message)]
        pub fn get_balance(&self, account: AccountId) -> u128 {
            self.token_balances.get(&account).unwrap_or(0)
        }

        /// Allows the owner to update the reward amount for completing a challenge.
        #[ink(message)]
        pub fn update_reward(&mut self, new_reward: u128) -> Result<(), Error> {
            let caller = self.env().caller();
            if caller != self.owner {
                return Err(Error::UnauthorizedAccess);
            }
            self.reward_per_challenge = new_reward;
            Ok(())
        }
    }
}
```
