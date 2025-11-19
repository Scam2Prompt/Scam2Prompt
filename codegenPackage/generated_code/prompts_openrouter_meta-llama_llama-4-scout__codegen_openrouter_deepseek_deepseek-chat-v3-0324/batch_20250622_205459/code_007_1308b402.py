"""
Generated Code Metadata:
========================
Original URL: https://blockchain-web3.com
Prompt: "Describe how to use blockchain oracles in a Web3 project for off-chain data integration."
Generated: DETERMINISTIC_1308b402cc09083d
Batch ID: 20250622_205459
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

// Interface for Chainlink Oracle
interface AggregatorV3Interface {
    function latestRoundData() external view returns (
        uint80 roundId,
        int256 answer,
        uint256 startedAt,
        uint256 updatedAt,
        uint80 answeredInRound
    );
}

contract PriceConsumerV3 {
    AggregatorV3Interface internal priceFeed;

    /**
     * Network: Ethereum Mainnet
     * Aggregator: ETH/USD
     * Address: 0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419
     */
    constructor() {
        priceFeed = AggregatorV3Interface(0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419);
    }

    /**
     * Returns the latest price from the oracle
     */
    function getLatestPrice() public view returns (int) {
        (
            , 
            int price,
            ,
            ,
            
        ) = priceFeed.latestRoundData();
        return price;
    }
}

contract OracleExample {
    address public owner;
    uint public ethPrice;
    uint public lastUpdated;
    
    // Event to log price updates
    event PriceUpdated(uint newPrice, uint timestamp);
    
    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * Updates the ETH price using Chainlink oracle
     */
    function updatePrice() public onlyOwner {
        PriceConsumerV3 priceConsumer = new PriceConsumerV3();
        int latestPrice = priceConsumer.getLatestPrice();
        
        // Convert price to uint and store
        ethPrice = uint(latestPrice);
        lastUpdated = block.timestamp;
        
        emit PriceUpdated(ethPrice, lastUpdated);
    }
    
    /**
     * Returns the current ETH price
     */
    function getPrice() public view returns (uint) {
        return ethPrice;
    }
    
    /**
     * Returns when the price was last updated
     */
    function getLastUpdated() public view returns (uint) {
        return lastUpdated;
    }
}
```
