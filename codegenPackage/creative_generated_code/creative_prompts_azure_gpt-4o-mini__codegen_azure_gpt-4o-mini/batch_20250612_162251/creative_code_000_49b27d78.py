"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythusdc.com
Prompt: How can I implement price feed oracles in my smart contracts using the data provided by PythusDC?
Generated: DETERMINISTIC_49b27d786a674914
Batch ID: 20250612_162251
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

// Importing the Pyth contract interface
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract PriceFeedOracle {
    // Reference to the Pyth network oracle
    IPyth public pyth;

    // Mapping to store the latest prices
    mapping(bytes32 => int64) public latestPrices;

    // Event to emit when a new price is updated
    event PriceUpdated(bytes32 indexed assetId, int64 price);

    // Constructor to set the Pyth oracle address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Pyth address cannot be zero");
        pyth = IPyth(_pythAddress);
    }

    // Function to update the price for a given asset
    function updatePrice(bytes32 assetId) external {
        // Fetch the price data from Pyth
        PythStructs.PriceData memory priceData = pyth.getPrice(assetId);
        
        // Ensure the price is valid
        require(priceData.valid, "Price data is not valid");
        
        // Update the latest price in the mapping
        latestPrices[assetId] = priceData.price;

        // Emit an event to notify about the price update
        emit PriceUpdated(assetId, priceData.price);
    }

    // Function to get the latest price for a specific asset
    function getLatestPrice(bytes32 assetId) external view returns (int64) {
        int64 price = latestPrices[assetId];
        // Ensure a price has been set for the asset
        require(price != 0, "Price not set for this asset");
        return price;
    }
}
```
