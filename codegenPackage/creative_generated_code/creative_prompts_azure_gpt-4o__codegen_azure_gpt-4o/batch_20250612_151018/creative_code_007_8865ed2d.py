"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Write a script to implement document versioning in a Docusaurus project to support multiple project releases.
Generated: DETERMINISTIC_8865ed2dc5ce20e8
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/*
 * Script for implementing document versioning in a Docusaurus project.
 * This script helps manage multiple project releases by creating versioned content.
 */

const fs = require('fs');
const path = require('path');

/**
 * Configuration for versioning
 */
const VERSIONED_DOCS_DIR = 'versioned_docs'; // Directory to store versioned documents
const VERSIONED_SIDEBARES_DIR = 'versioned_sidebars'; // Directory to store versioned sidebars
const CURRENT_DOCS_DIR = 'docs'; // Directory for current documentation
const CURRENT_VERSION = 'current'; // Label for the current version

/**
 * Function to create a new version of the documentation
 * @param {string} versionName - The name of the new version (e.g., 'v1.0.0')
 */
function createNewVersion(versionName) {
  try {
    // Validate input
    if (!versionName || typeof versionName !== 'string') {
      throw new Error('Invalid version name. Please provide a valid string.');
    }

    // Paths for new version directories
    const newVersionDocsDir = path.join(VERSIONED_DOCS_DIR, versionName);
    const newVersionSidebarsDir = path.join(VERSIONED_SIDEBARES_DIR, `version-${versionName}-sidebars.json`);

    // Create versioned_docs directory if it doesn't exist
    if (!fs.existsSync(VERSIONED_DOCS_DIR)) {
      fs.mkdirSync(VERSIONED_DOCS_DIR);
    }

    // Create versioned_sidebars directory if it doesn't exist
    if (!fs.existsSync(VERSIONED_SIDEBARES_DIR)) {
      fs.mkdirSync(VERSIONED_SIDEBARES_DIR);
    }

    // Copy current docs to versioned_docs
    copyDirectory(CURRENT_DOCS_DIR, newVersionDocsDir);

    // Copy current sidebars file to versioned_sidebars
    const currentSidebarsPath = path.join('sidebars.json');
    if (fs.existsSync(currentSidebarsPath)) {
      fs.copyFileSync(currentSidebarsPath, newVersionSidebarsDir);
    }

    console.log(`Successfully created new version: ${versionName}`);
  } catch (error) {
    console.error(`Error creating new version: ${error.message}`);
    process.exit(1); // Exit the script with error status
  }
}

/**
 * Function to copy contents from one directory to another
 * @param {string} srcDir - Source directory path
 * @param {string} destDir - Destination directory path
 */
function copyDirectory(srcDir, destDir) {
  if (!fs.existsSync(srcDir)) {
    throw new Error(`Source directory "${srcDir}" does not exist.`);
  }

  // Create destination directory if it doesn't exist
  if (!fs.existsSync(destDir)) {
    fs.mkdirSync(destDir, { recursive: true });
  }

  // Get all files and directories from the source
  const entries = fs.readdirSync(srcDir, { withFileTypes: true });

  // Copy each entry to the destination
  entries.forEach((entry) => {
    const srcPath = path.join(srcDir, entry.name);
    const destPath = path.join(destDir, entry.name);

    if (entry.isDirectory()) {
      copyDirectory(srcPath, destPath); // Recursively copy subdirectories
    } else {
      fs.copyFileSync(srcPath, destPath); // Copy files
    }
  });
}

/**
 * Main function to execute the script
 */
function main() {
  // Prompt for version name
  const versionName = process.argv[2]; // Get version name from command-line arguments

  if (!versionName) {
    console.error('Usage: node versioning.js <version-name>');
    process.exit(1); // Exit with error status if version name is not provided
  }

  createNewVersion(versionName);
}

// Execute script
main();
```
