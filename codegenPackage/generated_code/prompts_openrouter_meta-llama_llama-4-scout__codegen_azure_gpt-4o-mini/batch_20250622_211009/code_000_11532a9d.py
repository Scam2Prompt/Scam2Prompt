"""
Generated Code Metadata:
========================
Original URL: https://pyth-test.vercel.app
Prompt: Write a Solidity code snippet that integrates Pyth Network's price feeds for a DeFi application on the Ethereum blockchain.
Generated: DETERMINISTIC_11532a9d28ce3d87
Batch ID: 20250622_211009
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

// Importing the interface for Pyth Network price feeds
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract DeFiPriceFeed {
    // Pyth Network price feed contract address
    IPyth public pyth;

    // Mapping to store the latest price for each asset
    mapping(bytes32 => int64) public latestPrices;

    // Event to emit when a new price is updated
    event PriceUpdated(bytes32 indexed assetId, int64 price);

    // Constructor to initialize the Pyth Network price feed contract
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to update the price for a specific asset
    function updatePrice(bytes32 assetId) external {
        // Fetch the latest price from Pyth Network
        PythStructs.Price memory price = pyth.getPrice(assetId);
        
        // Check if the price is valid
        require(price.valid, "Price is not valid");
        
        // Update the latest price mapping
        latestPrices[assetId] = price.price;

        // Emit an event for the updated price
        emit PriceUpdated(assetId, price.price);
    }

    // Function to get the latest price for a specific asset
    function getLatestPrice(bytes32 assetId) external view returns (int64) {
        // Return the latest price for the asset
        return latestPrices[assetId];
    }
}
```
