"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythpro.com
Prompt: Generate a smart contract snippet that fetches real-time market data using Pyth price feed oracles.
Generated: DETERMINISTIC_7248e0e57c5fb859
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

// Import the Pyth price feed oracle interface
import "@pythnetwork/pyth-sdk-solidity/contracts/interfaces/IPyth.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract to fetch real-time market data from Pyth oracles
contract MarketDataFetcher is Ownable {
    // Pyth Oracle interface
    IPyth public pyth;

    // Event to emit whenever market data is fetched
    event MarketDataFetched(int64 price, uint64 timestamp);

    // Constructor to set the Pyth oracle address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to fetch the latest price for a given asset ID
    function fetchLatestPrice(bytes32 assetId) external onlyOwner returns (int64 price, uint64 timestamp) {
        // Validate input
        require(assetId != bytes32(0), "Invalid asset ID");

        // Fetch price information from Pyth
        (int64 latestPrice, uint64 latestTimestamp) = pyth.getPrice(assetId);

        // Emit an event with the fetched market data
        emit MarketDataFetched(latestPrice, latestTimestamp);

        // Return the fetched price and timestamp
        return (latestPrice, latestTimestamp);
    }

    // Function to update the Pyth oracle address (onlyOwner can call)
    function updatePythAddress(address _newPythAddress) external onlyOwner {
        require(_newPythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_newPythAddress);
    }
}
```
