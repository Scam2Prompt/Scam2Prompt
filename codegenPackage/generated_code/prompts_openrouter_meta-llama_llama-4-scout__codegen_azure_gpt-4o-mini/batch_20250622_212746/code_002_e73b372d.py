"""
Generated Code Metadata:
========================
Original URL: https://connectsflrsync.online
Prompt: Generate a smart contract code using Solidity to utilize Flare Time Series Oracle (FTSO) for fetching price and data feeds on Flare Network.
Generated: DETERMINISTIC_e73b372d636e8522
Batch ID: 20250622_212746
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

// Importing the interface for the Flare Time Series Oracle (FTSO)
interface IFTSO {
    function getLatestPrice(bytes32 _dataId) external view returns (uint256);
}

contract PriceFeedConsumer {
    // Address of the FTSO contract
    IFTSO public ftsOContract;

    // Event to emit when a price is fetched
    event PriceFetched(bytes32 indexed dataId, uint256 price);

    // Constructor to set the FTSO contract address
    constructor(address _ftsoAddress) {
        require(_ftsoAddress != address(0), "Invalid FTSO address");
        ftsOContract = IFTSO(_ftsoAddress);
    }

    // Function to fetch the latest price for a given data ID
    function fetchLatestPrice(bytes32 _dataId) external returns (uint256) {
        // Fetch the latest price from the FTSO
        uint256 price = ftsOContract.getLatestPrice(_dataId);
        
        // Emit an event with the fetched price
        emit PriceFetched(_dataId, price);
        
        return price;
    }

    // Function to fetch the latest price and handle potential errors
    function safeFetchLatestPrice(bytes32 _dataId) external returns (uint256) {
        uint256 price;
        try ftsOContract.getLatestPrice(_dataId) returns (uint256 fetchedPrice) {
            price = fetchedPrice;
        } catch {
            revert("Failed to fetch price from FTSO");
        }

        // Emit an event with the fetched price
        emit PriceFetched(_dataId, price);
        
        return price;
    }
}
```
