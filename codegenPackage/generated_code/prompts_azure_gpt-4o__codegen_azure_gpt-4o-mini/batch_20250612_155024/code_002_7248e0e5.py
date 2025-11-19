"""
Generated Code Metadata:
========================
Original URL: https://pythpro.com
Prompt: Generate a smart contract snippet that fetches real-time market data using Pyth price feed oracles.
Generated: DETERMINISTIC_7248e0e57c5fb859
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

// Importing the Pyth price feed interface
import "@pythnetwork/pyth-sdk-solidity/contracts/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/contracts/Pyth.sol";

contract MarketDataFetcher {
    // Pyth price feed contract address (example address, replace with actual)
    address public pythAddress;
    Pyth public pyth;

    // Event to emit when price data is fetched
    event PriceDataFetched(int64 price, uint64 timestamp);

    // Constructor to initialize the Pyth price feed contract
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pythAddress = _pythAddress;
        pyth = Pyth(_pythAddress);
    }

    // Function to fetch the latest price for a given asset
    function fetchLatestPrice(bytes32 assetId) external returns (int64 price, uint64 timestamp) {
        // Fetch price data from Pyth
        Pyth.Price memory priceData = pyth.getPrice(assetId);
        
        // Check if the price data is valid
        require(priceData.valid, "Price data is not valid");
        
        // Emit the fetched price data
        emit PriceDataFetched(priceData.price, priceData.timestamp);
        
        // Return the price and timestamp
        return (priceData.price, priceData.timestamp);
    }
}
```
