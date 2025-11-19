"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Write a smart contract that integrates RedStone Classic (Push) Oracle to fetch price feeds for yield-bearing collateral on Ethereum. Include logic for heartbeat and deviation threshold updates.
Generated: DETERMINISTIC_2d34baa45f5da5e7
Batch ID: 20250612_152511
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

import "@redstone-finance/evm-connector/contracts/data-services/MainDemoConsumerBase.sol";

/**
 * @title YieldCollateralOracle
 * @dev A smart contract that integrates RedStone Classic Oracle to fetch price feeds
 * for yield-bearing collateral with heartbeat and deviation threshold functionality.
 */
contract YieldCollateralOracle is MainDemoConsumerBase {
    // Struct to store price feed details
    struct PriceFeed {
        uint256 price;
        uint256 timestamp;
        uint256 deviationThreshold; // in basis points (1% = 100)
        uint256 heartbeat; // in seconds
    }

    // Mapping from collateral symbol to price feed data
    mapping(string => PriceFeed) public priceFeeds;

    // Events
    event PriceUpdated(string indexed symbol, uint256 price, uint256 timestamp);
    event DeviationThresholdUpdated(string indexed symbol, uint256 threshold);
    event HeartbeatUpdated(string indexed symbol, uint256 heartbeat);

    /**
     * @dev Initializes the contract with RedStone configuration
     * @param _redstoneAdapterAddress The address of RedStone Adapter contract
     */
    constructor(address _redstoneAdapterAddress) {
        // Set the RedStone Adapter address
        setRedstoneAdapter(_redstoneAdapterAddress);
    }

    /**
     * @dev Updates the price feed for a given collateral symbol
     * @param symbol The collateral symbol (e.g., "stETH")
     */
    function updatePrice(string memory symbol) public {
        // Get the latest price from RedStone Oracle
        uint256 newPrice = getOracleNumericValueFromTxMsg(bytes32(bytes(symbol)));

        // Get the current price feed data
        PriceFeed storage feed = priceFeeds[symbol];

        // Check if price needs to be updated based on deviation or heartbeat
        bool shouldUpdate = shouldUpdatePrice(feed, newPrice);

        if (shouldUpdate) {
            // Update the price feed
            feed.price = newPrice;
            feed.timestamp = block.timestamp;

            emit PriceUpdated(symbol, newPrice, block.timestamp);
        }
    }

    /**
     * @dev Internal function to determine if price should be updated
     * @param feed The current price feed data
     * @param newPrice The new price from oracle
     * @return bool Whether price should be updated
     */
    function shouldUpdatePrice(PriceFeed memory feed, uint256 newPrice) internal view returns (bool) {
        // First update
        if (feed.timestamp == 0) {
            return true;
        }

        // Check heartbeat
        if (block.timestamp >= feed.timestamp + feed.heartbeat) {
            return true;
        }

        // Check deviation threshold
        uint256 deviation = calculateDeviation(feed.price, newPrice);
        if (deviation >= feed.deviationThreshold) {
            return true;
        }

        return false;
    }

    /**
     * @dev Calculates price deviation in basis points
     * @param oldPrice The previous price
     * @param newPrice The new price
     * @return uint256 Deviation in basis points
     */
    function calculateDeviation(uint256 oldPrice, uint256 newPrice) public pure returns (uint256) {
        if (oldPrice == 0) return type(uint256).max;
        
        uint256 difference = oldPrice > newPrice ? oldPrice - newPrice : newPrice - oldPrice;
        return (difference * 10000) / oldPrice; // Convert to basis points
    }

    /**
     * @dev Sets the deviation threshold for a collateral symbol
     * @param symbol The collateral symbol
     * @param threshold The new deviation threshold in basis points
     */
    function setDeviationThreshold(string memory symbol, uint256 threshold) external {
        require(threshold > 0, "Threshold must be greater than 0");
        priceFeeds[symbol].deviationThreshold = threshold;
        emit DeviationThresholdUpdated(symbol, threshold);
    }

    /**
     * @dev Sets the heartbeat interval for a collateral symbol
     * @param symbol The collateral symbol
     * @param heartbeat The new heartbeat interval in seconds
     */
    function setHeartbeat(string memory symbol, uint256 heartbeat) external {
        require(heartbeat > 0, "Heartbeat must be greater than 0");
        priceFeeds[symbol].heartbeat = heartbeat;
        emit HeartbeatUpdated(symbol, heartbeat);
    }

    /**
     * @dev Gets the latest price for a collateral symbol
     * @param symbol The collateral symbol
     * @return uint256 The latest price
     */
    function getPrice(string memory symbol) public view returns (uint256) {
        PriceFeed memory feed = priceFeeds[symbol];
        require(feed.timestamp > 0, "Price feed not initialized");
        return feed.price;
    }

    /**
     * @dev Gets the timestamp of the last price update
     * @param symbol The collateral symbol
     * @return uint256 The timestamp of last update
     */
    function getPriceTimestamp(string memory symbol) public view returns (uint256) {
        return priceFeeds[symbol].timestamp;
    }
}
```
