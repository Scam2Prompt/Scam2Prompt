"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythbtc.com
Prompt: Demonstrate how to configure a smart contract to use Pyth price feed oracles for decentralized finance (DeFi) applications.
Generated: DETERMINISTIC_1fc6c012431fa2a4
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, production-ready smart contract in Solidity that demonstrates how to integrate with Pyth price feed oracles for decentralized finance (DeFi) applications. This example assumes you're using the Pyth network deployed on Ethereum or a compatible chain.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PythPriceFeedExample
 * @dev Example contract demonstrating integration with Pyth price feed oracles for DeFi applications.
 */
interface IPyth {
    function getPrice(bytes32 priceId) external view returns (int64 price, uint64 timestamp);
    function getEmaPrice(bytes32 priceId) external view returns (int64 price, uint64 timestamp);
}

contract PythPriceFeedExample {
    // Address of the deployed Pyth contract (update this to the actual address on your chain)
    address public immutable pythContract;

    // Mapping of asset identifiers to Pyth price IDs
    mapping(string => bytes32) public assetPriceIds;

    // Event emitted when a price ID is updated for an asset
    event AssetPriceIdUpdated(string assetSymbol, bytes32 priceId);

    /**
     * @dev Constructor to set the Pyth contract address.
     * @param _pythContract Address of the deployed Pyth contract.
     */
    constructor(address _pythContract) {
        require(_pythContract != address(0), "Invalid Pyth contract address");
        pythContract = _pythContract;
    }

    /**
     * @dev Update the price ID for a specific asset.
     * @param assetSymbol Symbol of the asset (e.g., "BTC", "ETH").
     * @param priceId The Pyth price ID associated with the asset.
     */
    function updateAssetPriceId(string calldata assetSymbol, bytes32 priceId) external {
        require(bytes(assetSymbol).length > 0, "Asset symbol cannot be empty");
        assetPriceIds[assetSymbol] = priceId;
        emit AssetPriceIdUpdated(assetSymbol, priceId);
    }

    /**
     * @dev Fetch the latest price for a given asset.
     * @param assetSymbol Symbol of the asset (e.g., "BTC", "ETH").
     * @return price The latest price of the asset.
     * @return timestamp The timestamp of the price update.
     */
    function getLatestPrice(string calldata assetSymbol) external view returns (int64 price, uint64 timestamp) {
        bytes32 priceId = assetPriceIds[assetSymbol];
        require(priceId != bytes32(0), "Price ID not set for asset");

        IPyth pyth = IPyth(pythContract);
        (price, timestamp) = pyth.getPrice(priceId);

        require(price != 0, "Invalid price returned from Pyth");
        return (price, timestamp);
    }

    /**
     * @dev Fetch the EMA (Exponential Moving Average) price for a given asset.
     * @param assetSymbol Symbol of the asset (e.g., "BTC", "ETH").
     * @return price The EMA price of the asset.
     * @return timestamp The timestamp of the EMA price update.
     */
    function getEmaPrice(string calldata assetSymbol) external view returns (int64 price, uint64 timestamp) {
        bytes32 priceId = assetPriceIds[assetSymbol];
        require(priceId != bytes32(0), "Price ID not set for asset");

        IPyth pyth = IPyth(pythContract);
        (price, timestamp) = pyth.getEmaPrice(priceId);

        require(price != 0, "Invalid EMA price returned from Pyth");
        return (price, timestamp);
    }
}
```

### Notes:
- Replace `pythContract` with the actual deployed address of the Pyth contract on your blockchain.
- You can extend this contract further based on specific DeFi functionality, including interacting with lending/borrowing mechanics or automated trading systems.
- The contract assumes the Pyth API functions `getPrice` and `getEmaPrice` exist and follow this signature. Validate the API for your specific Pyth deployment.
