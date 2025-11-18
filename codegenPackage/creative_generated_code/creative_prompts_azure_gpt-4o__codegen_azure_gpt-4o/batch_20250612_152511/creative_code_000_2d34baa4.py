"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: Write a smart contract that integrates RedStone Classic (Push) Oracle to fetch price feeds for yield-bearing collateral on Ethereum. Include logic for heartbeat and deviation threshold updates.
Generated: DETERMINISTIC_2d34baa45f5da5e7
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Importing RedStone libraries for price feed integration
import "@redstone-finance/evm-connector/lib/RedstoneConsumer.sol";

contract YieldBearingCollateral is RedstoneConsumer {
    // State variables
    uint256 public lastUpdateTimestamp; // Tracks the last time price feed was updated
    uint256 public heartbeat;           // Maximum allowed time between updates
    uint256 public deviationThreshold;  // Maximum deviation allowed between price updates
    int256 public latestPrice;          // Tracks the latest price fetched from the oracle

    // Events
    event PriceUpdated(int256 indexed newPrice);
    event HeartbeatUpdated(uint256 indexed newHeartbeat);
    event DeviationThresholdUpdated(uint256 indexed newThreshold);

    // Constructor to initialize heartbeat and deviation threshold
    constructor(uint256 _heartbeat, uint256 _deviationThreshold) {
        require(_heartbeat > 0, "Heartbeat must be positive");
        require(_deviationThreshold > 0, "Deviation threshold must be positive");
        heartbeat = _heartbeat;
        deviationThreshold = _deviationThreshold;
        lastUpdateTimestamp = block.timestamp; // Initialize last update timestamp
    }

    /**
     * @dev Fetches the latest price from RedStone Classic Oracle.
     * Ensures heartbeat and deviation thresholds are respected.
     */
    function updatePrice() external {
        // Fetch data from the RedStone Oracle
        int256 price = getPriceFromOracle(); // RedStone library query function

        // Ensure heartbeat logic
        require(
            block.timestamp - lastUpdateTimestamp <= heartbeat,
            "Price update exceeds heartbeat limit"
        );

        // Ensure deviation threshold logic
        require(
            latestPrice == 0 || withinAllowedDeviation(latestPrice, price),
            "Price deviation exceeds threshold"
        );

        // Update state variables
        latestPrice = price;
        lastUpdateTimestamp = block.timestamp;

        // Emit event for price update
        emit PriceUpdated(price);
    }

    /**
     * @dev Updates the heartbeat interval.
     * @param _newHeartbeat New heartbeat value in seconds.
     */
    function updateHeartbeat(uint256 _newHeartbeat) external {
        require(_newHeartbeat > 0, "Heartbeat must be positive");
        heartbeat = _newHeartbeat;
        emit HeartbeatUpdated(_newHeartbeat);
    }

    /**
     * @dev Updates the deviation threshold percentage.
     * @param _newThreshold New threshold value in percentage (e.g., 5 for 5%).
     */
    function updateDeviationThreshold(uint256 _newThreshold) external {
        require(_newThreshold > 0, "Deviation threshold must be positive");
        deviationThreshold = _newThreshold;
        emit DeviationThresholdUpdated(_newThreshold);
    }

    /**
     * @dev Internal function to fetch the price from the Oracle using RedStone.
     * @return Price fetched from the Oracle.
     */
    function getPriceFromOracle() internal view returns (int256) {
        return getPriceFromDataFeed("ETH"); // Replace "ETH" with appropriate asset identifier
    }

    /**
     * @dev Internal function to check deviation threshold.
     * @param oldPrice The previous price.
     * @param newPrice The new price.
     * @return True if the new price is within the allowed deviation percentage, false otherwise.
     */
    function withinAllowedDeviation(int256 oldPrice, int256 newPrice)
        internal
        view
        returns (bool)
    {
        int256 priceChange = newPrice - oldPrice;
        int256 allowedChange = (oldPrice * int256(deviationThreshold)) / 100;
        return priceChange >= -allowedChange && priceChange <= allowedChange;
    }
}
```
