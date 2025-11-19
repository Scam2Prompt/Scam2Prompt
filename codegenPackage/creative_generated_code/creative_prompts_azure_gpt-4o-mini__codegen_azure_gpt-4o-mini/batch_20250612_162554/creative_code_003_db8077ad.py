"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythclub.com
Prompt: What are the best practices for using market data oracles in smart contracts as described on pythclub.com?
Generated: DETERMINISTIC_db8077ad1c231424
Batch ID: 20250612_162554
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

// Importing the interface for the Oracle
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/// @title Market Data Oracle for Smart Contracts
/// @notice This contract demonstrates best practices for using market data oracles
contract MarketDataOracle {
    AggregatorV3Interface internal priceFeed;

    /// @dev Sets the address of the price feed contract
    /// @param _priceFeed Address of the price feed
    constructor(address _priceFeed) {
        require(_priceFeed != address(0), "Invalid price feed address");
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    /// @notice Fetches the latest price from the oracle
    /// @return The latest price as an integer (scaled up by 10^8)
    function getLatestPrice() public view returns (int) {
        (
            /* uint80 roundID */,
            int price,
            /* uint startedAt */,
            /* uint timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeed.latestRoundData();
        
        // Ensure the price is valid
        require(price > 0, "Price must be greater than zero");
        return price;
    }

    /// @notice Fetches the decimals used in the price feed
    /// @return The number of decimals for the price feed
    function getDecimals() public view returns (uint8) {
        return priceFeed.decimals();
    }

    /// @notice Fetches the round ID of the latest price
    /// @return The round ID of the latest price
    function getLatestRoundId() public view returns (uint80) {
        return priceFeed.latestRound();
    }

    /// @notice Checks if the latest price is valid and not stale
    /// @return Whether the latest price is valid
    function isPriceValid() public view returns (bool) {
        uint80 latestRound = priceFeed.latestRound();
        (, , , uint256 timeStamp, uint80 answeredInRound) = priceFeed.latestRoundData();
        return (latestRound == answeredInRound && (block.timestamp - timeStamp) < 60);
    }
}
```
