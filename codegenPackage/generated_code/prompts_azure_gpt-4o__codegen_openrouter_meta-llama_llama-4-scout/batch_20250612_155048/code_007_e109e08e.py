"""
Generated Code Metadata:
========================
Original URL: https://pythim.com
Prompt: Write a Solidity smart contract that incorporates Pythim's price feed oracles to calculate the value of a portfolio in real-time.
Generated: DETERMINISTIC_e109e08e456ec348
Batch ID: 20250612_155048
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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/Pyth.sol";

/**
 * @title PortfolioCalculator
 * @author [Your Name]
 * @notice Calculates the value of a portfolio in real-time using Pyth's price feed oracles.
 */
contract PortfolioCalculator {
    // Mapping of asset addresses to their respective price feeds
    mapping(address => bytes32) public assetPriceFeeds;

    // Mapping of asset addresses to their respective balances
    mapping(address => uint256) public assetBalances;

    // Pyth oracle instance
    IPyth public pyth;

    /**
     * @dev Constructor
     * @param _pyth Pyth oracle instance address
     */
    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }

    /**
     * @dev Adds an asset to the portfolio
     * @param _asset Asset address
     * @param _priceFeed Price feed ID
     */
    function addAsset(address _asset, bytes32 _priceFeed) public {
        assetPriceFeeds[_asset] = _priceFeed;
    }

    /**
     * @dev Updates the balance of an asset in the portfolio
     * @param _asset Asset address
     * @param _balance New balance
     */
    function updateBalance(address _asset, uint256 _balance) public {
        assetBalances[_asset] = _balance;
    }

    /**
     * @dev Calculates the value of the portfolio in real-time
     * @return Portfolio value in USD
     */
    function getPortfolioValue() public view returns (uint256) {
        uint256 portfolioValue = 0;

        // Iterate over assets in the portfolio
        for (address asset in assetPriceFeeds.keys()) {
            // Get the price feed ID for the asset
            bytes32 priceFeedId = assetPriceFeeds[asset];

            // Get the latest price from Pyth
            (, int256 price, , uint256 timestamp, ) = pyth.getPrice(priceFeedId);

            // Check if the price is valid
            if (price > 0 && timestamp > block.timestamp - 60 minutes) {
                // Calculate the value of the asset
                uint256 assetValue = uint256(price) * assetBalances[asset] / 1e8;

                // Add the asset value to the portfolio value
                portfolioValue += assetValue;
            } else {
                // Handle invalid price
                emit InvalidPrice(asset, priceFeedId);
            }
        }

        return portfolioValue;
    }

    /**
     * @dev Emitted when an invalid price is encountered
     * @param asset Asset address
     * @param priceFeedId Price feed ID
     */
    event InvalidPrice(address indexed asset, bytes32 indexed priceFeedId);
}
```
