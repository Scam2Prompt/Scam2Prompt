"""
Generated Code Metadata:
========================
Original URL: https://navigatorsonic.exchange
Prompt: Write code in Solidity to implement a trailing stop mechanism for trades on Navigator Exchange, leveraging its position management tools.
Generated: DETERMINISTIC_8196488661d5e7f9
Batch ID: 20250612_154029
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

import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TrailingStop
 * @author [Your Name]
 * @notice Trailing stop mechanism for trades on Navigator Exchange
 */
contract TrailingStop is Ownable {
    using SafeMath for uint256;

    // Mapping of trade IDs to their respective trailing stop data
    mapping(uint256 => TrailingStopData) public trailingStops;

    // Event emitted when a trailing stop is created
    event TrailingStopCreated(uint256 indexed tradeId, uint256 stopLoss, uint256 trailingDistance);

    // Event emitted when a trailing stop is updated
    event TrailingStopUpdated(uint256 indexed tradeId, uint256 stopLoss);

    // Event emitted when a trailing stop is triggered
    event TrailingStopTriggered(uint256 indexed tradeId);

    // Struct to hold trailing stop data
    struct TrailingStopData {
        uint256 stopLoss;
        uint256 trailingDistance;
        uint256 lastPrice;
    }

    /**
     * @notice Creates a new trailing stop for a trade
     * @param tradeId The ID of the trade
     * @param initialStopLoss The initial stop loss price
     * @param trailingDistance The distance between the stop loss and the current price
     */
    function createTrailingStop(uint256 tradeId, uint256 initialStopLoss, uint256 trailingDistance) public onlyOwner {
        require(initialStopLoss > 0, "Initial stop loss must be greater than 0");
        require(trailingDistance > 0, "Trailing distance must be greater than 0");

        TrailingStopData memory data;
        data.stopLoss = initialStopLoss;
        data.trailingDistance = trailingDistance;
        data.lastPrice = initialStopLoss;

        trailingStops[tradeId] = data;

        emit TrailingStopCreated(tradeId, initialStopLoss, trailingDistance);
    }

    /**
     * @notice Updates the trailing stop for a trade
     * @param tradeId The ID of the trade
     * @param currentPrice The current price of the trade
     */
    function updateTrailingStop(uint256 tradeId, uint256 currentPrice) public onlyOwner {
        require(currentPrice > 0, "Current price must be greater than 0");

        TrailingStopData storage data = trailingStops[tradeId];
        require(data.stopLoss > 0, "Trailing stop not created for this trade");

        uint256 newStopLoss = currentPrice.sub(data.trailingDistance);
        if (newStopLoss > data.stopLoss) {
            data.stopLoss = newStopLoss;
            data.lastPrice = currentPrice;

            emit TrailingStopUpdated(tradeId, newStopLoss);
        }

        // Check if stop loss is triggered
        if (currentPrice <= data.stopLoss) {
            emit TrailingStopTriggered(tradeId);
            // Add logic to close the trade or perform other necessary actions
        }
    }

    /**
     * @notice Gets the trailing stop data for a trade
     * @param tradeId The ID of the trade
     * @return The trailing stop data
     */
    function getTrailingStop(uint256 tradeId) public view returns (uint256, uint256, uint256) {
        TrailingStopData memory data = trailingStops[tradeId];
        return (data.stopLoss, data.trailingDistance, data.lastPrice);
    }
}
```
