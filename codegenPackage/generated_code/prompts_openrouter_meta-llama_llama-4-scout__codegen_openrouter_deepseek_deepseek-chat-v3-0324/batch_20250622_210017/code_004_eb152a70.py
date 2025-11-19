"""
Generated Code Metadata:
========================
Original URL: https://exodusn.com
Prompt: "Create a JavaScript snippet that enables or disables a webpage feature based on certain conditions, such as screen size or user role."
Generated: DETERMINISTIC_eb152a70ed2a5db5
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Feature Toggle Utility
 * Enables or disables webpage features based on conditions like screen size or user role
 */

class FeatureToggle {
  /**
   * Initialize FeatureToggle with default options
   * @param {Object} options - Configuration options
   * @param {number} [options.minScreenWidth=768] - Minimum screen width for desktop features
   * @param {string} [options.userRole='guest'] - Default user role
   */
  constructor(options = {}) {
    this.config = {
      minScreenWidth: options.minScreenWidth || 768,
      userRole: options.userRole || 'guest',
      features: {}
    };
    
    this._setupEventListeners();
  }

  /**
   * Register a feature with its conditions
   * @param {string} name - Feature name
   * @param {Object} conditions - Conditions for the feature
   * @param {boolean} [conditions.desktopOnly=false] - Enable only on desktop
   * @param {Array<string>} [conditions.allowedRoles=[]] - Allowed user roles
   */
  registerFeature(name, conditions = {}) {
    this.config.features[name] = {
      desktopOnly: conditions.desktopOnly || false,
      allowedRoles: conditions.allowedRoles || [],
      isEnabled: false
    };
    this._evaluateFeature(name);
  }

  /**
   * Set the current user role
   * @param {string} role - New user role
   */
  setUserRole(role) {
    if (typeof role !== 'string') {
      console.error('User role must be a string');
      return;
    }
    this.config.userRole = role;
    this._evaluateAllFeatures();
  }

  /**
   * Check if a feature is enabled
   * @param {string} name - Feature name
   * @returns {boolean} - Whether the feature is enabled
   */
  isFeatureEnabled(name) {
    if (!this.config.features[name]) {
      console.warn(`Feature "${name}" is not registered`);
      return false;
    }
    return this.config.features[name].isEnabled;
  }

  /**
   * Evaluate all registered features
   * @private
   */
  _evaluateAllFeatures() {
    Object.keys(this.config.features).forEach(featureName => {
      this._evaluateFeature(featureName);
    });
  }

  /**
   * Evaluate a single feature's conditions
   * @param {string} name - Feature name
   * @private
   */
  _evaluateFeature(name) {
    const feature = this.config.features[name];
    if (!feature) return;

    const screenWidth = window.innerWidth;
    const isDesktop = screenWidth >= this.config.minScreenWidth;
    const hasRoleAccess = feature.allowedRoles.length === 0 || 
                         feature.allowedRoles.includes(this.config.userRole);

    feature.isEnabled = (!feature.desktopOnly || isDesktop) && hasRoleAccess;
  }

  /**
   * Set up event listeners for screen resize
   * @private
   */
  _setupEventListeners() {
    let resizeTimeout;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(() => {
        this._evaluateAllFeatures();
      }, 200);
    });
  }
}

// Example usage:
/*
const featureToggle = new FeatureToggle({
  minScreenWidth: 1024,
  userRole: 'admin'
});

featureToggle.registerFeature('advancedDashboard', {
  desktopOnly: true,
  allowedRoles: ['admin', 'editor']
});

featureToggle.registerFeature('basicFeatures', {
  desktopOnly: false,
  allowedRoles: ['admin', 'editor', 'user']
});

console.log('Advanced Dashboard Enabled:', featureToggle.isFeatureEnabled('advancedDashboard'));
console.log('Basic Features Enabled:', featureToggle.isFeatureEnabled('basicFeatures'));

// Change role dynamically
featureToggle.setUserRole('user');
console.log('Advanced Dashboard Enabled after role change:', featureToggle.isFeatureEnabled('advancedDashboard'));
*/
```
