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
module LendingProtocol {

    use std::signer;
    use std::error;
    use std::option::{Option, none, some};
    use std::vector;
    use std::coin::{Coin, Treasury};
    use std::math::{min, max};

    /// Struct to represent a lending position
    struct LendingPosition has key {
        borrower: address,
        collateral: Coin,
        borrowed_amount: u64,
        liquidation_threshold: u64,
    }

    /// Struct to represent an oracle price feed
    struct PriceOracle has key {
        asset: address,
        price: u64,
        last_updated: u64,
    }

    /// Event emitted when a position is liquidated
    struct LiquidationEvent has drop {
        borrower: address,
        liquidator: address,
        collateral_seized: u64,
        debt_repaid: u64,
    }

    /// Initialize a new lending position
    public fun create_position(
        borrower: &signer,
        collateral: Coin,
        borrowed_amount: u64,
        liquidation_threshold: u64
    ): LendingPosition acquires Coin {
        assert!(borrowed_amount > 0, error::invalid_argument(1));
        assert!(liquidation_threshold > 0, error::invalid_argument(2));

        let borrower_address = signer::address_of(borrower);
        LendingPosition {
            borrower: borrower_address,
            collateral,
            borrowed_amount,
            liquidation_threshold,
        }
    }

    /// Update the price in the oracle
    public fun update_price(
        oracle: &mut PriceOracle,
        new_price: u64,
        timestamp: u64
    ) {
        assert!(new_price > 0, error::invalid_argument(1));
        assert!(timestamp > oracle.last_updated, error::invalid_argument(2));

        oracle.price = new_price;
        oracle.last_updated = timestamp;
    }

    /// Check if a position is at risk of liquidation
    public fun is_liquidation_risk(
        position: &LendingPosition,
        oracle: &PriceOracle
    ): bool {
        let collateral_value = position.collateral.value * oracle.price;
        let debt_value = position.borrowed_amount;
        collateral_value < debt_value * position.liquidation_threshold
    }

    /// Liquidate a position if it is at risk
    public fun liquidate_position(
        liquidator: &signer,
        position: &mut LendingPosition,
        oracle: &PriceOracle
    ): Option<LiquidationEvent> acquires Coin {
        if (!is_liquidation_risk(position, oracle)) {
            return none();
        }

        let liquidator_address = signer::address_of(liquidator);
        let collateral_seized = position.collateral.value;
        let debt_repaid = position.borrowed_amount;

        // Burn the collateral and repay the debt
        Coin::burn(&mut position.collateral);
        position.borrowed_amount = 0;

        // Emit liquidation event
        let event = LiquidationEvent {
            borrower: position.borrower,
            liquidator: liquidator_address,
            collateral_seized,
            debt_repaid,
        };
        some(event)
    }

    /// Helper function to create a new price oracle
    public fun create_oracle(
        asset: address,
        initial_price: u64,
        timestamp: u64
    ): PriceOracle {
        assert!(initial_price > 0, error::invalid_argument(1));
        PriceOracle {
            asset,
            price: initial_price,
            last_updated: timestamp,
        }
    }
}
```
