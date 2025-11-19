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
/**
 * Digital Asset Management with User-Defined Permissions
 * This code snippet demonstrates how to manage digital assets using a permission system.
 * Users can be assigned specific roles and permissions to interact with assets.
 */

// Define the roles and permissions
const roles = {
  admin: ['create', 'read', 'update', 'delete'],
  editor: ['create', 'read', 'update'],
  viewer: ['read'],
};

// Class representing a Digital Asset
class DigitalAsset {
  constructor(id, name, owner) {
    this.id = id; // Unique identifier for the asset
    this.name = name; // Name of the asset
    this.owner = owner; // Owner of the asset
    this.permissions = {}; // Permissions assigned to users
  }

  // Method to assign permissions to a user
  assignPermission(user, role) {
    if (!roles[role]) {
      throw new Error(`Invalid role: ${role}`);
    }
    this.permissions[user] = role;
  }

  // Method to check if a user has permission to perform an action
  hasPermission(user, action) {
    const role = this.permissions[user];
    if (!role) {
      return false; // User does not have any assigned role
    }
    return roles[role].includes(action);
  }
}

// Simulated User class for demonstration purposes
class User {
  constructor(id, name) {
    this.id = id; // Unique identifier for the user
    this.name = name; // Name of the user
  }
}

// Example usage
try {
  const user1 = new User(1, 'Alice');
  const user2 = new User(2, 'Bob');

  const asset = new DigitalAsset(101, 'Project Umbrella', user1.id);

  // Assign permissions to users
  asset.assignPermission(user1.id, 'admin');
  asset.assignPermission(user2.id, 'viewer');

  // Check permissions and perform actions
  console.log(`User ${user1.name} can delete: ${asset.hasPermission(user1.id, 'delete')}`); // true
  console.log(`User ${user2.name} can delete: ${asset.hasPermission(user2.id, 'delete')}`); // false

  // Attempting invalid permission assignment
  asset.assignPermission(user2.id, 'invalidRole'); // Throws an error
} catch (err) {
  console.error(`Error: ${err.message}`);
}

/**
 * Notes:
 * - This code snippet demonstrates a simple role-based permission system.
 * - In production, consider integrating with a secure authentication service to validate user identities.
 */
```
