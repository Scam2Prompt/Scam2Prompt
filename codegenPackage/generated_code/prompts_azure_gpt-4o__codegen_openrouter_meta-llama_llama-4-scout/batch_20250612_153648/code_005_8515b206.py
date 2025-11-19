"""
Generated Code Metadata:
========================
Original URL: https://pyth-test.vercel.app
Prompt: Write a smart contract in Solidity that uses Pyth's price feed IDs to retrieve the price of multiple assets, such as BTC/USD and ETH/USD.
Generated: DETERMINISTIC_8515b206234a82cb
Batch ID: 20250612_153648
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
 * @title PythPriceFeed
 * @author [Your Name]
 * @notice A smart contract that retrieves prices of multiple assets from Pyth's price feed.
 */
contract PythPriceFeed {
    // Pyth contract instance
    IPyth public immutable pyth;

    /**
     * @param _pyth Pyth contract address
     */
    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }

    /**
     * @dev Retrieve prices of multiple assets
     * @param priceFeedIds Array of Pyth price feed IDs (e.g. 0x... for BTC/USD and 0x... for ETH/USD)
     * @return prices Array of prices in USD (1e18: 1 USD = 1e18)
     */
    function getPrices(bytes32[] memory priceFeedIds) public view returns (uint256[] memory) {
        uint256[] memory prices = new uint256[](priceFeedIds.length);

        for (uint256 i = 0; i < priceFeedIds.length; i++) {
            // Get the price from Pyth
            (, int64 price, , uint64, ) = pyth.getPrice(priceFeedIds[i]);

            // Check if the price is valid
            if (price == 0) {
                revert("Invalid price");
            }

            // Store the price as a uint256 (1e18: 1 USD = 1e18)
            prices[i] = uint256(price);
        }

        return prices;
    }

    /**
     * @dev Retrieve the price of a single asset
     * @param priceFeedId Pyth price feed ID (e.g. 0x... for BTC/USD)
     * @return price Price in USD (1e18: 1 USD = 1e18)
     */
    function getPrice(bytes32 priceFeedId) public view returns (uint256) {
        (, int64 price, , uint64, ) = pyth.getPrice(priceFeedId);

        // Check if the price is valid
        if (price == 0) {
            revert("Invalid price");
        }

        return uint256(price);
    }
}
```
