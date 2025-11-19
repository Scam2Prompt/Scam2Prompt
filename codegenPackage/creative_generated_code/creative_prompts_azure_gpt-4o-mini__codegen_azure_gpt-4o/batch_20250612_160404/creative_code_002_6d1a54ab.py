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
// Import necessary modules
const Arweave = require('arweave');

/**
 * ans104UnbundleFilter - Filters files based on ans104 unbundling logic
 * 
 * This function helps to parse and unbundle files from an Arweave transaction 
 * manifest that adheres to Arweave Naming System (ANS-104) specifications.
 *
 * @param {Object} manifest - The manifest object fetched from Arweave.
 * @returns {Array} - Filtered list of unbundled files from the manifest.
 */
function ans104UnbundleFilter(manifest) {
  try {
    // Validate manifest structure
    if (!manifest || typeof manifest !== 'object' || !manifest.version || !manifest.paths) {
      throw new Error('Invalid manifest structure');
    }

    // Supported manifest versions
    const supportedVersions = ['0.1', '0.2', '0.3'];

    // Check if manifest version is supported
    if (!supportedVersions.includes(manifest.version)) {
      throw new Error(`Unsupported manifest version: ${manifest.version}`);
    }

    // Extract and filter file paths from manifest
    const filteredPaths = Object.keys(manifest.paths)
      .map(path => ({
        path,
        data: manifest.paths[path]
      }))
      .filter(file => {
        // Example filter logic: Include files with a defined 'content-type'
        return file.data && file.data['content-type'];
      });

    return filteredPaths;
  } catch (error) {
    // Log error details
    console.error('Error in ans104UnbundleFilter:', error.message);
    return [];
  }
}

// Example usage
(async () => {
  // Initialize Arweave client
  const arweave = Arweave.init({
    host: 'arweave.net', // Arweave Gateway
    port: 443,          // HTTPS port
    protocol: 'https'   // Protocol
  });

  try {
    // Fetch a transaction's manifest (replace 'transactionId' with an actual ID)
    const transactionId = 'replace_with_actual_transaction_id';
    const transactionData = await arweave.transactions.getData(transactionId, { decode: true, string: true });
    const manifest = JSON.parse(transactionData);

    // Apply ans104 unbundling filter
    const unbundledFiles = ans104UnbundleFilter(manifest);

    // Log the filtered files
    console.log('Unbundled files:', unbundledFiles);

  } catch (error) {
    // Handle Arweave client errors
    console.error('Error fetching manifest from Arweave:', error.message);
  }
})();
```
