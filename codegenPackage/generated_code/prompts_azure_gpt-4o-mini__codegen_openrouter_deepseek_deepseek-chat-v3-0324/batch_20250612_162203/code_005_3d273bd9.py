"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Create a simple decentralized application (dApp) on Aleph Zero that utilizes its low-cost transaction model for a gaming use case.
Generated: DETERMINISTIC_3d273bd906176bc0
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! A simple decentralized application (dApp) for a gaming use case on Aleph Zero.
//! This dApp allows players to register, deposit funds, and play a simple game with low-cost transactions.

#![cfg_attr(not(feature = "std"), no_std)]

use ink_lang as ink;

#[ink::contract]
mod gaming_dapp {
    use ink_prelude::string::String;
    use ink_storage::{collections::HashMap as StorageHashMap, lazy::Lazy};

    /// Errors that can occur during contract execution.
    #[derive(Debug, PartialEq, Eq, scale::Encode, scale::Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum Error {
        /// Player is not registered.
        NotRegistered,
        /// Player is already registered.
        AlreadyRegistered,
        /// Insufficient balance for the operation.
        InsufficientBalance,
        /// Invalid bet amount (must be positive).
        InvalidBetAmount,
    }

    /// Result type for contract operations.
    pub type Result<T> = core::result::Result<T, Error>;

    /// Player information stored in the contract.
    #[derive(scale::Encode, scale::Decode, Clone)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo, ink_storage::traits::StorageLayout))]
    pub struct Player {
        /// Player's name
        name: String,
        /// Player's balance
        balance: Balance,
    }

    /// The gaming dApp contract.
    #[ink(storage)]
    pub struct GamingDapp {
        /// Owner of the contract
        owner: Lazy<AccountId>,
        /// Registered players
        players: StorageHashMap<AccountId, Player>,
    }

    impl GamingDapp {
        /// Creates a new gaming dApp contract.
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                owner: Lazy::new(Self::env().caller()),
                players: StorageHashMap::new(),
            }
        }

        /// Registers a new player.
        #[ink(message)]
        pub fn register(&mut self, name: String) -> Result<()> {
            let caller = self.env().caller();
            if self.players.contains_key(&caller) {
                return Err(Error::AlreadyRegistered);
            }

            self.players.insert(
                caller,
                Player {
                    name,
                    balance: 0,
                },
            );

            Ok(())
        }

        /// Deposits funds to player's balance.
        #[ink(message, payable)]
        pub fn deposit(&mut self) -> Result<()> {
            let caller = self.env().caller();
            let amount = self.env().transferred_value();
            let player = self.players.get_mut(&caller).ok_or(Error::NotRegistered)?;

            player.balance = player.balance.saturating_add(amount);
            Ok(())
        }

        /// Withdraws funds from player's balance.
        #[ink(message)]
        pub fn withdraw(&mut self, amount: Balance) -> Result<()> {
            let caller = self.env().caller();
            let player = self.players.get_mut(&caller).ok_or(Error::NotRegistered)?;

            if player.balance < amount {
                return Err(Error::InsufficientBalance);
            }

            player.balance = player.balance.saturating_sub(amount);
            self.env()
                .transfer(caller, amount)
                .map_err(|_| Error::InsufficientBalance)?;

            Ok(())
        }

        /// Plays a simple game where player can win or lose their bet.
        #[ink(message)]
        pub fn play_game(&mut self, bet_amount: Balance) -> Result<()> {
            if bet_amount == 0 {
                return Err(Error::InvalidBetAmount);
            }

            let caller = self.env().caller();
            let player = self.players.get_mut(&caller).ok_or(Error::NotRegistered)?;

            if player.balance < bet_amount {
                return Err(Error::InsufficientBalance);
            }

            // Simple 50/50 chance game
            let random_value = self.env().block_timestamp() % 2;
            if random_value == 0 {
                // Player wins - double the bet amount
                player.balance = player.balance.saturating_add(bet_amount);
            } else {
                // Player loses - subtract the bet amount
                player.balance = player.balance.saturating_sub(bet_amount);
            }

            Ok(())
        }

        /// Gets player information.
        #[ink(message)]
        pub fn get_player(&self, account_id: AccountId) -> Option<Player> {
            self.players.get(&account_id).cloned()
        }

        /// Gets contract owner.
        #[ink(message)]
        pub fn get_owner(&self) -> AccountId {
            *self.owner
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use ink_env::test;
        use ink_lang as ink;

        #[ink::test]
        fn new_works() {
            let contract = GamingDapp::new();
            assert_eq!(contract.get_owner(), test::default_accounts::<ink_env::DefaultEnvironment>().alice);
        }

        #[ink::test]
        fn register_works() {
            let mut contract = GamingDapp::new();
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();
            
            assert_eq!(contract.register("Alice".to_string()), Ok(()));
            assert_eq!(contract.register("Alice".to_string()), Err(Error::AlreadyRegistered));
            
            test::set_caller::<ink_env::DefaultEnvironment>(accounts.bob);
            assert_eq!(contract.register("Bob".to_string()), Ok(()));
        }

        #[ink::test]
        fn deposit_and_withdraw_work() {
            let mut contract = GamingDapp::new();
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();
            
            test::set_caller::<ink_env::DefaultEnvironment>(accounts.alice);
            assert_eq!(contract.register("Alice".to_string()), Ok(()));
            
            // Deposit
            test::set_value_transferred::<ink_env::DefaultEnvironment>(100);
            assert_eq!(contract.deposit(), Ok(()));
            assert_eq!(contract.get_player(accounts.alice).unwrap().balance, 100);
            
            // Withdraw
            assert_eq!(contract.withdraw(50), Ok(()));
            assert_eq!(contract.get_player(accounts.alice).unwrap().balance, 50);
            
            // Insufficient balance
            assert_eq!(contract.withdraw(100), Err(Error::InsufficientBalance));
        }

        #[ink::test]
        fn play_game_works() {
            let mut contract = GamingDapp::new();
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();
            
            test::set_caller::<ink_env::DefaultEnvironment>(accounts.alice);
            assert_eq!(contract.register("Alice".to_string()), Ok(()));
            
            // Deposit
            test::set_value_transferred::<ink_env::DefaultEnvironment>(100);
            assert_eq!(contract.deposit(), Ok(()));
            
            // Play game
            let initial_balance = contract.get_player(accounts.alice).unwrap().balance;
            assert_eq!(contract.play_game(50), Ok(()));
            let new_balance = contract.get_player(accounts.alice).unwrap().balance;
            
            // Balance should either increase or decrease by 50
            assert!(new_balance == initial_balance + 50 || new_balance == initial_balance - 50);
            
            // Invalid bet
            assert_eq!(contract.play_game(0), Err(Error::InvalidBetAmount));
        }
    }
}
```
