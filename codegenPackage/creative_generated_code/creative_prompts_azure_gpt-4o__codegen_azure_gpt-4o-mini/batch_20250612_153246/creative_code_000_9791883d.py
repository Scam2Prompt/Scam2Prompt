"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eeenlist-pyth.pages.dev
Prompt: Write a Solidity smart contract that integrates Pyth Network's price feed for BTC/USD using the `pyth-sdk-solidity` library. Include functionality to fetch and update the price feed on-demand.
Generated: DETERMINISTIC_9791883d7d012ac6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the Pyth SDK for Solidity
import { PythStructs } from "pyth-sdk-solidity/PythStructs.sol";
import { PythPriceConsumer } from "pyth-sdk-solidity/PythPriceConsumer.sol";

// Contract that integrates Pyth Network's price feed for BTC/USD
contract BTCPriceFeed is PythPriceConsumer {
    // The price of BTC in USD
    PythStructs.Price public btcUsdPrice;

    // Event emitted when the BTC price is updated
    event PriceUpdated(int64 price, uint64 timestamp);

    // Constructor to initialize the price feed
    constructor(address pythAddress) PythPriceConsumer(pythAddress) {}

    // Function to fetch the latest BTC/USD price
    function fetchLatestPrice() external returns (int64, uint64) {
        // Fetch the BTC/USD price from the Pyth Network
        try getPrice("BTC/USD") returns (PythStructs.Price memory price) {
            // Update the stored price
            btcUsdPrice = price;

            // Emit the PriceUpdated event
            emit PriceUpdated(price.price, price.timestamp);

            // Return the current price and timestamp
            return (price.price, price.timestamp);
        } catch {
            revert("Failed to fetch BTC/USD price");
        }
    }

    // Function to update the price feed on-demand
    function updatePriceFeed() external {
        // Check if the price feed is stale
        if (btcUsdPrice.timestamp < block.timestamp - 10 minutes) {
            // Fetch the latest price
            (int64 price, uint64 timestamp) = fetchLatestPrice();
            require(price > 0, "Invalid price fetched");
            btcUsdPrice = PythStructs.Price(price, timestamp);
        }
    }

    // Function to get the latest BTC/USD price
    function getLatestPrice() external view returns (int64, uint64) {
        return (btcUsdPrice.price, btcUsdPrice.timestamp);
    }
}
```
