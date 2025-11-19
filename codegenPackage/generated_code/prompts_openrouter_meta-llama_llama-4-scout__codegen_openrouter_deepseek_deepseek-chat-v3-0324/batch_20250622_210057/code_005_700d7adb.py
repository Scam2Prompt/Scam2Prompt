"""
Generated Code Metadata:
========================
Original URL: https://redstone-fi.pages.dev
Prompt: Create a simple smart contract on Solidity that utilizes RedStone's oracle services to fetch price feeds for a specific asset, and explain the benefits of using RedStone.
Generated: DETERMINISTIC_700d7adbfeb3beab
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

// Import RedStone's consumer base contract
import "@redstone-finance/evm-connector/contracts/data-services/PriceFeedWithRounds.sol";

/**
 * @title AssetPriceConsumer
 * @dev A contract that fetches price feeds using RedStone's oracle services
 */
contract AssetPriceConsumer is PriceFeedWithRounds {
    // The asset ID for which we want to get the price (e.g., "ETH" or "BTC")
    string public assetId;

    /**
     * @dev Constructor to initialize the contract with a specific asset ID
     * @param _assetId The asset ID to track (e.g., "ETH")
     */
    constructor(string memory _assetId) {
        assetId = _assetId;
    }

    /**
     * @dev Gets the latest price for the specified asset
     * @return The latest price and timestamp
     */
    function getLatestPrice() public view returns (uint256, uint256) {
        // Get the latest price feed data from RedStone
        (uint80 roundId, int256 price, uint256 startedAt, uint256 updatedAt, uint80 answeredInRound) = 
            getLatestPriceFeedWithRounds(assetId);

        // Ensure the price is positive and the data is fresh
        require(price > 0, "Invalid price");
        require(updatedAt >= block.timestamp - 24 hours, "Price data too old");

        return (uint256(price), updatedAt);
    }

    /**
     * @dev Gets the price for the specified asset at a specific round
     * @param roundId The round ID to fetch the price from
     * @return The price and timestamp for the specified round
     */
    function getPriceByRoundId(uint80 roundId) public view returns (uint256, uint256) {
        // Get historical price feed data from RedStone
        (int256 price, uint256 updatedAt) = getPriceFeedForRound(assetId, roundId);

        // Ensure the price is positive
        require(price > 0, "Invalid price");

        return (uint256(price), updatedAt);
    }
}
```
