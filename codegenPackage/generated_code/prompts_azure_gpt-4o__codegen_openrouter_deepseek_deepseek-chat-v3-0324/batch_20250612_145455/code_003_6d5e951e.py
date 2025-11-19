"""
Generated Code Metadata:
========================
Original URL: https://sophon.pages.dev
Prompt: Create a smart contract using the Move programming language to support Web3 startups, leveraging the research and investment principles highlighted by SophonLabs.
Generated: DETERMINISTIC_6d5e951e628dcad7
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// Copyright (c) SophonLabs. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

module sophon::startup_fund {
    use std::error;
    use std::signer;
    use std::vector;
    use aptos_framework::coin;
    use aptos_framework::account;

    // Error codes
    const ENOT_STARTUP_OWNER: u64 = 1;
    const EINSUFFICIENT_FUNDS: u64 = 2;
    const ESTARTUP_NOT_FOUND: u64 = 3;
    const EINVALID_INVESTMENT: u64 = 4;
    const EALREADY_INVESTED: u64 = 5;
    const EINVALID_MILESTONE: u64 = 6;

    // Startup information
    struct Startup has key {
        name: vector<u8>,
        description: vector<u8>,
        website: vector<u8>,
        owner: address,
        total_funding: u64,
        current_funding: u64,
        investors: vector<address>,
        milestones: vector<Milestone>,
        active: bool
    }

    // Milestone tracking
    struct Milestone has store {
        description: vector<u8>,
        target_amount: u64,
        completed: bool
    }

    // Investor information
    struct Investor has key {
        investments: vector<Investment>
    }

    // Investment record
    struct Investment has store {
        startup_address: address,
        amount: u64,
        timestamp: u64
    }

    // Initialize the module
    public entry fun initialize(account: &signer) {
        account::create_account_for_test(signer::address_of(account));
    }

    /// Register a new startup
    public entry fun register_startup(
        owner: &signer,
        name: vector<u8>,
        description: vector<u8>,
        website: vector<u8>,
        initial_funding_goal: u64,
        milestones: vector<Milestone>
    ) acquires Startup {
        let owner_address = signer::address_of(owner);
        
        assert!(
            !exists<Startup>(owner_address),
            error::already_exists(ESTARTUP_NOT_FOUND)
        );

        move_to<Startup>(
            owner,
            Startup {
                name,
                description,
                website,
                owner: owner_address,
                total_funding: initial_funding_goal,
                current_funding: 0,
                investors: vector::empty(),
                milestones,
                active: true
            }
        );
    }

    /// Add a milestone to an existing startup
    public entry fun add_milestone(
        owner: &signer,
        description: vector<u8>,
        target_amount: u64
    ) acquires Startup {
        let owner_address = signer::address_of(owner);
        assert!(exists<Startup>(owner_address), error::not_found(ESTARTUP_NOT_FOUND));
        
        let startup = borrow_global_mut<Startup>(owner_address);
        assert!(startup.owner == owner_address, error::permission_denied(ENOT_STARTUP_OWNER));

        let milestone = Milestone {
            description,
            target_amount,
            completed: false
        };

        vector::push_back(&mut startup.milestones, milestone);
    }

    /// Invest in a startup
    public entry fun invest(
        investor: &signer,
        startup_address: address,
        amount: u64,
        coin_type: address
    ) acquires Startup, Investor {
        assert!(exists<Startup>(startup_address), error::not_found(ESTARTUP_NOT_FOUND));
        assert!(amount > 0, error::invalid_argument(EINVALID_INVESTMENT));

        let startup = borrow_global_mut<Startup>(startup_address);
        assert!(startup.active, error::invalid_state(EINVALID_INVESTMENT));

        let investor_address = signer::address_of(investor);
        assert!(
            !vector::contains(&startup.investors, &investor_address),
            error::invalid_state(EALREADY_INVESTED)
        );

        // Transfer funds
        let coin_store = account::get_coin_store(investor_address, coin_type);
        assert!(coin::value(coin_store) >= amount, error::invalid_state(EINSUFFICIENT_FUNDS));
        coin::transfer(investor, startup_address, amount, coin_type);

        // Update startup funding
        startup.current_funding = startup.current_funding + amount;
        vector::push_back(&mut startup.investors, investor_address);

        // Update investor record
        if (!exists<Investor>(investor_address)) {
            move_to<Investor>(
                investor,
                Investor {
                    investments: vector::empty()
                }
            );
        }

        let investor_record = borrow_global_mut<Investor>(investor_address);
        let investment = Investment {
            startup_address,
            amount,
            timestamp: aptos_framework::timestamp::now_seconds()
        };
        vector::push_back(&mut investor_record.investments, investment);

        // Check and complete milestones
        check_milestones(startup);
    }

    /// Check and complete milestones if funding targets are met
    fun check_milestones(startup: &mut Startup) {
        let milestones = &mut startup.milestones;
        let len = vector::length(milestones);
        let i = 0;

        while (i < len) {
            let milestone = vector::borrow_mut(milestones, i);
            if (!milestone.completed && startup.current_funding >= milestone.target_amount) {
                milestone.completed = true;
            };
            i = i + 1;
        };
    }

    /// Withdraw funds by startup owner
    public entry fun withdraw_funds(
        owner: &signer,
        amount: u64,
        coin_type: address
    ) acquires Startup {
        let owner_address = signer::address_of(owner);
        assert!(exists<Startup>(owner_address), error::not_found(ESTARTUP_NOT_FOUND));

        let startup = borrow_global_mut<Startup>(owner_address);
        assert!(startup.owner == owner_address, error::permission_denied(ENOT_STARTUP_OWNER));
        assert!(startup.current_funding >= amount, error::invalid_state(EINSUFFICIENT_FUNDS));

        coin::transfer(owner, owner_address, amount, coin_type);
        startup.current_funding = startup.current_funding - amount;
    }

    /// Close a startup (only owner can do this)
    public entry fun close_startup(owner: &signer) acquires Startup {
        let owner_address = signer::address_of(owner);
        assert!(exists<Startup>(owner_address), error::not_found(ESTARTUP_NOT_FOUND));

        let startup = borrow_global_mut<Startup>(owner_address);
        assert!(startup.owner == owner_address, error::permission_denied(ENOT_STARTUP_OWNER));

        startup.active = false;
    }

    /// Get startup information
    public fun get_startup_info(startup_address: address): Startup acquires Startup {
        assert!(exists<Startup>(startup_address), error::not_found(ESTARTUP_NOT_FOUND));
        *borrow_global<Startup>(startup_address)
    }

    /// Get investor information
    public fun get_investor_info(investor_address: address): Investor acquires Investor {
        assert!(exists<Investor>(investor_address), error::not_found(ESTARTUP_NOT_FOUND));
        *borrow_global<Investor>(investor_address)
    }
}
```
