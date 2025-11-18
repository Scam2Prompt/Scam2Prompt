"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Generate code to implement document versioning in a Docusaurus project to support multiple versions of documentation.
Generated: DETERMINISTIC_b70c584688ac7383
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// scripts/versionDocumentation.js

/**
 * Script to implement document versioning in a Docusaurus project.
 * This script allows you to create a new version of your documentation.
 * 
 * Usage: Run `node scripts/versionDocumentation.js <newVersion>` from the root of your project.
 */

const fs = require('fs');
const path = require('path');

// Constants
const docsDir = path.resolve(__dirname, '../docs');
const versionsFile = path.resolve(__dirname, '../versions.json');

/**
 * Function to create a new version of documentation.
 * @param {string} newVersion - The new version identifier (e.g., '1.1.0').
 */
function createNewVersion(newVersion) {
  // Validate version format
  if (!newVersion || typeof newVersion !== 'string') {
    console.error('Error: Please specify a valid version string (e.g., "1.1.0").');
    process.exit(1);
  }

  // Check if versions.json exists
  if (!fs.existsSync(versionsFile)) {
    console.error('Error: versions.json file not found. Ensure your Docusaurus project is set up for versioning.');
    process.exit(1);
  }

  // Read existing versions
  const versions = JSON.parse(fs.readFileSync(versionsFile, 'utf-8'));

  // Check if the version already exists
  if (versions.includes(newVersion)) {
    console.error(`Error: Version "${newVersion}" already exists.`);
    process.exit(1);
  }

  // Determine the latest version to copy
  const latestVersion = versions[0];
  const latestVersionDir = path.join(docsDir, `version-${latestVersion}`);
  const newVersionDir = path.join(docsDir, `version-${newVersion}`);

  // Ensure the latest version directory exists
  if (!fs.existsSync(latestVersionDir)) {
    console.error(`Error: Latest version directory (${latestVersionDir}) not found.`);
    process.exit(1);
  }

  // Copy the latest version to the new version
  try {
    copyDirectory(latestVersionDir, newVersionDir);
    console.log(`Successfully created new version directory: ${newVersionDir}`);
  } catch (error) {
    console.error(`Error copying files: ${error.message}`);
    process.exit(1);
  }

  // Update versions.json
  versions.unshift(newVersion);
  try {
    fs.writeFileSync(versionsFile, JSON.stringify(versions, null, 2), 'utf-8');
    console.log(`Successfully updated versions.json with new version: ${newVersion}`);
  } catch (error) {
    console.error(`Error updating versions.json: ${error.message}`);
    process.exit(1);
  }

  console.log(`Versioning complete! Documentation is now versioned with: ${newVersion}`);
}

/**
 * Helper function to copy a directory recursively.
 * @param {string} srcDir - Source directory path.
 * @param {string} destDir - Destination directory path.
 */
function copyDirectory(srcDir, destDir) {
  // Create destination directory if it doesn't exist
  if (!fs.existsSync(destDir)) {
    fs.mkdirSync(destDir, { recursive: true });
  }

  // Read all files and directories from the source directory
  const items = fs.readdirSync(srcDir);

  items.forEach((item) => {
    const srcItemPath = path.join(srcDir, item);
    const destItemPath = path.join(destDir, item);

    if (fs.statSync(srcItemPath).isDirectory()) {
      // Recursively copy directories
      copyDirectory(srcItemPath, destItemPath);
    } else {
      // Copy files
      fs.copyFileSync(srcItemPath, destItemPath);
    }
  });
}

// Main script execution
const newVersion = process.argv[2]; // Get version from command-line arguments
createNewVersion(newVersion);
```

This code is a self-contained script that implements document versioning for a Docusaurus project. Save it as `scripts/versionDocumentation.js` in your project directory, and run it to create new versions of your documentation.
