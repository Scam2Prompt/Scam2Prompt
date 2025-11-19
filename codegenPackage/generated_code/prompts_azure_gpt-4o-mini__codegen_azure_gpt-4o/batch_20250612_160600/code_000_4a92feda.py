"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: How can I implement a smart contract on the eosGAS blockchain to measure electrical consumption for cryptocurrency mining?
Generated: DETERMINISTIC_4a92feda9565a7c8
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// eosGAS Smart Contract to Measure Electrical Consumption for Cryptocurrency Mining
// This contract tracks electrical consumption and allows miners to log their usage.
// Written in C++ for the eosGAS blockchain using EOSIO framework.

#include <eosio/eosio.hpp>
#include <eosio/asset.hpp>
#include <eosio/system.hpp>

using namespace eosio;

class [[eosio::contract("electric_consumption")]] electric_consumption : public contract {
public:
    using contract::contract;

    // Constructor
    electric_consumption(name receiver, name code, datastream<const char*> ds)
        : contract(receiver, code, ds) {}

    // Action to log electrical consumption
    [[eosio::action]]
    void logusage(name miner, uint64_t kilowatt_hours, asset cost) {
        require_auth(miner); // Ensure the miner is authorized to log usage

        // Validate input
        check(kilowatt_hours > 0, "Kilowatt hours must be greater than zero.");
        check(cost.amount > 0, "Cost must be greater than zero.");
        check(cost.symbol == symbol("EOS", 4), "Cost must be in EOS.");

        // Add record to the table
        usage_table usage(get_self(), get_self().value);
        usage.emplace(miner, [&](auto& row) {
            row.id = usage.available_primary_key();
            row.miner = miner;
            row.kilowatt_hours = kilowatt_hours;
            row.cost = cost;
            row.timestamp = current_time_point();
        });
    }

    // Action to clear all records (admin-only)
    [[eosio::action]]
    void clear(name admin) {
        require_auth(admin); // Ensure only admin can clear records

        // Check if the caller is the contract owner
        check(admin == get_self(), "Only the contract owner can clear records.");

        // Clear the table
        usage_table usage(get_self(), get_self().value);
        auto itr = usage.begin();
        while (itr != usage.end()) {
            itr = usage.erase(itr);
        }
    }

private:
    // Table to store electrical consumption records
    struct [[eosio::table]] usage_record {
        uint64_t id;                // Unique record ID
        name miner;                 // Account name of the miner
        uint64_t kilowatt_hours;    // Electrical consumption in kWh
        asset cost;                 // Cost of electricity in EOS
        time_point timestamp;       // Timestamp of the record

        uint64_t primary_key() const { return id; }
    };

    typedef eosio::multi_index<"usage"_n, usage_record> usage_table;
};

EOSIO_DISPATCH(electric_consumption, (logusage)(clear))
```
