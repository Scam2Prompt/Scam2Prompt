"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: What is the purpose of the yarn build step in the Agoric SDK, and how does it relate to generating kernel bundles?
Generated: DETERMINISTIC_f434f479e845c01d
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules from the Agoric SDK
import { buildKernelBundles } from '@agoric/kernel/src/kernel/bundles.js';
import { writeFileSync } from 'fs';
import { join } from 'path';

/**
 * The purpose of the yarn build step in the Agoric SDK is to compile
 * the source code and generate the necessary kernel bundles that
 * are required for the Agoric platform to function correctly.
 * 
 * This script automates the build process and handles errors gracefully.
 */

async function buildAgoricKernelBundles(outputDir) {
  try {
    // Ensure the output directory exists
    if (!outputDir) {
      throw new Error('Output directory must be specified.');
    }

    // Generate kernel bundles
    const bundles = await buildKernelBundles();

    // Write each bundle to the specified output directory
    for (const [bundleName, bundleContent] of Object.entries(bundles)) {
      const filePath = join(outputDir, `${bundleName}.js`);
      writeFileSync(filePath, bundleContent);
      console.log(`Successfully wrote bundle: ${filePath}`);
    }

    console.log('All kernel bundles have been built successfully.');
  } catch (error) {
    // Handle errors during the build process
    console.error('Error during the build process:', error.message);
    process.exit(1); // Exit with a failure code
  }
}

// Example usage: specify the output directory for the bundles
const outputDirectory = './dist/kernel-bundles';
buildAgoricKernelBundles(outputDirectory);
```
