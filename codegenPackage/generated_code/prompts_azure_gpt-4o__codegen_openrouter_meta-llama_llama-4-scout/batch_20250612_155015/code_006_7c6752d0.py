"""
Generated Code Metadata:
========================
Original URL: https://pythnet.com
Prompt: Write a smart contract function in Solidity that uses PythNet's market data to trigger an event when an asset price crosses a specific threshold.
Generated: DETERMINISTIC_7c6752d053b29458
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

import "@pythnetwork/pyth-contracts/src/Pyth.sol";
import "@pythnetwork/pyth-contracts/src/interfaces/IPyth.sol";

/**
 * @title PythNet Price Threshold Checker
 * @author [Your Name]
 * @notice This contract checks the price of an asset on PythNet and triggers an event when it crosses a specific threshold.
 */
contract PythNetPriceThresholdChecker {
    // Mapping of asset feeds to their corresponding prices
    mapping(bytes32 => uint80) public assetPrices;

    // Mapping of asset feeds to their corresponding thresholds
    mapping(bytes32 => uint256) public assetThresholds;

    // Event emitted when an asset price crosses its threshold
    event PriceThresholdCrossed(bytes32 indexed assetFeed, uint256 price, uint256 threshold);

    // PythNet contract instance
    IPyth public pyth;

    /**
     * @param _pyth Address of the PythNet contract
     */
    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }

    /**
     * @dev Updates the price of an asset and checks if it has crossed its threshold
     * @param assetFeed The feed ID of the asset
     * @param priceUpdateData The price update data from PythNet
     */
    function updatePriceAndCheckThreshold(bytes32 assetFeed, bytes[] memory priceUpdateData) public {
        // Update the price of the asset
        pyth.updatePriceFeeds(priceUpdateData);

        // Get the current price of the asset
        (, int256 price, , uint256 timestamp, ) = pyth.getPrice(assetFeed);

        // Check if the price has been updated successfully
        require(timestamp > 0, "Price not updated");

        // Get the threshold for the asset
        uint256 threshold = assetThresholds[assetFeed];

        // Check if a threshold has been set for the asset
        require(threshold > 0, "Threshold not set");

        // Check if the price has crossed the threshold
        if ((price > 0 && uint256(price) >= threshold) || (price < 0 && uint256(-price) >= threshold)) {
            // Trigger the event
            emit PriceThresholdCrossed(assetFeed, uint256(price), threshold);
        }
    }

    /**
     * @dev Sets the threshold for an asset
     * @param assetFeed The feed ID of the asset
     * @param threshold The threshold price
     */
    function setAssetThreshold(bytes32 assetFeed, uint256 threshold) public {
        // Check if the threshold is valid
        require(threshold > 0, "Invalid threshold");

        // Set the threshold for the asset
        assetThresholds[assetFeed] = threshold;
    }

    /**
     * @dev Gets the current price of an asset
     * @param assetFeed The feed ID of the asset
     * @return The current price of the asset
     */
    function getAssetPrice(bytes32 assetFeed) public view returns (uint256) {
        (, int256 price, , , ) = pyth.getPrice(assetFeed);
        return uint256(price);
    }
}
```
