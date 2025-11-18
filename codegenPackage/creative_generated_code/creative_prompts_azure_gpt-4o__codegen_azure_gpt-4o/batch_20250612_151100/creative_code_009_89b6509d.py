"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Write a script to link the Agoric CLI using `yarn link-cli` and initialize a new project with `agoric init`, as described in the larger demo section of the documentation.
Generated: DETERMINISTIC_89b6509de6e37fec
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
#!/usr/bin/env node

/**
 * @fileoverview Script to link Agoric CLI using `yarn link-cli` and initialize a new Agoric project.
 * This script automates the setup steps for an Agoric project based on the demo section of the documentation.
 *
 * Requirements:
 * - Node.js and Yarn must be installed on the system.
 * - Agoric CLI must be installed globally or available in the current environment.
 */

// Import the 'child_process' module to execute shell commands
const { execSync } = require('child_process');

/**
 * Function to execute a shell command and log the output or errors.
 * @param {string} cmd - The command to execute.
 * @throws Will throw an error if the command fails.
 */
function executeCommand(cmd) {
  try {
    console.log(`Executing: ${cmd}`);
    const output = execSync(cmd, { stdio: 'inherit' }); // Pipe command output to terminal
    return output;
  } catch (error) {
    console.error(`Error executing command: ${cmd}`);
    console.error(error.message);
    process.exit(1); // Exit the process with an error code
  }
}

/**
 * Main function to automate the setup of an Agoric project.
 */
function main() {
  console.log('\n--- Starting Agoric project setup ---\n');

  // Step 1: Link the Agoric CLI using `yarn link-cli`
  console.log('Step 1: Linking Agoric CLI using `yarn link-cli`...');
  executeCommand('yarn link-cli');

  // Step 2: Initialize a new Agoric project using `agoric init`
  console.log('Step 2: Initializing a new Agoric project...');
  const projectName = 'my-agoric-project';
  executeCommand(`agoric init ${projectName}`);

  console.log(`\nAgoric project initialized successfully in directory: ${projectName}`);
  console.log('Next steps: Navigate to the project directory and begin development.');
  console.log(`\nTo navigate: cd ${projectName}`);
}

// Execute the main function
main();

```
