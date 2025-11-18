"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: How can I use the Pyth Network's on-demand oracle to fetch real-time price updates for multiple assets in an EVM-compatible blockchain? Provide code examples.
Generated: DETERMINISTIC_65a407a069dfe888
Batch ID: 20250612_152000
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
 * @title PythOracleClient
 * @dev A contract to fetch real-time price updates for multiple assets using the Pyth Network's on-demand oracle
 *      in an EVM-compatible blockchain.
 */
contract PythOracleClient {
    // Pyth network's on-chain contract address (replace with the actual deployed address of Pyth contract)
    address public constant PYTH_CONTRACT_ADDRESS = 0x1234567890123456789012345678901234567890;

    // Interface for interacting with the Pyth contract
    IPyth public pythContract;

    // Struct to store asset price data
    struct AssetPrice {
        int64 price;        // Price of the asset
        uint64 confidence;  // Confidence interval for the price
        uint256 publishTime; // Timestamp of the last published price
    }
    
    // Mapping to store price updates for assets using their Pyth price IDs
    mapping(bytes32 => AssetPrice) public assetPrices;

    // Events
    event PriceUpdated(bytes32 indexed priceId, int64 price, uint64 confidence, uint256 publishTime);

    // Constructor to initialize the Pyth contract
    constructor() {
        pythContract = IPyth(PYTH_CONTRACT_ADDRESS);
    }

    /**
     * @dev Fetches the latest price update for a list of assets from the Pyth network.
     * @param priceIds Array of asset price IDs (Pyth-specific identifiers).
     * @param updateData Byte data returned by Pyth's off-chain API (containing the price feeds).
     */
    function updateAssetPrices(bytes32[] memory priceIds, bytes memory updateData) external {
        // Update price data in Pyth contract
        try pythContract.updatePriceFeeds(updateData) {
            // Iterate through the provided price IDs
            for (uint256 i = 0; i < priceIds.length; i++) {
                bytes32 priceId = priceIds[i];
                (int64 price, uint64 confidence, uint256 publishTime) = pythContract.getPriceUnsafe(priceId);

                // Update asset price mapping
                assetPrices[priceId] = AssetPrice(price, confidence, publishTime);

                emit PriceUpdated(priceId, price, confidence, publishTime);
            }
        } catch (bytes memory error) {
            // Handle errors during price updates
            revert(string(abi.encodePacked("Error updating prices: ", error)));
        }
    }

    /**
     * @dev Fetches the latest price for a specific asset.
     * @param priceId The Pyth-specific price ID for the asset.
     * @return price The price of the asset.
     * @return confidence The confidence interval of the asset price.
     * @return publishTime The timestamp of the last price update.
     */
    function getAssetPrice(bytes32 priceId)
        external
        view
        returns (int64 price, uint64 confidence, uint256 publishTime)
    {
        AssetPrice memory assetPrice = assetPrices[priceId];
        return (assetPrice.price, assetPrice.confidence, assetPrice.publishTime);
    }
}

// Interface for interacting with the Pyth contract
interface IPyth {
    function updatePriceFeeds(bytes memory updateData) external;

    function getPriceUnsafe(bytes32 priceId) external view returns (int64 price, uint64 confidence, uint256 publishTime);
}
```
