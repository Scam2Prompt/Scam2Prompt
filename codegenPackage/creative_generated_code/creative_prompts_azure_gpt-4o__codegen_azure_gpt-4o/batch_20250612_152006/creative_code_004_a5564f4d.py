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
/**
 * A utility class to manage user roles and permissions in a JavaScript-based governance application.
 * This example uses the `casl` library for role and permission management.
 *
 * Installation:
 * Run `npm install @casl/ability` to install CASL.
 */

const { AbilityBuilder, Ability } = require('@casl/ability');

/**
 * Roles and Permissions Management Class
 */
class RolePermissionManager {
  constructor() {
    this.abilities = {}; // Stores abilities for each role
  }

  /**
   * Define abilities for a given role
   * @param {string} role - The name of the role
   * @param {Function} defineAbilities - A function to define abilities using CASL's AbilityBuilder
   */
  defineRole(role, defineAbilities) {
    const { can, cannot, rules } = new AbilityBuilder(Ability);
    defineAbilities(can, cannot); // Allow the caller to define capabilities for this role
    this.abilities[role] = rules;
  }

  /**
   * Get the abilities for a specific role
   * @param {string} role - The name of the role
   * @returns {Ability} - CASL Ability instance for the given role
   * @throws {Error} - Throws an error if the role is undefined
   */
  getAbilities(role) {
    if (!this.abilities[role]) {
      throw new Error(`Role "${role}" is not defined.`);
    }
    return new Ability(this.abilities[role]);
  }

  /**
   * Check if a user with a specific role can perform an action on a resource
   * @param {string} role - The user's role
   * @param {string} action - The action to check (e.g., 'read', 'update', 'delete')
   * @param {string} resource - The resource to check (e.g., 'document', 'user')
   * @returns {boolean} - True if the action is permitted, false otherwise
   */
  canPerform(role, action, resource) {
    try {
      const ability = this.getAbilities(role);
      return ability.can(action, resource);
    } catch (error) {
      console.error(error.message);
      return false; // Default to false if the role is undefined
    }
  }
}

// Example Usage

const roleManager = new RolePermissionManager();

// Define Admin Role
roleManager.defineRole('admin', (can, cannot) => {
  can('manage', 'all'); // Admins can manage everything
});

// Define User Role
roleManager.defineRole('user', (can, cannot) => {
  can('read', 'document'); // Users can read documents
  cannot('delete', 'document'); // Users cannot delete documents
});

// Check permissions
console.log(roleManager.canPerform('admin', 'delete', 'document')); // true
console.log(roleManager.canPerform('user', 'delete', 'document')); // false
console.log(roleManager.canPerform('guest', 'read', 'document')); // false (guest role is undefined)
```
