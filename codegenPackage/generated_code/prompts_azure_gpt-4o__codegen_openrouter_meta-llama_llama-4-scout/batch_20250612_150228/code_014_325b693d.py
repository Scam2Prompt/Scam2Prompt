"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: Generate a Move-based smart contract to interact with NAVI Protocol's NAVI X Ecosystem Fund for supporting Sui blockchain development projects.
Generated: DETERMINISTIC_325b693d2697b35f
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// SPDX-License-Identifier: Apache-2.0
// Copyright 2023 NAVI Protocol

module NAVI_X_Ecosystem_Fund {
    use std::vector;
    use sui::tx_context::TxContext;
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::coin::{Self, Coin};

    // Define a struct to represent the NAVI X Ecosystem Fund
    struct NAVI_X_Ecosystem_Fund has key, store {
        id: UID,
        // Mapping of project IDs to their respective funding amounts
        project_funding: vector<tuple<u64, u64>>,
    }

    // Define a struct to represent a project
    struct Project has store {
        id: u64,
        name: vector<u8>,
        funding_amount: u64,
    }

    // Public function to create a new NAVI X Ecosystem Fund
    public fun create_NAVI_X_Ecosystem_Fund(ctx: &mut TxContext): NAVI_X_Ecosystem_Fund {
        let fund = NAVI_X_Ecosystem_Fund {
            id: object::new(ctx),
            project_funding: vector::empty(),
        };
        transfer::transfer_to_object(ctx.signer(), fund.id);
        fund
    }

    // Public function to propose a new project for funding
    public fun propose_project(
        fund: &mut NAVI_X_Ecosystem_Fund,
        project_id: u64,
        project_name: vector<u8>,
        funding_amount: u64,
        ctx: &TxContext
    ) {
        // Check if the project already exists
        if vector::find(&fund.project_funding, project_id) != vector::end(&fund.project_funding) {
            panic!("Project already exists");
        }

        // Add the project to the funding mapping
        vector::push_back(&mut fund.project_funding, (project_id, funding_amount));

        // Create a new project object
        let project = Project {
            id: project_id,
            name: project_name,
            funding_amount: funding_amount,
        };

        // Transfer funding amount to the project
        let coin = coin::take(ctx.signer(), funding_amount);
        transfer::transfer_to_object(fund.id, coin);
    }

    // Public function to fund an existing project
    public fun fund_project(
        fund: &mut NAVI_X_Ecosystem_Fund,
        project_id: u64,
        funding_amount: u64,
        ctx: &TxContext
    ) {
        // Find the project's funding amount
        let project_funding = vector::find_mut(&mut fund.project_funding, project_id);
        if project_funding == vector::end(&mut fund.project_funding) {
            panic!("Project not found");
        }

        // Increase the project's funding amount
        let (_, funding) = *project_funding;
        *funding = *funding + funding_amount;

        // Transfer funding amount to the project
        let coin = coin::take(ctx.signer(), funding_amount);
        transfer::transfer_to_object(fund.id, coin);
    }

    // Public function to get the funding amount of a project
    public fun get_project_funding(
        fund: &NAVI_X_Ecosystem_Fund,
        project_id: u64
    ): u64 {
        // Find the project's funding amount
        let project_funding = vector::find(&fund.project_funding, project_id);
        if project_funding == vector::end(&fund.project_funding) {
            panic!("Project not found");
        }

        // Return the project's funding amount
        let (_, funding) = *project_funding;
        *funding
    }
}
```
