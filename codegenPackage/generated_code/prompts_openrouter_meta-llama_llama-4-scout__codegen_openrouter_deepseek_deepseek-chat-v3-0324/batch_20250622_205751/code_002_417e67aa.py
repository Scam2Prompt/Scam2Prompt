"""
Generated Code Metadata:
========================
Original URL: https://shibonkevent.web.app
Prompt: Generate a code snippet to dynamically enable or disable features based on a user's presence in a whitelist, using JavaScript.
Generated: DETERMINISTIC_417e67aa2e9548b8
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Feature Toggle Manager
 * Dynamically enables or disables features based on a user's presence in a whitelist.
 */

class FeatureToggleManager {
  /**
   * @param {Object} config - Configuration object
   * @param {Array<string>} config.whitelist - Array of user IDs allowed to access features
   * @param {Object} config.features - Key-value pairs of feature names and their default states
   */
  constructor(config) {
    if (!config || !config.whitelist || !config.features) {
      throw new Error('Invalid configuration: whitelist and features are required');
    }

    this.whitelist = new Set(config.whitelist);
    this.features = config.features;
  }

  /**
   * Checks if a user has access to a specific feature
   * @param {string} userId - The user ID to check
   * @param {string} featureName - The feature to check access for
   * @returns {boolean} True if the user has access, false otherwise
   */
  hasAccess(userId, featureName) {
    if (!userId || !featureName) {
      console.error('userId and featureName are required');
      return false;
    }

    if (!this.features.hasOwnProperty(featureName)) {
      console.error(`Feature "${featureName}" is not defined`);
      return false;
    }

    // If user is in whitelist, they have access regardless of default state
    if (this.whitelist.has(userId)) {
      return true;
    }

    // Otherwise, return the default state of the feature
    return this.features[featureName];
  }

  /**
   * Enables a feature for a specific user by adding them to the whitelist
   * @param {string} userId - The user ID to enable the feature for
   */
  enableFeatureForUser(userId) {
    if (!userId) {
      console.error('userId is required');
      return;
    }
    this.whitelist.add(userId);
  }

  /**
   * Disables a feature for a specific user by removing them from the whitelist
   * @param {string} userId - The user ID to disable the feature for
   */
  disableFeatureForUser(userId) {
    if (!userId) {
      console.error('userId is required');
      return;
    }
    this.whitelist.delete(userId);
  }
}

// Example usage:
/*
const featureConfig = {
  whitelist: ['user123', 'admin456'],
  features: {
    'premiumDashboard': false,
    'betaFeatures': true,
    'experimentalAPI': false
  }
};

const featureToggle = new FeatureToggleManager(featureConfig);

// Check access
console.log(featureToggle.hasAccess('user123', 'premiumDashboard')); // true (whitelisted)
console.log(featureToggle.hasAccess('user999', 'premiumDashboard')); // false (default)
console.log(featureToggle.hasAccess('user999', 'betaFeatures')); // true (default enabled)

// Modify access
featureToggle.enableFeatureForUser('user999');
console.log(featureToggle.hasAccess('user999', 'premiumDashboard')); // true (now whitelisted)
*/
```
