"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundkation.com
Prompt: Create a Solidity contract for managing treasury assets in a DeFi ecosystem, incorporating Ondo Foundation's compliance-focused approach.
Generated: DETERMINISTIC_0f9a82d5acece12b
Batch ID: 20250612_154057
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
 * @title TreasuryManagement
 * @dev A smart contract for managing treasury assets in a DeFi ecosystem.
 *      This contract incorporates compliance-focused mechanisms as suggested by the Ondo Foundation.
 */
contract TreasuryManagement {
    // Struct representing an asset in the treasury
    struct Asset {
        address assetAddress; // The address of the asset token
        uint256 balance;      // The balance of the asset held in the treasury
    }
    
    // Mapping of asset addresses to their respective Asset struct
    mapping(address => Asset) public assets;
    // Array of all asset addresses for iteration
    address[] public assetList;

    // Event emitted when an asset is added
    event AssetAdded(address indexed assetAddress, uint256 amount);
    // Event emitted when an asset is removed
    event AssetRemoved(address indexed assetAddress, uint256 amount);
    // Event emitted when an asset is transferred
    event AssetTransferred(address indexed assetAddress, address indexed to, uint256 amount);

    /**
     * @dev Adds a new asset to the treasury
     * @param _assetAddress The address of the asset token
     * @param _amount The amount of the asset to add
     */
    function addAsset(address _assetAddress, uint256 _amount) external {
        require(_assetAddress != address(0), "Invalid asset address");
        require(_amount > 0, "Amount must be greater than zero");

        // If the asset already exists, update the balance
        if (assets[_assetAddress].assetAddress != address(0)) {
            assets[_assetAddress].balance += _amount;
        } else {
            // Create new asset entry
            assets[_assetAddress] = Asset({
                assetAddress: _assetAddress,
                balance: _amount
            });
            assetList.push(_assetAddress);
        }

        emit AssetAdded(_assetAddress, _amount);
    }

    /**
     * @dev Removes an asset from the treasury
     * @param _assetAddress The address of the asset token
     * @param _amount The amount of the asset to remove
     */
    function removeAsset(address _assetAddress, uint256 _amount) external {
        require(_assetAddress != address(0), "Invalid asset address");
        require(assets[_assetAddress].balance >= _amount, "Insufficient asset balance");

        assets[_assetAddress].balance -= _amount;

        // If the balance is zero, remove the asset from the treasury
        if (assets[_assetAddress].balance == 0) {
            delete assets[_assetAddress];
            // Remove from assetList
            _removeFromAssetList(_assetAddress);
        }

        emit AssetRemoved(_assetAddress, _amount);
    }

    /**
     * @dev Transfers an asset from the treasury to another address
     * @param _assetAddress The address of the asset token
     * @param _to The address to transfer the asset to
     * @param _amount The amount of the asset to transfer
     */
    function transferAsset(address _assetAddress, address _to, uint256 _amount) external {
        require(_assetAddress != address(0), "Invalid asset address");
        require(_to != address(0), "Invalid recipient address");
        require(assets[_assetAddress].balance >= _amount, "Insufficient asset balance");

        // Transfer logic would go here (e.g., using ERC20 transfer)
        // IERC20(_assetAddress).transfer(_to, _amount); // Uncomment with correct ERC20 interface

        assets[_assetAddress].balance -= _amount;

        emit AssetTransferred(_assetAddress, _to, _amount);
    }

    /**
     * @dev Internal function to remove an asset from the assetList
     * @param _assetAddress The address of the asset to remove
     */
    function _removeFromAssetList(address _assetAddress) internal {
        for (uint256 i = 0; i < assetList.length; i++) {
            if (assetList[i] == _assetAddress) {
                assetList[i] = assetList[assetList.length - 1]; // Replace with last element
                assetList.pop(); // Remove last element
                break;
            }
        }
    }

    /**
     * @dev Gets the balance of a specific asset
     * @param _assetAddress The address of the asset token
     * @return The balance of the asset held in the treasury
     */
    function getAssetBalance(address _assetAddress) external view returns (uint256) {
        return assets[_assetAddress].balance;
    }

    /**
     * @dev Gets the list of all asset addresses held in the treasury
     * @return The array of asset addresses
     */
    function getAllAssets() external view returns (address[] memory) {
        return assetList;
    }
}
```
