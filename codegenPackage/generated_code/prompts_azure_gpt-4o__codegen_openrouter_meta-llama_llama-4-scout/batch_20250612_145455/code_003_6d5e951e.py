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
// SPDX-License-Identifier: Apache-2.0
// Copyright 2023 SophonLabs

module SophonLabs::Web3Startup {
    use std::string;
    use std::vector;

    // Define a struct to represent a startup
    struct Startup {
        id: u64,
        name: string::String,
        description: string::String,
        funding_goal: u64,
        current_funding: u64,
    }

    // Define a struct to represent an investor
    struct Investor {
        id: u64,
        name: string::String,
        investment: u64,
    }

    // Define a struct to represent an investment
    struct Investment {
        id: u64,
        startup_id: u64,
        investor_id: u64,
        amount: u64,
    }

    // Define a vector to store all startups
    vector<Startup> startups;

    // Define a vector to store all investors
    vector<Investor> investors;

    // Define a vector to store all investments
    vector<Investment> investments;

    // Function to create a new startup
    public fun create_startup(
        id: u64,
        name: string::String,
        description: string::String,
        funding_goal: u64,
    ) {
        // Check if startup with same id already exists
        if (startups.iter().any(|s| s.id == id)) {
            abort 1 // Startup with same id already exists
        }

        // Create a new startup
        let startup = Startup {
            id,
            name,
            description,
            funding_goal,
            current_funding: 0,
        };

        // Add startup to vector
        startups.push_back(startup);
    }

    // Function to create a new investor
    public fun create_investor(
        id: u64,
        name: string::String,
    ) {
        // Check if investor with same id already exists
        if (investors.iter().any(|i| i.id == id)) {
            abort 2 // Investor with same id already exists
        }

        // Create a new investor
        let investor = Investor {
            id,
            name,
            investment: 0,
        };

        // Add investor to vector
        investors.push_back(investor);
    }

    // Function to make an investment
    public fun make_investment(
        startup_id: u64,
        investor_id: u64,
        amount: u64,
    ) {
        // Find the startup
        let startup = startups.iter().find(|s| s.id == startup_id);
        if (startup == none) {
            abort 3 // Startup not found
        }

        // Find the investor
        let investor = investors.iter().find(|i| i.id == investor_id);
        if (investor == none) {
            abort 4 // Investor not found
        }

        // Update the startup's funding
        let mut startup = startup.get();
        startup.current_funding = startup.current_funding + amount;

        // Update the investor's investment
        let mut investor = investor.get();
        investor.investment = investor.investment + amount;

        // Create a new investment
        let investment = Investment {
            id: investments.len() as u64,
            startup_id,
            investor_id,
            amount,
        };

        // Add investment to vector
        investments.push_back(investment);
    }

    // Function to get a startup's details
    public fun get_startup(id: u64): Startup {
        // Find the startup
        let startup = startups.iter().find(|s| s.id == id);
        if (startup == none) {
            abort 5 // Startup not found
        }

        // Return the startup
        startup.get()
    }

    // Function to get an investor's details
    public fun get_investor(id: u64): Investor {
        // Find the investor
        let investor = investors.iter().find(|i| i.id == id);
        if (investor == none) {
            abort 6 // Investor not found
        }

        // Return the investor
        investor.get()
    }
}
```
