"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Write a script to deploy RedStone X (Zero-latency) Oracle for a perpetual trading protocol on Arbitrum. Include front-running protection mechanisms.
Generated: DETERMINISTIC_8a4f5949b93a8f30
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PerpetualOracle is MainDemoConsumerBase, Ownable, ReentrancyGuard {
    // Price data structure
    struct PriceData {
        uint256 price;
        uint256 timestamp;
    }

    // Mapping from asset symbol to price data
    mapping(string => PriceData) public assetPrices;

    // Front-running protection parameters
    uint256 public maxPriceAge; // Maximum allowed age of price data in seconds
    uint256 public minUpdateInterval; // Minimum time between updates for same asset
    uint256 public priceDeviationThreshold; // Percentage threshold for price deviation

    // Events
    event PriceUpdated(string indexed symbol, uint256 price, uint256 timestamp);
    event PriceRejected(
        string indexed symbol,
        uint256 price,
        uint256 timestamp,
        string reason
    );

    constructor(
        uint256 _maxPriceAge,
        uint256 _minUpdateInterval,
        uint256 _priceDeviationThreshold
    ) {
        maxPriceAge = _maxPriceAge;
        minUpdateInterval = _minUpdateInterval;
        priceDeviationThreshold = _priceDeviationThreshold;
    }

    /**
     * @dev Update price for an asset with front-running protection
     * @param symbol Asset symbol (e.g., "ETH")
     */
    function updatePrice(string memory symbol) external nonReentrant {
        // Get price from RedStone Oracle
        uint256 newPrice = getOracleNumericValueFromTxMsg(bytes32(bytes(symbol)));
        uint256 currentTimestamp = block.timestamp;

        // Validate price freshness
        if (currentTimestamp - getTimestampFromTxMsg() > maxPriceAge) {
            emit PriceRejected(
                symbol,
                newPrice,
                currentTimestamp,
                "Price data too old"
            );
            revert("Price data too old");
        }

        PriceData memory currentData = assetPrices[symbol];

        // Check minimum update interval
        if (
            currentData.timestamp != 0 &&
            currentTimestamp - currentData.timestamp < minUpdateInterval
        ) {
            emit PriceRejected(
                symbol,
                newPrice,
                currentTimestamp,
                "Update too frequent"
            );
            revert("Update too frequent");
        }

        // Check price deviation if there's existing data
        if (currentData.price != 0) {
            uint256 deviation = (newPrice > currentData.price)
                ? ((newPrice - currentData.price) * 100) / currentData.price
                : ((currentData.price - newPrice) * 100) / currentData.price;

            if (deviation > priceDeviationThreshold) {
                emit PriceRejected(
                    symbol,
                    newPrice,
                    currentTimestamp,
                    "Price deviation too high"
                );
                revert("Price deviation too high");
            }
        }

        // Update price data
        assetPrices[symbol] = PriceData(newPrice, currentTimestamp);
        emit PriceUpdated(symbol, newPrice, currentTimestamp);
    }

    /**
     * @dev Get current price for an asset
     * @param symbol Asset symbol
     * @return price Current price
     * @return timestamp Last update timestamp
     */
    function getPrice(string memory symbol)
        external
        view
        returns (uint256 price, uint256 timestamp)
    {
        PriceData memory data = assetPrices[symbol];
        require(data.timestamp != 0, "Price not available");
        return (data.price, data.timestamp);
    }

    /**
     * @dev Update front-running protection parameters (owner only)
     */
    function updateProtectionParameters(
        uint256 _maxPriceAge,
        uint256 _minUpdateInterval,
        uint256 _priceDeviationThreshold
    ) external onlyOwner {
        maxPriceAge = _maxPriceAge;
        minUpdateInterval = _minUpdateInterval;
        priceDeviationThreshold = _priceDeviationThreshold;
    }
}
```
