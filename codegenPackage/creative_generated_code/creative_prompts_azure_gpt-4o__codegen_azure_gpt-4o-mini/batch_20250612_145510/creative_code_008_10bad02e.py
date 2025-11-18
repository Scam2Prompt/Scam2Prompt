"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-dioneprotocol.pages.dev
Prompt: Develop a Solidity contract that uses Chainlink oracles on the Odyssey Chain to fetch external data, ensuring compatibility with the chain's scalable infrastructure.
Generated: DETERMINISTIC_10bad02e17f81eea
Batch ID: 20250612_145510
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

// Import Chainlink interface for interacting with price feeds
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ExternalDataFetcher
 * @dev This contract fetches external data using Chainlink oracles
 */
contract ExternalDataFetcher is Ownable {
    AggregatorV3Interface internal priceFeed;
    
    // Event emitted when new data is fetched
    event DataFetched(int256 price, uint256 timestamp);

    /**
     * @dev Constructor to initialize the price feed address
     * @param _priceFeed The address of the Chainlink price feed contract
     */
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    /**
     * @dev Fetch the latest price from the Chainlink price feed
     * @return price The latest price as an integer
     * @return timestamp The timestamp of when the price was fetched
     */
    function fetchLatestPrice() external returns (int256 price, uint256 timestamp) {
        // Fetching the latest price data
        (
            uint80 roundID,
            int256 answer,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();

        // Ensure the data is valid
        require(answeredInRound >= roundID, "Stale data");

        // Emit event for fetched data
        emit DataFetched(answer, updatedAt);

        return (answer, updatedAt);
    }

    /**
     * @dev Update the price feed address
     * @param _priceFeed The new price feed address
     */
    function updatePriceFeed(address _priceFeed) external onlyOwner {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }
}
```
