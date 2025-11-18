"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://governance-sym.biotic.fi
Prompt: Suggest APIs or libraries for managing user roles and permissions in a JavaScript-based governance application similar to "Symbiotic Governance."
Generated: DETERMINISTIC_a5564f4dc0df037c
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// userRolesPermissions.js

/**
 * A simple user role and permission management system for a governance application.
 * This module provides functions for defining roles, assigning permissions, 
 * and checking user permissions.
 */

// Define user roles and their associated permissions
const roles = {
    ADMIN: 'admin',
    MODERATOR: 'moderator',
    USER: 'user',
};

// Define available permissions
const permissions = {
    CREATE_CONTENT: 'create_content',
    EDIT_CONTENT: 'edit_content',
    DELETE_CONTENT: 'delete_content',
    VIEW_CONTENT: 'view_content',
};

// Role-Permission Mapping
const rolePermissions = {
    [roles.ADMIN]: [
        permissions.CREATE_CONTENT,
        permissions.EDIT_CONTENT,
        permissions.DELETE_CONTENT,
        permissions.VIEW_CONTENT,
    ],
    [roles.MODERATOR]: [
        permissions.EDIT_CONTENT,
        permissions.VIEW_CONTENT,
    ],
    [roles.USER]: [
        permissions.VIEW_CONTENT,
    ],
};

// User database for demonstration; in a real application, this would be a proper database
const users = {};

/**
 * Adds a user to the system with a specified role.
 * @param {string} userId - Unique identifier for the user
 * @param {string} role - The role to assign to the user
 * @throws Will throw an error if the role is not valid
 */
function addUser(userId, role) {
    if (!roles[role]) {
        throw new Error(`Invalid role: ${role}`);
    }

    users[userId] = {
        id: userId,
        role: role,
    };
}

/**
 * Checks if a user has a specific permission.
 * @param {string} userId - Unique identifier for the user
 * @param {string} permission - Permission to check
 * @returns {boolean} - Returns true if the user has the permission, otherwise false
 * @throws Will throw an error if the user does not exist
 */
function hasPermission(userId, permission) {
    if (!users[userId]) {
        throw new Error(`User not found: ${userId}`);
    }

    const userRole = users[userId].role;
    const userPermissions = rolePermissions[userRole] || [];

    return userPermissions.includes(permission);
}

// Example usage (Uncomment to test)
// addUser('user1', 'admin');
// console.log(hasPermission('user1', 'create_content')); // true
// console.log(hasPermission('user1', 'edit_content')); // true
// console.log(hasPermission('user1', 'view_content')); // true

// Export functions for external use
module.exports = {
    addUser,
    hasPermission,
    roles,
    permissions,
};
```
