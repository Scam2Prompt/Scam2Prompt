"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Generate code to build and test a package in the Agoric SDK using `yarn install`, `yarn build`, and `yarn test` commands. Include steps to resolve mismatched workspace dependencies as mentioned in the documentation.
Generated: DETERMINISTIC_6cde3af43fb6d55a
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// build-and-test-agoric-sdk.js
const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

/**
 * Builds and tests a package in the Agoric SDK.
 * 
 * @param {string} packagePath - The path to the package.
 */
function buildAndTestAgoricSdk(packagePath) {
  // Check if packagePath exists
  if (!fs.existsSync(packagePath)) {
    throw new Error(`Package path '${packagePath}' does not exist.`);
  }

  // Run yarn install
  runYarnCommand('install', packagePath);

  // Resolve mismatched workspace dependencies
  resolveMismatchedDependencies(packagePath);

  // Run yarn build
  runYarnCommand('build', packagePath);

  // Run yarn test
  runYarnCommand('test', packagePath);
}

/**
 * Runs a yarn command in the specified directory.
 * 
 * @param {string} command - The yarn command to run.
 * @param {string} directory - The directory to run the command in.
 */
function runYarnCommand(command, directory) {
  return new Promise((resolve, reject) => {
    const yarnCommand = `yarn ${command}`;
    const childProcess = exec(yarnCommand, { cwd: directory });

    childProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
    });

    childProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
    });

    childProcess.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(`Command '${yarnCommand}' failed with code ${code}.`));
      } else {
        resolve();
      }
    });
  });
}

/**
 * Resolves mismatched workspace dependencies.
 * 
 * @param {string} packagePath - The path to the package.
 */
function resolveMismatchedDependencies(packagePath) {
  const yarnLockPath = path.join(packagePath, 'yarn.lock');
  if (fs.existsSync(yarnLockPath)) {
    // Remove yarn.lock to allow yarn to resolve dependencies
    fs.unlinkSync(yarnLockPath);
    console.log('Removed yarn.lock to resolve dependencies.');
  }

  // Run yarn install to resolve dependencies
  runYarnCommand('install', packagePath);
}

// Example usage
async function main() {
  try {
    const packagePath = './agoric-sdk-package';
    await buildAndTestAgoricSdk(packagePath);
    console.log('Build and test completed successfully.');
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

main();
```
