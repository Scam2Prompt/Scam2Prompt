"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://umbrella-d96b1.web.app
Prompt: Write a JavaScript code snippet that demonstrates how to manage digital assets with user-defined permissions, inspired by the Umbrella platform.
Generated: DETERMINISTIC_205910f1131d33ca
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// DigitalAssetManager class to manage digital assets with user-defined permissions.
class DigitalAssetManager {
    constructor() {
        // Map to hold assets and their associated permissions
        this.assets = new Map();
    }

    /**
     * Adds a new asset with user-defined permissions.
     * @param {string} assetId - The unique identifier for the asset.
     * @param {Array<string>} permissions - Array of permission strings for the asset.
     * @throws {Error} If the asset already exists.
     */
    addAsset(assetId, permissions) {
        if (this.assets.has(assetId)) {
            throw new Error(`Asset with ID ${assetId} already exists.`);
        }
        this.assets.set(assetId, new Set(permissions));
    }

    /**
     * Updates the permissions of an existing asset.
     * @param {string} assetId - The unique identifier for the asset.
     * @param {Array<string>} newPermissions - Array of new permission strings.
     * @throws {Error} If the asset does not exist.
     */
    updatePermissions(assetId, newPermissions) {
        if (!this.assets.has(assetId)) {
            throw new Error(`Asset with ID ${assetId} does not exist.`);
        }
        this.assets.set(assetId, new Set(newPermissions));
    }

    /**
     * Checks if a user has permission to access an asset.
     * @param {string} assetId - The unique identifier for the asset.
     * @param {string} permission - The permission to check.
     * @returns {boolean} True if the user has the permission, false otherwise.
     * @throws {Error} If the asset does not exist.
     */
    hasPermission(assetId, permission) {
        if (!this.assets.has(assetId)) {
            throw new Error(`Asset with ID ${assetId} does not exist.`);
        }
        return this.assets.get(assetId).has(permission);
    }

    /**
     * Retrieves the permissions of a specific asset.
     * @param {string} assetId - The unique identifier for the asset.
     * @returns {Array<string>} An array of permission strings.
     * @throws {Error} If the asset does not exist.
     */
    getPermissions(assetId) {
        if (!this.assets.has(assetId)) {
            throw new Error(`Asset with ID ${assetId} does not exist.`);
        }
        return Array.from(this.assets.get(assetId));
    }
}

// Example usage
try {
    const assetManager = new DigitalAssetManager();
    assetManager.addAsset("asset1", ["read", "write"]);
    console.log(assetManager.hasPermission("asset1", "read")); // true
    console.log(assetManager.getPermissions("asset1")); // ['read', 'write']
    assetManager.updatePermissions("asset1", ["read"]);
    console.log(assetManager.getPermissions("asset1")); // ['read']
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
