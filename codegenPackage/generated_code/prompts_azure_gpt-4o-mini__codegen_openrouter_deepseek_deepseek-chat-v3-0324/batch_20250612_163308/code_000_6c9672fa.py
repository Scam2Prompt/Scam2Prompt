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

# Coin Flip Game on Aptos Blockchain

```rust
//! A simple coin flip game on Aptos blockchain
//! Inspired by Aptos Degen Flip project

use aptos_framework::coin;
use aptos_framework::aptos_coin::AptosCoin;
use aptos_framework::event;
use aptos_std::table::Table;
use aptos_std::type_info;
use std::string::String;

// Module constants
const HOUSE_EDGE_BASIS_POINTS: u64 = 200; // 2% house edge
const MIN_BET: u64 = 100000; // 0.1 APT
const MAX_BET: u64 = 100000000; // 100 APT

// Event structures
struct FlipEvent has drop, store {
    player: address,
    choice: bool,
    amount: u64,
    result: bool,
    payout: u64,
    flip_id: u64,
}

// Game state
struct GameState has key {
    flips: Table<address, u64>, // Tracks flip counts per player
    stats: Table<u64, u64>,     // Tracks game statistics
    next_flip_id: u64,          // Auto-incrementing flip ID
    admin: address,             // Admin address
    vault: coin::Coin<AptosCoin>, // Game vault
}

// Initialize the game module
fun init_module(account: &signer) {
    let account_addr = signer::address_of(account);
    
    // Create and initialize game state
    move_to(account, GameState {
        flips: table::new(),
        stats: table::new(),
        next_flip_id: 0,
        admin: account_addr,
        vault: coin::zero<AptosCoin>(),
    });

    // Initialize stats
    let game_state = borrow_global_mut<GameState>(account_addr);
    table::add(&mut game_state.stats, 0, 0); // Total flips
    table::add(&mut game_state.stats, 1, 0); // Heads wins
    table::add(&mut game_state.stats, 2, 0); // Tails wins
    table::add(&mut game_state.stats, 3, 0); // Total wagered
    table::add(&mut game_state.stats, 4, 0); // Total paid out
}

// Public entry function to play the game
public entry fun flip_coin(
    player: &signer,
    choice: bool, // true = heads, false = tails
    amount: u64,
) acquires GameState {
    let player_addr = signer::address_of(player);
    let game_addr = @game; // Replace with your module address

    // Validate bet amount
    assert!(amount >= MIN_BET, error::invalid_argument(1)); // Bet too small
    assert!(amount <= MAX_BET, error::invalid_argument(2)); // Bet too large

    // Transfer bet from player to game vault
    let bet = coin::withdraw<AptosCoin>(player, amount);
    let game_state = borrow_global_mut<GameState>(game_addr);
    coin::merge(&mut game_state.vault, bet);

    // Generate random result (true = heads, false = tails)
    let result = generate_random_result();

    // Calculate payout
    let payout = if choice == result {
        calculate_payout(amount)
    } else {
        0
    };

    // Update player flip count
    let flip_count = if (table::contains(&game_state.flips, player_addr)) {
        *table::borrow(&game_state.flips, player_addr) + 1
    } else {
        1
    };
    table::upsert(&mut game_state.flips, player_addr, flip_count);

    // Update game statistics
    *table::borrow_mut(&mut game_state.stats, 0) += 1; // Total flips
    if result {
        *table::borrow_mut(&mut game_state.stats, 1) += 1; // Heads wins
    } else {
        *table::borrow_mut(&mut game_state.stats, 2) += 1; // Tails wins
    };
    *table::borrow_mut(&mut game_state.stats, 3) += amount; // Total wagered
    *table::borrow_mut(&mut game_state.stats, 4) += payout; // Total paid out

    // Pay out winnings if any
    if payout > 0 {
        let payout_coin = coin::extract(&mut game_state.vault, payout);
        coin::deposit(player_addr, payout_coin);
    }

    // Emit event
    let flip_id = game_state.next_flip_id;
    game_state.next_flip_id += 1;
    event::emit(FlipEvent {
        player: player_addr,
        choice,
        amount,
        result,
        payout,
        flip_id,
    });
}

// Admin function to withdraw house profits
public entry fun withdraw_profits(
    admin: &signer,
    amount: u64,
) acquires GameState {
    let admin_addr = signer::address_of(admin);
    let game_addr = @game; // Replace with your module address
    let game_state = borrow_global_mut<GameState>(game_addr);

    // Only admin can withdraw
    assert!(admin_addr == game_state.admin, error::permission_denied(1));

    // Validate amount
    let balance = coin::value(&game_state.vault);
    assert!(amount <= balance, error::invalid_argument(1));

    // Withdraw profits
    let profits = coin::extract(&mut game_state.vault, amount);
    coin::deposit(admin_addr, profits);
}

// Helper function to calculate payout with house edge
fun calculate_payout(bet_amount: u64): u64 {
    let payout = (bet_amount * (10000 - HOUSE_EDGE_BASIS_POINTS)) / 10000;
    payout * 2 // Double the bet (minus house edge)
}

// Helper function to generate random result
fun generate_random_result(): bool {
    // In a real implementation, use a secure random number generator
    // This is a simplified version for demonstration
    let timestamp = timestamp::now_seconds();
    (timestamp % 2) == 0
}

// View functions to query game state
public fun get_flip_count(player_addr: address): u64 acquires GameState {
    let game_addr = @game; // Replace with your module address
    let game_state = borrow_global<GameState>(game_addr);
    
    if (table::contains(&game_state.flips, player_addr)) {
        *table::borrow(&game_state.flips, player_addr)
    } else {
        0
    }
}

public fun get_stats(stat_id: u64): u64 acquires GameState {
    let game_addr = @game; // Replace with your module address
    let game_state = borrow_global<GameState>(game_addr);
    assert!(stat_id <= 4, error::invalid_argument(1));
    *table::borrow(&game_state.stats, stat_id)
}

public fun get_vault_balance(): u64 acquires GameState {
    let game_addr = @game; // Replace with your module address
    let game_state = borrow_global<GameState>(game_addr);
    coin::value(&game_state.vault)
}

// Error codes
module error {
    const E_INVALID_BET_AMOUNT: u64 = 1;
    const E_PERMISSION_DENIED: u64 = 2;
    const E_INVALID_STAT_ID: u64 = 3;
}
```
