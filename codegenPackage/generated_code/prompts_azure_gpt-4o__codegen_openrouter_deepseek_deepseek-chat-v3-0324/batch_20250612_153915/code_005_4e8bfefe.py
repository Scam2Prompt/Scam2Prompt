"""
Generated Code Metadata:
========================
Original URL: https://suiio.vercel.app
Prompt: Provide an example of using the Sui Weather Oracle to fetch real-time weather data and integrate it into a Move-based smart contract.
Generated: DETERMINISTIC_4e8bfefe662e4171
Batch ID: 20250612_153915
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

module weather_oracle::weather_contract {
    use std::string::{Self, String};
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};

    // Struct representing weather data
    struct WeatherData has key, store {
        id: UID,
        temperature: u64,        // in Celsius
        humidity: u8,            // percentage
        wind_speed: u64,         // in km/h
        condition: String,       // e.g., "Sunny", "Rainy"
        timestamp: u64,          // Unix timestamp
        location: String         // e.g., "San Francisco, CA"
    }

    // Struct representing the oracle's configuration
    struct WeatherOracle has key {
        id: UID,
        authorized_callers: vector<address>,  // addresses allowed to update weather
    }

    // Error codes
    const E_NOT_AUTHORIZED: u64 = 0;
    const E_INVALID_DATA: u64 = 1;

    // Initialize a new WeatherOracle
    public fun new_oracle(ctx: &mut TxContext): WeatherOracle {
        WeatherOracle {
            id: object::new(ctx),
            authorized_callers: vector::empty(),
        }
    }

    // Add an authorized caller to the oracle
    public fun add_authorized_caller(
        oracle: &mut WeatherOracle,
        caller: address,
    ) {
        vector::push_back(&mut oracle.authorized_caller, caller);
    }

    // Remove an authorized caller from the oracle
    public fun remove_authorized_caller(
        oracle: &mut WeatherOracle,
        caller: address,
    ) {
        let index = vector::index_of(&oracle.authorized_callers, &caller);
        if (option::is_some(&index)) {
            vector::remove(&mut oracle.authorized_callers, option::extract(&mut index));
        }
    }

    // Update weather data (only callable by authorized addresses)
    public entry fun update_weather(
        oracle: &WeatherOracle,
        temperature: u64,
        humidity: u8,
        wind_speed: u64,
        condition: String,
        timestamp: u64,
        location: String,
        ctx: &mut TxContext,
    ) {
        // Verify caller is authorized
        assert!(
            vector::contains(&oracle.authorized_callers, &tx_context::sender(ctx)),
            E_NOT_AUTHORIZED
        );

        // Validate data
        assert!(humidity <= 100, E_INVALID_DATA);
        assert!(wind_speed < 500, E_INVALID_DATA); // Sanity check for wind speed

        // Create and transfer new WeatherData object
        let weather_data = WeatherData {
            id: object::new(ctx),
            temperature,
            humidity,
            wind_speed,
            condition,
            timestamp,
            location,
        };
        transfer::public_transfer(weather_data, tx_context::sender(ctx));
    }

    // Get weather data (sample function - in practice you'd query the object directly)
    public fun get_weather_data(weather_data: &WeatherData): (
        u64,
        u8,
        u64,
        String,
        u64,
        String
    ) {
        (
            weather_data.temperature,
            weather_data.humidity,
            weather_data.wind_speed,
            string::string(&weather_data.condition),
            weather_data.timestamp,
            string::string(&weather_data.location)
        )
    }
}
```
