"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Provide a detailed example of creating and installing a Zoe contract facet bundle using the Agoric SDK, ensuring the `yarn build` step is included to generate the contract facet bundle.
Generated: DETERMINISTIC_96da06df7e0f8683
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Agoric SDK
import { E } from '@endo/eventual-send';
import fs from 'fs';
import path from 'path';

// Define the Zoe contract facet bundle creation and installation
async function createAndInstallContractFacetBundle(homePromise) {
  const home = await homePromise;
  
  // Extract Zoe from the home object
  const { zoe, board } = home;

  // Path to the contract source directory
  const contractRoot = path.resolve('./contract');

  // Ensure the contract folder exists
  if (!fs.existsSync(contractRoot)) {
    throw new Error(`Contract source folder "${contractRoot}" does not exist.`);
  }

  // Run the build step to generate the contract facet bundle
  console.log('Running `yarn build` to generate contract facet bundle...');
  const { execSync } = require('child_process');
  execSync('yarn build', { cwd: contractRoot, stdio: 'inherit' });

  // Path to the generated contract bundle
  const bundlePath = path.resolve(contractRoot, './build/bundle.js');

  // Ensure the bundle file exists
  if (!fs.existsSync(bundlePath)) {
    throw new Error(`Bundle file "${bundlePath}" does not exist. Make sure `yarn build` was successful.`);
  }

  // Read the generated bundle file
  const bundle = fs.readFileSync(bundlePath, 'utf-8');

  // Install the contract on Zoe
  console.log('Installing contract bundle on Zoe...');
  const installation = await E(zoe).install(bundle);

  // Store the installation reference in the Agoric board for sharing
  console.log('Storing installation in the Agoric board...');
  const boardId = await E(board).getId(installation);

  console.log(`Contract installation complete. Board ID: ${boardId}`);
  return boardId;
}

// Example usage
(async () => {
  const homePromise = await import('@agoric/web-components/home.js'); // Adjust path based on environment
  try {
    const boardId = await createAndInstallContractFacetBundle(homePromise);
    console.log(`Contract installed and available at Board ID: ${boardId}`);
  } catch (error) {
    console.error('Error creating and installing contract facet bundle:', error);
  }
})();
```

Make sure the Agoric environment is properly set up, and the contract source directory contains the required files. Adjust paths accordingly based on your setup.
