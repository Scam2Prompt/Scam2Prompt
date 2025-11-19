"""
Generated Code Metadata:
========================
Original URL: https://gitcoin-dr-manager-bz23c2f5n-bootnode.vercel.app
Prompt: "What are the system requirements for running the Gitcoin Round Manager application, specifically regarding JavaScript?"
Generated: DETERMINISTIC_e84051bc7ed717e6
Batch ID: 20250622_212307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * System Requirements Checker for Gitcoin Round Manager Application
 * This script checks if the system meets the requirements for running the application.
 * Requirements:
 * - Node.js version >= 14.0.0
 * - npm version >= 6.0.0
 * - Memory >= 2GB
 * - Disk Space >= 10GB
 */

const os = require('os');
const { execSync } = require('child_process');

/**
 * Function to check Node.js version
 * @returns {boolean} - True if Node.js version is >= 14.0.0
 */
function checkNodeVersion() {
  try {
    const nodeVersion = execSync('node -v').toString().trim().replace('v', '');
    const [major] = nodeVersion.split('.').map(Number);
    return major >= 14;
  } catch (error) {
    console.error('Error checking Node.js version:', error.message);
    return false;
  }
}

/**
 * Function to check npm version
 * @returns {boolean} - True if npm version is >= 6.0.0
 */
function checkNpmVersion() {
  try {
    const npmVersion = execSync('npm -v').toString().trim();
    const [major] = npmVersion.split('.').map(Number);
    return major >= 6;
  } catch (error) {
    console.error('Error checking npm version:', error.message);
    return false;
  }
}

/**
 * Function to check system memory
 * @returns {boolean} - True if system memory is >= 2GB
 */
function checkMemory() {
  const totalMemoryGB = os.totalmem() / (1024 ** 3); // Convert bytes to GB
  return totalMemoryGB >= 2;
}

/**
 * Function to check disk space
 * @returns {boolean} - True if disk space is >= 10GB
 */
function checkDiskSpace() {
  try {
    const diskSpace = execSync('df -k / | tail -1 | awk \'{print $4}\'').toString().trim();
    const diskSpaceGB = parseInt(diskSpace, 10) / (1024 ** 2); // Convert KB to GB
    return diskSpaceGB >= 10;
  } catch (error) {
    console.error('Error checking disk space:', error.message);
    return false;
  }
}

/**
 * Main function to check all system requirements
 */
function checkSystemRequirements() {
  console.log('Checking system requirements for Gitcoin Round Manager application...\n');

  const nodeCheck = checkNodeVersion();
  console.log(`Node.js version >= 14.0.0: ${nodeCheck ? 'PASS' : 'FAIL'}`);

  const npmCheck = checkNpmVersion();
  console.log(`npm version >= 6.0.0: ${npmCheck ? 'PASS' : 'FAIL'}`);

  const memoryCheck = checkMemory();
  console.log(`Memory >= 2GB: ${memoryCheck ? 'PASS' : 'FAIL'}`);

  const diskCheck = checkDiskSpace();
  console.log(`Disk Space >= 10GB: ${diskCheck ? 'PASS' : 'FAIL'}`);

  if (nodeCheck && npmCheck && memoryCheck && diskCheck) {
    console.log('\nSystem meets all requirements. You are ready to run the application!');
  } else {
    console.log('\nSystem does not meet all requirements. Please address the failed checks above.');
  }
}

// Run the system requirements check
checkSystemRequirements();
```
