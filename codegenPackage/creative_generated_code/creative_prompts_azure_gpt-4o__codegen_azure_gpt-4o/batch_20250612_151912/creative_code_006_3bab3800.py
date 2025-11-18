"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eosgas.io
Prompt: Develop a smart contract that allows coin holders to loan or stake their tokens quarterly, representing electricity available for miners, as per eosGAS's staking mechanism.
Generated: DETERMINISTIC_3bab38002b1ad462
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-structured EOSIO smart contract written in C++ for the requested functionality. This contract allows users to stake or loan tokens quarterly, aligning with a mechanism like eosGAS.

```cpp
// SPDX-License-Identifier: MIT
#include <eosio/eosio.hpp>
#include <eosio/asset.hpp>
#include <eosio/system.hpp>

using namespace eosio;

class [[eosio::contract("staking_contract")]] staking_contract : public contract {
public:
    using contract::contract;

    // Constructor
    staking_contract(name receiver, name code, datastream<const char*> ds)
        : contract(receiver, code, ds) {}

    // Action to stake tokens
    [[eosio::action]]
    void stake(name user, asset quantity) {
        require_auth(user);

        // Ensure the quantity is valid
        check(quantity.amount > 0, "Stake amount must be positive");
        check(quantity.symbol == core_symbol, "Only core tokens are allowed to stake");

        // Subtract tokens from the user
        sub_balance(user, quantity);

        // Add tokens to the stake table
        stakes_table stakes(get_self(), get_self().value);
        auto itr = stakes.find(user.value);
        if (itr == stakes.end()) {
            stakes.emplace(user, [&](auto& row) {
                row.user = user;
                row.staked = quantity;
                row.last_stake_time = current_time_point();
            });
        } else {
            stakes.modify(itr, same_payer, [&](auto& row) {
                row.staked += quantity;
                row.last_stake_time = current_time_point();
            });
        }
    }

    // Action to unstake tokens
    [[eosio::action]]
    void unstake(name user, asset quantity) {
        require_auth(user);

        // Ensure the quantity is valid
        check(quantity.amount > 0, "Unstake amount must be positive");
        check(quantity.symbol == core_symbol, "Token symbol mismatch");

        // Modify the stake table
        stakes_table stakes(get_self(), get_self().value);
        auto itr = stakes.find(user.value);
        check(itr != stakes.end(), "No staked balance found for user");
        check(itr->staked >= quantity, "Insufficient staked balance");

        // Ensure the minimum staking period has elapsed (90 days)
        auto now = current_time_point();
        auto elapsed = now - itr->last_stake_time;
        check(elapsed.count() >= 90 * 24 * 60 * 60 * 1000000, "Tokens cannot be unstaked before 90 days");

        stakes.modify(itr, same_payer, [&](auto& row) {
            row.staked -= quantity;
        });

        // Add tokens back to the user
        add_balance(user, quantity, get_self());
    }

    // Action to claim rewards
    [[eosio::action]]
    void claim(name user) {
        require_auth(user);

        stakes_table stakes(get_self(), get_self().value);
        auto itr = stakes.find(user.value);
        check(itr != stakes.end(), "No staked balance found for user");

        // Calculate rewards based on staked balance and time elapsed
        auto now = current_time_point();
        auto elapsed = now - itr->last_stake_time;

        // Rewards formula: 1% reward per 90-day period
        int64_t reward_factor = elapsed.count() / (90 * 24 * 60 * 60 * 1000000);
        asset reward = itr->staked * reward_factor / 100;

        // Ensure rewards are non-zero
        check(reward.amount > 0, "No rewards available to claim");

        // Reset the staking time
        stakes.modify(itr, same_payer, [&](auto& row) {
            row.last_stake_time = now;
        });

        // Transfer rewards to the user
        add_balance(user, reward, get_self());
    }

private:
    // Table to store staking data
    struct [[eosio::table]] stake_info {
        name user;
        asset staked;
        time_point last_stake_time;

        uint64_t primary_key() const { return user.value; }
    };

    typedef multi_index<"stakes"_n, stake_info> stakes_table;

    // Core token symbol
    static constexpr symbol core_symbol = symbol("EOS", 4);

    // Helper function to subtract balance
    void sub_balance(name user, asset value) {
        accounts_table accounts(get_self(), user.value);
        auto itr = accounts.find(value.symbol.code().raw());
        check(itr != accounts.end(), "No balance object found");
        check(itr->balance >= value, "Overdrawn balance");

        if (itr->balance == value) {
            accounts.erase(itr);
        } else {
            accounts.modify(itr, same_payer, [&](auto& row) {
                row.balance -= value;
            });
        }
    }

    // Helper function to add balance
    void add_balance(name user, asset value, name ram_payer) {
        accounts_table accounts(get_self(), user.value);
        auto itr = accounts.find(value.symbol.code().raw());
        if (itr == accounts.end()) {
            accounts.emplace(ram_payer, [&](auto& row) {
                row.balance = value;
            });
        } else {
            accounts.modify(itr, same_payer, [&](auto& row) {
                row.balance += value;
            });
        }
    }

    // Table to track token balances
    struct [[eosio::table]] account {
        asset balance;

        uint64_t primary_key() const { return balance.symbol.code().raw(); }
    };

    typedef multi_index<"accounts"_n, account> accounts_table;
};

```

This code defines a staking mechanism that allows users to stake, unstake, and claim rewards on a quarterly basis, including proper error handling and best practices.
