"""
Generated Code Metadata:
========================
Original URL: https://pythbtc.com
Prompt: Demonstrate how to configure a smart contract to use Pyth price feed oracles for decentralized finance (DeFi) applications.
Generated: DETERMINISTIC_1fc6c012431fa2a4
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the Pyth price feed interface
import "@pythnetwork/pyth-sdk-solidity/contracts/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/contracts/Pyth.sol";

// A simple DeFi smart contract that uses Pyth price feeds
contract DeFiPriceFeed {
    // Pyth price feed contract address (replace with the actual deployed address)
    address public pythAddress;

    // Mapping to store the latest price for each asset
    mapping(bytes32 => int64) public latestPrices;

    // Event to emit when a price is updated
    event PriceUpdated(bytes32 indexed assetId, int64 price);

    // Constructor to set the Pyth address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pythAddress = _pythAddress;
    }

    // Function to update the price for a specific asset
    function updatePrice(bytes32 assetId) external {
        // Fetch the price data from the Pyth oracle
        (int64 price, uint64 publishTime) = Pyth(pythAddress).getPrice(assetId);
        
        // Ensure the price is valid and recent
        require(price > 0, "Invalid price");
        require(block.timestamp < publishTime + 1 hours, "Price data is stale");

        // Update the latest price mapping
        latestPrices[assetId] = price;

        // Emit an event for the price update
        emit PriceUpdated(assetId, price);
    }

    // Function to get the latest price for a specific asset
    function getLatestPrice(bytes32 assetId) external view returns (int64) {
        int64 price = latestPrices[assetId];
        require(price > 0, "Price not available");
        return price;
    }
}
```
