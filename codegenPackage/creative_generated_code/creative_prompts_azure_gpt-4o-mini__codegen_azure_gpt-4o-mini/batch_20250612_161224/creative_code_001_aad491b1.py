"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: Write a code snippet to connect RedStone's data feeds to a smart contract on Ethereum.
Generated: DETERMINISTIC_aad491b1d6a7a4b3
Batch ID: 20250612_161224
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

// Importing necessary interfaces for the Oracle
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract RedStoneDataFeed {
    // State variable to store the address of the data feed
    AggregatorV3Interface internal dataFeed;

    // Event to emit when new data is received
    event DataUpdated(uint256 indexed price, uint256 indexed timestamp);

    // Constructor to initialize the contract with the data feed address
    constructor(address _dataFeed) {
        require(_dataFeed != address(0), "Invalid data feed address");
        dataFeed = AggregatorV3Interface(_dataFeed);
    }

    // Function to get the latest price from the data feed
    function getLatestPrice() public view returns (uint256) {
        // Fetch the latest round data
        (
            , // Ignoring roundId
            int256 price,
            uint256 startedAt,
            uint256 timeStamp,
            uint80 answeredInRound
        ) = dataFeed.latestRoundData();

        // Ensure the price is valid and the data is fresh
        require(timeStamp > 0, "Price data not available");
        require(answeredInRound >= dataFeed.latestRound(), "Stale data");

        // Emit the data update event
        emit DataUpdated(uint256(price), timeStamp);
        
        return uint256(price);
    }
}
```
