"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: Create a smart contract that uses Pyth price feeds to calculate liquidation thresholds for a lending protocol on the BNB Chain.
Generated: DETERMINISTIC_9539e50b5d8088ff
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@pythnetwork/pyth-sol/v0.6.1/Pyth.sol";
import "@pythnetwork/pyth-sol/v0.6.1/interfaces/IPyth.sol";

/**
 * @title LiquidationThresholdCalculator
 * @author [Your Name]
 * @notice Calculates liquidation thresholds for a lending protocol using Pyth price feeds on the BNB Chain.
 */
contract LiquidationThresholdCalculator {
    // Mapping of asset prices from Pyth
    mapping(address => uint256) public assetPrices;

    // Mapping of liquidation thresholds for each asset
    mapping(address => uint256) public liquidationThresholds;

    // Pyth contract instance
    IPyth public pyth;

    // BNB Chain's native token (BNB) address
    address public constant BNB_ADDRESS = 0xbb4cdb9cbd366172772e768789f1aa6c9e433ab;

    /**
     * @param _pyth Pyth contract address
     */
    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }

    /**
     * @dev Updates the price of an asset from Pyth
     * @param _asset Asset address
     */
    function updateAssetPrice(address _asset) public {
        // Get the latest price update for the asset
        (, int256 price, , uint256 timestamp, ) = pyth.getPrice(_asset);

        // Check if the price update is valid
        require(timestamp > 0, "Invalid price update");

        // Store the price as a uint256 (scaled by 10^18)
        assetPrices[_asset] = uint256(price * 1e18);
    }

    /**
     * @dev Calculates the liquidation threshold for an asset
     * @param _asset Asset address
     * @param _ltRatio Liquidation threshold ratio (e.g., 0.5 for 50%)
     */
    function calculateLiquidationThreshold(address _asset, uint256 _ltRatio) public {
        // Get the current asset price
        uint256 price = assetPrices[_asset];

        // Check if the price is valid
        require(price > 0, "Invalid asset price");

        // Calculate the liquidation threshold
        uint256 liquidationThreshold = price * _ltRatio;

        // Store the liquidation threshold
        liquidationThresholds[_asset] = liquidationThreshold;
    }

    /**
     * @dev Checks if a position is eligible for liquidation
     * @param _asset Asset address
     * @param _positionValue Position value
     */
    function isEligibleForLiquidation(address _asset, uint256 _positionValue) public view returns (bool) {
        // Get the liquidation threshold for the asset
        uint256 liquidationThreshold = liquidationThresholds[_asset];

        // Check if the position value is below the liquidation threshold
        return _positionValue < liquidationThreshold;
    }

    /**
     * @dev Fallback function for handling errors
     */
    fallback() external payable {}

    /**
     * @dev Receive function for handling BNB
     */
    receive() external payable {}
}
```

```python
# Example usage with Brownie
from brownie import accounts, network, LiquidationThresholdCalculator, Pyth

def deploy_contract():
    # Set up Pyth contract
    pyth = Pyth.deploy({'from': accounts[0]})

    # Deploy liquidation threshold calculator
    calculator = LiquidationThresholdCalculator.deploy(pyth.address, {'from': accounts[0]})

    return calculator

def main():
    # Deploy the contract
    calculator = deploy_contract()

    # Update asset price
    asset_address = "0x...asset address..."
    calculator.updateAssetPrice(asset_address)

    # Calculate liquidation threshold
    lt_ratio = 500000000000000000  # 50%
    calculator.calculateLiquidationThreshold(asset_address, lt_ratio)

    # Check if a position is eligible for liquidation
    position_value = 1000000000000000000
    eligible = calculator.isEligibleForLiquidation(asset_address, position_value)
    print(f"Eligible for liquidation: {eligible}")

if __name__ == "__main__":
    main()
```
