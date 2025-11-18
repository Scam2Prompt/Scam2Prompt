"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Write a Solidity contract that uses Pyth's `updatePriceFeeds` method to fetch and store price data for multiple assets, including BTC/USD, ETH/USD, and PYTH/USD.
Generated: DETERMINISTIC_7edf3f8c4a6d5b09
Batch ID: 20250612_152000
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

// Importing the required interfaces for the Pyth network
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

// Contract to fetch and store price data from Pyth for multiple assets
contract PriceFeed {
    // Define the Pyth oracle interface
    IPyth public pyth;

    // Mapping to store the price of each asset
    mapping(string => int64) public assetPrices;

    // Events for price updates
    event PriceUpdated(string indexed asset, int64 price);

    // Constructor to set the Pyth oracle address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Pyth address cannot be zero");
        pyth = IPyth(_pythAddress);
    }

    // Function to update prices for specified assets
    function updatePrices(string[] memory assets) external {
        // Validate that assets array is not empty
        require(assets.length > 0, "Assets array cannot be empty");

        // Call the Pyth's updatePriceFeeds method
        pyth.updatePriceFeeds();

        // Loop through the assets and retrieve their prices
        for (uint256 i = 0; i < assets.length; i++) {
            // Fetch the price feed for the asset
            PriceInfo memory priceInfo = pyth.getPrice(assets[i]);

            // Ensure the price is valid
            require(priceInfo.price > 0, "Invalid price returned");

            // Store price in the mapping
            assetPrices[assets[i]] = priceInfo.price;

            // Emit an event for the price update
            emit PriceUpdated(assets[i], priceInfo.price);
        }
    }

    // Function to get the latest price for a specific asset
    function getLatestPrice(string memory asset) external view returns (int64) {
        return assetPrices[asset];
    }
}
```
