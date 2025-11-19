"""
Generated Code Metadata:
========================
Original URL: https://redstone-fi.pages.dev
Prompt: What are the benefits of using RedStone's modular oracle solution for a DeFi application on multiple EVM and non-EVM ecosystems, and how can it be deployed across different chains?
Generated: DETERMINISTIC_54fa1ab321ca0416
Batch ID: 20250622_210057
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RedStoneOracleConsumer
 * @dev A contract that demonstrates integration with RedStone's modular oracle solution
 * for fetching price data across multiple EVM and non-EVM chains
 */
contract RedStoneOracleConsumer is Ownable {
    using SafeMath for uint256;

    // RedStone data feed ID for the asset
    bytes32 public dataFeedId;
    
    // Address of the RedStone price feed adapter
    address public priceFeedAdapter;
    
    // Mapping to store prices by timestamp
    mapping(uint256 => uint256) public historicalPrices;
    
    // Events
    event PriceUpdated(uint256 timestamp, uint256 price);
    event FeedAdapterUpdated(address newAdapter);
    
    /**
     * @dev Constructor initializes the contract with RedStone data feed ID
     * @param _dataFeedId The RedStone data feed identifier
     * @param _priceFeedAdapter Address of the RedStone price feed adapter
     */
    constructor(bytes32 _dataFeedId, address _priceFeedAdapter) {
        dataFeedId = _dataFeedId;
        priceFeedAdapter = _priceFeedAdapter;
    }
    
    /**
     * @dev Updates the price feed adapter address
     * @param newAdapter Address of the new price feed adapter
     */
    function updatePriceFeedAdapter(address newAdapter) external onlyOwner {
        require(newAdapter != address(0), "Invalid adapter address");
        priceFeedAdapter = newAdapter;
        emit FeedAdapterUpdated(newAdapter);
    }
    
    /**
     * @dev Fetches the current price from RedStone oracle
     * @return currentPrice The current price of the asset
     */
    function getCurrentPrice() external view returns (uint256 currentPrice) {
        (bool success, bytes memory result) = priceFeedAdapter.staticcall(
            abi.encodeWithSignature("getPrice(bytes32)", dataFeedId)
        );
        require(success, "Price fetch failed");
        currentPrice = abi.decode(result, (uint256));
    }
    
    /**
     * @dev Updates and stores the current price
     */
    function updatePrice() external {
        (bool success, bytes memory result) = priceFeedAdapter.staticcall(
            abi.encodeWithSignature("getPrice(bytes32)", dataFeedId)
        );
        require(success, "Price fetch failed");
        
        uint256 price = abi.decode(result, (uint256));
        uint256 timestamp = block.timestamp;
        
        historicalPrices[timestamp] = price;
        emit PriceUpdated(timestamp, price);
    }
    
    /**
     * @dev Gets historical price for a specific timestamp
     * @param timestamp The timestamp to query
     * @return price The price at the given timestamp
     */
    function getHistoricalPrice(uint256 timestamp) external view returns (uint256 price) {
        price = historicalPrices[timestamp];
        require(price != 0, "Price not found for timestamp");
    }
}
```
