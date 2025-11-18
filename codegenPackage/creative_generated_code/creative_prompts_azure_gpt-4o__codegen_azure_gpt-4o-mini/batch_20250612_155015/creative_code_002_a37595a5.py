"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythbtc.com
Prompt: Generate a smart contract snippet that uses Pyth price feed oracles to fetch cryptocurrency price updates.
Generated: DETERMINISTIC_a37595a54fb35d02
Batch ID: 20250612_155015
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

// Importing the interface for Pyth price feeds
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract PriceFeed {
    // Pyth oracle instance
    IPyth private pyth;

    // Mapping to store the latest price for each asset
    mapping(bytes32 => int64) public latestPrices;

    // Event to emit when a new price is updated
    event PriceUpdated(bytes32 indexed assetId, int64 price);

    // Constructor to set the Pyth oracle address
    constructor(address pythAddress) {
        require(pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(pythAddress);
    }

    // Function to update the price for a specific asset
    function updatePrice(bytes32 assetId) public {
        // Fetching the price data from Pyth
        PythStructs.PriceData memory priceData = pyth.getPrice(assetId);
        
        // Checking if the price data is valid
        require(priceData.publishTime > 0, "Invalid price data");
        
        // Updating the latest price mapping
        latestPrices[assetId] = priceData.price;

        // Emitting the price update event
        emit PriceUpdated(assetId, priceData.price);
    }

    // Function to get the latest price for a specific asset
    function getLatestPrice(bytes32 assetId) external view returns (int64) {
        // Returning the latest price if it exists, otherwise returning 0
        return latestPrices[assetId];
    }
}
```

Make sure to replace the import paths with the actual paths of your Pyth SDK in your project environment, as they may differ based on your setup.
