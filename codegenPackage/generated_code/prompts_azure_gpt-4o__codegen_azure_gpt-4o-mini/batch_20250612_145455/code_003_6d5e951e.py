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
// SPDX-License-Identifier: MIT
// Smart contract for supporting Web3 startups using Move programming language

module Web3Startups::StartupFund {

    // Struct to represent a startup
    struct Startup has key {
        id: u64,
        name: vector<u8>,
        funding_goal: u64,
        current_funding: u64,
        is_funded: bool,
        owner: address,
    }

    // Resource to manage the startup fund
    struct FundManager has key {
        startups: vector<Startup>,
        total_funds: u64,
    }

    // Event emitted when a startup is created
    public fun emit_startup_created(startup_id: u64, owner: address) {
        // Emit event logic here
    }

    // Event emitted when funding is received
    public fun emit_funding_received(startup_id: u64, amount: u64) {
        // Emit event logic here
    }

    // Function to create a new startup
    public fun create_startup(
        fund_manager: &mut FundManager,
        name: vector<u8>,
        funding_goal: u64,
        owner: address
    ) {
        // Ensure the funding goal is positive
        assert!(funding_goal > 0, 0);

        // Create a new startup
        let startup_id = vector::length(&fund_manager.startups) as u64;
        let new_startup = Startup {
            id: startup_id,
            name,
            funding_goal,
            current_funding: 0,
            is_funded: false,
            owner,
        };

        // Add the new startup to the fund manager
        vector::push_back(&mut fund_manager.startups, new_startup);
        emit_startup_created(startup_id, owner);
    }

    // Function to fund a startup
    public fun fund_startup(
        fund_manager: &mut FundManager,
        startup_id: u64,
        amount: u64,
        sender: address
    ) {
        // Ensure the startup exists
        assert!(startup_id < vector::length(&fund_manager.startups) as u64, 1);

        // Get the startup
        let startup = &mut vector::borrow_mut(&mut fund_manager.startups, startup_id);

        // Ensure the funding amount is positive
        assert!(amount > 0, 2);
        // Ensure the sender is not the owner of the startup
        assert!(startup.owner != sender, 3);
        // Ensure the startup is not already fully funded
        assert!(!startup.is_funded, 4);

        // Update the current funding
        startup.current_funding += amount;
        fund_manager.total_funds += amount;

        // Check if the startup is fully funded
        if startup.current_funding >= startup.funding_goal {
            startup.is_funded = true;
        }

        emit_funding_received(startup_id, amount);
    }

    // Function to get startup details
    public fun get_startup_details(fund_manager: &FundManager, startup_id: u64): Startup {
        // Ensure the startup exists
        assert!(startup_id < vector::length(&fund_manager.startups) as u64, 1);
        vector::borrow(&fund_manager.startups, startup_id)
    }

    // Function to initialize the fund manager
    public fun initialize_fund_manager(): FundManager {
        FundManager {
            startups: vector::empty<Startup>(),
            total_funds: 0,
        }
    }
}
```
