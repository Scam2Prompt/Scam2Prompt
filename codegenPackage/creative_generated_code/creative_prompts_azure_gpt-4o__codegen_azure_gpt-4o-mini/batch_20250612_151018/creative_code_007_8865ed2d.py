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
// versioning.js
const fs = require('fs');
const path = require('path');

// Constants for the versioning process
const DOCS_DIR = path.join(__dirname, 'docs'); // Directory where documents are stored
const VERSIONS_DIR = path.join(__dirname, 'versions'); // Directory for versioned documents

/**
 * Initialize the versioning system by creating necessary directories.
 */
function initializeVersioning() {
    try {
        // Create versions directory if it does not exist
        if (!fs.existsSync(VERSIONS_DIR)) {
            fs.mkdirSync(VERSIONS_DIR);
            console.log('Created versions directory.');
        }
    } catch (error) {
        console.error('Error initializing versioning:', error);
    }
}

/**
 * Get a list of all document files in the specified directory.
 * @returns {Array} - List of document file names.
 */
function getDocumentFiles() {
    try {
        return fs.readdirSync(DOCS_DIR).filter(file => file.endsWith('.md'));
    } catch (error) {
        console.error('Error reading document files:', error);
        return [];
    }
}

/**
 * Create a versioned copy of each document.
 * @param {string} version - The version label to use for the document copies.
 */
function createVersionedDocuments(version) {
    const documents = getDocumentFiles();

    documents.forEach(doc => {
        const sourceFilePath = path.join(DOCS_DIR, doc);
        const targetFilePath = path.join(VERSIONS_DIR, `${version}_${doc}`);

        try {
            fs.copyFileSync(sourceFilePath, targetFilePath);
            console.log(`Versioned document created: ${targetFilePath}`);
        } catch (error) {
            console.error(`Error creating versioned document for ${doc}:`, error);
        }
    });
}

/**
 * Main function to execute the versioning workflow.
 * @param {string} version - The version label to create.
 */
function main(version) {
    if (!version) {
        console.error('Please provide a version label as an argument.');
        process.exit(1);
    }

    initializeVersioning();
    createVersionedDocuments(version);
}

// Run the script with the provided version argument
const versionArg = process.argv[2];
main(versionArg);
```

### Usage:
1. Save this script as `versioning.js` in your Docusaurus project root directory.
2. Ensure your documents are located in a `docs` folder.
3. Run the script from the command line, providing a version label:
   ```bash
   node versioning.js v1.0.0
   ```
4. This will create a new versioned copy of each document in the `versions` directory with the version label prefixed.
