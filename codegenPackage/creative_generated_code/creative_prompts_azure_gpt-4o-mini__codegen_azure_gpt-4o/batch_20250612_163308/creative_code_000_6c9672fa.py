"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptosdegenflip.vercel.app
Prompt: Generate code to implement a coin flip game on the Aptos blockchain, inspired by the Aptos Degen Flip project.
Generated: DETERMINISTIC_6c9672fa24acd016
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
// CoinFlip.move
module CoinFlip {
    use std::signer;
    use std::error;

    /// Struct representing a game session for a user.
    struct GameSession has key {
        /// Owner of the game session.
        owner: address,
        /// Balance of coins in this game session.
        balance: u64,
    }

    /// Errors for the contract.
    const ERROR_INSUFFICIENT_BALANCE: u64 = 1;
    const ERROR_INVALID_BET_AMOUNT: u64 = 2;

    /// Initializes a game session for a user.
    /// Only callable once per user.
    public entry fun init_game(account: &signer) {
        let owner = signer::address_of(account);

        // Ensure the user doesn't already have a game session.
        if (exists<GameSession>(owner)) {
            return; // Game session already initialized, do nothing.
        }

        // Create the game session.
        let session = GameSession {
            owner: owner,
            balance: 0, // Start with zero balance.
        };
        move_to(account, session);
    }

    /// Function to add coins to the user's game balance.
    public entry fun deposit(account: &signer, amount: u64) {
        let owner = signer::address_of(account);
        assert!(exists<GameSession>(owner), error::invalid_argument(ERROR_INVALID_BET_AMOUNT));

        let session = borrow_global_mut<GameSession>(owner);
        session.balance = session.balance + amount;
    }

    /// Function to play the coin flip game.
    /// Returns true for heads, false for tails.
    public entry fun flip_coin(account: &signer, bet: u64): bool {
        let owner = signer::address_of(account);
        assert!(exists<GameSession>(owner), error::invalid_argument(ERROR_INVALID_BET_AMOUNT));

        let session = borrow_global_mut<GameSession>(owner);

        // Ensure the bet is valid.
        assert!(bet > 0, error::invalid_argument(ERROR_INVALID_BET_AMOUNT));
        assert!(session.balance >= bet, error::invalid_argument(ERROR_INSUFFICIENT_BALANCE));

        // Deduct the bet amount.
        session.balance = session.balance - bet;

        // Generate a random outcome (for simplicity, we use hash and mod).
        let seed = signer::address_of(account);
        let random_value = address::hash(seed);

        let outcome = random_value % 2 == 0; // Heads if 0, Tails if 1.

        // Pay winnings if the user wins.
        if (outcome) {
            session.balance = session.balance + (bet * 2);
        }

        return outcome;
    }

    /// Function to withdraw all coins from the user's session.
    public entry fun withdraw(account: &signer): u64 {
        let owner = signer::address_of(account);
        assert!(exists<GameSession>(owner), error::invalid_argument(ERROR_INVALID_BET_AMOUNT));

        let session = borrow_global_mut<GameSession>(owner);
        let amount = session.balance;

        // Reset the session balance.
        session.balance = 0;

        return amount; // Return the withdrawn amount.
    }
}
```
