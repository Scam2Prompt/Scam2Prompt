"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Write a script to enable document versioning in a Docusaurus project, syncing documentation with multiple project releases.
Generated: DETERMINISTIC_3fd38433134fd105
Batch ID: 20250612_151018
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

// Configuration
const DOCUSAURUS_ROOT = process.cwd();
const DOCS_DIR = path.join(DOCUSAURUS_ROOT, 'docs');
const VERSIONS_DIR = path.join(DOCUSAURUS_ROOT, 'versioned_docs');
const VERSIONS_JSON = path.join(DOCUSAURUS_ROOT, 'versions.json');

/**
 * Validate Docusaurus project structure
 * @throws {Error} If project structure is invalid
 */
function validateProjectStructure() {
  if (!fs.existsSync(DOCS_DIR)) {
    throw new Error('Docs directory not found');
  }
  if (!fs.existsSync(path.join(DOCUSAURUS_ROOT, 'docusaurus.config.js'))) {
    throw new Error('Docusaurus config not found');
  }
}

/**
 * Get current version from package.json
 * @returns {string} Current version
 */
function getCurrentVersion() {
  const packageJson = require(path.join(DOCUSAURUS_ROOT, 'package.json'));
  return packageJson.version;
}

/**
 * Create versioned docs directory
 * @param {string} version - Version to create
 */
function createVersionedDocs(version) {
  const versionDir = path.join(VERSIONS_DIR, `version-${version}`);
  
  if (!fs.existsSync(VERSIONS_DIR)) {
    fs.mkdirSync(VERSIONS_DIR);
  }

  if (fs.existsSync(versionDir)) {
    throw new Error(`Version ${version} already exists`);
  }

  fs.mkdirSync(versionDir);
  return versionDir;
}

/**
 * Copy docs to versioned directory
 * @param {string} versionDir - Target version directory
 */
function copyDocsToVersion(versionDir) {
  const copyRecursive = (src, dest) => {
    const entries = fs.readdirSync(src, { withFileTypes: true });
    
    if (!fs.existsSync(dest)) {
      fs.mkdirSync(dest);
    }

    for (const entry of entries) {
      const srcPath = path.join(src, entry.name);
      const destPath = path.join(dest, entry.name);

      if (entry.isDirectory()) {
        copyRecursive(srcPath, destPath);
      } else {
        fs.copyFileSync(srcPath, destPath);
      }
    }
  };

  copyRecursive(DOCS_DIR, versionDir);
}

/**
 * Update versions.json with new version
 * @param {string} version - Version to add
 */
function updateVersionsJson(version) {
  let versions = [];
  
  if (fs.existsSync(VERSIONS_JSON)) {
    versions = JSON.parse(fs.readFileSync(VERSIONS_JSON, 'utf8'));
  }

  if (versions.includes(version)) {
    throw new Error(`Version ${version} already exists in versions.json`);
  }

  versions.unshift(version);
  fs.writeFileSync(VERSIONS_JSON, JSON.stringify(versions, null, 2));
}

/**
 * Run Docusaurus version command
 * @param {string} version - Version to create
 */
function runDocusaurusVersionCommand(version) {
  try {
    execSync(`npx docusaurus docs:version ${version}`, { stdio: 'inherit' });
  } catch (error) {
    throw new Error(`Failed to run Docusaurus version command: ${error.message}`);
  }
}

/**
 * Main function to version docs
 */
function versionDocs() {
  try {
    validateProjectStructure();
    const version = getCurrentVersion();
    
    console.log(`Creating version ${version}...`);
    const versionDir = createVersionedDocs(version);
    copyDocsToVersion(versionDir);
    updateVersionsJson(version);
    runDocusaurusVersionCommand(version);
    
    console.log(`Successfully created version ${version}`);
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Execute
versionDocs();
```
