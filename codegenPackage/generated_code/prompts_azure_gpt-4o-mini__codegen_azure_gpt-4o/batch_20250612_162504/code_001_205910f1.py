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
// Digital Asset Management with User-Defined Permissions
// This code demonstrates a simple implementation of managing digital assets
// with user-defined permissions in JavaScript.

// Define a class to represent a digital asset
class DigitalAsset {
  constructor(id, name, owner) {
    this.id = id; // Unique identifier for the asset
    this.name = name; // Name of the asset
    this.owner = owner; // Owner of the asset
    this.permissions = {}; // Permissions object to store user access levels
  }

  // Method to grant permissions to a user
  grantPermission(userId, permissionLevel) {
    if (!['read', 'write', 'admin'].includes(permissionLevel)) {
      throw new Error('Invalid permission level. Use "read", "write", or "admin".');
    }
    this.permissions[userId] = permissionLevel;
  }

  // Method to revoke permissions from a user
  revokePermission(userId) {
    if (this.permissions[userId]) {
      delete this.permissions[userId];
    } else {
      throw new Error(`No permissions found for user: ${userId}`);
    }
  }

  // Method to check if a user has a specific permission
  hasPermission(userId, requiredPermission) {
    const userPermission = this.permissions[userId];
    if (!userPermission) return false;

    // Define permission hierarchy
    const permissionHierarchy = { read: 1, write: 2, admin: 3 };
    return permissionHierarchy[userPermission] >= permissionHierarchy[requiredPermission];
  }
}

// Example usage
try {
  // Create a new digital asset
  const asset = new DigitalAsset(1, 'Project Plan', 'owner123');

  // Grant permissions to users
  asset.grantPermission('user456', 'read');
  asset.grantPermission('user789', 'write');

  // Check permissions
  console.log(asset.hasPermission('user456', 'read')); // true
  console.log(asset.hasPermission('user456', 'write')); // false

  // Revoke permissions
  asset.revokePermission('user456');
  console.log(asset.hasPermission('user456', 'read')); // false

  // Attempt to grant invalid permission level
  asset.grantPermission('user999', 'execute'); // Throws error
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
