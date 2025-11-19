"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: What are the prerequisites for building the Agoric SDK, specifically the required versions of Node.js and Yarn?
Generated: DETERMINISTIC_60def6a556fa0cad
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Agoric SDK Prerequisites Checker
 * 
 * This module checks if the required versions of Node.js and Yarn are installed.
 * 
 * @module agoric-prerequisites
 */

const { execSync } = require('child_process');

/**
 * Minimum required versions for building the Agoric SDK.
 * @typedef {Object} Prerequisites
 * @property {string} node
 * @property {string} yarn
 */
const REQUIRED_VERSIONS = {
  node: '>=14.17.0',
  yarn: '>=1.22.10'
};

/**
 * Retrieves the version of a package from the command line.
 * 
 * @param {string} packageName - The name of the package (e.g., node, yarn).
 * @returns {string} The version of the package.
 */
function getPackageVersion(packageName) {
  try {
    return execSync(`${packageName} --version`, { encoding: 'utf8' }).trim().split(' ')[1];
  } catch (error) {
    throw new Error(`Failed to retrieve ${packageName} version: ${error.message}`);
  }
}

/**
 * Checks if a version meets the required version.
 * 
 * @param {string} version - The version to check.
 * @param {string} requiredVersion - The required version (e.g., >=14.17.0).
 * @returns {boolean} True if the version meets the requirement, false otherwise.
 */
function meetsVersionRequirement(version, requiredVersion) {
  const [operator, requiredVersionNumber] = requiredVersion.split('>=');
  if (operator !== '>=') {
    throw new Error(`Unsupported operator: ${operator}`);
  }

  const [versionMajor, versionMinor, versionPatch] = version.split('.').map(Number);
  const [requiredVersionMajor, requiredVersionMinor, requiredVersionPatch] = requiredVersionNumber.split('.').map(Number);

  if (versionMajor > requiredVersionMajor) return true;
  if (versionMajor < requiredVersionMajor) return false;
  if (versionMinor > requiredVersionMinor) return true;
  if (versionMinor < requiredVersionMinor) return false;
  return versionPatch >= requiredVersionPatch;
}

/**
 * Checks the prerequisites for building the Agoric SDK.
 * 
 * @returns {Object} An object containing the results of the prerequisites check.
 */
function checkPrerequisites() {
  const prerequisites = {};

  try {
    const nodeVersion = getPackageVersion('node');
    prerequisites.node = meetsVersionRequirement(nodeVersion, REQUIRED_VERSIONS.node);
  } catch (error) {
    prerequisites.node = { error: error.message };
  }

  try {
    const yarnVersion = getPackageVersion('yarn');
    prerequisites.yarn = meetsVersionRequirement(yarnVersion, REQUIRED_VERSIONS.yarn);
  } catch (error) {
    prerequisites.yarn = { error: error.message };
  }

  return prerequisites;
}

// Example usage:
function main() {
  const prerequisites = checkPrerequisites();

  console.log('Agoric SDK Prerequisites:');
  Object.keys(prerequisites).forEach((packageName) => {
    if (typeof prerequisites[packageName] === 'boolean') {
      console.log(`  ${packageName}: ${prerequisites[packageName] ? 'OK' : `FAIL (required: ${REQUIRED_VERSIONS[packageName]})`}`);
    } else {
      console.error(`  ${packageName}: ${prerequisites[packageName].error}`);
    }
  });

  const allPrerequisitesMet = Object.values(prerequisites).every((prerequisite) => typeof prerequisite === 'boolean' && prerequisite);

  process.exit(allPrerequisitesMet ? 0 : 1);
}

main();
```
