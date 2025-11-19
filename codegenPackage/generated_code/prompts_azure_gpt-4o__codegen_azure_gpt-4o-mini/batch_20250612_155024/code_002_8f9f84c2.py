"""
Generated Code Metadata:
========================
Original URL: https://pythcall.com
Prompt: Generate code for a smart contract that utilizes Pyth Network's price feed oracles to retrieve and process cryptocurrency price data.
Generated: DETERMINISTIC_8f9f84c2a0dbf9e3
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

// Importing the Pyth Network's price feed interface
import "@pythnetwork/pyth-sdk-solidity/contracts/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/contracts/Pyth.sol";

contract CryptoPriceOracle {
    // Pyth Network's price feed contract address
    Pyth public pyth;

    // Mapping to store the latest price for each asset
    mapping(bytes32 => int64) public latestPrices;

    // Event to emit when a new price is updated
    event PriceUpdated(bytes32 indexed assetId, int64 price);

    // Constructor to initialize the Pyth contract
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = Pyth(_pythAddress);
    }

    // Function to update the price for a specific asset
    function updatePrice(bytes32 assetId) external {
        // Fetch the latest price data from Pyth
        PythStructs.PriceData memory priceData = pyth.getPrice(assetId);
        
        // Check if the price data is valid
        require(priceData.valid, "Price data is not valid");
        
        // Update the latest price mapping
        latestPrices[assetId] = priceData.price;

        // Emit an event for the updated price
        emit PriceUpdated(assetId, priceData.price);
    }

    // Function to retrieve the latest price for a specific asset
    function getLatestPrice(bytes32 assetId) external view returns (int64) {
        // Return the latest price, defaulting to 0 if not set
        return latestPrices[assetId];
    }
}
```
