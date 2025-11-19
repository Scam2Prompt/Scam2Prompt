"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: How do I run unit tests for a single package, such as eventual-send, in the Agoric SDK?
Generated: DETERMINISTIC_48a614359a450c8f
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
#!/usr/bin/env node

/**
 * Run unit tests for a single package in the Agoric SDK.
 * 
 * Usage: node run-unit-tests.js <package-name>
 * 
 * @param {string} packageName - The name of the package to test.
 */

// Check if package name is provided
if (process.argv.length !== 3) {
  console.error('Error: Please provide the package name.');
  console.error('Usage: node run-unit-tests.js <package-name>');
  process.exit(1);
}

const packageName = process.argv[2];

/**
 * Run unit tests for the specified package.
 * 
 * @param {string} packageName - The name of the package to test.
 */
function runUnitTests(packageName) {
  try {
    // Navigate to the package directory
    const { execSync } = require('child_process');
    const { join } = require('path');
    const rootDir = join(__dirname, '..');
    process.chdir(rootDir);

    // Run unit tests using Jest
    const testCommand = `jest packages/${packageName}/test`;
    execSync(testCommand, { stdio: 'inherit' });
  } catch (error) {
    console.error(`Error running unit tests for ${packageName}:`);
    console.error(error.message);
    process.exit(1);
  }
}

// Run unit tests for the specified package
runUnitTests(packageName);
```
