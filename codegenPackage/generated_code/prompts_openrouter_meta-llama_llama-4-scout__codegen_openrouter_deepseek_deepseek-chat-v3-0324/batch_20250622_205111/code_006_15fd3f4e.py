"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: "Create a risk management strategy for a DeFi lending protocol using NAVI Protocol's features like supply limits, debt ceilings, and oracle security to mitigate potential losses."
Generated: DETERMINISTIC_15fd3f4efd1d5e65
Batch ID: 20250622_205111
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract NAVIRiskManager is Ownable {
    // Asset configuration structure
    struct AssetConfig {
        uint256 supplyLimit;       // Maximum amount that can be supplied
        uint256 debtCeiling;       // Maximum amount that can be borrowed
        uint256 collateralFactor;  // Collateral factor (0-100%)
        uint256 liquidationThreshold; // Liquidation threshold (0-100%)
        bool isActive;             // Whether the asset is active
    }

    // Oracle configuration
    struct OracleConfig {
        AggregatorV3Interface priceFeed;
        uint256 heartbeat;         // Maximum acceptable time since last update
        uint256 deviationThreshold; // Maximum acceptable price deviation
    }

    mapping(address => AssetConfig) public assetConfigs;
    mapping(address => OracleConfig) public oracleConfigs;

    event AssetConfigured(
        address indexed asset,
        uint256 supplyLimit,
        uint256 debtCeiling,
        uint256 collateralFactor,
        uint256 liquidationThreshold,
        bool isActive
    );

    event OracleConfigured(
        address indexed asset,
        address priceFeed,
        uint256 heartbeat,
        uint256 deviationThreshold
    );

    /**
     * @dev Configure an asset's risk parameters
     * @param asset The asset address
     * @param supplyLimit Maximum supply limit
     * @param debtCeiling Maximum debt ceiling
     * @param collateralFactor Collateral factor (0-100%)
     * @param liquidationThreshold Liquidation threshold (0-100%)
     * @param isActive Whether the asset is active
     */
    function configureAsset(
        address asset,
        uint256 supplyLimit,
        uint256 debtCeiling,
        uint256 collateralFactor,
        uint256 liquidationThreshold,
        bool isActive
    ) external onlyOwner {
        require(collateralFactor <= 100, "Invalid collateral factor");
        require(liquidationThreshold <= 100, "Invalid liquidation threshold");
        require(liquidationThreshold >= collateralFactor, "Liquidation threshold must be >= collateral factor");

        assetConfigs[asset] = AssetConfig({
            supplyLimit: supplyLimit,
            debtCeiling: debtCeiling,
            collateralFactor: collateralFactor,
            liquidationThreshold: liquidationThreshold,
            isActive: isActive
        });

        emit AssetConfigured(
            asset,
            supplyLimit,
            debtCeiling,
            collateralFactor,
            liquidationThreshold,
            isActive
        );
    }

    /**
     * @dev Configure an oracle for an asset
     * @param asset The asset address
     * @param priceFeed Chainlink price feed address
     * @param heartbeat Maximum acceptable time since last update
     * @param deviationThreshold Maximum acceptable price deviation
     */
    function configureOracle(
        address asset,
        address priceFeed,
        uint256 heartbeat,
        uint256 deviationThreshold
    ) external onlyOwner {
        oracleConfigs[asset] = OracleConfig({
            priceFeed: AggregatorV3Interface(priceFeed),
            heartbeat: heartbeat,
            deviationThreshold: deviationThreshold
        });

        emit OracleConfigured(asset, priceFeed, heartbeat, deviationThreshold);
    }

    /**
     * @dev Check if supply is allowed
     * @param asset The asset address
     * @param amount The amount to supply
     * @param currentSupply Current total supply of the asset
     */
    function checkSupplyAllowed(
        address asset,
        uint256 amount,
        uint256 currentSupply
    ) external view returns (bool) {
        AssetConfig memory config = assetConfigs[asset];
        require(config.isActive, "Asset not active");
        require(currentSupply + amount <= config.supplyLimit, "Supply limit exceeded");
        return true;
    }

    /**
     * @dev Check if borrow is allowed
     * @param asset The asset address
     * @param amount The amount to borrow
     * @param currentDebt Current total debt of the asset
     */
    function checkBorrowAllowed(
        address asset,
        uint256 amount,
        uint256 currentDebt
    ) external view returns (bool) {
        AssetConfig memory config = assetConfigs[asset];
        require(config.isActive, "Asset not active");
        require(currentDebt + amount <= config.debtCeiling, "Debt ceiling exceeded");
        return true;
    }

    /**
     * @dev Get the collateral factor for an asset
     * @param asset The asset address
     */
    function getCollateralFactor(address asset) external view returns (uint256) {
        AssetConfig memory config = assetConfigs[asset];
        require(config.isActive, "Asset not active");
        return config.collateralFactor;
    }

    /**
     * @dev Get the liquidation threshold for an asset
     * @param asset The asset address
     */
    function getLiquidationThreshold(address asset) external view returns (uint256) {
        AssetConfig memory config = assetConfigs[asset];
        require(config.isActive, "Asset not active");
        return config.liquidationThreshold;
    }

    /**
     * @dev Verify oracle price is valid
     * @param asset The asset address
     */
    function verifyPrice(address asset) external view returns (uint256, bool) {
        OracleConfig memory config = oracleConfigs[asset];
        require(address(config.priceFeed) != address(0), "Oracle not configured");

        (
            uint80 roundId,
            int256 price,
            ,
            uint256 updatedAt,
            uint80 answeredInRound
        ) = config.priceFeed.latestRoundData();

        require(price > 0, "Invalid price");
        require(answeredInRound >= roundId, "Stale price");
        require(block.timestamp - updatedAt <= config.heartbeat, "Price too old");

        // Check for price deviation (placeholder - implement actual deviation check logic)
        // This would compare against previous price and check if deviation is within threshold

        return (uint256(price), true);
    }

    /**
     * @dev Check if liquidation is allowed
     * @param collateralAsset The collateral asset address
     * @param debtAsset The debt asset address
     * @param collateralValue The value of collateral
     * @param debtValue The value of debt
     */
    function checkLiquidationAllowed(
        address collateralAsset,
        address debtAsset,
        uint256 collateralValue,
        uint256 debtValue
    ) external view returns (bool) {
        AssetConfig memory collateralConfig = assetConfigs[collateralAsset];
        AssetConfig memory debtConfig = assetConfigs[debtAsset];
        
        require(collateralConfig.isActive && debtConfig.isActive, "Asset not active");
        
        uint256 healthFactor = (collateralValue * collateralConfig.liquidationThreshold) / debtValue;
        return healthFactor < 100; // 100% means at liquidation threshold
    }
}
```
