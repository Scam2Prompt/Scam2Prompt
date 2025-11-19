"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://huijiatw.com
Prompt: What libraries or APIs can assist in ensuring JavaScript compatibility on the KING website?
Generated: DETERMINISTIC_de95bfb5e355bbcb
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Compatibility Check Module
 * This module checks JavaScript compatibility for the KING website
 * using the caniuse-lite database and the Browserslist library.
 * 
 * Dependencies:
 * - Browserslist: A query language for targeting specific browser versions.
 * - caniuse-lite: A database for tracking feature compatibility across browsers.
 * 
 * Ensure to install the required libraries:
 * npm install browserslist caniuse-lite
 */

const browserslist = require('browserslist');
const caniuseDb = require('caniuse-lite');

/**
 * Function to check if a feature is supported in the specified browsers.
 * @param {string} feature - The feature to check (e.g., "fetch", "Promise").
 * @param {string[]} browsers - Array of browser names or queries.
 * @returns {boolean} - Returns true if the feature is supported, false otherwise.
 */
function isFeatureSupported(feature, browsers) {
    try {
        // Get the support data for the feature from caniuse-lite
        const supportData = caniuseDb.features[feature];
        if (!supportData) {
            throw new Error(`Feature "${feature}" not found in caniuse-lite.`);
        }

        // Get the list of supported browsers for the feature
        const support = supportData.stats;

        // Check against the specified browsers
        for (const browser of browsers) {
            const version = browserslist(browser)[0];
            if (support[version] && support[version][0] === 'y') {
                return true; // Feature is supported in this browser version
            }
        }
        return false; // Feature not supported in any of the given browsers
    } catch (error) {
        console.error(`Error checking feature support: ${error.message}`);
        return false; // Return false if an error occurs
    }
}

// Example Usage
const browsers = ['> 1%', 'last 2 versions', 'not dead'];
const featureToCheck = 'fetch';

const isSupported = isFeatureSupported(featureToCheck, browsers);
console.log(`Is "${featureToCheck}" supported in the specified browsers? ${isSupported}`);
```
