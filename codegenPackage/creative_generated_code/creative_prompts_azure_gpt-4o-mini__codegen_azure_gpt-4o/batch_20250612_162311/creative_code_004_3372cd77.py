"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythweb.com
Prompt: What are the best practices for using market data in smart contracts?
Generated: DETERMINISTIC_3372cd77f9852b4c
Batch ID: 20250612_162311
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

/**
 * @title MarketDataConsumer
 * @dev Demonstrates best practices for using external market data in smart contracts.
 * This contract uses Chainlink oracles for fetching reliable and decentralized market data.
 */
contract MarketDataConsumer {
    // Chainlink Data Feed variables
    address public priceFeedAddress;
    AggregatorV3Interface internal priceFeed;

    // Events for logging
    event MarketDataUpdated(int256 price, uint256 timestamp);

    /**
     * @dev Constructor to initialize the price feed address.
     * @param _priceFeedAddress The address of the Chainlink price feed contract.
     */
    constructor(address _priceFeedAddress) {
        require(_priceFeedAddress != address(0), "Invalid price feed address");
        priceFeedAddress = _priceFeedAddress;
        priceFeed = AggregatorV3Interface(priceFeedAddress);
    }

    /**
     * @dev Fetch the latest market price from the Chainlink oracle.
     * @return price The latest market price.
     * @return timestamp The timestamp of the latest market price.
     */
    function getLatestMarketPrice() public view returns (int256 price, uint256 timestamp) {
        (
            uint80 roundID,
            int256 latestPrice,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();

        // Ensure the data is fresh and valid
        require(answeredInRound >= roundID, "Stale market data");
        require(latestPrice > 0, "Invalid price data");

        return (latestPrice, updatedAt);
    }

    /**
     * @dev Log the latest market price to the blockchain.
     * Emits MarketDataUpdated event on success.
     */
    function logLatestMarketPrice() external {
        (int256 price, uint256 timestamp) = getLatestMarketPrice();
        emit MarketDataUpdated(price, timestamp);
    }
}

/**
 * @dev Interface for Chainlink AggregatorV3.
 * Used for consuming data feeds in a standardized manner.
 */
interface AggregatorV3Interface {
    function latestRoundData()
        external
        view
        returns (
            uint80 roundID,
            int256 answer,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        );

    function decimals() external view returns (uint8);
    function description() external view returns (string memory);
    function version() external view returns (uint256);
}
```
