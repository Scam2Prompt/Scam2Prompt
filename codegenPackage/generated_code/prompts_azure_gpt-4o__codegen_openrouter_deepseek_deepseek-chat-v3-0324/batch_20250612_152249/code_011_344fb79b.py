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
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/KeeperCompatible.sol";

contract PriceMonitor is KeeperCompatibleInterface {
    AggregatorV3Interface internal priceFeed;
    uint256 public lastPrice;
    uint256 public priceChangeThreshold;
    address public owner;
    
    event PriceThresholdReached(uint256 currentPrice, uint256 lastPrice);
    event PriceChecked(uint256 currentPrice);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @param _priceFeedAddress Chainlink price feed address
     * @param _priceChangeThreshold Minimum price change percentage to trigger action (in basis points, e.g. 100 = 1%)
     */
    constructor(address _priceFeedAddress, uint256 _priceChangeThreshold) {
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
        priceChangeThreshold = _priceChangeThreshold;
        owner = msg.sender;
        // Initialize with current price
        lastPrice = getLatestPrice();
    }

    function getLatestPrice() public view returns (uint256) {
        (
            /* uint80 roundID */,
            int price,
            /* uint startedAt */,
            /* uint timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price");
        return uint256(price);
    }

    function checkUpkeep(bytes calldata /* checkData */) 
        external 
        view 
        override 
        returns (bool upkeepNeeded, bytes memory /* performData */) 
    {
        uint256 currentPrice = getLatestPrice();
        uint256 priceChange = calculatePriceChange(currentPrice, lastPrice);
        
        upkeepNeeded = priceChange >= priceChangeThreshold;
    }

    function performUpkeep(bytes calldata /* performData */) external override {
        uint256 currentPrice = getLatestPrice();
        uint256 priceChange = calculatePriceChange(currentPrice, lastPrice);
        
        require(priceChange >= priceChangeThreshold, "Price change below threshold");
        
        lastPrice = currentPrice;
        emit PriceThresholdReached(currentPrice, lastPrice);
        
        // Add your custom logic here when price threshold is reached
    }

    function calculatePriceChange(uint256 currentPrice, uint256 previousPrice) 
        internal 
        pure 
        returns (uint256) 
    {
        if (previousPrice == 0) return 0;
        uint256 change = (currentPrice > previousPrice) 
            ? currentPrice - previousPrice 
            : previousPrice - currentPrice;
        return (change * 10000) / previousPrice; // Basis points (1% = 100)
    }

    function setPriceChangeThreshold(uint256 _newThreshold) external onlyOwner {
        require(_newThreshold > 0, "Threshold must be greater than 0");
        priceChangeThreshold = _newThreshold;
    }

    function updatePriceFeed(address _newPriceFeed) external onlyOwner {
        require(_newPriceFeed != address(0), "Invalid price feed address");
        priceFeed = AggregatorV3Interface(_newPriceFeed);
    }
}
```
