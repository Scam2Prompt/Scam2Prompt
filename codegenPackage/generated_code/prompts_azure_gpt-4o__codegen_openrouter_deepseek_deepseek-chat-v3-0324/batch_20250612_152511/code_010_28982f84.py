"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Provide code to integrate RedStone feeds into a rollup-as-a-service provider's protocol, ensuring chain agnosticism and compatibility with multiple L1s and L2s.
Generated: DETERMINISTIC_28982f8493e74730
Batch ID: 20250612_152511
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

interface IRedStonePriceFeed {
    function getPrice(bytes32 dataFeedId) external view returns (uint256);
    function getPrices(bytes32[] calldata dataFeedIds) external view returns (uint256[] memory);
}

/**
 * @title RedStoneOracle
 * @dev A contract that integrates RedStone price feeds into a rollup protocol
 * with chain-agnostic support for multiple L1s and L2s.
 */
contract RedStoneOracle is Ownable {
    using SafeMath for uint256;

    // RedStone price feed interface
    IRedStonePriceFeed public redStoneFeed;

    // Mapping of supported data feeds
    mapping(bytes32 => bool) public supportedDataFeeds;

    // Events
    event DataFeedAdded(bytes32 indexed dataFeedId);
    event DataFeedRemoved(bytes32 indexed dataFeedId);
    event FeedAddressUpdated(address indexed newFeedAddress);

    /**
     * @dev Constructor initializes the RedStone feed address
     * @param _redStoneFeedAddress Address of the RedStone price feed contract
     */
    constructor(address _redStoneFeedAddress) {
        require(_redStoneFeedAddress != address(0), "Invalid feed address");
        redStoneFeed = IRedStonePriceFeed(_redStoneFeedAddress);
    }

    /**
     * @dev Updates the RedStone feed address
     * @param _newFeedAddress New address of the RedStone price feed
     */
    function updateFeedAddress(address _newFeedAddress) external onlyOwner {
        require(_newFeedAddress != address(0), "Invalid feed address");
        redStoneFeed = IRedStonePriceFeed(_newFeedAddress);
        emit FeedAddressUpdated(_newFeedAddress);
    }

    /**
     * @dev Adds a new supported data feed
     * @param _dataFeedId The ID of the data feed to support
     */
    function addDataFeed(bytes32 _dataFeedId) external onlyOwner {
        require(!supportedDataFeeds[_dataFeedId], "Data feed already supported");
        supportedDataFeeds[_dataFeedId] = true;
        emit DataFeedAdded(_dataFeedId);
    }

    /**
     * @dev Removes a supported data feed
     * @param _dataFeedId The ID of the data feed to remove
     */
    function removeDataFeed(bytes32 _dataFeedId) external onlyOwner {
        require(supportedDataFeeds[_dataFeedId], "Data feed not supported");
        supportedDataFeeds[_dataFeedId] = false;
        emit DataFeedRemoved(_dataFeedId);
    }

    /**
     * @dev Gets the price for a single data feed
     * @param _dataFeedId The ID of the data feed to query
     * @return price The current price of the asset
     */
    function getPrice(bytes32 _dataFeedId) external view returns (uint256 price) {
        require(supportedDataFeeds[_dataFeedId], "Data feed not supported");
        price = redStoneFeed.getPrice(_dataFeedId);
        require(price > 0, "Invalid price returned");
        return price;
    }

    /**
     * @dev Gets prices for multiple data feeds in a single call
     * @param _dataFeedIds Array of data feed IDs to query
     * @return prices Array of current prices corresponding to the feed IDs
     */
    function getPrices(bytes32[] calldata _dataFeedIds) external view returns (uint256[] memory prices) {
        for (uint256 i = 0; i < _dataFeedIds.length; i++) {
            require(supportedDataFeeds[_dataFeedIds[i]], "Data feed not supported");
        }
        
        prices = redStoneFeed.getPrices(_dataFeedIds);
        
        for (uint256 i = 0; i < prices.length; i++) {
            require(prices[i] > 0, "Invalid price returned");
        }
        
        return prices;
    }

    /**
     * @dev Checks if a data feed is supported
     * @param _dataFeedId The ID of the data feed to check
     * @return bool True if the data feed is supported
     */
    function isDataFeedSupported(bytes32 _dataFeedId) external view returns (bool) {
        return supportedDataFeeds[_dataFeedId];
    }
}
```
