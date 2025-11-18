"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestwebtrand.cc
Prompt: Write a script using Cadence to dynamically enable or disable JavaScript features based on user preferences.
Generated: DETERMINISTIC_abfa143ed64a6b34
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { API, FeatureFlags } from 'your-feature-toggle-library'; // Replace with actual library

/**
 * Dynamically enable or disable JavaScript features based on user preferences.
 * 
 * @param {Object} userPreferences - The user's feature preferences.
 * @param {Array} userPreferences.enabledFeatures - Array of feature names to enable.
 * @param {Array} userPreferences.disabledFeatures - Array of feature names to disable.
 * @throws {Error} Will throw an error if userPreferences is not an object or is improperly structured.
 */
async function configureFeatures(userPreferences) {
    // Validate userPreferences input
    if (typeof userPreferences !== 'object' || userPreferences === null) {
        throw new Error('Invalid user preferences: Expected an object.');
    }

    const { enabledFeatures = [], disabledFeatures = [] } = userPreferences;

    // Ensure enabledFeatures and disabledFeatures are arrays
    if (!Array.isArray(enabledFeatures) || !Array.isArray(disabledFeatures)) {
        throw new Error('Invalid feature lists: Both enabledFeatures and disabledFeatures should be arrays.');
    }

    try {
        // Iterate through enabled features and activate them
        for (const feature of enabledFeatures) {
            await FeatureFlags.enable(feature);
            console.log(`Feature ${feature} has been enabled.`);
        }

        // Iterate through disabled features and deactivate them
        for (const feature of disabledFeatures) {
            await FeatureFlags.disable(feature);
            console.log(`Feature ${feature} has been disabled.`);
        }

    } catch (error) {
        console.error('Error while configuring features:', error);
        throw new Error('Failed to configure features due to an internal error.');
    }
}

// Example usage
(async () => {
    const userPreferences = {
        enabledFeatures: ['feature1', 'feature2'],
        disabledFeatures: ['feature3']
    };

    try {
        await configureFeatures(userPreferences);
        console.log('Features configured successfully.');
    } catch (error) {
        console.error('Error:', error.message);
    }
})();
```
