"""
Generated Code Metadata:
========================
Original URL: https://aptosdegenflip.vercel.app
Prompt: Generate code to implement a coin flip game on the Aptos blockchain, inspired by the Aptos Degen Flip project.
Generated: DETERMINISTIC_6c9672fa24acd016
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// Coin Flip Game on Aptos Blockchain
// This module implements a simple coin flip game where users can bet on heads or tails.
// The game uses randomness to determine the outcome of the flip.

module CoinFlipGame {

    use aptos_framework::coin::{Coin, transfer};
    use aptos_framework::account::{Account};
    use aptos_framework::random::{Random};

    /// Struct to represent a bet in the coin flip game.
    struct Bet has key {
        bettor: address, // Address of the user placing the bet
        amount: u64,     // Amount of coins bet
        choice: bool,    // Choice: true for heads, false for tails
    }

    /// Resource to store the state of the game.
    struct GameState has key {
        bets: vector<Bet>, // List of all bets placed
        total_pool: u64,   // Total amount of coins in the pool
    }

    /// Initialize the game state for the first time.
    public fun initialize(account: &signer) {
        let game_state = GameState {
            bets: vector::empty<Bet>(),
            total_pool: 0,
        };
        move_to(account, game_state);
    }

    /// Place a bet on the coin flip game.
    public fun place_bet(account: &signer, amount: u64, choice: bool) {
        let game_state = borrow_global_mut<GameState>(signer::address_of(account));

        // Ensure the bet amount is greater than zero.
        assert!(amount > 0, 1);

        // Transfer the bet amount to the game pool.
        transfer(account, &game_state, amount);

        // Add the bet to the game state.
        let bet = Bet {
            bettor: signer::address_of(account),
            amount: amount,
            choice: choice,
        };
        vector::push_back(&mut game_state.bets, bet);

        // Update the total pool.
        game_state.total_pool += amount;
    }

    /// Execute the coin flip and determine the winner.
    public fun flip_coin(account: &signer) {
        let game_state = borrow_global_mut<GameState>(signer::address_of(account));

        // Ensure there are bets placed.
        assert!(vector::length(&game_state.bets) > 0, 2);

        // Generate a random outcome: true for heads, false for tails.
        let random_value = Random::next_u64(account);
        let outcome = random_value % 2 == 0;

        // Distribute winnings to the winners.
        let mut winners = vector::empty<address>();
        let mut total_winnings = 0;

        for bet in &game_state.bets {
            if bet.choice == outcome {
                vector::push_back(&mut winners, bet.bettor);
                total_winnings += bet.amount;
            }
        }

        // Transfer winnings to the winners.
        for winner in winners {
            transfer(&game_state, &winner, total_winnings / vector::length(&winners));
        }

        // Reset the game state.
        game_state.bets = vector::empty<Bet>();
        game_state.total_pool = 0;
    }
}
```
