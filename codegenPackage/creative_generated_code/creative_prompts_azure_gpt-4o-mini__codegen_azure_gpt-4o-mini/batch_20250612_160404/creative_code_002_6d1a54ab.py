"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arweave.ar
Prompt: Can you provide an example of how to implement the ans104UnbundleFilter in a project using Arweave's supported manifest versions?
Generated: DETERMINISTIC_6d1a54ab7b90aff6
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { createFilter } = require('arweave/node/lib/filter');
const { getManifest } = require('arweave/node/lib/manifest');

// Define the ans104UnbundleFilter function
/**
 * Creates a filter that unbundles assets from an Arweave manifest.
 * 
 * @param {Object} manifest - The manifest object to be processed.
 * @returns {Function} - A function that filters the unbundled assets.
 */
function ans104UnbundleFilter(manifest) {
    // Validate the input manifest
    if (!manifest || typeof manifest !== 'object') {
        throw new Error('Invalid manifest object provided.');
    }

    // Check if the manifest version is supported
    const supportedVersions = ['1.0.4', '1.1.0']; // Example supported versions
    if (!supportedVersions.includes(manifest.version)) {
        throw new Error('Unsupported manifest version: ' + manifest.version);
    }

    // Create a filter for unbundling assets
    return createFilter(function (asset) {
        // Check if the asset is not bundled
        return !asset.bundled;
    });
}

// Example usage
(async () => {
    try {
        // Fetch the manifest for a specific Arweave transaction
        const transactionId = 'exampleTransactionId'; // Replace with actual transaction ID
        const manifest = await getManifest(transactionId);

        // Create the unbundle filter based on the fetched manifest
        const unbundleFilter = ans104UnbundleFilter(manifest);

        // Apply the filter to the assets in the manifest
        const unbundledAssets = manifest.assets.filter(unbundleFilter);

        console.log('Unbundled Assets:', unbundledAssets);
    } catch (error) {
        // Handle errors appropriately
        console.error('An error occurred:', error.message);
    }
})();
```

Make sure to replace `'exampleTransactionId'` with an actual transaction ID for testing.
