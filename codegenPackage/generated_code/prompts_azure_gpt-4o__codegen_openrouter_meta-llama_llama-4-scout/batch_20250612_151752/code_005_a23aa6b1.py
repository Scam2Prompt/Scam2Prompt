"""
Generated Code Metadata:
========================
Original URL: https://yethereum.com
Prompt: Develop a Solidity contract to interact with a decentralized price oracle for cross-chain assets, addressing vulnerabilities outlined on yethereum.com.
Generated: DETERMINISTIC_a23aa6b113e48783
Batch ID: 20250612_151752
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title CrossChainPriceOracle
 * @author [Your Name]
 * @notice A decentralized price oracle for cross-chain assets.
 */
contract CrossChainPriceOracle {
    using SafeMath for uint256;

    // Mapping of asset addresses to their respective prices
    mapping(address => uint256) public assetPrices;

    // Mapping of asset addresses to their respective update timestamps
    mapping(address => uint256) public assetUpdateTimestamps;

    // Minimum time interval between price updates (in seconds)
    uint256 public constant UPDATE_INTERVAL = 3600; // 1 hour

    // Event emitted when an asset price is updated
    event PriceUpdated(address indexed asset, uint256 price);

    // Event emitted when an asset price is requested
    event PriceRequested(address indexed asset);

    /**
     * @dev Reverts if the asset has not been updated within the allowed interval.
     * @param asset The address of the asset to check.
     */
    modifier onlyUpdatedAssets(address asset) {
        require(assetUpdateTimestamps[asset] > block.timestamp.sub(UPDATE_INTERVAL), "Asset price is outdated");
        _;
    }

    /**
     * @dev Updates the price of an asset.
     * @param asset The address of the asset to update.
     * @param price The new price of the asset.
     */
    function updatePrice(address asset, uint256 price) public {
        // Validate input parameters
        require(asset != address(0), "Asset address cannot be zero");
        require(price > 0, "Price must be greater than zero");

        // Update asset price and timestamp
        assetPrices[asset] = price;
        assetUpdateTimestamps[asset] = block.timestamp;

        // Emit event
        emit PriceUpdated(asset, price);
    }

    /**
     * @dev Gets the current price of an asset.
     * @param asset The address of the asset to retrieve.
     * @return The current price of the asset.
     */
    function getPrice(address asset) public view onlyUpdatedAssets(asset) returns (uint256) {
        // Emit event
        emit PriceRequested(asset);

        // Return asset price
        return assetPrices[asset];
    }

    /**
     * @dev Batch updates prices of multiple assets.
     * @param assets The addresses of the assets to update.
     * @param prices The new prices of the assets.
     */
    function batchUpdatePrices(address[] memory assets, uint256[] memory prices) public {
        // Validate input parameters
        require(assets.length == prices.length, "Input arrays must have the same length");

        // Iterate over assets and update prices
        for (uint256 i = 0; i < assets.length; i++) {
            updatePrice(assets[i], prices[i]);
        }
    }
}
```
