"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Provide an example of integrating Chainlink Market and Data Feeds to trigger smart contracts based on asset price changes.
Generated: DETERMINISTIC_344fb79b3c2cba60
Batch ID: 20250612_152249
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

// Importing the Chainlink Aggregator interface
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract to monitor asset prices and trigger actions based on price changes
contract PriceTrigger is Ownable {
    // State variables
    AggregatorV3Interface internal priceFeed; // Chainlink price feed
    uint256 public lastPrice; // Last recorded price
    uint256 public priceThreshold; // Price change threshold for triggering actions

    // Event to log price updates
    event PriceUpdated(uint256 newPrice);

    // Constructor to initialize the price feed and threshold
    constructor(address _priceFeed, uint256 _priceThreshold) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        priceThreshold = _priceThreshold;
        lastPrice = getLatestPrice(); // Initialize lastPrice with the current price
    }

    // Function to get the latest price from the Chainlink price feed
    function getLatestPrice() public view returns (uint256) {
        (
            /* uint80 roundID */,
            int256 price,
            /* uint256 startedAt */,
            /* uint256 timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price data");
        return uint256(price);
    }

    // Function to check price and trigger action if the price has changed significantly
    function checkPrice() external {
        uint256 currentPrice = getLatestPrice();
        // Check if the price change exceeds the defined threshold
        if (currentPrice >= lastPrice + priceThreshold || currentPrice <= lastPrice - priceThreshold) {
            lastPrice = currentPrice; // Update lastPrice
            emit PriceUpdated(currentPrice); // Emit event for price update
            // Trigger your action here (e.g., execute another contract function)
        }
    }

    // Function to update the price threshold
    function updatePriceThreshold(uint256 newThreshold) external onlyOwner {
        priceThreshold = newThreshold;
    }

    // Function to withdraw any funds sent to the contract (if applicable)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
