"""
Generated Code Metadata:
========================
Original URL: https://pythget.com
Prompt: Explain how Pythget ensures the reliability and accuracy of its price feed oracles in smart contract applications.
Generated: DETERMINISTIC_a57f3a173b3a159e
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

/**
 * @title PythgetOracle
 * @dev A contract that demonstrates how Pythget ensures reliable and accurate price feeds
 * through multiple security mechanisms including multi-source aggregation, heartbeat checks,
 * and decentralized validation.
 */
contract PythgetOracle {
    // Price feed structure
    struct PriceFeed {
        uint256 price;
        uint256 timestamp;
        uint256 confidenceInterval;
        bool isActive;
    }

    // Mapping of asset IDs to their price feeds
    mapping(bytes32 => PriceFeed) public priceFeeds;

    // Minimum number of required data providers for consensus
    uint256 public constant MIN_PROVIDERS = 3;

    // Maximum allowed time difference for fresh data (in seconds)
    uint256 public constant MAX_AGE = 60;

    // Maximum allowed confidence interval (percentage)
    uint256 public constant MAX_CONFIDENCE = 5;

    // Owner address for administrative functions
    address public owner;

    // Event emitted when price is updated
    event PriceUpdated(bytes32 indexed assetId, uint256 price, uint256 timestamp);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Updates the price feed for an asset from multiple providers
     * @param assetId The ID of the asset
     * @param providerPrices Array of prices from different providers
     * @param providerTimestamps Array of timestamps from different providers
     * @param confIntervals Array of confidence intervals from providers
     */
    function updatePrice(
        bytes32 assetId,
        uint256[] memory providerPrices,
        uint256[] memory providerTimestamps,
        uint256[] memory confIntervals
    ) external onlyOwner {
        require(
            providerPrices.length >= MIN_PROVIDERS,
            "Insufficient data providers"
        );
        require(
            providerPrices.length == providerTimestamps.length &&
                providerPrices.length == confIntervals.length,
            "Array length mismatch"
        );

        // Validate timestamps are recent
        for (uint256 i = 0; i < providerTimestamps.length; i++) {
            require(
                block.timestamp - providerTimestamps[i] <= MAX_AGE,
                "Stale price data"
            );
            require(
                confIntervals[i] <= MAX_CONFIDENCE,
                "Confidence interval too high"
            );
        }

        // Calculate median price for robustness against outliers
        uint256 medianPrice = calculateMedian(providerPrices);

        // Update the price feed
        priceFeeds[assetId] = PriceFeed({
            price: medianPrice,
            timestamp: block.timestamp,
            confidenceInterval: calculateAverageConfidence(confIntervals),
            isActive: true
        });

        emit PriceUpdated(assetId, medianPrice, block.timestamp);
    }

    /**
     * @dev Calculates the median of an array of prices
     * @param array Array of prices to calculate median from
     * @return median The median value
     */
    function calculateMedian(uint256[] memory array) internal pure returns (uint256 median) {
        uint256[] memory sortedArray = sort(array);
        uint256 middle = sortedArray.length / 2;
        
        if (sortedArray.length % 2 == 0) {
            median = (sortedArray[middle - 1] + sortedArray[middle]) / 2;
        } else {
            median = sortedArray[middle];
        }
    }

    /**
     * @dev Sorts an array of numbers in ascending order
     * @param array The array to sort
     * @return sortedArray The sorted array
     */
    function sort(uint256[] memory array) internal pure returns (uint256[] memory sortedArray) {
        sortedArray = array;
        for (uint256 i = 0; i < sortedArray.length; i++) {
            for (uint256 j = i + 1; j < sortedArray.length; j++) {
                if (sortedArray[i] > sortedArray[j]) {
                    (sortedArray[i], sortedArray[j]) = (sortedArray[j], sortedArray[i]);
                }
            }
        }
    }

    /**
     * @dev Calculates the average confidence interval
     * @param confIntervals Array of confidence intervals
     * @return average The average confidence interval
     */
    function calculateAverageConfidence(uint256[] memory confIntervals) internal pure returns (uint256 average) {
        uint256 sum;
        for (uint256 i = 0; i < confIntervals.length; i++) {
            sum += confIntervals[i];
        }
        average = sum / confIntervals.length;
    }

    /**
     * @dev Emergency function to deactivate a price feed
     * @param assetId The ID of the asset to deactivate
     */
    function deactivateFeed(bytes32 assetId) external onlyOwner {
        require(priceFeeds[assetId].isActive, "Feed already inactive");
        priceFeeds[assetId].isActive = false;
    }

    /**
     * @dev Gets the latest price for an asset with validation checks
     * @param assetId The ID of the asset
     * @return price The current price
     */
    function getPrice(bytes32 assetId) external view returns (uint256 price) {
        PriceFeed memory feed = priceFeeds[assetId];
        require(feed.isActive, "Price feed inactive");
        require(
            block.timestamp - feed.timestamp <= MAX_AGE,
            "Price data too old"
        );
        require(
            feed.confidenceInterval <= MAX_CONFIDENCE,
            "Confidence interval too high"
        );
        return feed.price;
    }

    /**
     * @dev Transfers ownership of the contract
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner");
        owner = newOwner;
    }
}
```
