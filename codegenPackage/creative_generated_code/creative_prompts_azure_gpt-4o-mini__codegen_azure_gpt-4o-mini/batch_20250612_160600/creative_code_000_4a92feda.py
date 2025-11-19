"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eosgas.io
Prompt: How can I implement a smart contract on the eosGAS blockchain to measure electrical consumption for cryptocurrency mining?
Generated: DETERMINISTIC_4a92feda9565a7c8
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <eosio/eosio.hpp>
#include <eosio/print.hpp>

using namespace eosio;

CONTRACT energy_monitor : public contract {
  public:
    using contract::contract;

    // Structure to hold energy consumption data
    struct [[eosio::table]] consumption_data {
        name miner;               // The miner's account name
        uint64_t timestamp;       // Time of data recording
        double consumption;       // Energy consumed in kWh

        uint64_t primary_key() const { return miner.value; }
        uint64_t get_timestamp() const { return timestamp; }
    };

    // Table to store energy consumption records
    using consumption_table = eosio::multi_index<"consumption"_n, consumption_data,
        indexed_by<"bytime"_n, const_mem_fun<consumption_data, uint64_t, &consumption_data::get_timestamp>>>;

    // Action to record energy consumption
    [[eosio::action]]
    void record(name miner, double consumption) {
        // Check if the miner is a valid account
        require_auth(miner);
        
        // Validate energy consumption value
        check(consumption >= 0, "Energy consumption must be a non-negative value");

        // Create or update consumption record
        consumption_table consumption(get_self(), get_self().value);
        auto iterator = consumption.find(miner.value);

        // Get the current timestamp
        uint64_t current_time = current_time_point().sec_since_epoch();

        if (iterator == consumption.end()) {
            // If miner does not have a record, create a new one
            consumption.emplace(miner, [&](auto& row) {
                row.miner = miner;
                row.timestamp = current_time;
                row.consumption = consumption;
            });
        } else {
            // If miner exists, update the record
            consumption.modify(iterator, miner, [&](auto& row) {
                row.timestamp = current_time;
                row.consumption += consumption; // Add to existing consumption
            });
        }

        print("Energy consumption recorded successfully for ", miner);
    }

    // Action to retrieve energy consumption for a miner
    [[eosio::action]]
    void getdata(name miner) {
        // Validate if the miner exists
        consumption_table consumption(get_self(), get_self().value);
        auto iterator = consumption.find(miner.value);
        check(iterator != consumption.end(), "No consumption data found for this miner");

        // Print out the consumption data
        print("Miner: ", miner, " | Timestamp: ", iterator->timestamp, " | Consumption: ", iterator->consumption, " kWh");
    }
};

EOSIO_DISPATCH(energy_monitor, (record)(getdata))
```
