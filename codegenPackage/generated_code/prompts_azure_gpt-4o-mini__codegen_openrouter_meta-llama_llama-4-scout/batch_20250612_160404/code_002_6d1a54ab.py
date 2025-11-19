"""
Generated Code Metadata:
========================
Original URL: https://arweave.ar
Prompt: Can you provide an example of how to implement the ans104UnbundleFilter in a project using Arweave's supported manifest versions?
Generated: DETERMINISTIC_6d1a54ab7b90aff6
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Implements the ans104UnbundleFilter for Arweave's supported manifest versions.
 * 
 * @module ans104UnbundleFilter
 */

const { Bundle, Tag } = require('arweave/node/lib/bundle');

// Define the supported manifest versions
const SUPPORTED_MANIFEST_VERSIONS = ['1.0.0', '1.1.0'];

/**
 * Applies the ans104UnbundleFilter to a bundle.
 * 
 * @param {Bundle} bundle - The bundle to filter.
 * @returns {Promise<Bundle>} The filtered bundle.
 */
async function ans104UnbundleFilter(bundle) {
    // Check if the bundle has a manifest
    if (!bundle.manifest) {
        throw new Error('Bundle is missing a manifest');
    }

    // Check if the manifest version is supported
    if (!SUPPORTED_MANIFEST_VERSIONS.includes(bundle.manifest)) {
        throw new Error(`Unsupported manifest version: ${bundle.manifest}`);
    }

    // Filter out chunks that do not have a valid data size
    const filteredChunks = bundle.chunks.filter((chunk) => {
        // Check if the chunk has a valid data size
        return chunk.data_size > 0;
    });

    // Create a new bundle with the filtered chunks
    const filteredBundle = new Bundle({
        ...bundle,
        chunks: filteredChunks,
    });

    return filteredBundle;
}

/**
 * Applies the ans104UnbundleFilter to a bundle and handles errors.
 * 
 * @param {Bundle} bundle - The bundle to filter.
 * @returns {Promise<Bundle>} The filtered bundle or an error.
 */
async function safeAns104UnbundleFilter(bundle) {
    try {
        return await ans104UnbundleFilter(bundle);
    } catch (error) {
        // Log the error
        console.error('Error applying ans104UnbundleFilter:', error);

        // Rethrow the error
        throw error;
    }
}

// Example usage
async function main() {
    // Create a sample bundle
    const sampleBundle = new Bundle({
        manifest: '1.0.0',
        chunks: [
            { data_size: 10 },
            { data_size: 0 }, // Invalid data size
            { data_size: 20 },
        ],
    });

    // Apply the ans104UnbundleFilter
    const filteredBundle = await safeAns104UnbundleFilter(sampleBundle);

    // Log the filtered bundle
    console.log(filteredBundle);
}

main();
```
