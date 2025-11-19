"""
Generated Code Metadata:
========================
Original URL: https://governance-sym.biotic.fi
Prompt: Create a JavaScript function to dynamically enable or disable specific app features based on user permissions, as might be required for a governance platform.
Generated: DETERMINISTIC_c604b93d8ceee915
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Feature Toggle Manager for Governance Platform
 * Dynamically enables/disables features based on user permissions
 */

class FeatureToggleManager {
  /**
   * Initialize the FeatureToggleManager with user permissions
   * @param {Object} userPermissions - User permissions object
   * @param {Object} featureConfig - Feature configuration object
   */
  constructor(userPermissions, featureConfig) {
    if (!userPermissions || typeof userPermissions !== 'object') {
      throw new Error('Invalid user permissions provided');
    }
    if (!featureConfig || typeof featureConfig !== 'object') {
      throw new Error('Invalid feature configuration provided');
    }

    this.userPermissions = userPermissions;
    this.featureConfig = featureConfig;
    this.enabledFeatures = {};
  }

  /**
   * Check if a feature is enabled for the user
   * @param {string} featureName - Name of the feature to check
   * @returns {boolean} Whether the feature is enabled
   */
  isFeatureEnabled(featureName) {
    if (!featureName || typeof featureName !== 'string') {
      throw new Error('Invalid feature name provided');
    }

    // Check if we've already determined this feature's status
    if (this.enabledFeatures.hasOwnProperty(featureName)) {
      return this.enabledFeatures[featureName];
    }

    // Get feature configuration
    const feature = this.featureConfig[featureName];
    if (!feature) {
      console.warn(`Feature "${featureName}" not found in configuration`);
      return false;
    }

    // Check if feature is globally disabled
    if (feature.globallyDisabled === true) {
      this.enabledFeatures[featureName] = false;
      return false;
    }

    // Check permission requirements
    const requiredPermissions = feature.requiredPermissions || [];
    const hasPermission = requiredPermissions.every(perm => 
      this.userPermissions[perm] === true
    );

    this.enabledFeatures[featureName] = hasPermission;
    return hasPermission;
  }

  /**
   * Get all enabled features for the user
   * @returns {Object} Object with feature names as keys and enabled status as values
   */
  getAllEnabledFeatures() {
    Object.keys(this.featureConfig).forEach(featureName => {
      if (!this.enabledFeatures.hasOwnProperty(featureName)) {
        this.isFeatureEnabled(featureName);
      }
    });
    return {...this.enabledFeatures};
  }

  /**
   * Update user permissions and reset feature cache
   * @param {Object} newPermissions - Updated user permissions
   */
  updateUserPermissions(newPermissions) {
    if (!newPermissions || typeof newPermissions !== 'object') {
      throw new Error('Invalid user permissions provided');
    }
    this.userPermissions = newPermissions;
    this.enabledFeatures = {}; // Reset cache
  }
}

// Example usage:
/*
const userPermissions = {
  canEditContent: true,
  canManageUsers: false,
  canViewReports: true
};

const featureConfig = {
  contentEditor: {
    requiredPermissions: ['canEditContent'],
    globallyDisabled: false
  },
  userManagement: {
    requiredPermissions: ['canManageUsers'],
    globallyDisabled: false
  },
  reportingDashboard: {
    requiredPermissions: ['canViewReports'],
    globallyDisabled: false
  },
  experimentalFeature: {
    requiredPermissions: [],
    globallyDisabled: true
  }
};

const featureManager = new FeatureToggleManager(userPermissions, featureConfig);
console.log(featureManager.isFeatureEnabled('contentEditor')); // true
console.log(featureManager.isFeatureEnabled('userManagement')); // false
console.log(featureManager.getAllEnabledFeatures());
*/
```
