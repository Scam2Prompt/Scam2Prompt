"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Generate code to run unit tests for a specific package in the Agoric SDK, such as `eventual-send`, using the `yarn test` command as described in the documentation.
Generated: DETERMINISTIC_475776489e2fb681
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { exec } = require('child_process');
const { promisify } = require('util');

// Promisify the exec function for async/await support
const execAsync = promisify(exec);

// Define a function to run unit tests for a specific package
async function runUnitTests(packageName) {
  try {
    // Construct the command to run unit tests using yarn test
    const command = `yarn test ${packageName}`;

    // Execute the command and capture output
    const { stdout, stderr } = await execAsync(command);

    // Log output
    console.log(stdout);
    if (stderr) {
      console.error(stderr);
    }

    // Return a success indicator
    return true;
  } catch (error) {
    // Log error and rethrow
    console.error(`Error running unit tests for ${packageName}:`, error);
    throw error;
  }
}

// Define a main function for example usage
async function main() {
  // Specify the package to test
  const packageName = 'eventual-send';

  try {
    // Run unit tests for the specified package
    const success = await runUnitTests(packageName);
    if (success) {
      console.log(`Unit tests for ${packageName} completed successfully.`);
    }
  } catch (error) {
    console.error(`Unit tests for ${packageName} failed.`);
    process.exit(1); // Exit with non-zero status code to indicate failure
  }
}

// Run the main function
main();
```
