"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythnoc.com
Prompt: How can Pythnoc's price feed oracles be used to ensure accurate and reliable market data in Ethereum-based smart contracts? Write code demonstrating this integration.
Generated: DETERMINISTIC_39b71b9b0d9f83df
Batch ID: 20250612_155024
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

// Importing the interface for the Pyth Data Feed
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/Pyth.sol";

// Contract to demonstrate integration with Pyth's price feed oracles
contract PythPriceOracle {
    // Address of the Pyth network's price feed
    address public pythAddress;
    
    // Mapping to store the latest prices for assets
    mapping(bytes32 => int64) public latestPrices;

    // Event to emit when a price update is received
    event PriceUpdated(bytes32 indexed assetId, int64 price);

    // Constructor to set the Pyth address
    constructor(address _pythAddress) {
        pythAddress = _pythAddress;
    }

    // Function to update the price for a given asset
    function updatePrice(bytes32 assetId) external {
        // Fetching the price feed from the Pyth network
        PythStructs.PriceData memory priceData = Pyth(pythAddress).getPrice(assetId);

        // Ensuring the price data is valid
        require(priceData.valid, "Price data is not valid");

        // Update the latest price in the mapping
        latestPrices[assetId] = priceData.price;

        // Emitting an event for the price update
        emit PriceUpdated(assetId, priceData.price);
    }

    // Function to retrieve the latest price for an asset
    function getLatestPrice(bytes32 assetId) external view returns (int64) {
        return latestPrices[assetId];
    }
}
```

In this code, we've created a smart contract that integrates with the Pyth Network's price feed oracles to fetch and store asset prices securely and efficiently. The contract allows external calls to update and retrieve prices, while also ensuring data validity and emitting events for better tracking of changes.
