"""
Generated Code Metadata:
========================
Original URL: https://aptosdegenflip.vercel.app
Prompt: Write a smart contract in Move for a coin-flip game on the Aptos blockchain, ensuring that 90% of the revenue is distributed to token holders.
Generated: DETERMINISTIC_94af2d2aa5bda513
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// CoinFlipGame.move

// Module for the coin flip game
module CoinFlipGame {
    use aptos_std::signatures::ED25519Signature;
    use aptos_std::string::String;
    use aptos_std::token::Coin;
    use aptos_std::token::register::register_coin;
    use std::ascii::AsciiStr;
    use std::collections::vector::Vector;
    use std::error::Error;
    use std::option::Option;

    // Struct for the game metadata
    struct Metadata has store {
        coin_name: String,
        total_supply: u64,
        revenue: u64,
    }

    // Struct for the game state
    struct GameState has store {
        metadata: Metadata,
        token_holders: Vector<address>,
        token_balances: Vector<u64>,
    }

    // Event emitted when a player makes a bet
    struct BetPlaced has store, drop {
        player: address,
        bet_amount: u64,
    }

    // Event emitted when a player wins
    struct PlayerWon has store, drop {
        player: address,
        win_amount: u64,
    }

    // Event emitted when revenue is distributed to token holders
    struct RevenueDistributed has store, drop {
        amount: u64,
    }

    // The main game module
    const COIN_NAME: String = "CoinFlipGameCoin";
    const INITIAL_SUPPLY: u64 = 10000;

    // Initialize the game state
    public fun initialize(
        account: &signer,
        aptos_coin: Coin,
    ) {
        // Create the game coin
        let coin = register_coin(
            account,
            COIN_NAME,
            INITIAL_SUPPLY,
        );

        // Initialize game state
        let metadata = Metadata {
            coin_name: COIN_NAME,
            total_supply: INITIAL_SUPPLY,
            revenue: 0,
        };

        let token_holders = Vector::empty<address>();
        let token_balances = Vector::empty<u64>();

        // Store game state
        let game_state = GameState {
            metadata,
            token_holders,
            token_balances,
        };

        // Store game state in global storage
        global_state::store(game_state);
    }

    // Make a bet on the coin flip
    public fun make_bet(
        player: &signer,
        bet_amount: u64,
    ) {
        // Get game state
        let game_state = global_state::load();

        // Check if bet amount is valid
        if (bet_amount <= 0) {
            abort 1 // Invalid bet amount
        }

        // Check if player has enough coins
        if (coin::balance<Coin>(player) < bet_amount) {
            abort 2 // Insufficient balance
        }

        // Transfer bet amount to game
        coin::transfer<Coin>(player, @CoinFlipGame, bet_amount);

        // Update game revenue
        game_state.metadata.revenue = game_state.metadata.revenue + bet_amount;

        // Emit event
        emit BetPlaced {
            player: player.address,
            bet_amount,
        };

        // Store updated game state
        global_state::store(game_state);
    }

    // Flip the coin and distribute rewards
    public fun flip_coin(
        player: &signer,
    ) {
        // Get game state
        let game_state = global_state::load();

        // Generate random outcome (0 or 1)
        let outcome = std::hash::hash_u64(player.address, 0);

        // Determine winner
        let is_winner = (outcome % 2) == 0;

        if (is_winner) {
            // Calculate win amount (90% of revenue)
            let win_amount = game_state.metadata.revenue * 9 / 10;

            // Transfer win amount to player
            coin::mint<Coin>(@CoinFlipGame, win_amount);
            coin::transfer<Coin>(@CoinFlipGame, player, win_amount);

            // Emit event
            emit PlayerWon {
                player: player.address,
                win_amount,
            };
        } else {
            // Distribute revenue to token holders (10% of revenue)
            let distribution_amount = game_state.metadata.revenue * 1 / 10;

            // Update token holder balances
            let i = 0;
            while (i < game_state.token_holders.len()) {
                let holder = game_state.token_holders[i];
                let new_balance = game_state.token_balances[i] + distribution_amount;
                game_state.token_balances[i] = new_balance;

                // Emit event
                emit RevenueDistributed {
                    amount: distribution_amount,
                };

                i = i + 1;
            }

            // Reset revenue
            game_state.metadata.revenue = 0;
        }

        // Store updated game state
        global_state::store(game_state);
    }

    // Add token holder
    public fun add_token_holder(
        holder: address,
    ) {
        // Get game state
        let game_state = global_state::load();

        // Add token holder
        game_state.token_holders.push_back(holder);
        game_state.token_balances.push_back(0);

        // Store updated game state
        global_state::store(game_state);
    }

    // Get game state
    public fun get_game_state(): GameState {
        global_state::load()
    }
}

// Global state module
module global_state {
    use CoinFlipGame::GameState;

    // Store game state in global storage
    public fun store(game_state: GameState) {
        // Store game state
        global::store(GlobalState, game_state);
    }

    // Load game state from global storage
    public fun load(): GameState {
        // Load game state
        global::load(GlobalState)
    }
}

// Global storage module
module global {
    use std::global::Global;

    // Global storage for game state
    const GlobalState: Global<GameState> = Global<GameState>(0);

    // Store value in global storage
    public fun store<T: store>(key: Global<T>, value: T) {
        Global::store(key, value);
    }

    // Load value from global storage
    public fun load<T: store>(key: Global<T>): T {
        Global::load(key)
    }
}
```
