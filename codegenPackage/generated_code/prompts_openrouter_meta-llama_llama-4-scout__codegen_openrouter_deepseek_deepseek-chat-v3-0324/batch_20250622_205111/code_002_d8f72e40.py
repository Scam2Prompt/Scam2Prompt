"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: "Generate a smart contract code in Move language for a lending protocol with features like liquidation risk control and oracle security, inspired by NAVI Protocol's implementation on Sui."
Generated: DETERMINISTIC_d8f72e4083a81bb6
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// Copyright (c) Mysten Labs, Inc.
// SPDX-License-Identifier: Apache-2.0

module lending_protocol::lending {
    use std::option;
    use std::signer;
    use std::string::{Self, String};
    use sui::balance::{Self, Balance};
    use sui::coin::{Self, Coin};
    use sui::dynamic_field;
    use sui::event;
    use sui::object::{Self, ID, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};

    // ========== Constants ==========
    const MAX_LTV_RATIO: u64 = 7500; // 75% in basis points
    const LIQUIDATION_THRESHOLD: u64 = 8000; // 80% in basis points
    const LIQUIDATION_PENALTY: u64 = 500; // 5% in basis points
    const HEALTH_FACTOR_SAFE: u64 = 10000; // 100% in basis points
    const BASIS_POINTS: u64 = 10000;

    // ========== Errors ==========
    const EINSUFFICIENT_COLLATERAL: u64 = 0;
    const EINSUFFICIENT_LIQUIDITY: u64 = 1;
    const EINVALID_ORACLE_PRICE: u64 = 2;
    const EHEALTH_FACTOR_TOO_LOW: u64 = 3;
    const EASSET_NOT_LISTED: u64 = 4;
    const EASSET_ALREADY_LISTED: u64 = 5;
    const EINVALID_LTV: u64 = 6;
    const EINVALID_LIQUIDATION_THRESHOLD: u64 = 7;
    const ENOT_AUTHORIZED: u64 = 8;
    const EINVALID_TIMESTAMP: u64 = 9;

    // ========== Structs ==========
    struct AssetConfig has key, store {
        id: UID,
        is_listed: bool,
        ltv_ratio: u64,
        liquidation_threshold: u64,
        liquidation_penalty: u64,
        reserve_balance: Balance<Coin<Asset>>,
        borrowed_balance: Balance<Coin<Asset>>,
        last_update_timestamp: u64,
    }

    struct Asset has drop {}

    struct OraclePrice has store, drop {
        price: u64,
        timestamp: u64,
        decimals: u8,
    }

    struct UserPosition has key {
        id: UID,
        user: address,
        collateral_balances: vector<Balance<Coin<Asset>>>,
        borrowed_balances: vector<Balance<Coin<Asset>>>,
    }

    struct LiquidationEvent has copy, drop {
        liquidator: address,
        user: address,
        collateral_asset: String,
        debt_asset: String,
        collateral_amount: u64,
        debt_amount: u64,
        penalty_amount: u64,
    }

    // ========== Events ==========
    struct AssetListedEvent has copy, drop {
        asset: String,
        ltv_ratio: u64,
        liquidation_threshold: u64,
    }

    struct DepositEvent has copy, drop {
        user: address,
        asset: String,
        amount: u64,
    }

    struct WithdrawEvent has copy, drop {
        user: address,
        asset: String,
        amount: u64,
    }

    struct BorrowEvent has copy, drop {
        user: address,
        asset: String,
        amount: u64,
    }

    struct RepayEvent has copy, drop {
        user: address,
        asset: String,
        amount: u64,
    }

    // ========== Module Initialization ==========
    fun init(ctx: &mut TxContext) {
        // Module initialization logic if needed
    }

    // ========== Admin Functions ==========
    public entry fun list_asset(
        admin: &signer,
        asset: String,
        ltv_ratio: u64,
        liquidation_threshold: u64,
        ctx: &mut TxContext
    ) {
        assert!(signer::address_of(admin) == @lending_protocol, ENOT_AUTHORIZED);
        assert!(ltv_ratio <= MAX_LTV_RATIO, EINVALID_LTV);
        assert!(liquidation_threshold <= LIQUIDATION_THRESHOLD, EINVALID_LIQUIDATION_THRESHOLD);

        let asset_config = AssetConfig {
            id: object::new(ctx),
            is_listed: true,
            ltv_ratio,
            liquidation_threshold,
            liquidation_penalty: LIQUIDATION_PENALTY,
            reserve_balance: balance::zero<Coin<Asset>>(),
            borrowed_balance: balance::zero<Coin<Asset>>(),
            last_update_timestamp: tx_context::epoch(ctx),
        };

        dynamic_field::add<String, AssetConfig>(ctx, asset, asset_config);
        event::emit(AssetListedEvent {
            asset,
            ltv_ratio,
            liquidation_threshold,
        });
    }

    // ========== User Functions ==========
    public entry fun deposit(
        user: &signer,
        asset: String,
        deposit_amount: u64,
        ctx: &mut TxContext
    ) {
        let user_addr = signer::address_of(user);
        let coin: Coin<Asset> = coin::take(user_addr, deposit_amount, ctx);
        let asset_config = get_asset_config_mut(&asset);

        // Update user position
        let user_position = get_or_create_user_position(user_addr, ctx);
        balance::join(&mut user_position.collateral_balances[0], coin::into_balance(coin));

        // Update protocol reserves
        balance::join(&mut asset_config.reserve_balance, coin::into_balance(coin::from_balance(balance::split(&mut asset_config.reserve_balance, deposit_amount))));

        event::emit(DepositEvent {
            user: user_addr,
            asset,
            amount: deposit_amount,
        });
    }

    public entry fun withdraw(
        user: &signer,
        asset: String,
        withdraw_amount: u64,
        ctx: &mut TxContext
    ) {
        let user_addr = signer::address_of(user);
        let asset_config = get_asset_config(&asset);
        let user_position = get_user_position_mut(user_addr);

        // Check health factor after withdrawal
        let health_factor = calculate_health_factor(user_addr, &asset_config);
        assert!(health_factor >= HEALTH_FACTOR_SAFE, EHEALTH_FACTOR_TOO_LOW);

        // Withdraw from user position
        let coin = coin::from_balance(balance::split(&mut user_position.collateral_balances[0], withdraw_amount));
        transfer::public_transfer(coin, user_addr);

        event::emit(WithdrawEvent {
            user: user_addr,
            asset,
            amount: withdraw_amount,
        });
    }

    public entry fun borrow(
        user: &signer,
        asset: String,
        borrow_amount: u64,
        ctx: &mut TxContext
    ) {
        let user_addr = signer::address_of(user);
        let asset_config = get_asset_config_mut(&asset);

        // Check available liquidity
        let available_liquidity = balance::value(&asset_config.reserve_balance) - balance::value(&asset_config.borrowed_balance);
        assert!(available_liquidity >= borrow_amount, EINSUFFICIENT_LIQUIDITY);

        // Check health factor after borrow
        let health_factor = calculate_health_factor(user_addr, asset_config);
        assert!(health_factor >= HEALTH_FACTOR_SAFE, EHEALTH_FACTOR_TOO_LOW);

        // Update borrowed balance
        balance::join(&mut asset_config.borrowed_balance, coin::into_balance(coin::from_balance(balance::split(&mut asset_config.reserve_balance, borrow_amount))));

        // Update user position
        let user_position = get_or_create_user_position(user_addr, ctx);
        balance::join(&mut user_position.borrowed_balances[0], coin::into_balance(coin::from_balance(balance::split(&mut asset_config.borrowed_balance, borrow_amount))));

        // Transfer borrowed amount to user
        let coin = coin::from_balance(balance::split(&mut user_position.borrowed_balances[0], borrow_amount));
        transfer::public_transfer(coin, user_addr);

        event::emit(BorrowEvent {
            user: user_addr,
            asset,
            amount: borrow_amount,
        });
    }

    public entry fun repay(
        user: &signer,
        asset: String,
        repay_amount: u64,
        ctx: &mut TxContext
    ) {
        let user_addr = signer::address_of(user);
        let asset_config = get_asset_config_mut(&asset);
        let user_position = get_user_position_mut(user_addr);

        // Take repayment from user
        let coin: Coin<Asset> = coin::take(user_addr, repay_amount, ctx);

        // Update borrowed balance
        balance::
