"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.gmx-oracle.io
Prompt: Explain how to use GMX documentation to implement a custom oracle solution for price feeds on Arbitrum.
Generated: DETERMINISTIC_a6d5b476d854c349
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the GMX price feed
interface IGMXPriceFeed {
    function getLatestPrice(address _asset) external view returns (uint256);
}

// Custom Oracle contract for price feeds on Arbitrum
contract CustomOracle is Ownable {
    using SafeMath for uint256;

    // Mapping to store price feeds for assets
    mapping(address => address) public priceFeeds;

    // Event to log the addition of a new price feed
    event PriceFeedAdded(address indexed asset, address indexed priceFeed);
    
    // Event to log price updates
    event PriceUpdated(address indexed asset, uint256 price);

    // Function to add a new price feed
    // Only the contract owner can add a price feed
    function addPriceFeed(address _asset, address _priceFeed) external onlyOwner {
        require(_asset != address(0), "Invalid asset address");
        require(_priceFeed != address(0), "Invalid price feed address");
        
        priceFeeds[_asset] = _priceFeed;
        emit PriceFeedAdded(_asset, _priceFeed);
    }

    // Function to get the latest price of an asset
    function getPrice(address _asset) external view returns (uint256) {
        address priceFeed = priceFeeds[_asset];
        require(priceFeed != address(0), "Price feed not found for the asset");
        
        uint256 latestPrice = IGMXPriceFeed(priceFeed).getLatestPrice(_asset);
        require(latestPrice > 0, "Invalid price received");

        emit PriceUpdated(_asset, latestPrice);
        return latestPrice;
    }
}
```
