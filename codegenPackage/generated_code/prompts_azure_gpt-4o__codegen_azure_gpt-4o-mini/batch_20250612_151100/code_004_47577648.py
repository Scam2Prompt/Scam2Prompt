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
// Import necessary modules from the Agoric SDK
const { exec } = require('child_process');

// Function to run unit tests for a specific package
async function runUnitTests(packageName) {
  return new Promise((resolve, reject) => {
    // Construct the command to run tests using yarn
    const command = `yarn workspace ${packageName} test`;

    // Execute the command
    exec(command, (error, stdout, stderr) => {
      if (error) {
        // Log the error and reject the promise
        console.error(`Error executing tests for ${packageName}:`, error);
        return reject(`Test execution failed: ${stderr}`);
      }
      // Log the output and resolve the promise
      console.log(`Test results for ${packageName}:\n${stdout}`);
      resolve(stdout);
    });
  });
}

// Main function to execute the test runner
(async () => {
  const packageName = 'eventual-send'; // Specify the package name

  try {
    // Run the unit tests for the specified package
    await runUnitTests(packageName);
    console.log(`Unit tests for ${packageName} completed successfully.`);
  } catch (error) {
    // Handle any errors that occur during test execution
    console.error(`Failed to run unit tests: ${error}`);
  }
})();
```
