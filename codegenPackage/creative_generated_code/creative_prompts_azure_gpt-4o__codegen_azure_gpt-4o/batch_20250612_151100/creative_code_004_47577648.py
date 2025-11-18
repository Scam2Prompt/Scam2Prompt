"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Generate code to run unit tests for a specific package in the Agoric SDK, such as `eventual-send`, using the `yarn test` command as described in the documentation.
Generated: DETERMINISTIC_475776489e2fb681
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: runTests.js

// Import necessary modules
const { exec } = require('child_process');

/**
 * Runs unit tests for a specific package in the Agoric SDK.
 * @param {string} packageName - Name of the package to run tests for (e.g., "eventual-send").
 */
function runTests(packageName) {
  // Validate input
  if (!packageName || typeof packageName !== 'string') {
    console.error('Error: Package name must be a non-empty string.');
    return;
  }

  // Construct the command to run tests using yarn
  const command = `yarn test`;

  // Navigate to the specific package directory
  const packagePath = `packages/${packageName}`;
  const fullCommand = `cd ${packagePath} && ${command}`;

  console.log(`Executing: ${fullCommand}`);

  // Execute the command
  exec(fullCommand, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error running tests: ${error.message}`);
      return;
    }

    if (stderr) {
      console.error(`Test execution errors (stderr): ${stderr}`);
    }

    console.log(`Test results:\n${stdout}`);
  });
}

// Example usage:
// Replace "eventual-send" with the name of the package you want to test.
runTests('eventual-send');

// Export the function for external use (optional, if used in a larger application)
module.exports = runTests;
```

This code defines a function, `runTests`, that allows you to execute unit tests for a specific package in the Agoric SDK using the `yarn test` command. It handles errors gracefully and follows best practices.
