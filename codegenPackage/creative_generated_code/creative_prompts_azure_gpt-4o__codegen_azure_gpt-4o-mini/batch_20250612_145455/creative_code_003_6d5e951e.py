"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.pages.dev
Prompt: Create a smart contract using the Move programming language to support Web3 startups, leveraging the research and investment principles highlighted by SophonLabs.
Generated: DETERMINISTIC_6d5e951e628dcad7
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
// SPDX-License-Identifier: MIT
// This smart contract is designed to support Web3 startups
// leveraging the research and investment principles highlighted by SophonLabs

module SophiLabs::Web3Startup {
    use 0x1::account;
    use 0x1::coin;
    use 0x1::vector;

    // Structure to hold startup details
    struct Startup {
        name: vector<u8>,
        description: vector<u8>,
        funding_goal: u64,
        raised_amount: u64,
        is_funded: bool,
        owner: address,
    }

    // Storage for startups
    public fun initialize_startup(owner: &signer, name: vector<u8>, description: vector<u8>, funding_goal: u64) {
        let startup = Startup {
            name,
            description,
            funding_goal,
            raised_amount: 0,
            is_funded: false,
            owner: signer::address_of(owner),
        };
        
        // Persist the startup in the account resource
        account::create_resource<SophiLabs::Web3Startup::Startup>(signer::address_of(owner), startup);
    }

    // Function to contribute funds to a startup
    public fun contribute(owner: &signer, amount: u64) acquires Startup {
        let startup_ref = borrow_global_mut<SophiLabs::Web3Startup::Startup>(signer::address_of(owner));

        // Ensure the startup is not already fully funded
        assert!(!startup_ref.is_funded, 10001, "Startup is already fully funded");

        // Ensure the contribution doesn't exceed the funding goal
        assert!(startup_ref.raised_amount + amount <= startup_ref.funding_goal, 10002, "Contribution exceeds funding goal");

        // Update raised amount and check if funding goal is met
        startup_ref.raised_amount += amount;
        if startup_ref.raised_amount >= startup_ref.funding_goal {
            startup_ref.is_funded = true;
        }

        // Transfer the funds from the contributor's account
        coin::transfer(signer::address_of(owner), startup_ref.owner, amount);
    }

    // Function to withdraw funds if the startup is successfully funded
    public fun withdraw_funds(owner: &signer) acquires Startup {
        let startup_ref = borrow_global<SophiLabs::Web3Startup::Startup>(signer::address_of(owner));

        // Ensure the startup is fully funded before withdrawing
        assert!(startup_ref.is_funded, 10003, "Startup is not fully funded");

        // Transfer the raised funds to the startup owner
        coin::transfer(signer::address_of(owner), startup_ref.owner, startup_ref.raised_amount);
    }

    // Function to get startup details
    public fun get_startup_details(owner: address): (vector<u8>, vector<u8>, u64, u64, bool) acquires Startup {
        let startup_ref = borrow_global<SophiLabs::Web3Startup::Startup>(owner);
        (startup_ref.name, startup_ref.description, startup_ref.funding_goal, startup_ref.raised_amount, startup_ref.is_funded)
    }
}
```
