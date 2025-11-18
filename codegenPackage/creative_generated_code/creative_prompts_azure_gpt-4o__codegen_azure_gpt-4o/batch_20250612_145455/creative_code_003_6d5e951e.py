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
module SophonLabs::Web3StartupSupport {

    use std::signer;
    use std::string;
    use std::vector;

    // Struct to represent a Web3 startup
    struct Startup has key {
        name: string::String,
        description: string::String,
        owner: signer::Address,
        total_investment: u64,
        investors: vector::Vector<signer::Address>,
        investment_breakdown: vector::Vector<u64>, // Matching investments from investors
    }

    // Event to log new startup registration
    struct StartupRegistered has drop, store {
        name: string::String,
        owner: signer::Address,
    }

    // Event to log investment in a startup
    struct InvestmentMade has drop, store {
        startup_name: string::String,
        investor: signer::Address,
        amount: u64,
    }

    // Table to store registered startups
    struct StartupsTable has key {
        startups: vector::Vector<Startup>,
    }

    // Initialize StartupsTable resource
    public fun init_startups_table(account: &signer) {
        let startups_table = StartupsTable {
            startups: vector::empty<Startup>(),
        };
        move_to(account, startups_table);
    }

    // Function to register a Web3 startup
    public fun register_startup(
        account: &signer,
        name: string::String,
        description: string::String
    ) acquires StartupsTable {
        let owner_address = signer::address_of(account);

        // Check if the startup already exists
        let startups_table = &mut borrow_global_mut<StartupsTable>(owner_address);
        let startups = &mut startups_table.startups;
        let mut i = 0;
        while (i < vector::length(startups)) {
            let startup = vector::borrow(startups, i);
            assert!(startup!=!// NO startup overlap`;
