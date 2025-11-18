"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Write a script to enable document versioning in a Docusaurus project, syncing documentation with multiple project releases.
Generated: DETERMINISTIC_3fd38433134fd105
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// versioning.js
// Script to enable document versioning in a Docusaurus project
// Syncs documentation with multiple project releases

const fs = require('fs');
const path = require('path');

// Configuration
const docsPath = path.resolve(__dirname, 'docs'); // Source docs folder
const versionedDocsPath = path.resolve(__dirname, 'versioned_docs'); // Target folder for versioned docs
const versionsFile = path.resolve(__dirname, 'versions.json'); // File to track available versions

// Create necessary directories if they don't exist
function ensureDirectoriesExist() {
  if (!fs.existsSync(versionedDocsPath)) {
    fs.mkdirSync(versionedDocsPath, { recursive: true });
  }
  if (!fs.existsSync(versionsFile)) {
    fs.writeFileSync(versionsFile, JSON.stringify([])); // Initialize empty versions file
  }
}

// Get current version list from the versions file
function getCurrentVersions() {
  const data = fs.readFileSync(versionsFile, 'utf8');
  return JSON.parse(data);
}

// Add a new version and sync documents
function createVersion(version) {
  if (!version || typeof version !== 'string' || version.trim() === '') {
    throw new Error('Invalid version name.');
  }

  // Ensure directories and file structures exist
  ensureDirectoriesExist();

  const currentVersions = getCurrentVersions();
  if (currentVersions.includes(version)) {
    throw new Error(`Version ${version} already exists.`);
  }

  const versionedPath = path.resolve(versionedDocsPath, version);
  fs.mkdirSync(versionedPath, { recursive: true });

  // Copy documentation files to versioned folder
  copyDocs(docsPath, versionedPath);

  // Update versions file
  currentVersions.push(version);
  fs.writeFileSync(versionsFile, JSON.stringify(currentVersions, null, 2));

  console.log(`Version ${version} successfully created.`);
}

// Copy documentation files recursively
function copyDocs(src, dest) {
  const entries = fs.readdirSync(src, { withFileTypes: true });

  entries.forEach((entry) => {
    const srcPath = path.resolve(src, entry.name);
    const destPath = path.resolve(dest, entry.name);

    if (entry.isDirectory()) {
      fs.mkdirSync(destPath, { recursive: true });
      copyDocs(srcPath, destPath); // Recursive copy for subdirectories
    } else {
      fs.copyFileSync(srcPath, destPath); // Copy individual file
    }
  });
}

// Main function to handle versioning
function main() {
  const args = process.argv.slice(2);

  if (args.length !== 1) {
    console.error('Usage: node versioning.js <version>');
    process.exit(1);
  }

  const version = args[0];

  try {
    createVersion(version);
  } catch (error) {
    console.error(`Error creating version: ${error.message}`);
    process.exit(1);
  }
}

// Execute script if run directly
if (require.main === module) {
  main();
}
```

To run the script, execute the following command in your terminal:
```bash
node versioning.js <version>
```
Replace `<version>` with the desired version name (e.g., `1.0.0`). Ensure you have a `docs/` folder containing your source documentation in the same directory as the script.
