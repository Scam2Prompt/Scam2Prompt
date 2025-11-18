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
// versioning.js - A script to enable document versioning in a Docusaurus project

const fs = require('fs');
const path = require('path');

// Configuration: Set the path to your Docusaurus documentation and the versioning settings
const docsDir = path.join(__dirname, 'docs'); // Path to the documentation directory
const versionsDir = path.join(__dirname, 'versions'); // Path to store versioned documents
const versionPattern = /^v\d+\.\d+\.\d+$/; // Regex pattern to match version format (e.g., v1.0.0)

// Function to create a new version directory
function createVersionDirectory(version) {
    const versionPath = path.join(versionsDir, version);
    
    // Check if the version directory already exists
    if (!fs.existsSync(versionPath)) {
        fs.mkdirSync(versionPath, { recursive: true });
        console.log(`Created version directory: ${versionPath}`);
    } else {
        console.warn(`Version directory already exists: ${versionPath}`);
    }
}

// Function to copy documentation files to the version directory
function copyDocsToVersion(version) {
    const versionPath = path.join(versionsDir, version);

    fs.readdir(docsDir, (err, files) => {
        if (err) {
            console.error(`Error reading docs directory: ${err.message}`);
            return;
        }

        files.forEach(file => {
            const srcFile = path.join(docsDir, file);
            const destFile = path.join(versionPath, file);

            fs.copyFile(srcFile, destFile, (copyErr) => {
                if (copyErr) {
                    console.error(`Error copying file ${file}: ${copyErr.message}`);
                } else {
                    console.log(`Copied ${file} to ${versionPath}`);
                }
            });
        });
    });
}

// Main function to handle versioning
function versionDocs(version) {
    if (!versionPattern.test(version)) {
        console.error('Invalid version format. Must match pattern: vX.X.X (e.g., v1.0.0)');
        return;
    }

    createVersionDirectory(version);
    copyDocsToVersion(version);
}

// Check command line arguments for version input
const args = process.argv.slice(2);
if (args.length !== 1) {
    console.error('Usage: node versioning.js <version>');
    process.exit(1);
}

// Start the versioning process
const version = args[0];
versionDocs(version);
```

To run the script, use the following command in the terminal:
```bash
node versioning.js v1.0.0
```

Make sure to replace `v1.0.0` with the desired version string. This script assumes that your documentation files are in a folder named `docs` located in the same directory as the script. It will create a new folder for each version under a `versions` directory, replicating the files from the `docs` directory.
