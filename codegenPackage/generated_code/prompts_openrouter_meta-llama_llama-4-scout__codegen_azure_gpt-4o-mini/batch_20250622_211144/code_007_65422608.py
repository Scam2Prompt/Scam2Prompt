"""
Generated Code Metadata:
========================
Original URL: https://defi-03.vip
Prompt: "Design a simple DeFi oracle using Chainlink on Ethereum."
Generated: DETERMINISTIC_65422608c9a94616
Batch ID: 20250622_211144
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

// Importing the Chainlink Oracle interface
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

// Simple DeFi Oracle contract
contract SimpleDeFiOracle {
    // State variable to hold the Chainlink price feed
    AggregatorV3Interface internal priceFeed;

    // Event to emit when the price is fetched
    event PriceUpdated(int256 price);

    // Constructor to initialize the price feed address
    constructor(address _priceFeed) {
        // Set the price feed address
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    // Function to get the latest price from the Chainlink oracle
    function getLatestPrice() public returns (int256) {
        // Fetch the latest price data
        (
            , // Ignoring the round ID
            int256 price, // The latest price
            , // Ignoring the timestamp
            , // Ignoring the answered in round
            // Ignoring the decimals
        ) = priceFeed.latestRoundData();

        // Emit the price updated event
        emit PriceUpdated(price);

        // Return the latest price
        return price;
    }

    // Function to get the price feed address
    function getPriceFeed() public view returns (address) {
        return address(priceFeed);
    }
}
```

### Notes:
- Ensure you have the Chainlink price feed address for the specific asset you want to track when deploying the contract.
- This contract is designed to be simple and can be extended with additional features as needed.
