"""
Generated Code Metadata:
========================
Original URL: https://pythsite.com
Prompt: Write a smart contract that integrates Pyth price feed oracles to calculate the average price of an asset over a specified time period.
Generated: DETERMINISTIC_cf415609ed930cdd
Batch ID: 20250612_155015
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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/Pyth.sol";

/**
 * @title PythPriceFeedOracle
 * @author [Your Name]
 * @notice This contract integrates Pyth price feed oracles to calculate the average price of an asset over a specified time period.
 */
contract PythPriceFeedOracle {
    // Mapping of asset feeds to their respective prices
    mapping(address => mapping(uint256 => uint256)) public assetPrices;

    // Mapping of asset feeds to their respective timestamps
    mapping(address => mapping(uint256 => uint256)) public assetTimestamps;

    // Pyth oracle instance
    IPyth public pyth;

    // Mapping of asset feeds to their respective cumulative prices
    mapping(address => uint256) public cumulativePrices;

    // Mapping of asset feeds to their respective count of prices
    mapping(address => uint256) public priceCounts;

    /**
     * @param _pyth Address of the Pyth oracle instance
     */
    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }

    /**
     * @dev Updates the price of an asset feed
     * @param assetFeed Address of the asset feed
     */
    function updatePrice(address assetFeed) public {
        // Get the latest price update from Pyth
        (, int64 price, , uint64 timestamp, ) = pyth.getPrice(assetFeed);

        // Check if the price update is valid
        require(price > 0, "Invalid price update");

        // Update the asset price and timestamp
        assetPrices[assetFeed][timestamp] = uint256(price);
        assetTimestamps[assetFeed][timestamp] = timestamp;

        // Update the cumulative price and count
        cumulativePrices[assetFeed] += uint256(price);
        priceCounts[assetFeed]++;
    }

    /**
     * @dev Calculates the average price of an asset feed over a specified time period
     * @param assetFeed Address of the asset feed
     * @param startTimestamp Start of the time period
     * @param endTimestamp End of the time period
     * @return The average price of the asset feed over the specified time period
     */
    function getAveragePrice(address assetFeed, uint256 startTimestamp, uint256 endTimestamp) public view returns (uint256) {
        // Get the prices of the asset feed within the time period
        uint256 cumulativePrice;
        uint256 count;
        for (uint256 timestamp = startTimestamp; timestamp <= endTimestamp; timestamp++) {
            if (assetTimestamps[assetFeed][timestamp] != 0) {
                cumulativePrice += assetPrices[assetFeed][timestamp];
                count++;
            }
        }

        // Check if there are any prices within the time period
        require(count > 0, "No prices available within the time period");

        // Return the average price
        return cumulativePrice / count;
    }

    /**
     * @dev Gets the latest price of an asset feed
     * @param assetFeed Address of the asset feed
     * @return The latest price of the asset feed
     */
    function getLatestPrice(address assetFeed) public view returns (uint256) {
        // Get the latest price update from Pyth
        (, int64 price, , , ) = pyth.getPrice(assetFeed);

        // Return the latest price
        return uint256(price);
    }
}
```
