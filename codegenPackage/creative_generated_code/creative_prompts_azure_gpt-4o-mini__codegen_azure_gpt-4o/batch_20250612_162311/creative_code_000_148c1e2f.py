"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pytheth.com
Prompt: How can I integrate price feed oracles into my smart contracts using the data from Pytheth?
Generated: DETERMINISTIC_148c1e2f0adab6d5
Batch ID: 20250612_162311
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

// Import the Aggregator interface for interacting with price feed oracles
interface IPyth {
    function getPriceUnsafe(bytes32 id) external view returns (int64 price, uint64 expo);
    function getUpdateTimeUnsafe(bytes32 id) external view returns (uint64 timestamp);
}

contract PriceFeedOracle {
    // Address of the Pyth price feed contract
    IPyth private pythOracle;

    // Mapping to store the IDs of the assets and their corresponding Pyth price feeds
    mapping(string => bytes32) private assetPriceFeedIDs;

    // Event for logging price retrieval
    event PriceRetrieved(string asset, int64 price, uint64 expo, uint64 timestamp);

    // Constructor to set the address of the Pyth price feed contract
    constructor(address _pythOracleAddress) {
        require(_pythOracleAddress != address(0), "Invalid Oracle address");
        pythOracle = IPyth(_pythOracleAddress);
    }

    // Function to add or update an asset's price feed ID
    function setAssetPriceFeedID(string memory asset, bytes32 priceFeedID) external {
        assetPriceFeedIDs[asset] = priceFeedID;
    }

    // Function to get the latest price of an asset
    function getPrice(string memory asset) external view returns (int64 price, uint64 expo, uint64 timestamp) {
        bytes32 priceFeedID = assetPriceFeedIDs[asset];
        require(priceFeedID != bytes32(0), "Asset not found");

        // Fetch the price and its exponent
        (price, expo) = pythOracle.getPriceUnsafe(priceFeedID);

        // Fetch the last update time
        timestamp = pythOracle.getUpdateTimeUnsafe(priceFeedID);

        return (price, expo, timestamp);
    }

    // Example function to retrieve and log the price of an asset
    function logPrice(string memory asset) external {
        bytes32 priceFeedID = assetPriceFeedIDs[asset];
        require(priceFeedID != bytes32(0), "Asset not found");

        // Fetch the price details
        (int64 price, uint64 expo, uint64 timestamp) = getPrice(asset);

        // Emit the event with price details
        emit PriceRetrieved(asset, price, expo, timestamp);
    }
}
```
