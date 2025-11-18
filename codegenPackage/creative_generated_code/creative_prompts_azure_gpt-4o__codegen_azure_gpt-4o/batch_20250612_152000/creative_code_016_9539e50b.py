"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Create a smart contract that uses Pyth price feeds to calculate liquidation thresholds for a lending protocol on the BNB Chain.
Generated: DETERMINISTIC_9539e50b5d8088ff
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
 * @title LendingProtocolLiquidation
 * @dev A smart contract that uses Pyth price feeds to calculate liquidation thresholds
 *      for a lending protocol on the BNB Chain.
 * @notice Ensure Pyth price feed contract address is correct for the deployed network.
 */
interface IPyth {
    function getPrice(bytes32 priceId) external view returns (int64 price, uint64 conf, int32 expo, uint64 publishTime);
}

contract LendingProtocolLiquidation {
    // Address of the Pyth price feed contract on BNB Chain
    IPyth public pythPriceFeed;

    // Mapping to store collateral asset price IDs
    mapping(address => bytes32) public assetPriceIds;

    // Event emitted when a liquidation threshold is calculated
    event LiquidationThresholdCalculated(address indexed user, uint256 threshold);

    // Constructor to initialize Pyth price feed contract
    constructor(address _pythPriceFeed) {
        require(_pythPriceFeed != address(0), "Invalid Pyth price feed address");
        pythPriceFeed = IPyth(_pythPriceFeed);
    }

    /**
     * @dev Sets the price ID for a collateral asset.
     * @param asset Address of the collateral asset.
     * @param priceId Pyth price ID corresponding to the asset.
     */
    function setAssetPriceId(address asset, bytes32 priceId) external {
        require(asset != address(0), "Invalid asset address");
        assetPriceIds[asset] = priceId;
    }

    /**
     * @dev Calculates the liquidation threshold based on collateral asset price.
     * @param user Address of the user to calculate the threshold for.
     * @param collateralAsset Address of the collateral asset.
     * @param collateralAmount Amount of the collateral asset provided.
     * @param loanAmount Amount of the loan taken.
     * @return liquidationThreshold The calculated liquidation threshold.
     */
    function calculateLiquidationThreshold(
        address user,
        address collateralAsset,
        uint256 collateralAmount,
        uint256 loanAmount
    ) external returns (uint256 liquidationThreshold) {
        require(user != address(0), "Invalid user address");
        require(collateralAsset != address(0), "Invalid collateral asset");
        require(collateralAmount > 0, "Collateral amount must be greater than zero");
        require(loanAmount > 0, "Loan amount must be greater than zero");

        // Get the price ID for the collateral asset
        bytes32 priceId = assetPriceIds[collateralAsset];
        require(priceId != 0, "Price ID not set for collateral asset");

        // Fetch price data from Pyth
        (int64 price, , int32 expo, ) = pythPriceFeed.getPrice(priceId);
        require(price > 0, "Invalid price data received from Pyth");

        // Convert price to unsigned integer and adjust for exponent
        uint256 adjustedPrice = uint256(int256(price)) * 10**uint256(int256(expo));

        // Calculate liquidation threshold: (collateralValue / loanAmount) * 100
        uint256 collateralValue = collateralAmount * adjustedPrice;
        liquidationThreshold = (collateralValue * 100) / loanAmount;

        // Emit event for the calculated liquidation threshold
        emit LiquidationThresholdCalculated(user, liquidationThreshold);
    }
}
```
