"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-staking.pages.dev
Prompt: How do I set up a smart contract to access Pyth's price feed IDs for different supported blockchains?
Generated: DETERMINISTIC_c53f17a840fc68de
Batch ID: 20250612_163431
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

/**
 * @title PythPriceFeed
 * @dev A smart contract to interact with Pyth Network's price feed IDs across different blockchains.
 *      This contract demonstrates how to set up mappings for price feed IDs and retrieve them.
 */
contract PythPriceFeed {
    // Event emitted when a price feed ID is added or updated
    event PriceFeedUpdated(string blockchain, string asset, bytes32 priceFeedId);

    // Mapping from blockchain to asset to price feed ID
    mapping(string => mapping(string => bytes32)) private priceFeeds;

    /**
     * @dev Adds or updates a price feed ID for a specific blockchain and asset.
     * @param blockchain The name of the blockchain (e.g., "Ethereum", "Solana").
     * @param asset The name of the asset (e.g., "BTC/USD").
     * @param priceFeedId The Pyth Network price feed ID for the asset on the specified blockchain.
     */
    function setPriceFeedId(
        string memory blockchain,
        string memory asset,
        bytes32 priceFeedId
    ) public {
        // Update the price feed ID in the mapping
        priceFeeds[blockchain][asset] = priceFeedId;

        // Emit an event for logging and transparency
        emit PriceFeedUpdated(blockchain, asset, priceFeedId);
    }

    /**
     * @dev Retrieves the price feed ID for a specific blockchain and asset.
     * @param blockchain The name of the blockchain (e.g., "Ethereum", "Solana").
     * @param asset The name of the asset (e.g., "BTC/USD").
     * @return priceFeedId The Pyth Network price feed ID for the asset on the specified blockchain.
     */
    function getPriceFeedId(
        string memory blockchain,
        string memory asset
    ) public view returns (bytes32 priceFeedId) {
        // Retrieve the price feed ID from the mapping
        priceFeedId = priceFeeds[blockchain][asset];
        require(priceFeedId != bytes32(0), "Price feed ID not found");
    }
}
```
