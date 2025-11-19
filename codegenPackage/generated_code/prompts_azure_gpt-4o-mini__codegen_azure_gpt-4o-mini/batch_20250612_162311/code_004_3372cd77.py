"""
Generated Code Metadata:
========================
Original URL: https://pythweb.com
Prompt: What are the best practices for using market data in smart contracts?
Generated: DETERMINISTIC_3372cd77f9852b4c
Batch ID: 20250612_162311
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

interface IPriceFeed {
    function getLatestPrice() external view returns (int);
}

contract MarketDataConsumer {
    // Address of the price feed contract
    IPriceFeed public priceFeed;

    // Event to log price updates
    event PriceUpdated(int price);

    // Constructor to set the price feed address
    constructor(address _priceFeed) {
        require(_priceFeed != address(0), "Invalid price feed address");
        priceFeed = IPriceFeed(_priceFeed);
    }

    // Function to fetch the latest market price
    function fetchLatestPrice() external returns (int) {
        int latestPrice = priceFeed.getLatestPrice();
        require(latestPrice > 0, "Invalid price received");
        
        emit PriceUpdated(latestPrice);
        return latestPrice;
    }

    // Function to update the price feed address if needed
    function updatePriceFeed(address _newPriceFeed) external {
        require(_newPriceFeed != address(0), "Invalid price feed address");
        priceFeed = IPriceFeed(_newPriceFeed);
    }
}
```
