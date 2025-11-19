"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: How do I manage workspace dependencies in the Agoric SDK when using Yarn?
Generated: DETERMINISTIC_6c6f5a0f91ee9588
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { readFileSync, writeFileSync } = require('fs');

// Define constants
const AGORIC_SDK_DIR = 'agoric-sdk';
const YARN_LOCK_FILE = 'yarn.lock';
const PACKAGE_JSON_FILE = 'package.json';

/**
 * Manage workspace dependencies in the Agoric SDK when using Yarn.
 */
class AgoricSdkDependencyManager {
  /**
   * Initialize the dependency manager.
   * @param {string} sdkDir - The directory of the Agoric SDK.
   */
  constructor(sdkDir = AGORIC_SDK_DIR) {
    this.sdkDir = sdkDir;
  }

  /**
   * Get the yarn.lock file path.
   * @returns {string} The yarn.lock file path.
   */
  getYarnLockFilePath() {
    return path.join(this.sdkDir, YARN_LOCK_FILE);
  }

  /**
   * Get the package.json file path.
   * @returns {string} The package.json file path.
   */
  getPackageJsonFilePath() {
    return path.join(this.sdkDir, PACKAGE_JSON_FILE);
  }

  /**
   * Check if yarn.lock file exists.
   * @returns {boolean} True if yarn.lock file exists, false otherwise.
   */
  yarnLockFileExists() {
    return fs.existsSync(this.getYarnLockFilePath());
  }

  /**
   * Check if package.json file exists.
   * @returns {boolean} True if package.json file exists, false otherwise.
   */
  packageJsonFileExists() {
    return fs.existsSync(this.getPackageJsonFilePath());
  }

  /**
   * Run yarn install in the Agoric SDK directory.
   */
  yarnInstall() {
    try {
      execSync('yarn install', { cwd: this.sdkDir, stdio: 'inherit' });
    } catch (error) {
      console.error(`Error running yarn install: ${error.message}`);
      throw error;
    }
  }

  /**
   * Update dependencies in package.json and run yarn install.
   * @param {object} dependencies - The dependencies to update.
   */
  updateDependencies(dependencies) {
    if (!this.packageJsonFileExists()) {
      throw new Error('package.json file does not exist');
    }

    const packageJson = JSON.parse(readFileSync(this.getPackageJsonFilePath(), 'utf8'));
    packageJson.dependencies = { ...packageJson.dependencies, ...dependencies };
    writeFileSync(this.getPackageJsonFilePath(), JSON.stringify(packageJson, null, 2));

    this.yarnInstall();
  }

  /**
   * Add a new dependency to package.json and run yarn install.
   * @param {string} packageName - The name of the package to add.
   * @param {string} version - The version of the package to add.
   */
  addDependency(packageName, version) {
    this.updateDependencies({ [packageName]: version });
  }

  /**
   * Remove a dependency from package.json and run yarn install.
   * @param {string} packageName - The name of the package to remove.
   */
  removeDependency(packageName) {
    if (!this.packageJsonFileExists()) {
      throw new Error('package.json file does not exist');
    }

    const packageJson = JSON.parse(readFileSync(this.getPackageJsonFilePath(), 'utf8'));
    delete packageJson.dependencies[packageName];
    writeFileSync(this.getPackageJsonFilePath(), JSON.stringify(packageJson, null, 2));

    this.yarnInstall();
  }
}

// Example usage
const manager = new AgoricSdkDependencyManager();

// Add a new dependency
manager.addDependency('new-package', '1.0.0');

// Remove a dependency
manager.removeDependency('old-package');

// Update dependencies
manager.updateDependencies({ 'package-a': '2.0.0', 'package-b': '3.0.0' });
```
