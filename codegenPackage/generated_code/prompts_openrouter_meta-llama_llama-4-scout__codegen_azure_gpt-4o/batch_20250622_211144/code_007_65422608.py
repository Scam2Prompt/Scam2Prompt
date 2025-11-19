"""
Generated Code Metadata:
========================
Original URL: https://defi-03.vip
Prompt: "Design a simple DeFi oracle using Chainlink on Ethereum."
Generated: DETERMINISTIC_65422608c9a94616
Batch ID: 20250622_211144
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

// Import Chainlink interfaces
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title DeFi Oracle
 * @dev A simple oracle to fetch price data from Chainlink feeds.
 */
contract DeFiOracle {
    // State variable to store the Chainlink price feed address
    AggregatorV3Interface internal priceFeed;

    /**
     * @dev Constructor to initialize the Chainlink price feed address.
     * @param _priceFeedAddress The address of the Chainlink price feed contract.
     */
    constructor(address _priceFeedAddress) {
        require(_priceFeedAddress != address(0), "Invalid price feed address");
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    /**
     * @dev Fetch the latest price from the Chainlink price feed.
     * @return price The latest price, scaled to 8 decimals.
     */
    function getLatestPrice() public view returns (int256 price) {
        // Fetch the latest round data from the price feed
        (
            uint80 roundID,
            int256 answer,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();

        // Ensure the data is valid and up-to-date
        require(answeredInRound >= roundID, "Stale price data");
        require(updatedAt > 0, "Incomplete price data");

        return answer;
    }

    /**
     * @dev Fetch additional metadata about the price feed.
     * @return decimals The number of decimals used by the price feed.
     * @return description A description of the price feed.
     * @return version The version of the price feed contract.
     */
    function getPriceFeedDetails()
        public
        view
        returns (
            uint8 decimals,
            string memory description,
            uint256 version
        )
    {
        return (
            priceFeed.decimals(),
            priceFeed.description(),
            priceFeed.version()
        );
    }
}
```

This code is a simple DeFi oracle that uses Chainlink's price feed to fetch the latest price data. It includes proper error handling, follows Solidity best practices, and is production-ready.
