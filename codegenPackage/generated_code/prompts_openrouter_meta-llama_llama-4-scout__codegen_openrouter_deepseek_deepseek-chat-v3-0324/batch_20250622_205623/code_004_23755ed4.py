"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: Design a smart contract on Aptos that utilizes Pyth Network's price feeds to update a decentralized application's (dApp) state based on real-time market data.
Generated: DETERMINISTIC_23755ed4963836eb
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Smart contract utilizing Pyth Network price feeds on Aptos
//! to update dApp state based on real-time market data.

use aptos_framework::coin;
use aptos_std::type_info;
use pyth_sdk::price_feed::{PriceFeed, PriceIdentifier};
use pyth_sdk::price_update::PriceUpdate;
use std::string::String;

/// Module containing the dApp state and related functions
module dapp_owner::price_oracle {
    use aptos_framework::event;
    use aptos_std::error;
    use std::string::utf8;

    // Import Pyth SDK types
    use pyth_sdk::price_feed::{Self, PriceFeed, PriceIdentifier};
    use pyth_sdk::price_update::PriceUpdate;

    /// Errors that can occur in the price oracle
    const E_INVALID_PRICE_FEED: u64 = 1;
    const E_PRICE_STALE: u64 = 2;
    const E_PRICE_NEGATIVE: u64 = 3;
    const E_UNAUTHORIZED: u64 = 4;

    /// Struct representing the price oracle state
    struct PriceOracle has key {
        // Mapping from price feed ID to latest price
        prices: table::Table<PriceIdentifier, PriceFeed>,
        // Admin address with permission to update prices
        admin: address,
        // Event handle for price updates
        price_update_events: event::EventHandle<PriceUpdateEvent>,
    }

    /// Event emitted when a price is updated
    struct PriceUpdateEvent has drop, store {
        price_id: PriceIdentifier,
        price: u64,
        timestamp: u64,
    }

    /// Initialize the price oracle with an admin address
    public entry fun initialize(admin: &signer) {
        let admin_address = signer::address_of(admin);
        assert!(
            !exists<PriceOracle>(admin_address),
            error::already_exists(E_INVALID_PRICE_FEED)
        );

        move_to(
            admin,
            PriceOracle {
                prices: table::new(),
                admin: admin_address,
                price_update_events: event::new_event_handle<PriceUpdateEvent>(admin),
            },
        );
    }

    /// Update price feed with new data from Pyth Network
    public entry fun update_price(
        oracle: &signer,
        price_id: PriceIdentifier,
        price_update: PriceUpdate,
    ) {
        let oracle_addr = signer::address_of(oracle);
        assert!(
            exists<PriceOracle>(oracle_addr),
            error::not_found(E_INVALID_PRICE_FEED)
        );

        let oracle_state = borrow_global_mut<PriceOracle>(oracle_addr);
        assert!(
            oracle_state.admin == oracle_addr,
            error::permission_denied(E_UNAUTHORIZED)
        );

        // Validate the price update
        let price_feed = price_update.to_price_feed();
        assert!(
            price_feed.get_price_unchecked().price >= 0,
            error::invalid_argument(E_PRICE_NEGATIVE)
        );
        assert!(
            !price_feed.is_stale(aptos_std::timestamp::now_seconds()),
            error::invalid_argument(E_PRICE_STALE)
        );

        // Update the price feed
        if (table::contains(&oracle_state.prices, price_id)) {
            let old_feed = table::borrow_mut(&mut oracle_state.prices, price_id);
            *old_feed = price_feed;
        } else {
            table::add(&mut oracle_state.prices, price_id, price_feed);
        }

        // Emit price update event
        let current_price = price_feed.get_price_unchecked().price as u64;
        event::emit_event(
            &mut oracle_state.price_update_events,
            PriceUpdateEvent {
                price_id,
                price: current_price,
                timestamp: aptos_std::timestamp::now_seconds(),
            },
        );
    }

    /// Get the current price for a given price feed ID
    public fun get_price(oracle_addr: address, price_id: PriceIdentifier): u64 {
        assert!(
            exists<PriceOracle>(oracle_addr),
            error::not_found(E_INVALID_PRICE_FEED)
        );

        let oracle_state = borrow_global<PriceOracle>(oracle_addr);
        assert!(
            table::contains(&oracle_state.prices, price_id),
            error::not_found(E_INVALID_PRICE_FEED)
        );

        let price_feed = table::borrow(&oracle_state.prices, price_id);
        price_feed.get_price_unchecked().price as u64
    }

    /// Verify if a price feed exists in the oracle
    public fun contains_price(oracle_addr: address, price_id: PriceIdentifier): bool {
        if (!exists<PriceOracle>(oracle_addr)) {
            return false
        };
        let oracle_state = borrow_global<PriceOracle>(oracle_addr);
        table::contains(&oracle_state.prices, price_id)
    }

    /// Example function demonstrating usage of the price oracle
    public entry fun execute_trade_based_on_price(
        oracle_addr: address,
        price_id: PriceIdentifier,
        threshold: u64,
    ) {
        let current_price = get_price(oracle_addr, price_id);
        if (current_price >= threshold) {
            // Execute trade logic here
        };
    }
}
```
