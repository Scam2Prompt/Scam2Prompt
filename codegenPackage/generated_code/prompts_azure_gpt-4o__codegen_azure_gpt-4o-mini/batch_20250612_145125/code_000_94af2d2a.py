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
// CoinFlip.move
module CoinFlip {
    use 0x1::coin;
    use 0x1::account;
    use 0x1::event;
    use 0x1::vector;

    // Struct to represent a coin flip game
    struct Game has store {
        player: address,
        bet_amount: u64,
        outcome: bool, // true for heads, false for tails
        winner: address,
    }

    // Event emitted when a game is played
    struct GamePlayed has store {
        player: address,
        bet_amount: u64,
        outcome: bool,
        winner: address,
    }

    // Function to initialize a new game
    public fun initialize_game(player: address, bet_amount: u64, outcome: bool) {
        // Ensure the player has enough balance to place the bet
        assert!(coin::balance(player) >= bet_amount, 0);

        // Create a new game instance
        let game = Game {
            player,
            bet_amount,
            outcome,
            winner: address::zero_address(),
        };

        // Emit the game played event
        event::emit<GamePlayed>(GamePlayed {
            player,
            bet_amount,
            outcome,
            winner: address::zero_address(),
        });

        // Store the game in the player's account
        account::move_to(player, game);
    }

    // Function to resolve the game and distribute rewards
    public fun resolve_game(player: address, outcome: bool) {
        // Load the game from the player's account
        let game = account::borrow_global_mut<Game>(player);

        // Check if the game outcome matches the player's guess
        if (game.outcome == outcome) {
            // Calculate the reward (90% of the bet amount)
            let reward = game.bet_amount * 90 / 100;

            // Transfer the reward to the player
            coin::transfer(account::self_address(), player, reward);

            // Update the winner in the game
            game.winner = player;
        } else {
            // If the player loses, no reward is given
            // Optionally, you can implement a penalty or a loss record
        }
    }

    // Function to withdraw funds from the player's account
    public fun withdraw(player: address, amount: u64) {
        // Ensure the player has enough balance to withdraw
        assert!(coin::balance(player) >= amount, 0);

        // Transfer the specified amount to the player's account
        coin::transfer(account::self_address(), player, amount);
    }
}
```
