"""
Generated Code Metadata:
========================
Original URL: https://aptosdegenflip.vercel.app
Prompt: What are the steps to integrate a free minting process for a coin flip game on Aptos, based on the Aptos Degen Flip model?
Generated: DETERMINISTIC_65c3938fefb5d7a8
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary modules from the Aptos framework
use aptos_framework::coin;
use aptos_framework::aptos_coin;
use aptos_framework::aptos_account;
use aptos_framework::event;
use aptos_framework::account;
use aptos_framework::signer;
use aptos_framework::system_addresses;
use std::string::String;

// Define the module for the coin flip game
module my_game::coin_flip {
    use std::error;
    use std::signer;
    use std::vector;
    use aptos_framework::coin::{Self, Coin};
    use aptos_framework::aptos_coin::AptosCoin;
    use aptos_framework::event::{Self, EventHandle};
    use aptos_framework::account;

    // Constants
    const MIN_BET: u64 = 1000000; // 1 APTOS
    const HOUSE_EDGE: u64 = 2; // 2% house edge

    // Struct to hold game data
    struct Game has key {
        bets: EventHandle<BetEvent>,
        wins: EventHandle<WinEvent>,
    }

    // Event emitted when a bet is placed
    struct BetEvent has drop, store {
        player: address,
        amount: u64,
        is_heads: bool,
    }

    // Event emitted when a player wins
    struct WinEvent has drop, store {
        player: address,
        amount: u64,
    }

    // Initialize the game module
    public entry fun initialize(account: &signer) {
        let account_addr = signer::address_of(account);
        assert!(account_addr == @my_game, error::permission_denied(1));

        // Create and move the Game resource to the account
        move_to(account, Game {
            bets: account::new_event_handle<BetEvent>(account),
            wins: account::new_event_handle<WinEvent>(account),
        });
    }

    // Free minting function for initial coins (for testing)
    public entry fun free_mint(player: &signer, amount: u64) acquires Game {
        let game = borrow_global_mut<Game>(@my_game);
        let player_addr = signer::address_of(player);

        // Mint coins for the player (only in testnet or devnet)
        coin::register<AptosCoin>(player);
        let coins = coin::mint<AptosCoin>(amount, player_addr);
        event::emit_event(&mut game.bets, BetEvent {
            player: player_addr,
            amount,
            is_heads: false, // Default value for mint event
        });
    }

    // Function to place a bet
    public entry fun place_bet(
        player: &signer,
        amount: u64,
        is_heads: bool,
    ) acquires Game {
        assert!(amount >= MIN_BET, error::invalid_argument(1));

        let game = borrow_global_mut<Game>(@my_game);
        let player_addr = signer::address_of(player);

        // Transfer coins from player to the game
        let bet_coins = coin::withdraw<AptosCoin>(player, amount);

        // Emit bet event
        event::emit_event(&mut game.bets, BetEvent {
            player: player_addr,
            amount,
            is_heads,
        });

        // Flip the coin (randomness simulation)
        let random_number = *&player_addr.to_u128() % 2;
        let player_wins = (random_number == 0 && is_heads) || (random_number == 1 && !is_heads);

        if player_wins {
            let win_amount = amount * (100 - HOUSE_EDGE) / 100;
            let win_coins = coin::mint<AptosCoin>(win_amount, player_addr);
            coin::deposit(player_addr, win_coins);

            // Emit win event
            event::emit_event(&mut game.wins, WinEvent {
                player: player_addr,
                amount: win_amount,
            });
        }
    }
}
```
