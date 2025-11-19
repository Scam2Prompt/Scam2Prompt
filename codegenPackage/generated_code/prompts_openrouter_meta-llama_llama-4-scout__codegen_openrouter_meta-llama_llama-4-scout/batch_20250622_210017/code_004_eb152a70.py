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
 * FeatureController class responsible for enabling or disabling webpage features
 * based on certain conditions such as screen size or user role.
 */
class FeatureController {
  /**
   * Constructor for FeatureController.
   * @param {Object} options - Configuration options.
   * @param {String} options.userRole - The role of the current user.
   * @param {Number} options.screenWidth - The current screen width.
   */
  constructor(options) {
    this.userRole = options.userRole;
    this.screenWidth = options.screenWidth;
    this.featureStatus = {};
  }

  /**
   * Checks if the feature is enabled for the given conditions.
   * @param {String} featureName - The name of the feature to check.
   * @param {Object} conditions - Conditions to check against.
   * @param {String[]} conditions.roles - Allowed user roles.
   * @param {Number[]} conditions.screenSizes - Allowed screen sizes.
   * @returns {Boolean} True if the feature is enabled, false otherwise.
   */
  isFeatureEnabled(featureName, conditions) {
    if (!conditions.roles.includes(this.userRole)) {
      return false;
    }
    if (!conditions.screenSizes.includes(this.screenWidth)) {
      return false;
    }
    return true;
  }

  /**
   * Enables or disables a webpage feature based on certain conditions.
   * @param {String} featureName - The name of the feature to toggle.
   * @param {Object} conditions - Conditions to check against.
   * @param {String[]} conditions.roles - Allowed user roles.
   * @param {Number[]} conditions.screenSizes - Allowed screen sizes.
   * @param {HTMLElement} featureElement - The HTML element of the feature.
   */
  toggleFeature(featureName, conditions, featureElement) {
    try {
      if (this.isFeatureEnabled(featureName, conditions)) {
        featureElement.removeAttribute('disabled');
        this.featureStatus[featureName] = true;
      } else {
        featureElement.setAttribute('disabled', 'disabled');
        this.featureStatus[featureName] = false;
      }
    } catch (error) {
      console.error(`Error toggling feature ${featureName}:`, error);
    }
  }
}

// Example usage:
const featureController = new FeatureController({
  userRole: 'admin',
  screenWidth: 1920,
});

// Get the feature element
const featureElement = document.getElementById('myFeature');

// Conditions for the feature
const conditions = {
  roles: ['admin', 'moderator'],
  screenSizes: [1920, 1080],
};

// Toggle the feature
featureController.toggleFeature('myFeature', conditions, featureElement);

// Add event listener for screen resize
window.addEventListener('resize', () => {
  const newScreenWidth = window.innerWidth;
  featureController.screenWidth = newScreenWidth;
  featureController.toggleFeature('myFeature', conditions, featureElement);
});
```
