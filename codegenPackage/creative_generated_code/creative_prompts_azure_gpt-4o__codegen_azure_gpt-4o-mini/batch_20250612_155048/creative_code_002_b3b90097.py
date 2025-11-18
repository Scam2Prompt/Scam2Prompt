"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythim.com
Prompt: Generate a smart contract example that uses Pythim's market data API to fetch cryptocurrency prices.
Generated: DETERMINISTIC_b3b90097282bd07c
Batch ID: 20250612_155048
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

// Import the interface for the Pyth contract
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/PriceFeed.sol";

contract CryptoPriceFetcher {
    // Address of the Pyth price feed contract (update with the actual contract address)
    address public pythAddress;

    // Mapping to store fetched prices for specific assets
    mapping(bytes32 => int256) public assetPrices;

    // Event to log price updates
    event PriceUpdated(bytes32 indexed assetId, int256 price);

    // Constructor to set the Pyth address
    constructor(address _pythAddress) {
        pythAddress = _pythAddress;
    }

    // Function to fetch the price of a specific cryptocurrency
    function fetchPrice(bytes32 assetId) external {
        // Retrieve the price data from Pyth
        (int256 price, uint256 publishTime) = PriceFeed(pythAddress).getPrice(assetId);
        
        // Check for valid price data
        require(price > 0, "Invalid price retrieved");

        // Update the asset price in the mapping
        assetPrices[assetId] = price;

        // Emit an event for price update
        emit PriceUpdated(assetId, price);
    }

    // Function to get the latest price of an asset
    function getLatestPrice(bytes32 assetId) external view returns (int256) {
        // Return the latest price from the mapping
        require(assetPrices[assetId] != 0, "Price not available");
        return assetPrices[assetId];
    }
}
```
