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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Pyth price feeds
interface IPyth {
    function getPrice(bytes32 _priceId) external view returns (int256);
}

contract LendingProtocol is Ownable {
    // Mapping for collateral asset thresholds
    mapping(address => uint256) public collateralThresholds;

    // Pyth price feed contract address
    IPyth public pyth;

    // Event emitted when the collateral threshold is updated
    event CollateralThresholdUpdated(address indexed asset, uint256 newThreshold);

    // Constructor to set the Pyth price feed contract
    constructor(IPyth _pyth) {
        pyth = _pyth;
    }

    // Function to set collateral threshold for a specific asset
    function setCollateralThreshold(address asset, uint256 threshold) external onlyOwner {
        require(asset != address(0), "Invalid asset address");
        require(threshold > 0, "Threshold must be greater than zero");

        collateralThresholds[asset] = threshold;
        emit CollateralThresholdUpdated(asset, threshold);
    }

    // Function to get the current price from Pyth for a specific asset
    function getAssetPrice(bytes32 priceId) public view returns (int256) {
        int256 price = pyth.getPrice(priceId);
        require(price > 0, "Price must be greater than zero");
        return price;
    }

    // Function to calculate whether a position is under liquidation
    function isUnderLiquidation(address asset, bytes32 priceId) external view returns (bool) {
        uint256 threshold = collateralThresholds[asset];
        int256 price = getAssetPrice(priceId);

        // Implement your own logic for checking liquidation
        // Currently checks if the price is below the set threshold
        return uint256(price) < threshold;
    }
}
```
