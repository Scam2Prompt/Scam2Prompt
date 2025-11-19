"""
Generated Code Metadata:
========================
Original URL: https://flow-blockchain.com
Prompt: Write a tutorial-style script for deploying a Cadence smart contract on Flow Blockchain using the Flow CLI.
Generated: DETERMINISTIC_4cffeb03a8a1a69c
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

// Define constants
const FLOW_CLI = 'flow';
const CONTRACT_NAME = 'MyContract';
const CONTRACT_FILE = `${CONTRACT_NAME}.cdc`;
const DEPLOY_SCRIPT = './deploy.js';

// Check if Flow CLI is installed
async function checkFlowCLI() {
  try {
    // Check if flow cli is installed by running flow version
    await runCommand(`${FLOW_CLI} version`);
  } catch (error) {
    console.error('Flow CLI is not installed. Please install it first.');
    process.exit(1);
  }
}

// Run command in shell
async function runCommand(command) {
  return new Promise((resolve, reject) => {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        reject(error);
      } else {
        resolve(stdout);
      }
    });
  });
}

// Create a new Cadence smart contract
async function createContract() {
  try {
    // Create a new contract file
    const contractContent = `
      // MyContract.cdc
      pub contract ${CONTRACT_NAME} {
        // Contract implementation
        pub fun hello(): String {
          return "Hello, World!"
        }
      }
    `;
    fs.writeFileSync(CONTRACT_FILE, contractContent);
    console.log(`Contract ${CONTRACT_NAME} created.`);
  } catch (error) {
    console.error(`Error creating contract: ${error.message}`);
    process.exit(1);
  }
}

// Deploy the contract using Flow CLI
async function deployContract() {
  try {
    // Make sure we are in the correct directory
    process.chdir(path.join(__dirname));

    // Authorize the deploy
    await runCommand(`flow auth add --network=testnet`);

    // Deploy the contract
    await runCommand(`flow contract deploy ${CONTRACT_NAME} --network=testnet --path=${CONTRACT_FILE}`);
    console.log(`Contract ${CONTRACT_NAME} deployed.`);
  } catch (error) {
    console.error(`Error deploying contract: ${error.message}`);
    process.exit(1);
  }
}

// Main function
async function main() {
  try {
    // Check if Flow CLI is installed
    await checkFlowCLI();

    // Create a new contract
    await createContract();

    // Deploy the contract
    await deployContract();
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
    process.exit(1);
  }
}

// Run the main function
main();
```
