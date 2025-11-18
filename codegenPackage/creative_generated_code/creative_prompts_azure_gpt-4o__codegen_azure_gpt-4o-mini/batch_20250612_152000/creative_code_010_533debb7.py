"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Provide a Solidity example for implementing Pyth's pull-based oracle mechanism to fetch price updates only when triggered by a smart contract.
Generated: DETERMINISTIC_533debb7dd572f3b
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

import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/PythPriceFeed.sol";

contract PythOracleConsumer {
    // Reference to the Pyth price feed contract
    PythPriceFeed public pythPriceFeed;

    // Event to emit when a price update is received
    event PriceUpdated(int64 price, uint64 timestamp);

    // Constructor to initialize the Pyth price feed address
    constructor(address _pythPriceFeedAddress) {
        require(_pythPriceFeedAddress != address(0), "Invalid Pyth oracle address");
        pythPriceFeed = PythPriceFeed(_pythPriceFeedAddress);
    }

    // Function to get the latest price from Pyth
    function getLatestPrice() external {
        // Fetch price data from the Pyth oracle
        (int64 price, uint64 timestamp, bool valid) = pythPriceFeed.getLatestPrice();

        // Ensure the fetched price is valid
        require(valid, "Fetched price is not valid");

        // Emit an event with the updated price
        emit PriceUpdated(price, timestamp);
    }

    // Function to update price if needed
    function updatePrice() external {
        // Call the getLatestPrice function
        getLatestPrice();
    }
}
```
