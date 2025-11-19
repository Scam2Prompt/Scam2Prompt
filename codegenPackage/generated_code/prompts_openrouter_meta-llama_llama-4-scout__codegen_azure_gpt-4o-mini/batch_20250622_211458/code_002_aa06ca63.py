"""
Generated Code Metadata:
========================
Original URL: https://blockchainsupport.infy.uk
Prompt: "Write a Solidity smart contract example that utilizes blockchain oracles for real-world data integration."
Generated: DETERMINISTIC_aa06ca63bcf2e561
Batch ID: 20250622_211458
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

// Importing the interface for the Chainlink Oracle
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract RealWorldDataConsumer {
    // State variable to store the price of an asset
    int256 public assetPrice;

    // Address of the Chainlink price feed contract
    AggregatorV3Interface internal priceFeed;

    // Event to emit when the price is updated
    event PriceUpdated(int256 newPrice);

    /**
     * @dev Constructor to initialize the price feed address
     * @param _priceFeedAddress The address of the Chainlink price feed contract
     */
    constructor(address _priceFeedAddress) {
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    /**
     * @dev Function to fetch the latest price from the oracle
     * @return The latest price of the asset
     */
    function fetchLatestPrice() public returns (int256) {
        // Fetching the latest price data from the oracle
        (
            /* uint80 roundID */,
            int256 price,
            /* uint startedAt */,
            /* uint timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeed.latestRoundData();

        // Check if the price is valid
        require(price > 0, "Invalid price received from oracle");

        // Update the state variable with the new price
        assetPrice = price;

        // Emit an event for the price update
        emit PriceUpdated(assetPrice);

        return assetPrice;
    }

    /**
     * @dev Function to get the latest price without updating the state
     * @return The latest price of the asset
     */
    function getLatestPrice() public view returns (int256) {
        (
            /* uint80 roundID */,
            int256 price,
            /* uint startedAt */,
            /* uint timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeed.latestRoundData();

        // Check if the price is valid
        require(price > 0, "Invalid price received from oracle");

        return price;
    }
}
```
