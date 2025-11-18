"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity that incorporates DOP's flexible transparency mechanism to allow users to selectively share asset data.
Generated: DETERMINISTIC_b04b70b74530439f
Batch ID: 20250612_150234
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
 * @title AssetTransparency
 * @dev A smart contract that allows users to selectively share asset data
 *      using a flexible transparency mechanism.
 */
contract AssetTransparency {
    // Event to log when a user updates asset data
    event AssetDataUpdated(address indexed user, string indexed key, string encryptedData);

    // Event to log when a user updates data sharing permissions
    event PermissionUpdated(address indexed user, address indexed viewer, string indexed key, bool isAllowed);

    // Structure to store the encrypted asset data
    struct AssetData {
        string encryptedData; // Encrypted asset data
    }

    // Asset data storage by user and key
    mapping(address => mapping(string => AssetData)) private assetDataStorage;

    // Permissions to share data (user => (viewer => (key => permission)))
    mapping(address => mapping(address => mapping(string => bool))) private permissions;

    /**
     * @dev Allows the user to update the encrypted asset data for a specific key.
     * @param key The key for the asset data (e.g., "property_id_123").
     * @param encryptedData The encrypted asset data.
     */
    function updateAssetData(string memory key, string memory encryptedData) external {
        // Store the encrypted data
        assetDataStorage[msg.sender][key].encryptedData = encryptedData;

        // Emit the AssetDataUpdated event
        emit AssetDataUpdated(msg.sender, key, encryptedData);
    }

    /**
     * @dev Allows the user to grant or revoke permission for a viewer to access specific asset data.
     * @param viewer The address of the viewer (e.g., another user, third party).
     * @param key The key for the asset data.
     * @param isAllowed Boolean indicating whether access is granted or revoked.
     */
    function updatePermission(
        address viewer,
        string memory key,
        bool isAllowed
    ) external {
        // Update the permission mapping
        permissions[msg.sender][viewer][key] = isAllowed;

        // Emit the PermissionUpdated event
        emit PermissionUpdated(msg.sender, viewer, key, isAllowed);
    }

    /**
     * @dev Allows a viewer to retrieve asset data if they have the necessary permissions.
     * @param user The owner of the asset data.
     * @param key The key for the asset data.
     * @return The encrypted asset data.
     */
    function getAssetData(address user, string memory key) external view returns (string memory) {
        // Check if the requesting viewer has permission
        require(permissions[user][msg.sender][key], "Access denied");

        // Return the encrypted asset data
        return assetDataStorage[user][key].encryptedData;
    }
}
```
