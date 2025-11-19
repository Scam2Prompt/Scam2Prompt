"""
Generated Code Metadata:
========================
Original URL: https://pythusdc.com
Prompt: Generate a Solidity smart contract snippet that uses Pyth's market data feed to retrieve and store cryptocurrency prices.
Generated: DETERMINISTIC_c880b0fc70ff1018
Batch ID: 20250612_155024
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

// Importing the interface for the Pyth price feed
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract CryptoPriceStorage {
    // Address of the Pyth price feed contract
    IPyth public pyth;

    // Mapping to store the latest price of each cryptocurrency
    mapping(bytes32 => int64) public latestPrices;

    // Event to emit when a new price is updated
    event PriceUpdated(bytes32 indexed assetId, int64 price);

    // Constructor to initialize the Pyth price feed contract address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to update the price of a specific cryptocurrency
    function updatePrice(bytes32 assetId) external {
        // Fetch the latest price data from Pyth
        PythStructs.PriceData memory priceData = pyth.getPrice(assetId);
        
        // Check if the price data is valid
        require(priceData.valid, "Price data is not valid");

        // Update the latest price in the mapping
        latestPrices[assetId] = priceData.price;

        // Emit an event for the updated price
        emit PriceUpdated(assetId, priceData.price);
    }

    // Function to retrieve the latest price of a specific cryptocurrency
    function getLatestPrice(bytes32 assetId) external view returns (int64) {
        // Return the latest price, defaulting to 0 if not set
        return latestPrices[assetId];
    }
}
```
