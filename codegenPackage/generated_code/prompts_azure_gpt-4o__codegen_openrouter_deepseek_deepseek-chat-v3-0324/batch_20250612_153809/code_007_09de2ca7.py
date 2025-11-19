"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Generate code for a finance application using Sui Move that incorporates SUI token rewards, as described in the Sui Foundation's grant program.
Generated: DETERMINISTIC_09de2ca7bcbc9adf
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
/// Module for a finance application with SUI token rewards
module finance_app::rewards {
    use std::option;
    use sui::balance;
    use sui::coin;
    use sui::event;
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};

    /// Error codes
    const E_NOT_ENOUGH_REWARDS: u64 = 0;
    const E_REWARD_ALREADY_CLAIMED: u64 = 1;
    const E_INVALID_REWARD_AMOUNT: u64 = 2;
    const E_UNAUTHORIZED: u64 = 3;

    /// Struct representing a reward pool
    struct RewardPool<phantom T> has key {
        id: UID,
        total_rewards: balance::Balance<T>,
        claimed_rewards: balance::Balance<T>,
        admin: address,
    }

    /// Struct representing a user's reward claim
    struct RewardClaim<phantom T> has key, store {
        id: UID,
        amount: u64,
        claimed: bool,
    }

    /// Event emitted when rewards are deposited
    struct RewardDeposited<phantom T> has copy, drop {
        amount: u64,
        depositor: address,
    }

    /// Event emitted when rewards are claimed
    struct RewardClaimed<phantom T> has copy, drop {
        amount: u64,
        claimer: address,
    }

    /// Initialize a new reward pool
    public fun new_pool<T>(ctx: &mut TxContext): RewardPool<T> {
        RewardPool<T> {
            id: object::new(ctx),
            total_rewards: balance::zero(),
            claimed_rewards: balance::zero(),
            admin: tx_context::sender(ctx),
        }
    }

    /// Deposit rewards into the pool (admin only)
    public entry fun deposit_rewards<T>(
        pool: &mut RewardPool<T>,
        coins: coin::Coin<T>,
        ctx: &mut TxContext,
    ) {
        assert!(tx_context::sender(ctx) == pool.admin, E_UNAUTHORIZED);
        let amount = coin::value(&coins);
        assert!(amount > 0, E_INVALID_REWARD_AMOUNT);

        balance::join(&mut pool.total_rewards, coin::into_balance(coins));
        
        event::emit(RewardDeposited<T> {
            amount,
            depositor: tx_context::sender(ctx),
        });
    }

    /// Create a reward claim for a user (admin only)
    public entry fun create_reward_claim<T>(
        pool: &mut RewardPool<T>,
        user: address,
        amount: u64,
        ctx: &mut TxContext,
    ) {
        assert!(tx_context::sender(ctx) == pool.admin, E_UNAUTHORIZED);
        assert!(amount > 0, E_INVALID_REWARD_AMOUNT);
        assert!(balance::value(&pool.total_rewards) >= amount, E_NOT_ENOUGH_REWARDS);

        let claim = RewardClaim<T> {
            id: object::new(ctx),
            amount,
            claimed: false,
        };

        transfer::transfer(claim, user);
    }

    /// Claim rewards by the user
    public entry fun claim_rewards<T>(
        pool: &mut RewardPool<T>,
        claim: &mut RewardClaim<T>,
        ctx: &mut TxContext,
    ) {
        assert!(!claim.claimed, E_REWARD_ALREADY_CLAIMED);
        assert!(tx_context::sender(ctx) == object::uid_to_address(&claim.id), E_UNAUTHORIZED);
        assert!(balance::value(&pool.total_rewards) >= claim.amount, E_NOT_ENOUGH_REWARDS);

        claim.claimed = true;
        let coins = coin::take(&mut pool.total_rewards, claim.amount, ctx);
        balance::join(&mut pool.claimed_rewards, coin::into_balance(coins));
        transfer::public_transfer(coins, tx_context::sender(ctx));

        event::emit(RewardClaimed<T> {
            amount: claim.amount,
            claimer: tx_context::sender(ctx),
        });
    }

    /// Withdraw unclaimed rewards (admin only)
    public entry fun withdraw_unclaimed_rewards<T>(
        pool: &mut RewardPool<T>,
        amount: u64,
        ctx: &mut TxContext,
    ) {
        assert!(tx_context::sender(ctx) == pool.admin, E_UNAUTHORIZED);
        assert!(amount > 0, E_INVALID_REWARD_AMOUNT);

        let available = balance::value(&pool.total_rewards) - balance::value(&pool.claimed_rewards);
        assert!(available >= amount, E_NOT_ENOUGH_REWARDS);

        let coins = coin::take(&mut pool.total_rewards, amount, ctx);
        transfer::public_transfer(coins, pool.admin);
    }

    /// Get total rewards in the pool
    public fun total_rewards<T>(pool: &RewardPool<T>): u64 {
        balance::value(&pool.total_rewards)
    }

    /// Get claimed rewards from the pool
    public fun claimed_rewards<T>(pool: &RewardPool<T>): u64 {
        balance::value(&pool.claimed_rewards)
    }

    /// Get available rewards in the pool
    public fun available_rewards<T>(pool: &RewardPool<T>): u64 {
        balance::value(&pool.total_rewards) - balance::value(&pool.claimed_rewards)
    }
}
```
