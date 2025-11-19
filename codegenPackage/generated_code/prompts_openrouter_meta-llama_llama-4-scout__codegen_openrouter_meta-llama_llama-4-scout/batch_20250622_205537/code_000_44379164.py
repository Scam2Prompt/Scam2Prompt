"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: "Write a smart contract that utilizes eosGAS tokens to measure electrical consumption for cryptocurrency mining, based on the power plant's energy output."
Generated: DETERMINISTIC_44379164bd66f520
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// SPDX-License-Identifier: MIT
#pragma once

#include <eosiolib/eosio.hpp>
#include <eosiolib/asset.hpp>

using namespace eosio;

class [[eosio::contract]] powerplant : public contract {
  public:
    using contract::contract;

    // Action to add a new power plant
    [[eosio::action]] void addplant(name plantname, double energyoutput) {
      // Check if plant already exists
      require_auth(get_self());
      auto plant = plants.find(plantname);
      eosio_assert(plant == plants.end(), "Plant already exists");

      // Add plant to table
      plants.emplace(get_self(), [&](auto& p) {
        p.name = plantname;
        p.energy_output = energyoutput;
      });
    }

    // Action to update a power plant's energy output
    [[eosio::action]] void updateplant(name plantname, double energyoutput) {
      // Check if plant exists
      require_auth(get_self());
      auto plant = plants.find(plantname);
      eosio_assert(plant != plants.end(), "Plant does not exist");

      // Update plant's energy output
      plants.modify(plant, get_self(), [&](auto& p) {
        p.energy_output = energyoutput;
      });
    }

    // Action to measure electrical consumption for cryptocurrency mining
    [[eosio::action]] void measureconsumption(name plantname, double consumption, asset eosgas) {
      // Check if plant exists
      auto plant = plants.find(plantname);
      eosio_assert(plant != plants.end(), "Plant does not exist");

      // Calculate cost based on energy output and consumption
      double cost = plant->energy_output * consumption;

      // Check if sufficient eosGAS tokens were provided
      eosio_assert(eosgas.amount >= cost, "Insufficient eosGAS tokens provided");

      // Transfer eosGAS tokens to power plant account
      eosio::asset transfer_amount = eosio::asset(cost, eosgas.symbol);
      eosio::transfer(eosgas.contract, get_self(), transfer_amount);

      // Record consumption
      consumption_records.emplace(get_self(), [&](auto& r) {
        r.plant_name = plantname;
        r.consumption = consumption;
        r.cost = cost;
      });
    }

  private:
    // Table to store power plant information
    struct [[eosio::table]] plant {
      name name;
      double energy_output;

      uint64_t primary_key() const { return name; }
    };

    // Table to store consumption records
    struct [[eosio::table]] consumption_record {
      name plant_name;
      double consumption;
      double cost;

      uint64_t primary_key() const { return plant_name; }
    };

    // Typedefs for tables
    typedef eosio::multi_index<"plants"_n, plant> plant_table;
    typedef eosio::multi_index<"consumption"_n, consumption_record> consumption_table;

    // Tables
    plant_table plants;
    consumption_table consumption_records;
};
```
