"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Write a code snippet to integrate Chainlink Data Feeds for triggering smart contracts in a DeFi application.
Generated: DETERMINISTIC_8b743512db1e8d71
Batch ID: 20250612_160853
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

// Import the required Chainlink dependencies
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract demonstrates how to integrate Chainlink Data Feeds
contract DeFiTrigger is Ownable {
    AggregatorV3Interface internal priceFeed;

    // Event to emit when the condition is met
    event Triggered(string message, uint256 price);

    // Constructor to initialize the price feed address
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    // Function to get the latest price from the Chainlink data feed
    function getLatestPrice() public view returns (int256) {
        (
            /* uint80 roundID */,
            int256 price,
            /* uint startedAt */,
            /* uint timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeed.latestRoundData();
        return price;
    }

    // Function to trigger an action based on price condition
    function checkPriceAndTrigger(uint256 triggerPrice) external onlyOwner {
        int256 currentPrice = getLatestPrice();

        // Ensure price is not negative
        require(currentPrice > 0, "Invalid price data");

        // Check if the current price exceeds the trigger price
        if (uint256(currentPrice) > triggerPrice) {
            emit Triggered("Price exceeded trigger limit!", uint256(currentPrice));
            // Add additional logic here for the action to be triggered
        } else {
            // Optionally handle the case where the condition is not met
            emit Triggered("Price is below trigger limit.", uint256(currentPrice));
        }
    }
}
```
