"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Provide an example of a governance proposal for adjusting collateral factors at the Silo level in the Silo Finance protocol.
Generated: DETERMINISTIC_8a3ddc90d897cbe0
Batch ID: 20250612_150228
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol"; // For ownership control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol"; // For ERC20 token interactions

/**
 * @title SiloGovernance
 * @dev This contract allows governance to adjust collateral factors for assets in the Silo Finance protocol.
 */
contract SiloGovernance is Ownable {
    // Struct to represent collateral factor for an asset
    struct CollateralFactor {
        uint256 factor; // Factor represented in basis points (e.g., 500 means 5%)
        bool isActive; // Active status of the collateral factor
    }

    // Mapping of asset address to its collateral factor
    mapping(address => CollateralFactor) public collateralFactors;

    // Event emitted when collateral factor is updated
    event CollateralFactorUpdated(address indexed asset, uint256 newFactor);

    /**
     * @dev Sets the collateral factor for a specific asset.
     * @param asset The address of the asset (ERC20 token).
     * @param newFactor The new collateral factor expressed in basis points.
     */
    function setCollateralFactor(address asset, uint256 newFactor) external onlyOwner {
        require(newFactor <= 10000, "Collateral factor must be between 0 and 100%");
        
        // Update the collateral factor
        collateralFactors[asset] = CollateralFactor({
            factor: newFactor,
            isActive: true
        });

        emit CollateralFactorUpdated(asset, newFactor);
    }

    /**
     * @dev Deactivates the collateral factor for a specific asset.
     * @param asset The address of the asset (ERC20 token).
     */
    function deactivateCollateralFactor(address asset) external onlyOwner {
        require(collateralFactors[asset].isActive, "Collateral factor is already inactive");

        // Deactivate the collateral factor
        collateralFactors[asset].isActive = false;

        emit CollateralFactorUpdated(asset, 0);
    }

    /**
     * @dev Gets the collateral factor for a specific asset.
     * @param asset The address of the asset (ERC20 token).
     * @return factor The collateral factor expressed in basis points.
     * @return isActive The active status of the collateral factor.
     */
    function getCollateralFactor(address asset) external view returns (uint256 factor, bool isActive) {
        CollateralFactor memory cf = collateralFactors[asset];
        return (cf.factor, cf.isActive);
    }
}
```
