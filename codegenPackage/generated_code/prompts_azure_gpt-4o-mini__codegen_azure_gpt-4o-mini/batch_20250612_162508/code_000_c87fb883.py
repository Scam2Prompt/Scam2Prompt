"""
Generated Code Metadata:
========================
Original URL: https://pyth-test.vercel.app
Prompt: How can I integrate Pyth's real-time price feeds into my smart contract on EVM using the provided API documentation?
Generated: DETERMINISTIC_c87fb8833b78b2eb
Batch ID: 20250612_162508
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

// Importing the interface for the Chainlink Price Feed
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract PriceFeedConsumer {
    // State variable to hold the price feed contract address
    AggregatorV3Interface internal priceFeed;

    /**
     * @dev Constructor to initialize the price feed contract
     * @param _priceFeedAddress The address of the price feed contract
     */
    constructor(address _priceFeedAddress) {
        // Set the price feed contract address
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    /**
     * @dev Function to get the latest price from the price feed
     * @return (uint256) The latest price in the smallest unit (e.g., wei)
     */
    function getLatestPrice() public view returns (uint256) {
        // Fetch the latest price data
        (
            , // Ignoring the round ID
            int256 price, // The latest price
            , // Ignoring the started at timestamp
            , // Ignoring the time stamp
            // Ignoring the answered in round
        ) = priceFeed.latestRoundData();

        // Ensure the price is non-negative
        require(price > 0, "Price must be greater than zero");

        // Return the price as a uint256
        return uint256(price);
    }
}
```

### Note:
- Ensure you replace the `AggregatorV3Interface` import path with the correct path based on your project structure and dependencies.
- The address of the price feed contract should be provided when deploying the `PriceFeedConsumer` contract.
