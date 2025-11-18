"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eeenlist-pyth.pages.dev
Prompt: Write a smart contract that calculates the average price of BTC/USD over the last 7 days using Pyth Network's benchmarks and updates the value on-chain.
Generated: DETERMINISTIC_3f7e3250441bd1da
Batch ID: 20250612_153246
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

// Import Pyth interface for fetching BTC/USD data
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract BTCUSDPriceAverage {
    // Address of the Pyth contract on the corresponding chain
    IPyth public pythContract;

    // Pyth price identifier for BTC/USD
    bytes32 public constant BTC_USD_PRICE_ID = 0xYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY;

    // Number of days for the average calculation
    uint256 public constant DAYS = 7;

    // Mapping to store daily prices
    mapping(uint256 => int256) public dailyPrices;

    // Last updated timestamp
    uint256 public lastUpdatedTimestamp;

    // Event triggered when average price is updated
    event AveragePriceUpdated(int256 averagePrice);

    constructor(address _pythContractAddress) {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        pythContract = IPyth(_pythContractAddress);
    }

    /**
     * @dev Fetch BTC/USD price from Pyth and store it as the daily price.
     * Only callable once per day.
     */
    function updateDailyPrice() external {
        // Ensure only one update per day
        uint256 currentDay = block.timestamp / 1 days;
        require(currentDay > lastUpdatedTimestamp / 1 days, "Already updated today");

        // Fetch the BTC/USD price from Pyth
        try pythContract.getPriceUnsafe(BTC_USD_PRICE_ID) returns (IPyth.Price memory priceData) {
            require(priceData.price > 0, "Invalid price data");

            // Store the daily price
            dailyPrices[currentDay % DAYS] = priceData.price;
            lastUpdatedTimestamp = block.timestamp;

            // Emit event
            emit AveragePriceUpdated(calculateAveragePrice());
        } catch {
            revert("Failed to fetch price data from Pyth");
        }
    }

    /**
     * @dev Calculate the average price of BTC/USD over the last DAYS.
     * @return averagePrice The average price.
     */
    function calculateAveragePrice() public view returns (int256 averagePrice) {
        int256 sum = 0;
        uint256 count = 0;

        for (uint256 i = 0; i < DAYS; i++) {
            // Only include valid prices in the calculation
            if (dailyPrices[i] > 0) {
                sum += dailyPrices[i];
                count++;
            }
        }

        // Return average price (avoid division by zero)
        require(count > 0, "No valid prices available for calculation");
        return sum / int256(count);
    }
}
```
