"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: "Generate a smart contract code in Move language for a lending protocol with features like liquidation risk control and oracle security, inspired by NAVI Protocol's implementation on Sui."
Generated: DETERMINISTIC_d8f72e4083a81bb6
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// Lending Protocol Smart Contract in Move Language

// Import necessary modules
use std::collections::map::Map;
use sui::transfer::Transfer;
use sui::tx_context::TxContext;

// Define the LendingProtocol module
module lending_protocol {
    // Define a struct for LendingPool
    struct LendingPool has store {
        pool_id: u64,
        collateral_asset: vector<u8>,
        loan_asset: vector<u8>,
        liquidation_threshold: u128,
        liquidation_penalty: u128,
        oracle: address,
    }

    // Define a struct for Loan
    struct Loan has store {
        loan_id: u64,
        borrower: address,
        collateral: u128,
        loan_amount: u128,
        interest_rate: u128,
        due_time: u64,
    }

    // Define a struct for OraclePrice
    struct OraclePrice has store {
        price: u128,
    }

    // Define a table for LendingPools
    public table<LendingPool> LendingPools;

    // Define a table for Loans
    public table<Loan> Loans;

    // Define a table for OraclePrices
    public table<OraclePrice> OraclePrices;

    // Function to create a new lending pool
    public fun create_lending_pool(
        ctx: &mut TxContext,
        pool_id: u64,
        collateral_asset: vector<u8>,
        loan_asset: vector<u8>,
        liquidation_threshold: u128,
        liquidation_penalty: u128,
        oracle: address,
    ) {
        // Check if the pool already exists
        if (LendingPools.contains(pool_id)) {
            // If the pool exists, abort with an error
            abort(1);
        }

        // Create a new LendingPool
        let pool = LendingPool {
            pool_id,
            collateral_asset,
            loan_asset,
            liquidation_threshold,
            liquidation_penalty,
            oracle,
        };

        // Add the pool to the LendingPools table
        LendingPools.add(pool_id, pool);

        // Emit an event to indicate the creation of a new lending pool
        emit_event("NewLendingPoolCreated", pool_id);
    }

    // Function to borrow from a lending pool
    public fun borrow(
        ctx: &mut TxContext,
        pool_id: u64,
        borrower: address,
        collateral: u128,
        loan_amount: u128,
        interest_rate: u128,
        due_time: u64,
    ) {
        // Get the lending pool
        let pool = LendingPools.get(pool_id);

        // Check if the borrower has sufficient collateral
        if (collateral < pool.liquidation_threshold) {
            // If the borrower does not have sufficient collateral, abort with an error
            abort(2);
        }

        // Create a new Loan
        let loan = Loan {
            loan_id: Loans.size() as u64,
            borrower,
            collateral,
            loan_amount,
            interest_rate,
            due_time,
        };

        // Add the loan to the Loans table
        Loans.add(loan.loan_id, loan);

        // Transfer the loan amount from the lending pool to the borrower
        Transfer::transfer(&pool.loan_asset, borrower, loan_amount);

        // Emit an event to indicate a new loan
        emit_event("NewLoanCreated", loan.loan_id);
    }

    // Function to repay a loan
    public fun repay(ctx: &mut TxContext, loan_id: u64) {
        // Get the loan
        let loan = Loans.get(loan_id);

        // Check if the loan is overdue
        if (loan.due_time < ctx.block_timestamp()) {
            // If the loan is overdue, liquidate the loan
            liquidate(loan_id);
        } else {
            // If the loan is not overdue, repay the loan
            let borrower = loan.borrower;
            let loan_amount = loan.loan_amount;
            let interest_rate = loan.interest_rate;

            // Calculate the repayment amount
            let repayment_amount = loan_amount + (loan_amount * interest_rate) / 100;

            // Transfer the repayment amount from the borrower to the lending pool
            Transfer::transfer(&loan.loan_asset, borrower, repayment_amount);

            // Emit an event to indicate the repayment of a loan
            emit_event("LoanRepaid", loan_id);
        }
    }

    // Function to liquidate a loan
    public fun liquidate(ctx: &mut TxContext, loan_id: u64) {
        // Get the loan
        let loan = Loans.get(loan_id);

        // Get the lending pool
        let pool = LendingPools.get(loan.loan_id);

        // Calculate the liquidation penalty
        let liquidation_penalty = pool.liquidation_penalty;

        // Calculate the liquidation amount
        let liquidation_amount = loan.loan_amount + (loan.loan_amount * liquidation_penalty) / 100;

        // Transfer the liquidation amount from the borrower to the lending pool
        Transfer::transfer(&loan.loan_asset, loan.borrower, liquidation_amount);

        // Emit an event to indicate the liquidation of a loan
        emit_event("LoanLiquidated", loan_id);
    }

    // Function to get the oracle price
    public fun get_oracle_price(ctx: &mut TxContext, oracle: address) {
        // Get the oracle price
        let price = OraclePrices.get(oracle);

        // Return the oracle price
        price.price;
    }

    // Function to update the oracle price
    public fun update_oracle_price(ctx: &mut TxContext, oracle: address, price: u128) {
        // Get the oracle price
        let oracle_price = OraclePrice { price };

        // Update the oracle price
        OraclePrices.add(oracle, oracle_price);

        // Emit an event to indicate the update of the oracle price
        emit_event("OraclePriceUpdated", oracle);
    }
}
```
