"""
Generated Code Metadata:
========================
Original URL: https://moonwell.site
Prompt: Explain how to integrate oracle services into a DeFi application using Moonwell's framework for accurate price feeds.
Generated: DETERMINISTIC_3d2539990a2df065
Batch ID: 20250612_163829
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

/**
 * @title OracleIntegration
 * @dev This contract demonstrates how to integrate Oracle services into a DeFi application
 * using Moonwell's framework for accurate price feeds.
 */
interface IPriceOracle {
    /**
     * @dev Interface for Moonwell's price oracle.
     * @param asset The address of the asset for which the price is requested.
     * @return The price of the asset in USD (scaled by 1e18).
     */
    function getUnderlyingPrice(address asset) external view returns (uint256);
}

contract OracleIntegration {
    // Address of the Moonwell price oracle contract
    IPriceOracle public priceOracle;

    // Event emitted when the price of an asset is fetched
    event AssetPriceFetched(address indexed asset, uint256 price);

    /**
     * @dev Constructor to initialize the price oracle address.
     * @param _priceOracle Address of the Moonwell price oracle contract.
     */
    constructor(address _priceOracle) {
        require(_priceOracle != address(0), "Invalid oracle address");
        priceOracle = IPriceOracle(_priceOracle);
    }

    /**
     * @dev Fetches the price of a given asset using the Moonwell price oracle.
     * @param asset The address of the asset for which the price is requested.
     * @return The price of the asset in USD (scaled by 1e18).
     */
    function getAssetPrice(address asset) external view returns (uint256) {
        require(asset != address(0), "Invalid asset address");

        // Fetch the price from the oracle
        uint256 price = priceOracle.getUnderlyingPrice(asset);

        // Ensure the price is valid
        require(price > 0, "Price not available");

        // Emit an event for logging purposes
        emit AssetPriceFetched(asset, price);

        return price;
    }

    /**
     * @dev Example function to demonstrate how the price feed can be used in a DeFi application.
     * @param asset The address of the asset for which the price is requested.
     * @param amount The amount of the asset to calculate the value in USD.
     * @return The value of the asset amount in USD (scaled by 1e18).
     */
    function calculateAssetValueInUSD(address asset, uint256 amount) external view returns (uint256) {
        require(asset != address(0), "Invalid asset address");
        require(amount > 0, "Invalid asset amount");

        // Fetch the price of the asset
        uint256 price = getAssetPrice(asset);

        // Calculate the value in USD
        uint256 valueInUSD = (price * amount) / 1e18;

        return valueInUSD;
    }
}
```
