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

Below is an example smart contract written in C++ for the EOSIO blockchain (which eosGAS is based on, assuming eosGAS supports EOSIO-compatible smart contracts). This contract tracks electrical consumption for cryptocurrency mining. Make sure to configure your local eosGAS development environment correctly to deploy and test this code.

```cpp
#include <eosio/eosio.hpp>
#include <eosio/asset.hpp>
#include <eosio/time.hpp>

using namespace eosio;

class [[eosio::contract("electric_consumption")]] electric_consumption : public contract {
public:
    using contract::contract;

    // Constructor
    electric_consumption(name receiver, name code, datastream<const char*> ds)
        : contract(receiver, code, ds) {}

    /**
     * @brief Action to log electricity consumption data for a miner.
     * @param miner - The account name of the miner.
     * @param kilowatt_hours - The number of kilowatt-hours consumed.
     * @param timestamp - Optional timestamp of consumption (defaults to current time if omitted).
     */
    [[eosio::action]]
    void logconsumption(name miner, double kilowatt_hours, std::optional<time_point_sec> timestamp) {
        require_auth(miner);

        check(kilowatt_hours > 0, "Consumption value must be positive.");

        // Use current time if timestamp is not provided
        time_point_sec time = timestamp.has_value() ? timestamp.value() : current_time_point();

        // Record the consumption data in the table
        consumption_table consumption(get_self(), get_self().value);
        consumption.emplace(miner, [&](auto& row) {
            row.id = consumption.available_primary_key();
            row.miner = miner;
            row.kilowatt_hours = kilowatt_hours;
            row.timestamp = time;
        });
    }

    /**
     * @brief Action to delete a miner's consumption record.
     * @param miner - The account name of the miner whose records will be deleted.
     */
    [[eosio::action]]
    void deleteconsumption(name miner) {
        require_auth(miner);

        consumption_table consumption(get_self(), get_self().value);
        auto miner_index = consumption.get_index<"miner"_n>();
        auto miner_itr = miner_index.find(miner.value);

        check(miner_itr != miner_index.end(), "No consumption records found for this miner.");

        while (miner_itr != miner_index.end() && miner_itr->miner == miner) {
            miner_itr = miner_index.erase(miner_itr);
        }
    }

private:
    /**
     * @brief Multi-index table to store electricity consumption records.
     */
    struct [[eosio::table]] consumption_record {
        uint64_t id;                // Unique identifier for the record
        name miner;                 // Account name of the miner
        double kilowatt_hours;      // Electricity consumed in kilowatt-hours
        time_point_sec timestamp;   // Timestamp of record creation

        uint64_t primary_key() const { return id; }
        uint64_t by_miner() const { return miner.value; }
    };

    typedef eosio::multi_index<"consumption"_n, consumption_record,
        indexed_by<"miner"_n, const_mem_fun<consumption_record, uint64_t, &consumption_record::by_miner>>
    > consumption_table;
};

```

### Notes:
- Place this code in a `.cpp` file with the same name as the contract (e.g., `electric_consumption.cpp`).
- Compile using the EOSIO CDT (Contract Development Toolkit).
- Deploy the contract to the eosGAS blockchain using the appropriate tools and commands (`cleos`, for example).
- Unit tests, deployment scripts, and integration tests should be written separately to verify functionality.
