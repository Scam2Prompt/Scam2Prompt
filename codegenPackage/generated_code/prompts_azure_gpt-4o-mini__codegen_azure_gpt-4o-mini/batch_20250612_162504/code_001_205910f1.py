"""
Generated Code Metadata:
========================
Original URL: https://umbrella-d96b1.web.app
Prompt: Write a JavaScript code snippet that demonstrates how to manage digital assets with user-defined permissions, inspired by the Umbrella platform.
Generated: DETERMINISTIC_205910f1131d33ca
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// DigitalAssetManager class to manage digital assets with user-defined permissions
class DigitalAssetManager {
    constructor() {
        // Initialize an empty object to hold assets and their permissions
        this.assets = {};
    }

    /**
     * Adds a new digital asset with specified permissions.
     * @param {string} assetId - Unique identifier for the asset.
     * @param {Object} permissions - Object defining user permissions for the asset.
     * @throws Will throw an error if the asset already exists.
     */
    addAsset(assetId, permissions) {
        if (this.assets[assetId]) {
            throw new Error(`Asset with ID ${assetId} already exists.`);
        }
        this.assets[assetId] = {
            permissions: permissions,
            data: null // Placeholder for asset data
        };
    }

    /**
     * Updates the permissions for an existing asset.
     * @param {string} assetId - Unique identifier for the asset.
     * @param {Object} newPermissions - New permissions to set for the asset.
     * @throws Will throw an error if the asset does not exist.
     */
    updatePermissions(assetId, newPermissions) {
        if (!this.assets[assetId]) {
            throw new Error(`Asset with ID ${assetId} does not exist.`);
        }
        this.assets[assetId].permissions = newPermissions;
    }

    /**
     * Retrieves the asset data if the user has permission.
     * @param {string} assetId - Unique identifier for the asset.
     * @param {string} userId - User ID requesting access.
     * @returns {Object|null} - Returns asset data or null if access is denied.
     */
    getAssetData(assetId, userId) {
        const asset = this.assets[assetId];
        if (!asset) {
            throw new Error(`Asset with ID ${assetId} does not exist.`);
        }
        if (this.hasPermission(asset.permissions, userId)) {
            return asset.data;
        } else {
            console.warn(`User ${userId} does not have permission to access asset ${assetId}.`);
            return null;
        }
    }

    /**
     * Checks if a user has permission to access the asset.
     * @param {Object} permissions - The permissions object for the asset.
     * @param {string} userId - User ID to check permissions for.
     * @returns {boolean} - True if the user has permission, false otherwise.
     */
    hasPermission(permissions, userId) {
        return permissions[userId] === true; // Simple boolean permission check
    }

    /**
     * Sets the asset data for a given asset.
     * @param {string} assetId - Unique identifier for the asset.
     * @param {Object} data - The data to set for the asset.
     * @throws Will throw an error if the asset does not exist.
     */
    setAssetData(assetId, data) {
        if (!this.assets[assetId]) {
            throw new Error(`Asset with ID ${assetId} does not exist.`);
        }
        this.assets[assetId].data = data;
    }
}

// Example usage
try {
    const manager = new DigitalAssetManager();
    manager.addAsset('asset1', { 'user1': true, 'user2': false });
    manager.setAssetData('asset1', { content: 'This is a digital asset.' });

    const data = manager.getAssetData('asset1', 'user1'); // Should return the asset data
    console.log(data);

    const deniedData = manager.getAssetData('asset1', 'user2'); // Should return null
    console.log(deniedData);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
