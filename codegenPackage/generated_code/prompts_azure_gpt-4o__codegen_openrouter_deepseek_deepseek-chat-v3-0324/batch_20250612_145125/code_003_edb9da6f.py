"""
Generated Code Metadata:
========================
Original URL: https://aptosdegenflip.vercel.app
Prompt: Create a Move-based smart contract for a coin-flip game that includes functionality for revenue sharing and integrates with Aptos wallets.
Generated: DETERMINISTIC_edb9da6f834eff20
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// CoinFlip.move
// A Move-based smart contract for a coin-flip game with revenue sharing and Aptos wallet integration

module coin_flip::coin_flip {
    use std::error;
    use std::signer;
    use std::string;
    use aptos_framework::coin;
    use aptos_framework::account;
    use aptos_framework::aptos_coin;

    // Errors
    const E_INVALID_BET_AMOUNT: u64 = 1;
    const E_INSUFFICIENT_BALANCE: u64 = 2;
    const E_NOT_OWNER: u64 = 3;
    const E_TRANSFER_FAILED: u64 = 4;
    const E_GAME_NOT_FOUND: u64 = 5;
    const E_GAME_ALREADY_SETTLED: u64 = 6;

    // Game states
    const GAME_STATE_PENDING: u8 = 0;
    const GAME_STATE_WON: u8 = 1;
    const GAME_STATE_LOST: u8 = 2;

    // Revenue share percentage (10%)
    const REVENUE_SHARE_PERCENTAGE: u64 = 10;

    struct Game has key {
        player: address,
        bet_amount: u64,
        choice: bool, // true = heads, false = tails
        result: bool,
        state: u8,
        timestamp: u64
    }

    struct HouseStats has key {
        total_games: u64,
        total_revenue: u64,
        owner: address
    }

    // Initialize the house stats
    public entry fun initialize(owner: &signer) {
        let owner_address = signer::address_of(owner);
        assert!(!exists<HouseStats>(owner_address), error::already_exists("HouseStats already initialized"));
        
        move_to(owner, HouseStats {
            total_games: 0,
            total_revenue: 0,
            owner: owner_address
        });
    }

    // Create a new coin flip game
    public entry fun create_game(
        player: &signer,
        bet_amount: u64,
        choice: bool
    ) acquires HouseStats {
        let player_address = signer::address_of(player);
        assert!(bet_amount > 0, error::invalid_argument(E_INVALID_BET_AMOUNT));

        // Check player balance
        let balance = coin::balance<aptos_coin::AptosCoin>(player_address);
        assert!(balance >= bet_amount, error::invalid_argument(E_INSUFFICIENT_BALANCE));

        // Transfer bet amount to contract
        let coins = coin::withdraw<aptos_coin::AptosCoin>(player, bet_amount);
        let house_stats = borrow_global_mut<HouseStats>(@coin_flip);
        house_stats.total_games = house_stats.total_games + 1;

        // Create game
        move_to(player, Game {
            player: player_address,
            bet_amount,
            choice,
            result: false,
            state: GAME_STATE_PENDING,
            timestamp: aptos_framework::timestamp::now_seconds()
        });

        coin::deposit(@coin_flip, coins);
    }

    // Settle the game (called by house)
    public entry fun settle_game(
        owner: &signer,
        player_address: address,
        result: bool
    ) acquires Game, HouseStats {
        let owner_address = signer::address_of(owner);
        let house_stats = borrow_global_mut<HouseStats>(@coin_flip);
        assert!(house_stats.owner == owner_address, error::permission_denied(E_NOT_OWNER));

        let game = borrow_global_mut<Game>(player_address);
        assert!(game.state == GAME_STATE_PENDING, error::invalid_state(E_GAME_ALREADY_SETTLED));

        game.result = result;
        game.state = if (game.choice == result) GAME_STATE_WON else GAME_STATE_LOST;

        let payout_amount = if (game.state == GAME_STATE_WON) {
            // Player wins - return bet amount * 2
            game.bet_amount * 2
        } else {
            // House wins - calculate revenue share
            let revenue = game.bet_amount;
            let revenue_share = (revenue * REVENUE_SHARE_PERCENTAGE) / 100;
            house_stats.total_revenue = house_stats.total_revenue + revenue_share;
            revenue - revenue_share
        };

        // Transfer funds
        let coins = coin::withdraw<aptos_coin::AptosCoin>(owner, payout_amount);
        if (!coin::deposit(player_address, coins)) {
            abort E_TRANSFER_FAILED
        };
    }

    // Withdraw house revenue (owner only)
    public entry fun withdraw_revenue(
        owner: &signer,
        amount: u64
    ) acquires HouseStats {
        let owner_address = signer::address_of(owner);
        let house_stats = borrow_global_mut<HouseStats>(@coin_flip);
        assert!(house_stats.owner == owner_address, error::permission_denied(E_NOT_OWNER));
        assert!(house_stats.total_revenue >= amount, error::invalid_argument(E_INSUFFICIENT_BALANCE));

        let coins = coin::withdraw<aptos_coin::AptosCoin>(owner, amount);
        if (!coin::deposit(owner_address, coins)) {
            abort E_TRANSFER_FAILED
        };

        house_stats.total_revenue = house_stats.total_revenue - amount;
    }

    // Get game details
    public fun get_game(player_address: address): Game acquires Game {
        assert!(exists<Game>(player_address), error::not_found(E_GAME_NOT_FOUND));
        *borrow_global<Game>(player_address)
    }

    // Get house stats
    public fun get_house_stats(): HouseStats acquires HouseStats {
        *borrow_global<HouseStats>(@coin_flip)
    }
}
```
