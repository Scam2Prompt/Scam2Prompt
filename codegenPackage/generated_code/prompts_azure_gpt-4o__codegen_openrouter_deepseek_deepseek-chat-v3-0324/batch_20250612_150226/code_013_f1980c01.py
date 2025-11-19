"""
Generated Code Metadata:
========================
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: Write a smart contract that uses Chainlink's Market Feeds to calculate and display the average price of a cryptocurrency.
Generated: DETERMINISTIC_f1980c01258ad675
Batch ID: 20250612_150226
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

/**
 * @title CryptoPriceAverager
 * @dev A smart contract that calculates and displays the average price of a cryptocurrency
 * using Chainlink's Market Feeds.
 */
contract CryptoPriceAverager {
    // Array to store price feed addresses
    address[] public priceFeedAddresses;
    
    // Mapping to store price feed interfaces
    mapping(address => AggregatorV3Interface) public priceFeeds;
    
    // Event to log average price calculation
    event AveragePriceCalculated(uint256 averagePrice, uint256 timestamp);
    
    /**
     * @dev Constructor to initialize the contract with price feed addresses
     * @param _priceFeedAddresses Array of Chainlink price feed addresses
     */
    constructor(address[] memory _priceFeedAddresses) {
        require(_priceFeedAddresses.length > 0, "At least one price feed address required");
        
        for (uint256 i = 0; i < _priceFeedAddresses.length; i++) {
            address feedAddress = _priceFeedAddresses[i];
            require(feedAddress != address(0), "Invalid price feed address");
            priceFeeds[feedAddress] = AggregatorV3Interface(feedAddress);
            priceFeedAddresses.push(feedAddress);
        }
    }
    
    /**
     * @dev Adds a new price feed address to the contract
     * @param _priceFeedAddress The Chainlink price feed address to add
     */
    function addPriceFeed(address _priceFeedAddress) external {
        require(_priceFeedAddress != address(0), "Invalid price feed address");
        require(address(priceFeeds[_priceFeedAddress]) == address(0), "Price feed already exists");
        
        priceFeeds[_priceFeedAddress] = AggregatorV3Interface(_priceFeedAddress);
        priceFeedAddresses.push(_priceFeedAddress);
    }
    
    /**
     * @dev Gets the latest price from a specific price feed
     * @param _priceFeedAddress The Chainlink price feed address to query
     * @return The latest price and timestamp
     */
    function getLatestPrice(address _priceFeedAddress) public view returns (int256, uint256) {
        require(address(priceFeeds[_priceFeedAddress]) != address(0), "Price feed not found");
        
        (
            uint80 roundID,
            int256 price,
            uint256 startedAt,
            uint256 timestamp,
            uint80 answeredInRound
        ) = priceFeeds[_priceFeedAddress].latestRoundData();
        
        require(price > 0, "Invalid price returned");
        require(timestamp > 0, "Invalid timestamp returned");
        require(answeredInRound >= roundID, "Stale price data");
        
        return (price, timestamp);
    }
    
    /**
     * @dev Calculates the average price across all registered price feeds
     * @return The average price and the timestamp of the calculation
     */
    function calculateAveragePrice() external returns (uint256, uint256) {
        require(priceFeedAddresses.length > 0, "No price feeds registered");
        
        uint256 sum = 0;
        uint256 count = 0;
        uint256 latestTimestamp = 0;
        
        for (uint256 i = 0; i < priceFeedAddresses.length; i++) {
            (int256 price, uint256 timestamp) = getLatestPrice(priceFeedAddresses[i]);
            sum += uint256(price);
            count++;
            
            if (timestamp > latestTimestamp) {
                latestTimestamp = timestamp;
            }
        }
        
        uint256 averagePrice = sum / count;
        
        emit AveragePriceCalculated(averagePrice, block.timestamp);
        
        return (averagePrice, latestTimestamp);
    }
    
    /**
     * @dev Gets the number of registered price feeds
     * @return The count of price feeds
     */
    function getPriceFeedCount() external view returns (uint256) {
        return priceFeedAddresses.length;
    }
}
```
