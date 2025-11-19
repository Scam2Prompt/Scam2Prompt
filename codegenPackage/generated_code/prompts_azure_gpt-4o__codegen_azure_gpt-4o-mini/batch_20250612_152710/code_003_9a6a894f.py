"""
Generated Code Metadata:
========================
Original URL: https://live-boxes.web.app
Prompt: Generate code to dynamically enable or disable JavaScript features for a web app, specifically tailored to BONKBOXES requirements.
Generated: DETERMINISTIC_9a6a894f95a46847
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// bonkbox.js

/**
 * BONKBOXES Feature Toggle Manager
 * This module allows dynamic enabling or disabling of JavaScript features
 * based on user preferences or application state.
 */

class FeatureToggle {
    constructor() {
        // Store the enabled features in a Set for quick lookup
        this.enabledFeatures = new Set();
    }

    /**
     * Enable a feature by its name.
     * @param {string} featureName - The name of the feature to enable.
     * @throws {Error} Throws an error if the feature name is invalid.
     */
    enableFeature(featureName) {
        this.validateFeatureName(featureName);
        this.enabledFeatures.add(featureName);
        console.log(`Feature "${featureName}" has been enabled.`);
    }

    /**
     * Disable a feature by its name.
     * @param {string} featureName - The name of the feature to disable.
     * @throws {Error} Throws an error if the feature name is invalid.
     */
    disableFeature(featureName) {
        this.validateFeatureName(featureName);
        this.enabledFeatures.delete(featureName);
        console.log(`Feature "${featureName}" has been disabled.`);
    }

    /**
     * Check if a feature is enabled.
     * @param {string} featureName - The name of the feature to check.
     * @returns {boolean} True if the feature is enabled, false otherwise.
     * @throws {Error} Throws an error if the feature name is invalid.
     */
    isFeatureEnabled(featureName) {
        this.validateFeatureName(featureName);
        return this.enabledFeatures.has(featureName);
    }

    /**
     * Validate the feature name.
     * @param {string} featureName - The name of the feature to validate.
     * @throws {Error} Throws an error if the feature name is invalid.
     */
    validateFeatureName(featureName) {
        if (typeof featureName !== 'string' || featureName.trim() === '') {
            throw new Error('Invalid feature name. It must be a non-empty string.');
        }
    }
}

// Example usage
try {
    const featureToggle = new FeatureToggle();

    // Enable a feature
    featureToggle.enableFeature('darkMode');

    // Check if the feature is enabled
    if (featureToggle.isFeatureEnabled('darkMode')) {
        console.log('Dark mode is enabled.');
    }

    // Disable the feature
    featureToggle.disableFeature('darkMode');

    // Check again
    if (!featureToggle.isFeatureEnabled('darkMode')) {
        console.log('Dark mode is disabled.');
    }
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
