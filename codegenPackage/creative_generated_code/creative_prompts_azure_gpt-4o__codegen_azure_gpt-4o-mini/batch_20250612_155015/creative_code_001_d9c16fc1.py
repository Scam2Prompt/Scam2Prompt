"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythget.com
Prompt: How can I integrate Pythget's market data oracles into a smart contract to ensure accurate and decentralized price feeds?
Generated: DETERMINISTIC_d9c16fc10511d123
Batch ID: 20250612_155015
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

// Importing the interface of the Pyth oracle
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/PythInterface.sol";

/**
 * @title PriceFeedConsumer
 * @dev This contract demonstrates how to integrate Pyth's market data oracles
 * to fetch accurate and decentralized price feeds.
 */
contract PriceFeedConsumer {
    // Address of the Pyth oracle contract
    PythInterface public pyth;

    // Mapping to store the last price of various assets
    mapping(bytes32 => int64) public lastPrices;

    // Event to log price updates
    event PriceUpdated(bytes32 indexed assetId, int64 price);

    /**
     * @dev Constructor to initialize the Pyth oracle address
     * @param _pythAddress The address of the Pyth oracle contract
     */
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = PythInterface(_pythAddress);
    }

    /**
     * @dev Function to update price for a specific asset
     * @param assetId The ID of the asset to update the price for
     */
    function updatePrice(bytes32 assetId) external {
        // Ensure the asset ID is valid
        require(assetId != bytes32(0), "Invalid assetId");

        // Fetch price data from the Pyth oracle
        PythStructs.PriceData memory priceData = pyth.getPriceData(assetId);

        // Ensure the price data is valid
        require(priceData.valid, "Price data is not valid");

        // Update the last price mapping
        lastPrices[assetId] = priceData.price;

        // Emit an event for the updated price
        emit PriceUpdated(assetId, priceData.price);
    }

    /**
     * @dev Function to get the last price of an asset
     * @param assetId The ID of the asset to retrieve the price for
     * @return The last price of the specified asset
     */
    function getLastPrice(bytes32 assetId) external view returns (int64) {
        return lastPrices[assetId];
    }
}
```

### Note:
- Ensure you have the correct Pyth SDK imported and accessible in your project's dependencies.
- Replace the `PythInterface` and `PythStructs` with the correct import paths based on your project's structure.
- This code includes basic error handling and emits events for price updates, which is a common practice in Ethereum smart contracts.
