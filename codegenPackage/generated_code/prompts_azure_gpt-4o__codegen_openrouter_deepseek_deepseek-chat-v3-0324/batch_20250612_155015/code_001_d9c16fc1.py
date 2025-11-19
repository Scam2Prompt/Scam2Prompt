"""
Generated Code Metadata:
========================
Original URL: https://pythget.com
Prompt: How can I integrate Pythget's market data oracles into a smart contract to ensure accurate and decentralized price feeds?
Generated: DETERMINISTIC_d9c16fc10511d123
Batch ID: 20250612_155015
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

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title PythPriceOracle
 * @dev A smart contract that integrates with Pyth Network's price oracles
 * to provide decentralized and accurate price feeds.
 */
contract PythPriceOracle {
    // Pyth price feed address for the desired asset pair
    address public pythPriceFeedAddress;
    
    // Chainlink fallback price feed address
    address public chainlinkFallbackFeed;
    
    // Owner address
    address public owner;
    
    // Maximum allowed price deviation between Pyth and Chainlink (in percentage)
    uint256 public maxDeviationPercentage;
    
    // Events
    event PriceFeedUpdated(address newPythFeed, address newChainlinkFeed);
    event MaxDeviationUpdated(uint256 newDeviation);
    
    /**
     * @dev Constructor initializes the contract with Pyth and Chainlink feed addresses
     * @param _pythPriceFeed Address of the Pyth price feed contract
     * @param _chainlinkFeed Address of the Chainlink fallback price feed
     * @param _maxDeviation Maximum allowed percentage deviation between feeds
     */
    constructor(
        address _pythPriceFeed,
        address _chainlinkFeed,
        uint256 _maxDeviation
    ) {
        require(_pythPriceFeed != address(0), "Invalid Pyth feed address");
        require(_chainlinkFeed != address(0), "Invalid Chainlink feed address");
        require(_maxDeviation <= 100, "Deviation must be <= 100%");
        
        pythPriceFeedAddress = _pythPriceFeed;
        chainlinkFallbackFeed = _chainlinkFeed;
        maxDeviationPercentage = _maxDeviation;
        owner = msg.sender;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this");
        _;
    }
    
    /**
     * @dev Updates the price feed addresses
     * @param _newPythFeed New Pyth price feed address
     * @param _newChainlinkFeed New Chainlink price feed address
     */
    function updatePriceFeeds(
        address _newPythFeed,
        address _newChainlinkFeed
    ) external onlyOwner {
        require(_newPythFeed != address(0), "Invalid Pyth feed address");
        require(_newChainlinkFeed != address(0), "Invalid Chainlink feed address");
        
        pythPriceFeedAddress = _newPythFeed;
        chainlinkFallbackFeed = _newChainlinkFeed;
        
        emit PriceFeedUpdated(_newPythFeed, _newChainlinkFeed);
    }
    
    /**
     * @dev Updates the maximum allowed deviation percentage
     * @param _newDeviation New maximum deviation percentage
     */
    function updateMaxDeviation(uint256 _newDeviation) external onlyOwner {
        require(_newDeviation <= 100, "Deviation must be <= 100%");
        maxDeviationPercentage = _newDeviation;
        emit MaxDeviationUpdated(_newDeviation);
    }
    
    /**
     * @dev Gets the latest price from Pyth with fallback to Chainlink if deviation is too high
     * @return price The verified price
     * @return decimals The number of decimals in the price
     */
    function getVerifiedPrice() external view returns (int256, uint8) {
        (int256 pythPrice, uint8 pythDecimals) = getPythPrice();
        (int256 chainlinkPrice, uint8 chainlinkDecimals) = getChainlinkPrice();
        
        require(pythDecimals == chainlinkDecimals, "Decimal mismatch");
        
        // Calculate deviation percentage
        uint256 deviation = calculateDeviation(pythPrice, chainlinkPrice);
        
        if (deviation > maxDeviationPercentage) {
            return (chainlinkPrice, chainlinkDecimals);
        }
        
        return (pythPrice, pythDecimals);
    }
    
    /**
     * @dev Gets the latest price from Pyth Network
     * @return price The Pyth price
     * @return decimals The number of decimals in the price
     */
    function getPythPrice() public view returns (int256, uint8) {
        // In a real implementation, this would call Pyth's specific interface
        // For demonstration, we're using Chainlink's interface as a placeholder
        AggregatorV3Interface priceFeed = AggregatorV3Interface(pythPriceFeedAddress);
        (
            uint80 roundID,
            int256 price,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        
        uint8 decimals = priceFeed.decimals();
        
        return (price, decimals);
    }
    
    /**
     * @dev Gets the latest price from Chainlink
     * @return price The Chainlink price
     * @return decimals The number of decimals in the price
     */
    function getChainlinkPrice() public view returns (int256, uint8) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(chainlinkFallbackFeed);
        (
            uint80 roundID,
            int256 price,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        
        uint8 decimals = priceFeed.decimals();
        
        return (price, decimals);
    }
    
    /**
     * @dev Calculates the percentage deviation between two prices
     * @param price1 First price
     * @param price2 Second price
     * @return deviation The percentage deviation between the two prices
     */
    function calculateDeviation(int256 price1, int256 price2) public pure returns (uint256) {
        if (price1 == 0 || price2 == 0) {
            return 100; // Treat zero prices as 100% deviation
        }
        
        uint256 absDiff = price1 > price2 
            ? uint256(price1 - price2) 
            : uint256(price2 - price1);
        
        uint256 avgPrice = (uint256(price1) + uint256(price2)) / 2;
        
        return (absDiff * 100) / avgPrice;
    }
}
```
