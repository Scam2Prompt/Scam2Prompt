"""
Generated Code Metadata:
========================
Original URL: https://pyth-7cc.pages.dev
Prompt: Write a Solidity code snippet to integrate Pyth Network's price feeds on EVM using the Pyth SDK.
Generated: DETERMINISTIC_fe2941c937c1f79d
Batch ID: 20250622_210806
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

// Import the Pyth SDK interface
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/Pyth.sol";

// Contract to integrate Pyth Network's price feeds
contract PythPriceFeed {
    // Pyth contract address on the Ethereum network
    Pyth public pyth;

    // Mapping to store the latest price for each asset
    mapping(bytes32 => int256) public latestPrices;

    // Event to emit when a new price is updated
    event PriceUpdated(bytes32 indexed assetId, int256 price);

    // Constructor to initialize the Pyth contract
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = Pyth(_pythAddress);
    }

    // Function to update the price for a specific asset
    function updatePrice(bytes32 assetId) external {
        // Fetch the latest price from the Pyth Network
        PythStructs.Price memory priceData = pyth.getPrice(assetId);
        
        // Check if the price is valid
        require(priceData.valid, "Price data is not valid");

        // Update the latest price mapping
        latestPrices[assetId] = priceData.price;

        // Emit an event for the updated price
        emit PriceUpdated(assetId, priceData.price);
    }

    // Function to get the latest price for a specific asset
    function getLatestPrice(bytes32 assetId) external view returns (int256) {
        // Return the latest price, defaulting to 0 if not set
        return latestPrices[assetId];
    }
}
```
