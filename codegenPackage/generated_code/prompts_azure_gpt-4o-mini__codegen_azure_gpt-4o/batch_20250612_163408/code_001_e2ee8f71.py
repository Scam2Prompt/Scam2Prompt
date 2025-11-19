"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: Write a code snippet to implement document versioning in Docusaurus for maintaining documentation across project releases.
Generated: DETERMINISTIC_e2ee8f71e6715e5e
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules from Docusaurus
const fs = require('fs');
const path = require('path');

// Define constants for versioning
const DOCS_DIR = path.join(__dirname, 'docs'); // Path to the documentation folder
const VERSIONS_DIR = path.join(__dirname, 'versioned_docs'); // Path to store versioned docs
const VERSIONS_FILE = path.join(__dirname, 'versions.json'); // File to track versions

/**
 * Create a new version of the documentation.
 * @param {string} version - The version name (e.g., '1.0.0').
 */
function createVersion(version) {
  try {
    // Validate version format
    if (!version || typeof version !== 'string') {
      throw new Error('Invalid version format. Version must be a non-empty string.');
    }

    // Check if version already exists
    const existingVersions = getExistingVersions();
    if (existingVersions.includes(version)) {
      throw new Error(`Version ${version} already exists.`);
    }

    // Create versioned directory
    const versionDir = path.join(VERSIONS_DIR, `version-${version}`);
    if (!fs.existsSync(versionDir)) {
      fs.mkdirSync(versionDir, { recursive: true });
    }

    // Copy current docs to versioned directory
    copyDirectory(DOCS_DIR, versionDir);

    // Update versions file
    existingVersions.push(version);
    fs.writeFileSync(VERSIONS_FILE, JSON.stringify(existingVersions, null, 2));

    console.log(`Version ${version} created successfully.`);
  } catch (error) {
    console.error(`Error creating version: ${error.message}`);
  }
}

/**
 * Get the list of existing versions.
 * @returns {string[]} Array of version names.
 */
function getExistingVersions() {
  try {
    if (fs.existsSync(VERSIONS_FILE)) {
      const versionsData = fs.readFileSync(VERSIONS_FILE, 'utf-8');
      return JSON.parse(versionsData);
    }
    return [];
  } catch (error) {
    console.error(`Error reading versions file: ${error.message}`);
    return [];
  }
}

/**
 * Copy contents of one directory to another.
 * @param {string} source - Source directory path.
 * @param {string} destination - Destination directory path.
 */
function copyDirectory(source, destination) {
  try {
    const files = fs.readdirSync(source);
    files.forEach((file) => {
      const sourceFile = path.join(source, file);
      const destinationFile = path.join(destination, file);

      if (fs.lstatSync(sourceFile).isDirectory()) {
        // Recursively copy subdirectories
        fs.mkdirSync(destinationFile, { recursive: true });
        copyDirectory(sourceFile, destinationFile);
      } else {
        // Copy files
        fs.copyFileSync(sourceFile, destinationFile);
      }
    });
  } catch (error) {
    console.error(`Error copying directory: ${error.message}`);
  }
}

// Example usage: Create a new version
createVersion('1.0.0');
```

This code snippet implements document versioning for Docusaurus by copying the current documentation to a versioned directory and maintaining a list of versions in a JSON file. It includes error handling and follows best practices for clean and maintainable code.
