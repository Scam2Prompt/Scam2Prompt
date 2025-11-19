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
// This script demonstrates the yarn build process in Agoric SDK
// and how it generates kernel bundles for the Agoric VM.

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

/**
 * Builds Agoric components and generates kernel bundles
 * @throws {Error} If build process fails
 */
function buildAgoricSDK() {
  try {
    console.log('Starting Agoric SDK build process...');
    
    // Run yarn build which compiles all packages
    execSync('yarn build', { stdio: 'inherit' });
    
    // Verify kernel bundle generation
    const kernelBundlePath = path.join(
      process.cwd(), 
      'packages', 
      'kernel', 
      'bundles', 
      'bundle-kernel.js'
    );
    
    if (!fs.existsSync(kernelBundlePath)) {
      throw new Error('Kernel bundle not generated');
    }
    
    console.log('Agoric SDK build completed successfully');
    console.log(`Kernel bundle generated at: ${kernelBundlePath}`);
    
    return kernelBundlePath;
  } catch (error) {
    console.error('Build process failed:', error.message);
    throw error;
  }
}

// Example usage
if (require.main === module) {
  buildAgoricSDK();
}
```
