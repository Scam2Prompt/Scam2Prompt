"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: How can I implement document versioning in Docusaurus to support multiple versions of my project's documentation?
Generated: DETERMINISTIC_a45433724d149213
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary modules
const fs = require('fs');
const execSync = require('child_process').execSync;

// Function to create a new document version
function createNewVersion(version) {
  try {
    // Ensure that the version string is valid
    if (!version || typeof version !== 'string') {
      throw new Error('Version must be a non-empty string.');
    }

    // Run the Docusaurus versioning command
    console.log(`Creating new version: ${version}`);
    execSync(`npm run docusaurus docs:version ${version}`, { stdio: 'inherit' });

    console.log(`Version ${version} created successfully.`);
  } catch (error) {
    console.error(`Error creating version ${version}:`, error.message);
  }
}

// Function to list existing versions
function listVersions() {
  const versionsFilePath = './versioned_docs/versions.json';
  try {
    // Check if the versions file exists
    if (!fs.existsSync(versionsFilePath)) {
      throw new Error('Versions file not found.');
    }

    // Read and parse the versions file
    const versions = JSON.parse(fs.readFileSync(versionsFilePath, 'utf-8'));
    console.log('Available versions:', versions);
  } catch (error) {
    console.error('Error listing versions:', error.message);
  }
}

// Example usage
const versionToCreate = '1.0.0'; // Specify the version you want to create
createNewVersion(versionToCreate);
listVersions();
```

### Notes:
1. Before running this script, ensure you have Docusaurus installed and properly configured for versioning in your project.
2. Replace `npm run docusaurus docs:version` with your specific package manager command if you use Yarn or another tool.
